# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        Step 1 Export Metadata
# Purpose:     Process metadata recprds
#
# Author:      john.f.kennedy
#
# Created:     11/20/2024
# Copyright:   (c) john.f.kennedy 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Python Built-in's modules are loaded first
import os, sys
import traceback, inspect
import importlib

# Third-party modules are loaded second
import arcpy

# Append the location of this scrip to the System Path
#sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

def schema_field_report(project_gdb=""):
    try:
        # Imports

        # Use all of the cores on the machine
        arcpy.env.parallelProcessingFactor = "100%"
        arcpy.env.overwriteOutput = True

        # Define variables
        project_folder = os.path.dirname(project_gdb)
        scratch_folder = rf"{project_folder}\Scratch"
        scratch_gdb    = rf"{scratch_folder}\scratch.gdb"
        #schema_folder  = rf"{project_folder}\Schema"
        #create_export_folder(schema_folder)
        #del schema_folder

        # Set the workspace environment to local file geodatabase
        arcpy.env.workspace = project_gdb
        # Set the scratchWorkspace environment to local file geodatabase
        arcpy.env.scratchWorkspace = scratch_gdb

        # Clean-up variables
        del scratch_folder, scratch_gdb

        arcpy.AddMessage(f"\n{'--Start' * 10}--\n")

        fcs = arcpy.ListFeatureClasses()

        fc_field_report = {}

        header = []

        arcpy.AddMessage(f"Check if feature classes exists in Project GDB\n")
        for fc in sorted(fcs):
            arcpy.AddMessage(f"{fc}")
            fc_field_report[fc] = {}

            #fc_path = rf"{source_gdb}\{fc}"

            #fields = [f for f in arcpy.ListFields(fc_path) if f.type not in ['Geometry', 'OID'] and not f.name.startswith('Shape_')]
            fields = [f for f in arcpy.ListFields(fc) if f.type not in ['Geometry', 'OID'] and not f.name.startswith('Shape_')]

            if not header:
                header.append("Feature Class")
                header.extend(["Field Name", "Alias", "Type", "Field Length", "Text Length"] * len(fields))

            for field in fields:

                #arcpy.AddMessage(f"\t{field.name}\n\t\t{field.aliasName}\n\t\t{field.type}\n\t\t{field.length}")

                if field.type == "String":

                    #with arcpy.da.SearchCursor(fc_path, [field.name]) as cursor:
                    with arcpy.da.SearchCursor(fc, [field.name]) as cursor:
                        text_length = 0
                        for row in cursor:
                            if row[0] != None and len(row[0]) > text_length:
                                text_length = len(row[0])
                            else:
                                text_length = text_length
                            del row
                    del cursor

                    fc_field_report[fc][field.name] = [field.aliasName, field.type, field.length, text_length]
                    del text_length
                else:

                    fc_field_report[fc][field.name] = [field.aliasName, field.type, 0, 0]

                del field
            del fields
            #del fc_path
            del fc

        del fcs

        # Feature Class,Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Length, Text Length,,,,,,,,,,
        f = open('species ranges field name type length report 20241209.csv','w')
        f.write(", ".join(header) + '\n') #Give your csv text here.

        for fc in fc_field_report:

            field_report = fc_field_report[fc]
            fields  = []

            for field in field_report:
                fields.append(field)
                fields.append(field_report[field][0])
                fields.append(field_report[field][1])
                fields.append(field_report[field][2])
                fields.append(field_report[field][3])
                del field

            #print(f"{fc}, {', '.join([str(f) for f in fields])}")

            f.write(f"{fc}, {', '.join([str(f) for f in fields])}" + "\n")

            del fields
            del field_report
            del fc
        del fc_field_report

        ## Python will convert \n to os.linesep
        f.close()

        del f

        del header
        del project_folder

        arcpy.AddMessage(f"\n{'--End' * 10}--")

        # Imports

        # Function parameters
        del project_gdb

    except KeyboardInterrupt:
        raise SystemExit
    except arcpy.ExecuteWarning:
        arcpy.AddWarning(arcpy.GetMessages())
    except arcpy.ExecuteError:
        traceback.print_exc()
        arcpy.AddError(arcpy.GetMessages())
        raise Exception
    except Exception as e:
        arcpy.AddError(str(e))
        raise Exception
    except:
        traceback.print_exc()
        raise Exception
    else:
        try:
            remaining_keys = [key for key in locals().keys() if not key.startswith('__')]
            if remaining_keys:
                arcpy.AddWarning(f"Remaining Keys in '{inspect.stack()[0][3]}': ##--> '{', '.join(remaining_keys)}' <--## Line Number: {traceback.extract_stack()[-1].lineno}")
            else:
                pass
            del remaining_keys
        except:
            raise Exception(traceback.print_exc())
    finally:
        # Cleanup
        arcpy.management.ClearWorkspaceCache()

def update_existing_contacts(project_gdb=""):
    try:
        # Imports
        from lxml import etree
        from io import StringIO
        import copy
        from arcpy import metadata as md

        arcpy.env.overwriteOutput          = True
        arcpy.env.parallelProcessingFactor = "100%"
        arcpy.SetLogMetadata(True)
        arcpy.SetSeverityLevel(2)
        arcpy.SetMessageLevels(['NORMAL']) # NORMAL, COMMANDSYNTAX, DIAGNOSTICS, PROJECTIONTRANSFORMATION

        project_folder = os.path.dirname(project_gdb)
        scratch_folder      = rf"{project_folder}\Scratch"
# Moved dictionaries to JSON
##        root_dict = {"Esri"       :  0, "dataIdInfo" :  1, "mdChar"      :  2,
##                     "mdContact"  :  3, "mdDateSt"   :  4, "mdFileID"    :  5,
##                     "mdLang"     :  6, "mdMaint"    :  7, "mdHrLv"      :  8,
##                     "mdHrLvName" :  9, "refSysInfo" : 10, "spatRepInfo" : 11,
##                     "spdoinfo"   : 12, "dqInfo"     : 13, "distInfo"    : 14,
##                     "eainfo"     : 15, "contInfo"   : 16, "spref"       : 17,
##                     "spatRepInfo" : 18, "dataSetFn" : 19, "Binary"      : 100,}
# Moved dictionaries to JSON
##        RoleCd_dict = {"001" : "Resource Provider", "002" : "Custodian",
##                       "003" : "Owner",             "004" : "User",
##                       "005" : "Distributor",       "006" : "Originator",
##                       "007" : "Point of Contact",  "008" : "Principal Investigator",
##                       "009" : "Processor",         "010" : "Publisher",
##                       "011" : "Author",            "012" : "Collaborator",
##                       "013" : "Editor",            "014" : "Mediator",
##                       "015" : "Rights Holder",}

        workspaces = [project_gdb]

        contacts_xml = rf"{os.environ['USERPROFILE']}\Documents\ArcGIS\Descriptions\contacts.xml"
        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
        contacts_xml_tree = etree.parse(contacts_xml, parser=parser) # To parse from a string, use the fromstring() function instead.
        del parser
        del contacts_xml
        contacts_xml_root = contacts_xml_tree.getroot()
        #etree.indent(contacts_xml_root, space="  ")
        #print(etree.tostring(contacts_xml_root, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())

        for workspace in workspaces:

            arcpy.env.workspace        = workspace
            arcpy.env.scratchWorkspace = rf"{scratch_folder}\scratch.gdb"

            datasets = list()

            walk = arcpy.da.Walk(workspace)

            for dirpath, dirnames, filenames in walk:
                for filename in filenames:
                    datasets.append(os.path.join(dirpath, filename))
                    del filename
                del dirpath, dirnames, filenames
            del walk

            for dataset_path in sorted(datasets):
                #print(dataset_path)
                dataset_name = os.path.basename(dataset_path)

                #print(f"Dataset Name:     {dataset_name}")
                #print(f"\tDataset Location: {os.path.basename(os.path.dirname(dataset_path))}")

                dataset_md = md.Metadata(dataset_path)
                dataset_md_xml = dataset_md.xml
                del dataset_md

                # Parse the XML
                parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
                tree = etree.parse(StringIO(dataset_md_xml), parser=parser)
                root = tree.getroot()
                del parser, dataset_md_xml

                # print(etree.tostring(tree, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
                # etree.indent(tree, space='   ')
                # tree.write(xml_file, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True)

                print(f"Dataset Name: {dataset_name}")

                contact_parents = root.xpath(f".//eMailAdd/text()/ancestor::*//rpIndName/text()/ancestor::*//rpIndName/..")
                #contact_parents = copy.deepcopy(root.xpath(f".//eMailAdd/text()/ancestor::*//rpIndName/text()/ancestor::*//rpIndName/.."))
                #contact_parents = root.xpath(f".//eMailAdd/text()/ancestor::rpCntInfo/..")

                if len(contact_parents) > 0:
                    #count = 0
                    for contact_parent in contact_parents:
                        #count+=1
                        old_contact_parent = contact_parent.tag
                        print(f"\tContact Parent: {old_contact_parent}")
                        #print(etree.tostring(contact_parent, encoding='UTF-8',  method='xml', pretty_print=True).decode())


                        if isinstance(contact_parent.find(f"./rpCntInfo"), type(None)):
                            _xml = etree.XML('<rpCntInfo><cntAddress addressType="both"><delPoint></delPoint><city></city><adminArea></adminArea> \
                                              <postCode></postCode><eMailAdd></eMailAdd><country></country></cntAddress><cntPhone><voiceNum tddtty=""></voiceNum> \
                                              <faxNum></faxNum></cntPhone><cntHours></cntHours><cntOnlineRes><linkage></linkage><protocol>REST Service</protocol> \
                                              <orName></orName><orDesc></orDesc><orFunct><OnFunctCd value="002"></OnFunctCd></orFunct></cntOnlineRes></rpCntInfo>')
                            # Append element
                            contact_parent.append(_xml)
                            del _xml

                        if not isinstance(contact_parent.find(f".//eMailAdd"), type(None)):
                            email_address = contact_parent.find(f".//eMailAdd")
                            #print(f"\t\tEmail Address: {email_address}")
                            if not email_address.text:
                                _user_name = contact_parent.find(f"./rpIndName").text
                                _email_address = _user_name.lower().replace(" ", ".") + "@noaa.gov"
                                email_address.text = _email_address
                                del _email_address, _user_name
                            else:
                                pass
                        else:
                            pass
                            _rpCntInfo = contact_parent.find(f".//rpCntInfo")
                            _cntAddress = _rpCntInfo.find(f".//cntAddress")
                            _user_name = contact_parent.find(f"./rpIndName").text
                            #print(f"\t\tUser Name:     {_user_name}")
                            _email_address = _user_name.lower().replace(" ", ".") + "@noaa.gov"
                            _xml = etree.XML(f'<eMailAdd>{_email_address}</eMailAdd>')
                            # Append element
                            _cntAddress.append(_xml)
                            del _xml, _user_name, _cntAddress, _rpCntInfo

                        if old_contact_parent == "citRespParty":
                            if not isinstance(contact_parent.find(f"./role"), type(None)):
                                user_role = contact_parent.find(f".//RoleCd")
                                user_role.set("value", "002")
                            else:
                                _xml = etree.XML('<role><RoleCd value="002"/></role>')
                                # Append element
                                contact_parent.append(_xml)
                                del _xml

                        if old_contact_parent == "idPoC":
                            if not isinstance(contact_parent.find(f"./role"), type(None)):
                                user_role = contact_parent.find(f".//RoleCd")
                                user_role.set("value", "007")
                            else:
                                _xml = etree.XML('<role><RoleCd value="007"/></role>')
                                # Append element
                                contact_parent.append(_xml)
                                del _xml

                        if old_contact_parent == "distorCont":
                            if not isinstance(contact_parent.find(f"./role"), type(None)):
                                user_role = contact_parent.find(f".//RoleCd")
                                user_role.set("value", "005")
                            else:
                                _xml = etree.XML('<role><RoleCd value="005"/></role>')
                                # Append element
                                contact_parent.append(_xml)
                                del _xml

                        if old_contact_parent == "mdContact":
                            if not isinstance(contact_parent.find(f"./role"), type(None)):
                                user_role = contact_parent.find(f".//RoleCd")
                                user_role.set("value", "011")
                            else:
                                _xml = etree.XML('<role><RoleCd value="011"/></role>')
                                # Append element
                                contact_parent.append(_xml)
                                del _xml

                        if old_contact_parent == "stepProc":
                            if not isinstance(contact_parent.find(f"./role"), type(None)):
                                user_role = contact_parent.find(f".//RoleCd")
                                user_role.set("value", "009")
                            else:
                                _xml = etree.XML('<role><RoleCd value="009"/></role>')
                                # Append element
                                contact_parent.append(_xml)
                                del _xml

                        if not isinstance(contact_parent.find(f"./rpIndName"), type(None)):
                            user_name = contact_parent.find(f"./rpIndName").text
                            print(f"\t\tUser Name:     {user_name}")
                        else:
                            user_name = ""

                        if not isinstance(contact_parent.find(f".//eMailAdd"), type(None)):
                            email_address = contact_parent.find(f".//eMailAdd").text
                            print(f"\t\tEmail Address: {email_address}")
                        else:
                            email_address = ""
                        if not isinstance(contact_parent.find(f".//RoleCd"), type(None)):
                            user_role = contact_parent.find(f".//RoleCd")
                            print(f"\t\tRole:          {user_role.attrib}")
                        else:
                            user_role = ""

                        contact_root = root.xpath(f".//eMailAdd[text()='{email_address}']/ancestor::{old_contact_parent}/rpIndName[text()='{user_name}']/..")
                        #contact_root = copy.deepcopy(root.xpath(f".//eMailAdd[text()='{email_address}']/ancestor::{old_contact_parent}/rpIndName[text()='{user_name}']/.."))
                        #print(etree.tostring(contact_root[0], encoding='UTF-8',  method='xml', pretty_print=True).decode())
                        #print(etree.tostring(contact_root[0], encoding='UTF-8',  method='xml', pretty_print=True).decode())

                        new_contact_root = contacts_xml_root.xpath(f".//eMailAdd[text()='{email_address}']/ancestor::contact/rpIndName[text()='{user_name}']/ancestor::contact/editorSave[text()='True']/..")

                        if len(new_contact_root) == 1:
                            new_contact = copy.deepcopy(new_contact_root[0])
                            new_contact.tag = old_contact_parent
                            #new_contact.append(contact_root[0].find(f".//role"))
                            #print(etree.tostring(new_contact, encoding='UTF-8',  method='xml', pretty_print=True).decode())

                            contact_root[0].getparent().replace(contact_root[0], new_contact)
                            #print(etree.tostring(contact_root[0], encoding='UTF-8',  method='xml', pretty_print=True).decode())

                            del new_contact

                        del new_contact_root, contact_root
                        del user_role, email_address, user_name
                        del old_contact_parent, contact_parent

                dataset_md = md.Metadata(dataset_path)
                dataset_md.xml = etree.tostring(tree, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode()
                dataset_md.save()
                dataset_md.synchronize("ALWAYS")
                del dataset_md

                del contact_parents
                del dataset_name, dataset_path
                del root, tree
            del datasets
            del workspace

        # Declared Variables set in function
        del contacts_xml_root, contacts_xml_tree
        del RoleCd_dict, root_dict
        del project_folder, scratch_folder
        del workspaces

        # Imports
        del md, etree, StringIO, copy

        # Function Parameters
        del project_gdb

    except Exception:
        traceback.print_exc()
    except:
        traceback.print_exc()
    else:
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        pass

def change_existing_contacts(project_gdb="", assigned_contacts=""):
    try:
        # Imports
        from lxml import etree
        from io import StringIO
        import copy
        from arcpy import metadata as md

        # Project modules
        from src.project_tools import pretty_format_xml_file

        arcpy.env.overwriteOutput          = True
        arcpy.env.parallelProcessingFactor = "100%"
        arcpy.SetLogMetadata(True)
        arcpy.SetSeverityLevel(2)
        arcpy.SetMessageLevels(['NORMAL']) # NORMAL, COMMANDSYNTAX, DIAGNOSTICS, PROJECTIONTRANSFORMATION

        project_folder = os.path.dirname(project_gdb)
        scratch_folder      = rf"{project_folder}\Scratch"
# Moved dictionaries to JSON
##        root_dict = {"Esri"       :  0, "dataIdInfo" :  1, "mdChar"      :  2,
##                     "mdContact"  :  3, "mdDateSt"   :  4, "mdFileID"    :  5,
##                     "mdLang"     :  6, "mdMaint"    :  7, "mdHrLv"      :  8,
##                     "mdHrLvName" :  9, "refSysInfo" : 10, "spatRepInfo" : 11,
##                     "spdoinfo"   : 12, "dqInfo"     : 13, "distInfo"    : 14,
##                     "eainfo"     : 15, "contInfo"   : 16, "spref"       : 17,
##                     "spatRepInfo" : 18, "dataSetFn" : 19, "Binary"      : 100,}
# Moved dictionaries to JSON
##        RoleCd_dict = {"001" : "Resource Provider", "002" : "Custodian",
##                       "003" : "Owner",             "004" : "User",
##                       "005" : "Distributor",       "006" : "Originator",
##                       "007" : "Point of Contact",  "008" : "Principal Investigator",
##                       "009" : "Processor",         "010" : "Publisher",
##                       "011" : "Author",            "012" : "Collaborator",
##                       "013" : "Editor",            "014" : "Mediator",
##                       "015" : "Rights Holder",}

        workspaces = [project_gdb]

        contacts_xml = rf"{os.environ['USERPROFILE']}\Documents\ArcGIS\Descriptions\contacts.xml"
        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
        contacts_xml_tree = etree.parse(contacts_xml, parser=parser) # To parse from a string, use the fromstring() function instead.
        del parser
        del contacts_xml
        contacts_xml_root = contacts_xml_tree.getroot()
        #etree.indent(contacts_xml_root, space="  ")
        #print(etree.tostring(contacts_xml_root, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())

        for workspace in workspaces:

            arcpy.env.workspace        = workspace
            arcpy.env.scratchWorkspace = rf"{scratch_folder}\scratch.gdb"

            datasets = list()

            walk = arcpy.da.Walk(workspace)

            for dirpath, dirnames, filenames in walk:
                for filename in filenames:
                    datasets.append(os.path.join(dirpath, filename))
                    del filename
                del dirpath, dirnames, filenames
            del walk

            for dataset_path in sorted(datasets):
                #print(dataset_path)
                dataset_name = os.path.basename(dataset_path)

                #print(f"Dataset Name:     {dataset_name}")
                #print(f"\tDataset Location: {os.path.basename(os.path.dirname(dataset_path))}")

                dataset_md = md.Metadata(dataset_path)
                dataset_md_xml = dataset_md.xml
                del dataset_md

                # Parse the XML
                parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
                tree = etree.parse(StringIO(dataset_md_xml), parser=parser)
                root = tree.getroot()
                del parser, dataset_md_xml

                # print(etree.tostring(tree, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
                # etree.indent(tree, space='   ')
                # tree.write(xml_file, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True)

                print(f"Dataset Name: {dataset_name}")

                for assigned_contact in assigned_contacts:
                    if assigned_contact in ["citRespParty", "idPoC", "mdContact"]:
                        email_address = assigned_contacts[assigned_contact]
                        print(f"\t\tProcessing: {assigned_contact} Email: {email_address}")
                        contact_parents = root.xpath(f".//{assigned_contact}")
                        new_contact_root = contacts_xml_root.xpath(f".//eMailAdd[text()='{email_address}']/ancestor::contact/editorSave[text()='True']/..")
                        print(new_contact_root)
                        if len(new_contact_root) == 1:
                            new_contact = copy.deepcopy(new_contact_root[0])
                            new_contact.tag = assigned_contact
                            #contact_root[0].getparent().replace(contact_root[0], new_contact)
                            print(etree.tostring(contact_root[0], encoding='UTF-8',  method='xml', pretty_print=True).decode())
                            del new_contact
                        del new_contact_root

                        del email_address

##                        for contact_parent in contact_parents:
##                            print(contact_parent.tag)
##                            del contact_parent
                        del contact_parents

                    elif assigned_contact in ["distorCont", "stepProc"]:
                        print(f"\t\tProcessing: {assigned_contact} Email: {assigned_contacts[assigned_contact]}")
                        contact_parents = root.xpath(f".//{assigned_contact}")
##                        for contact_parent in contact_parents:
##                            print(contact_parent.tag)
##                            del contact_parent
                        del contact_parents
                    else:
                        pass

                    del assigned_contact


##                    for contact_parent in contact_parents:
##                        if isinstance(contact_parent, type(None)):
##                            print(f"\t\t###--->>> {assigned_contact} is missing!! <<<---###")
##                        elif not isinstance(contact_parent, type(None)):
##                            if assigned_contact in ["citRespParty", "idPoC", "mdContact"]:
##                                print(f"\t\tProcessing: {assigned_contact}")
##                                for contact in contact_parent:
##                                    print(contact.tag)
##                                email_address = contact_parent.find(f".//eMailAdd")
##                                if isinstance(email_address, type(None)):
##                                    print(f"\t\t\tEmail Address is missing")
##                                    kids = contact_parent.iterchildren()
##                                    for kid in kids:
##                                        print(f"\t\t\t\t\t{kid.tag}: {kid.text}")
##                                        del kid
##                                    del kids
##                                elif not isinstance(contact_parent, type(None)):
##                                    print(f"\t\t\tEmail Address: {email_address.text}")
##
##                                del email_address
##
##                            elif assigned_contact in ["distorCont", "stepProc"]:
##                                print(f"\t\tProcessing: {assigned_contact}")
##                                email_address = contact_parent.find(f".//eMailAdd")pIndName
##                                if isinstance(email_address, type(None)):
##                                    print(f"\t\t\tEmail Address is missing")
##                                    kids = contact_parent.iterchildren()
##                                    for kid in kids:
##                                        print(f"\t\t\t\t\t{kid.tag}: {kid.text}")
##                                        del kid
##                                    del kids
##                                elif not isinstance(contact_parent, type(None)):
##                                    print(f"\t\t\tEmail Address: {email_address.text}")
##                                del email_address


                      #  {"citRespParty" : {"Resource Citation Contacts" : "nikki.wildart@noaa.gov"},
                      #   "idPoC"        : {"Points of Contact"          : "nikki.wildart@noaa.gov"},
                      #   "distorCont"   : {"Distribution Contacts"      : "nikki.wildart@noaa.gov"},
                      #   "mdContact"    : {"Metadata Contacts"          : "nikki.wildart@noaa.gov"},
                      #   "stepProc"     : {"Step Processors"            : "nikki.wildart@noaa.gov",},
                      #          }


##                            print(f"\t\tProcessing: {assigned_contact}")
##                            #print(etree.tostring(contact_parent, encoding='UTF-8',  method='xml', pretty_print=True).decode())
##                            rpIndNames = contact_parent.xpath(f".//rpIndName")
##                            if len(rpIndNames) == 0:
##                                print(f"\t\t\trpIndName is missing")
##                                kids = contact_parent.iterchildren()
##                                for kid in kids:
##                                    print(kid.tag)
##                                    del kid
##                                del kids
##
##                            elif len(rpIndNames) > 0:
##                                print(f"\t\t\tThere are {len(rpIndNames)} rpIndName")
##                                for rpIndName in rpIndNames:
##                                    print(f"\t\t\t\tContact: {rpIndName.text}")
##
##                                    del rpIndName
##                            del rpIndNames

                    #"citRespParty"
                    #"idPoC"
                    #"distorCont"
                    #"mdContact"
                    #"stepProc"

##                        else:
##                            pass
##
##                        del contact_parent
##                    del assigned_contact

                    #del contact_parents
##                contact_parents = root.xpath(f".//eMailAdd/text()/ancestor::*//rpIndName/text()/ancestor::*//rpIndName/..")
##
##                if len(contact_parents) > 0:
##                    #count = 0
##                    for contact_parent in contact_parents:
##                        #count+=1
##                        old_contact_parent = contact_parent.tag
##                        print(f"\tContact Parent: {old_contact_parent}")
##                        #print(etree.tostring(contact_parent, encoding='UTF-8',  method='xml', pretty_print=True).decode())
##
##
##                        if isinstance(contact_parent.find(f"./rpCntInfo"), type(None)):
##                            _xml = etree.XML('<rpCntInfo><cntAddress addressType="both"><delPoint></delPoint><city></city><adminArea></adminArea> \
##                                              <postCode></postCode><eMailAdd></eMailAdd><country></country></cntAddress><cntPhone><voiceNum tddtty=""></voiceNum> \
##                                              <faxNum></faxNum></cntPhone><cntHours></cntHours><cntOnlineRes><linkage></linkage><protocol>REST Service</protocol> \
##                                              <orName></orName><orDesc></orDesc><orFunct><OnFunctCd value="002"></OnFunctCd></orFunct></cntOnlineRes></rpCntInfo>')
##                            # Append element
##                            contact_parent.append(_xml)
##                            del _xml
##
##                        if not isinstance(contact_parent.find(f".//eMailAdd"), type(None)):
##                            email_address = contact_parent.find(f".//eMailAdd")
##                            #print(f"\t\tEmail Address: {email_address}")
##                            if not email_address.text:
##                                _user_name = contact_parent.find(f"./rpIndName").text
##                                _email_address = _user_name.lower().replace(" ", ".") + "@noaa.gov"
##                                email_address.text = _email_address
##                                del _email_address, _user_name
##                            else:
##                                pass
##                        else:
##                            pass
##                            _rpCntInfo = contact_parent.find(f".//rpCntInfo")
##                            _cntAddress = _rpCntInfo.find(f".//cntAddress")
##                            _user_name = contact_parent.find(f"./rpIndName").text
##                            #print(f"\t\tUser Name:     {_user_name}")
##                            _email_address = _user_name.lower().replace(" ", ".") + "@noaa.gov"
##                            _xml = etree.XML(f'<eMailAdd>{_email_address}</eMailAdd>')
##                            # Append element
##                            _cntAddress.append(_xml)
##                            del _xml, _user_name, _cntAddress, _rpCntInfo
##
##                        if old_contact_parent == "citRespParty":
##                            if not isinstance(contact_parent.find(f"./role"), type(None)):
##                                user_role = contact_parent.find(f".//RoleCd")
##                                user_role.set("value", "002")
##                            else:
##                                _xml = etree.XML('<role><RoleCd value="002"/></role>')
##                                # Append element
##                                contact_parent.append(_xml)
##                                del _xml
##
##                        if old_contact_parent == "idPoC":
##                            if not isinstance(contact_parent.find(f"./role"), type(None)):
##                                user_role = contact_parent.find(f".//RoleCd")
##                                user_role.set("value", "007")
##                            else:
##                                _xml = etree.XML('<role><RoleCd value="007"/></role>')
##                                # Append element
##                                contact_parent.append(_xml)
##                                del _xml
##
##                        if old_contact_parent == "distorCont":
##                            if not isinstance(contact_parent.find(f"./role"), type(None)):
##                                user_role = contact_parent.find(f".//RoleCd")
##                                user_role.set("value", "005")
##                            else:
##                                _xml = etree.XML('<role><RoleCd value="005"/></role>')
##                                # Append element
##                                contact_parent.append(_xml)
##                                del _xml
##
##                        if old_contact_parent == "mdContact":
##                            if not isinstance(contact_parent.find(f"./role"), type(None)):
##                                user_role = contact_parent.find(f".//RoleCd")
##                                user_role.set("value", "011")
##                            else:
##                                _xml = etree.XML('<role><RoleCd value="011"/></role>')
##                                # Append element
##                                contact_parent.append(_xml)
##                                del _xml
##
##                        if old_contact_parent == "stepProc":
##                            if not isinstance(contact_parent.find(f"./role"), type(None)):
##                                user_role = contact_parent.find(f".//RoleCd")
##                                user_role.set("value", "009")
##                            else:
##                                _xml = etree.XML('<role><RoleCd value="009"/></role>')
##                                # Append element
##                                contact_parent.append(_xml)
##                                del _xml
##
##
##                        #if count == 1:
##                        #    _xml = etree.XML('<role><RoleCd value="011"/></role>')
##                        #    # Append element
##                        #    contact_root[0].append(_xml)
##                        #    # Change element name
##                        #    contact_parent.tag = "mdContact"
##                        #    del _xml
##                        #elif count == 2:
##                        #    _xml = etree.XML('<role><RoleCd value="005"/></role>')
##                        #    contact_root[0].append(_xml)
##                        #    contact_parent.tag = "distributor"
##                        #    del _xml
##                        #elif count == 3:
##                        #    _xml = etree.XML('<role><RoleCd value="002"/></role>')
##                        #    contact_root[0].append(_xml)
##                        #    contact_parent.tag = "citRespParty"
##                        #    del _xml
##                        #elif count == 4:
##                        #    _xml = etree.XML('<role><RoleCd value="007"/></role>')
##                        #    contact_root[0].append(_xml)
##                        #    contact_parent.tag = "idPoC"
##                        #    del _xml
##
##                        if not isinstance(contact_parent.find(f"./rpIndName"), type(None)):
##                            user_name = contact_parent.find(f"./rpIndName").text
##                            print(f"\t\tUser Name:     {user_name}")
##                        else:
##                            user_name = ""
##
##                        if not isinstance(contact_parent.find(f".//eMailAdd"), type(None)):
##                            email_address = contact_parent.find(f".//eMailAdd").text
##                            print(f"\t\tEmail Address: {email_address}")
##                        else:
##                            email_address = ""
##                        if not isinstance(contact_parent.find(f".//RoleCd"), type(None)):
##                            user_role = contact_parent.find(f".//RoleCd")
##                            print(f"\t\tRole:          {user_role.attrib}")
##                        else:
##                            user_role = ""
##
##                        contact_root = root.xpath(f".//eMailAdd[text()='{email_address}']/ancestor::{old_contact_parent}/rpIndName[text()='{user_name}']/..")
##                        #contact_root = copy.deepcopy(root.xpath(f".//eMailAdd[text()='{email_address}']/ancestor::{old_contact_parent}/rpIndName[text()='{user_name}']/.."))
##                        #print(etree.tostring(contact_root[0], encoding='UTF-8',  method='xml', pretty_print=True).decode())
##
##                        new_contact_root = contacts_xml_root.xpath(f".//eMailAdd[text()='{email_address}']/ancestor::contact/rpIndName[text()='{user_name}']/ancestor::contact/editorSave[text()='True']/..")
##
##                        if len(new_contact_root) == 1:
##                            new_contact = copy.deepcopy(new_contact_root[0])
##                            new_contact.tag = old_contact_parent
##                            #new_contact.append(contact_root[0].find(f".//role"))
##                            #print(etree.tostring(new_contact, encoding='UTF-8',  method='xml', pretty_print=True).decode())
##
##                            contact_root[0].getparent().replace(contact_root[0], new_contact)
##                            #print(etree.tostring(contact_root[0], encoding='UTF-8',  method='xml', pretty_print=True).decode())
##
##                            del new_contact
##
##                        del new_contact_root, contact_root
##                        del user_role, email_address, user_name
##                        del old_contact_parent, contact_parent
##
##                dataset_md = md.Metadata(dataset_path)
##                dataset_md.xml = etree.tostring(tree, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode()
##                dataset_md.save()
##                dataset_md.synchronize("ALWAYS")
##                del dataset_md
##
##                del contact_parents
                del dataset_name, dataset_path
                del root, tree
            del datasets
            del workspace

        # Declared Variables set in function
        del contacts_xml_root, contacts_xml_tree
        del RoleCd_dict, root_dict
        del project_folder, scratch_folder
        del workspaces

        # Imports
        del md, etree, StringIO, copy, pretty_format_xml_file

        # Function Parameters
        del project_gdb, assigned_contacts

    except Exception:
        traceback.print_exc()
    except:
        traceback.print_exc()
    else:
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        pass

# Main function
def main(project_folder=str()):
    try:
        from time import gmtime, localtime, strftime, time
        # Set a start time so that we can see how log things take
        start_time = time()
        print(f"{'-' * 80}")
        print(f"Python Script:  {os.path.basename(__file__)}")
        print(f"Location:       {os.path.dirname(__file__)}")
        print(f"Python Version: {sys.version} Environment: {os.path.basename(sys.exec_prefix)}")
        print(f"{'-' * 80}\n")
        project_gdb     = rf"{project_folder}\National Mapper.gdb"
        #source_zip_file = rf"{project_folder}\NMFS_ESA_Range.gdb (20241121).zip"
        #source_zip_file = rf"{project_folder}\NMFS_ESA_Range.gdb (20241209).zip"
        #source_gdb      = rf"{project_folder}\NMFS_ESA_Range_20241121.gdb"
        source_gdb      = rf"{project_folder}\NMFS_ESA_Range.gdb"

        version = "20241212"

        SchemaFieldReport = False
        if SchemaFieldReport:
            schema_field_report(project_gdb=project_gdb)
        del SchemaFieldReport

        UpdateExistingContacts = False
        if UpdateExistingContacts:
            update_existing_contacts(project_gdb=project_gdb)
        else:
            pass
        del UpdateExistingContacts

        ChangeExistingContacts = False
        if ChangeExistingContacts:
            #assigned_contacts = {"citRespParty" : {"Resource Citation Contacts" : "nikki.wildart@noaa.gov"},
            #                     "idPoC"        : {"Points of Contact"          : "nikki.wildart@noaa.gov"},
            #                     "distorCont"   : {"Distribution Contacts"      : "nikki.wildart@noaa.gov"},
            #                     "mdContact"    : {"Metadata Contacts"          : "nikki.wildart@noaa.gov"},
            #                     "stepProc"     : {"Step Processors"            : "nikki.wildart@noaa.gov",},
            #                    }
            assigned_contacts = {"citRespParty" : {"pIndName" : "Nikki Wildart", "eMailAdd" : "nikki.wildart@noaa.gov"},
                                 "idPoC"        : {"pIndName" : "Nikki Wildart", "eMailAdd" : "nikki.wildart@noaa.gov"},
                                 "distorCont"   : {"pIndName" : "Nikki Wildart", "eMailAdd" : "nikki.wildart@noaa.gov"},
                                 "mdContact"    : {"pIndName" : "Nikki Wildart", "eMailAdd" : "nikki.wildart@noaa.gov"},
                                 "stepProc"     : {"pIndName" : "Nikki Wildart", "eMailAdd" : "nikki.wildart@noaa.gov"},
                                }
            change_existing_contacts(project_gdb=project_gdb, assigned_contacts=assigned_contacts)
            del assigned_contacts
        else:
            pass
        del ChangeExistingContacts

        # Declared Variables
        del project_gdb, source_gdb, version
        # Imports
        del project_folder

        # Elapsed time
        end_time = time()
        elapse_time =  end_time - start_time
        print(flush=True)
        print(f"\n{'-' * 80}", flush=True)
        print(f"Python script: {os.path.basename(__file__)} successfully completed {strftime('%a %b %d %I:%M %p', localtime())}", flush=True)
        print(u"Elapsed Time {0} (H:M:S)".format(strftime("%H:%M:%S", gmtime(elapse_time))), flush=True)
        print(f"{'-' * 80}", flush=True)
        del elapse_time, end_time, start_time
        del gmtime, localtime, strftime, time

    except:
        traceback.print_exc()
    else:
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        # Cleanup
        arcpy.management.ClearWorkspaceCache()

if __name__ == '__main__':
    try:
        main(project_folder=rf"{os.path.dirname(os.path.dirname(__file__))}")
    except:
        traceback.print_exc()
