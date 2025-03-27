# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john.f.kennedy
#
# Created:     03/03/2024
# Copyright:   (c) john.f.kennedy 2024
# Licence:     <your licence>
# -------------------------------------------------------------------------------
import os, sys  # built-ins first
import traceback
import importlib
import inspect

#import arcpy  # third-parties second

def new_function():
    try:

        pass

    except:
        traceback.print_exc()
    else:
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        pass

# Selectors
def selectors(project_gdb=""):
    try:
        # Imports
        from lxml import etree
        from io import StringIO
        import copy
        import arcpy
        from arcpy import metadata as md

        arcpy.env.overwriteOutput          = True
        arcpy.env.parallelProcessingFactor = "100%"
        arcpy.SetLogMetadata(True)
        arcpy.SetSeverityLevel(2)
        arcpy.SetMessageLevels(['NORMAL']) # NORMAL, COMMANDSYNTAX, DIAGNOSTICS, PROJECTIONTRANSFORMATION

        project_folder = os.path.dirname(project_gdb)
        scratch_folder = rf"{project_folder}\Scratch"
        workspaces = [project_gdb]

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

            #for dataset_path in sorted([d for d in datasets if d.endswith("SeaTurtleLeatherback_20210129")]):
            for dataset_path in sorted(datasets):
                dataset_name = os.path.basename(dataset_path)
                print(f"Dataset Name: {dataset_name}")
                #print(f"\tDataset Location: {os.path.basename(os.path.dirname(dataset_path))}")

                dataset_md = md.Metadata(dataset_path)
                dataset_md_xml = dataset_md.xml
                del dataset_md

                # Parse the XML
                parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
                tree = etree.parse(StringIO(dataset_md_xml), parser=parser)
                root = tree.getroot()
                del parser, dataset_md_xml

                # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                # #    Separate your steps with /. Use two (//) if you don’t want to select direct children.    # #
                # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
##                print("EXAMPLE #1")
##                print(f"\tPrefix: ., What: everywhere,  Descendant: all elements, Selector: .")
##                elements = tree.xpath(".")
##                count = 0; element_count = len(elements)
##                for element in elements:
##                    count+=1
##                    print(f"\tElement: {element.tag:<12} {count} of {element_count}")
##                    etree.indent(tree, space='   ')
##                    #print(etree.tostring(element, encoding='UTF-8', method='xml', pretty_print=True).decode())
##                    # Output: the complete XML document
##                    del element
##                del count, element_count
##                del elements
##
##                print("EXAMPLE #2")
##                print(f"\tPrefix: /, What: everywhere,  Descendant: none, Selector: /")
##                elements = tree.xpath("/")
##                count = 0; element_count = len(elements)
##                for element in elements:
##                    count+=1
##                    print(f"\tElement: {element.tag:<12} {count} of {element_count}")
##                    etree.indent(tree, space='   ')
##                    #print(etree.tostring(element, encoding='UTF-8', method='xml', pretty_print=True).decode())
##                    # Output: nothing. / character seperates steps. No selectors were entered on either side
##                    # of the /. Use // characters if you don’t want to select direct children
##                    del element
##                del count, element_count
##                del elements

##                print("EXAMPLE #3")
##                print(f"\tPrefix: ./, What: list children of the parent element,  Descendant: children of parent, Selector: ./rpIndName")
##                print(f"\t\tNo results, as rpIndName is not a direct descendant of parent")
##                elements = root.xpath("./rpIndName")
##                count = 0; element_count = len(elements)
##                for element in elements:
##                    count+=1
##                    print(f"\tElement: {element.tag:<12} {count} of {element_count}")
##                    etree.indent(tree, space='   ')
##                    #print(etree.tostring(element, encoding='UTF-8', method='xml', pretty_print=True).decode())
##                    # Output: nothing. The . indicates all elements, the / seperates the selectors, but the selector
##                    # is not a direct descendant of parent
##                    del element
##                del count, element_count
##                del elements

##                print("EXAMPLE #4")
##                print(f"\tPrefix: //, What: a child found anywhere, Descendant: rpIndName, Selector: //rpIndName")
##                print(f"\t\tFinds all elements with the tag rpIndName. Does not check for the existance of text")
##                elements = tree.xpath("//rpIndName") # descendant : rpIndName, selector : //rpIndName, prefix : //, what : anywhere
##                count = 0; element_count = len(elements)
##                for element in elements:
##                    count+=1
##                    print(f"\tElement: {element.tag:<12} {count} of {element_count}")
##                    etree.indent(tree, space='   ')
##                    print(etree.tostring(element, encoding='UTF-8',  method='xml', pretty_print=True).decode())
##                    # Output -- the prefixes and selector combination results in finding all elements with the select tag
##                    '''<rpIndName xmlns="">Jennifer Schultz</rpIndName>'''
##                    '''<rpIndName xmlns="">Jennifer Schultz</rpIndName>'''
##                    del element
##                del count, element_count
##                del elements

##                print("EXAMPLE #4a")
##                print(f"\tPrefix: //, What: a child found anywhere, Descendant: rpIndName, Selector: //rpIndName")
##                print(f"\t\tFinds all elements with the tag rpIndName. Checks for text (one selector /text()) and the find parent (one selector above) /..")
##                print(f"\t\t\tNOTE: without the /.. the result would be a text object created using the text() function")
##                elements = tree.xpath("//rpIndName/text()/..") # descendant : rpIndName, selector : //rpIndName, prefix : //, what : anywhere
##                count = 0; element_count = len(elements)
##                for element in elements:
##                    count+=1
##                    print(f"\tElement: {element.tag:<12} {count} of {element_count}")
##                    etree.indent(tree, space='   ')
##                    print(etree.tostring(element, encoding='UTF-8',  method='xml', pretty_print=True).decode())
##                    # Output -- the prefixes and selector combination results in finding all elements with the select tag
##                    '''<rpIndName xmlns="">Jennifer Schultz</rpIndName>'''
##                    '''<rpIndName xmlns="">Jennifer Schultz</rpIndName>'''
##                    del element
##                del count, element_count
##                del elements

##                print("EXAMPLE #5")
##                print(f"\tPrefix: //, What: any elements with the first and second selector,  Descendant: mdContact, rpIndName, Selector: //mdContact//rpIndName")
##                print(f"\t\tThe first selector takes precident. Selects for rpIndName that is a descendate of mdContact")
##                print(f"\t\tNOTE: this case selects for a element that has a named descendent")
##                elements = tree.xpath("//mdContact//rpIndName")
##                count = 0; element_count = len(elements)
##                for element in elements:
##                    count+=1
##                    print(f"\tElement: {element.tag:<12} {count} of {element_count}")
##                    etree.indent(tree, space='   ')
##                    print(etree.tostring(element, encoding='UTF-8',  method='xml', pretty_print=True).decode())
##                    # Output: any elements with the first and second selector
##                    '''<rpIndName xmlns="">Jennifer Schultz</rpIndName>'''
##                    del element
##                del count, element_count
##                del elements

##                print("EXAMPLE #6")
##                print(f"\tPrefix: ./, What: any elements with the first and second selector,  Descendant: mdContact, rpIndName, Selector: ./mdContact/rpIndName")
##                print(f"\t\tSelects for rpIndName that is a descendate of mdContact, returning unique element")
##                elements = tree.xpath("./mdContact/rpIndName")
##                count = 0; element_count = len(elements)
##                for element in elements:
##                    count+=1
##                    print(f"\tElement: {element.tag:<12} {count} of {element_count}")
##                    etree.indent(tree, space='   ')
##                    #print(etree.tostring(element, encoding='UTF-8',  method='xml', pretty_print=True).decode())
##                    # Output: any elements with the first and second selector
##                    '''<rpIndName xmlns="">Jennifer Schultz</rpIndName>'''
##                    del element
##                del count, element_count
##                del elements

##                print("EXAMPLE #7")
##                print(f"\tPrefix: //, What: anywhere,  Descendant: rpIndName, Selector: //rpIndName, text(), /..")
##                elements = tree.xpath("//rpIndName/text()/../..") # 2 * /.. moves the focus from the text() selector, to the rpIndName, and then to the parent of rpIndName
##                count = 0; element_count = len(elements)
##                if not isinstance(element_count, type(None)) and len(elements) > 0:
##                    for element in elements:
##                        count+=1
##                        print(f"\tElement: {element.tag:<12} {count} of {element_count}")
##                        etree.indent(tree, space='   ')
##                        print(etree.tostring(element, encoding='UTF-8',  method='xml', pretty_print=True).decode())
##                        del element
##                else:
##                    print(f"\t\tNo Results.")
##                del count, element_count
##                del elements

##                print("EXAMPLE #8")
##                print(f"\tPrefix: //, What: anywhere,  Descendant: rpIndName, Selector: //rpIndName, text(), /..")
##                print(f"\t\tNote: using text() to test for a persons name")
##                search_name = "Jennifer Schultz"
##                elements = tree.xpath(f"//rpIndName[text() = '{search_name}']/..")
##                count = 0; element_count = len(elements)
##                if not isinstance(element_count, type(None)) and len(elements) > 0:
##                    for element in elements:
##                        count+=1
##                        print(f"\tElement: {element.tag:<12} {count} of {element_count}")
##                        etree.indent(tree, space='   ')
##                        print(etree.tostring(element, encoding='UTF-8',  method='xml', pretty_print=True).decode())
##                        del element
##                        # Element: idPoC        1 of 2
##                        '''<idPoC xmlns="">
##                             <rpIndName>Jennifer Schultz</rpIndName>
##                             <rpOrgName>NMFS</rpOrgName>
##                             <rpPosName>OPR</rpPosName>
##                             <role>
##                                <RoleCd value="006"/>
##                             </role>
##                             <displayName>Jennifer Schultz</displayName>
##                          </idPoC>'''
##                        # Element: mdContact    2 of 2
##                        '''<mdContact xmlns="">
##                              <rpIndName>Jennifer Schultz</rpIndName>
##                              <rpOrgName>NMFS</rpOrgName>
##                              <rpPosName>OPR</rpPosName>
##                              <role>
##                                 <RoleCd value="006"/>
##                              </role>
##                           </mdContact>'''
##
##                else:
##                    print(f"\t\tNo Results.")
##                del count, element_count
##                del elements
##                del search_name

##                print("EXAMPLE #9")
##                print(f"\tPrefix: //, What: anywhere,  Descendant: rpIndName, Selector: //rpIndName, text(), /..")
##                elements = tree.xpath("//eMailAdd/text()/../../../..") # 2 * /.. moves the focus from the text() selector, to the rpIndName, and then to the parent of rpIndName
##                count = 0; element_count = len(elements)
##                if not isinstance(element_count, type(None)) and len(elements) > 0:
##                    for element in elements:
##                        count+=1
##                        print(f"\tElement: {element.tag:<12} {count} of {element_count}")
##                        etree.indent(tree, space='   ')
##                        print(etree.tostring(element, encoding='UTF-8',  method='xml', pretty_print=True).decode())
##                        del element
##                else:
##                    print(f"\t\tNo Results.")
##                del count, element_count
##                del elements

##                print("EXAMPLE #10")
##                print(f"\tPrefix: //, What: anywhere,  Descendant: rpIndName, Selector: //rpIndName, text(), /..")
##                print(f"\t\tNOTE: This creates an 'AND' condition statement. 'This and that.'")
##                print(f"\t\tNOTE: In this case, the target element is the common parent of the two given elements that have text")
##                elements = tree.xpath("//eMailAdd/text()/../../../..//rpIndName/text()/../..") # 2 * /.. moves the focus from the text() selector, to the rpIndName, and then to the parent of rpIndName
##                count = 0; element_count = len(elements)
##                if not isinstance(element_count, type(None)) and len(elements) > 0:
##                    for element in elements:
##                        count+=1
##                        print(f"\tElement: {element.tag:<12} {count} of {element_count}")
##                        etree.indent(tree, space='   ')
##                        print(etree.tostring(element, encoding='UTF-8',  method='xml', pretty_print=True).decode())
##                        del element
##                else:
##                    print(f"\t\tNo Results.")
##                del count, element_count
##                del elements

##                print("EXAMPLE #11")
##                print(f"\tPrefix: //, What: anywhere,  Descendant: rpIndName, Selector: //rpIndName, text(), /..")
##                print(f"\t\tNOTE: result includes all eMailAdd elements with text and all rpIndName elements also with text")
##                print(f"\t\tNOTE: However, rpIndName elements with text, my not have sibling-descendents of eMailAdd elements with text")
##                #elements = tree.xpath("//rpCntInfo/cntAddress/eMailAdd/text()/ancestor::*//rpIndName/text()/ancestor::*//rpIndName/..")
##                elements = tree.xpath("//eMailAdd/text()/ancestor::*//rpIndName/text()/../..")
##                #elements = tree.xpath("//rpIndName/text()/ancestor::*//eMailAdd/text()/../../../..")
##                count = 0; element_count = len(elements)
##                if not isinstance(element_count, type(None)) and len(elements) > 0:
##                    for element in elements:
##                        count+=1
##                        print(f"\tElement: {element.tag:<12} {count} of {element_count}")
##                        etree.indent(tree, space='   ')
##                        print(etree.tostring(element, encoding='UTF-8',  method='xml', pretty_print=True).decode())
##                        del element
##                else:
##                    print(f"\t\tNo Results.")
##                del count, element_count
##                del elements

##                print("EXAMPLE #11")
##                print(f"\tPrefix: //, What: anywhere,  Descendant: rpIndName, Selector: //rpIndName, text(), /..")
##                elements = tree.xpath("//eMailAdd/text()ancestor::*[not //rpIndName/text()]/../..") # 2 * /.. moves the focus from the text() selector, to the rpIndName, and then to the parent of rpIndName
##                count = 0; element_count = len(elements)
##                if not isinstance(element_count, type(None)) and len(elements) > 0:
##                    for element in elements:
##                        count+=1
##                        print(f"\tElement: {element.tag:<12} {count} of {element_count}")
##                        etree.indent(tree, space='   ')
##                        print(etree.tostring(element, encoding='UTF-8',  method='xml', pretty_print=True).decode())
##                        del element
##                else:
##                    print(f"\t\tNo Results.")
##                del count, element_count
##                del elements
##                print("\n")

                del dataset_name, tree, root

            del workspace, datasets, dataset_path

        #Prefixes
        # Prefix Example              What
        # //     //hr[@class='edge']  Anywhere
        # ./     ./a                  Relative
        # /     /html/body/div        Root

        #Selectors
        # Descendant           selectors
        # h1                   //h1
        # mdContact            //mdContact              # Example #1
        # rpIndName            //rpIndName              # Example #2
        # div p                //div//p
        # mdContact rpIndName  //mdContact//rpIndName   # Example #3

        # ul > li              //ul/li
        # ul > li > a          //ul/li/a
        # div > *              //div/*
        # :root                /
        # :root > body         /body


        # Declared variables
        del project_folder, scratch_folder, workspaces
        # Imports
        del etree, StringIO, copy, arcpy, md
        # Function parameters
        del project_gdb

    except:
        traceback.print_exc()
    else:
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        pass

def main(project_gdb=""):
    try:
        from time import gmtime, localtime, strftime, time
        # Set a start time so that we can see how log things take
        start_time = time()
        print(f"{'-' * 80}")
        print(f"Python Script:  {os.path.basename(__file__)}")
        print(f"Location:       ..\Documents\ArcGIS\Projects\..\{os.path.basename(os.path.dirname(__file__))}\{os.path.basename(__file__)}")
        print(f"Python Version: {sys.version}")
        print(f"Environment:    {os.path.basename(sys.exec_prefix)}")
        print(f"{'-' * 80}\n")

        selectors(project_gdb)

        root_dict = {"Esri"       :  0, "dataIdInfo"  :  1, "mdChar"      :  2,
                     "mdContact"  :  3, "mdDateSt"    :  4, "mdFileID"    :  5,
                     "mdLang"     :  6, "mdMaint"     :  7, "mdHrLv"      :  8,
                     "mdHrLvName" :  9, "mdStanName"  : 10, "mdStanVer"   : 11,
                     "refSysInfo" : 12, "spatRepInfo" : 13, "spdoinfo"    : 14,
                     "dqInfo"     : 15, "distInfo"    : 16, "eainfo"      : 17,
                     "contInfo"   : 18, "spref"       : 19, "spatRepInfo" : 20,
                     "dataSetFn"  : 19, "Binary"      : 100,}

        esri_dict ={"CreaDate"      :  0, "CreaTime"   :  1, "ArcGISFormat"   : 2,
                    "ArcGISstyle"   :  3, "SyncOnce"   :  4, "DataProperties" : 5,
                    "itemProps"     :  0, "itemName"   :  0, "imsContentType" : 1,
                    "nativeExtBox"  :  2, "westBL"     :  0, "eastBL"   :  1, "southBL"  : 2,
                    "northBL"       :  3, "exTypeCode" :  4, "coordRef" :  1, "type"     : 0,
                    "geogcsn"       :  2, "csUnits"    :  3, "peXml"    :  4, "SyncDate" : 6,
                    "SyncTime"      :  7, "ModDate"    :  8, "ModTime"  :  9,
                    "scaleRange"    : 10, "minScale"   : 11, "maxScale" : 12,
                    "ArcGISProfile" : 13,}

        dataIdInfo_dict = { "idCitation" :  0, "searchKeys" :  1, "idPurp"    : 2,
                            "idAbs"      :  3, "idCredit"   :  4, "idStatus"  : 5,
                            "idPoC"      :  6, "themeKeys"  :  7, "placeKeys" : 8,
                            "tempKeys"   : 9, "otherKeys"   : 10, "resConst"  : 12,
                            "resMaint"   : 13, "envirDesc"  : 14, "dataLang"  : 15,
                            "dataChar"   : 16, "spatRpType" : 17, "dataExt"   : 18,
                            "" : 19, "tpCat"      : 20,}

        idCitation_dict = {"idCitation" : 0, "resTitle" : 0, "resAltTitle" : 1,
                           "collTitle"  : 2, "presForm" : 3, "PresFormCd"  : 0,
                           "fgdcGeoform" : 1, "date" : 4, "createDate" : 0,
                           "pubDate"    : 1, "reviseDate" : 2, "citRespParty"  : 6,
                           }

        contact_dict = {"editorSource" : 0, "editorDigest" : 1,"rpIndName"     : 2,
                        "rpOrgName"    : 3, "rpPosName"    : 4, "rpCntInfo"    : 5,
                        "cntAddress"   : 0, "delPoint"     : 0, "city"         : 1,
                        "adminArea"    : 2, "postCode"     : 3, "eMailAdd"     : 4,
                        "country"      : 5, "cntPhone"     : 1, "voiceNum"     : 0,
                        "faxNum"       : 1, "cntHours"     : 2, "cntOnlineRes" : 3,
                        "linkage"      : 0, "protocol"     : 1, "orName"       : 2,
                        "orDesc"       : 3, "orFunct"      : 4, "OnFunctCd"    : 0,
                        "editorSave"   : 6, "displayName"  : 7, "role"         : 8,
                        "RoleCd"       : 0,
                        }

        dqInfo_dict = { "dqScope"     : 0, "scpLvl"     : 0, "ScopeCd"    : 0,
                        "scpLvlDesc"  : 1, "datasetSet" : 0, "report"     : 1,
                        "measDesc"    : 0, "report"     : 2, "measDesc"   : 0,
                        "dataLineage" : 3, "statement"  : 0, "dataSource" : 1,
                        "srcDesc"     : 0, "srcCitatn"  : 1, "resTitle"   : 0,
                        "date"        : 1, "createDate" : 0, "prcStep"    : 2,
                        "stepDesc"    : 0, "stepProc"   : 1, "stepDateTm" : 2,
                      }

        RoleCd_dict = {"001" : "Resource Provider", "002" : "Custodian",
                       "003" : "Owner",             "004" : "User",
                       "005" : "Distributor",       "006" : "Originator",
                       "007" : "Point of Contact",  "008" : "Principal Investigator",
                       "009" : "Processor",         "010" : "Publisher",
                       "011" : "Author",            "012" : "Collaborator",
                       "013" : "Editor",            "014" : "Mediator",
                       "015" : "Rights Holder",}

        tpCat_dict = {"002": '<tpCat><TopicCatCd value="002"></TopicCatCd></tpCat>',
         "007": '<tpCat><TopicCatCd value="007"></TopicCatCd></tpCat>',
         "014": '<tpCat><TopicCatCd value="014"></TopicCatCd></tpCat>',}

        # ###################### DisMAP ########################################
        contacts = {"citRespParty"     : {"rpIndName" : "Timothy J Haverland",                   "eMailAdd" : "tim.haverland@noaa.gov"},
                        "idPoC"        : {"rpIndName" : "Melissa Karp",                          "eMailAdd" : "melissa.karp@noaa.gov"},
                        "distorCont"   : {"rpIndName" : "NMFS Office of Science and Technology", "eMailAdd" : "tim.haverland@noaa.gov"},
                        "mdContact"    : {"rpIndName" : "John F Kennedy",                        "eMailAdd" : "john.f.kennedy@noaa.gov"},
                        "stepProc"     : [{"rpIndName" : "John F Kennedy",                        "eMailAdd" : "john.f.kennedy@noaa.gov"},
                                          {"rpIndName" : "Melissa Karp",                          "eMailAdd" : "melissa.karp@noaa.gov"},
                                         ],}
        # ###################### DisMAP ########################################
        # ###################### ESA ########################################

        contacts = {"citRespParty"     : [{"role"  : "Custodian",        "rpIndName" : "Nikki Wildart",       "eMailAdd" : "nikki.wildart@noaa.gov"},],
                        "idPoC"        : [{"role"  : "Point of Contact", "rpIndName" : "Nikki Wildart",       "eMailAdd" : "nikki.wildart@noaa.gov"},],
                        "distorCont"   : [{"role"  : "Distributor",      "rpIndName" : "Nikki Wildart",       "eMailAdd" : "nikki.wildart@noaa.gov"},],
                        "mdContact"    : [{"role"  : "Author",           "rpIndName" : "Nikki Wildart",       "eMailAdd" : "nikki.wildart@noaa.gov"},],
                        "stepProc"     : [{"role" : "Processor",        "rpIndName" : "Nikki Wildart",       "eMailAdd" : "nikki.wildart@noaa.gov"},
                                          {"role" : "Processor",        "rpIndName" : "Dan Lawson",          "eMailAdd" : "dan.lawson@noaa.gov"},
                                          {"role" : "Processor",        "rpIndName" : "Jeffrey A. Seminoff", "eMailAdd" : "jeffrey.seminoff@noaa.gov"},
                                          {"role" : "Processor",        "rpIndName" : "Jennifer Schultz",    "eMailAdd" : "jennifer.schultz@noaa.gov"},
                                          {"role" : "Processor",        "rpIndName" : "Jonathan Molineaux",  "eMailAdd" : "jonathan.molineaux@noaa.gov"},
                                          {"role" : "Processor",        "rpIndName" : "Marc Romano",         "eMailAdd" : "marc.romano@noaa.gov"},
                                          {"role" : "Processor",        "rpIndName" : "Susan Wang",          "eMailAdd" : "susan.wang@noaa.gov"},
                                         ],}


        # Declared Varaiables
        del root_dict, esri_dict, dataIdInfo_dict, idCitation_dict, contact_dict, dqInfo_dict, RoleCd_dict, tpCat_dict, contacts
        # Imports
        # Function Parameters
        del project_gdb

        # Elapsed time
        end_time = time()
        elapse_time =  end_time - start_time

        print(f"\n{'-' * 80}")
        print(f"Python script: {os.path.basename(__file__)}\nCompleted: {strftime('%a %b %d %I:%M %p', localtime())}")
        print(u"Elapsed Time {0} (H:M:S)".format(strftime("%H:%M:%S", gmtime(elapse_time))))
        print(f"{'-' * 80}")
        del elapse_time, end_time, start_time
        del gmtime, localtime, strftime, time

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

if __name__ == "__main__":
    try:
        # Imports
        # Append the location of this scrip to the System Path
        #sys.path.append(os.path.dirname(__file__))
        sys.path.append(os.path.dirname(os.path.dirname(__file__)))

        project_folder = rf"{os.path.dirname(os.path.dirname(__file__))}"
        project_name     = "National Mapper"
        project_gdb      = rf"{project_folder}\{project_name}.gdb"

        main(project_gdb=project_gdb)

        # Declared Variables
        del project_gdb, project_name, project_folder
        # Imports
    except:
        traceback.print_exc()
    else:
        pass
    finally:
        pass
