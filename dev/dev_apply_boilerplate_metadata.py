#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john.f.kennedy
#
# Created:     24/11/2024
# Copyright:   (c) john.f.kennedy 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Python Built-in's modules are loaded first
import os, sys
import traceback, inspect

# Third-party modules are loaded second
import arcpy

def pretty_format_xml_files():
    try:
        # Imports
        from src.project_tools import pretty_format_xml_file
        #arcpy.AddMessage("Pretty Print XMLs")
        xml_files = []
        #arcpy.AddMessage("Walking directories for XML files")
        project_folder = rf"{os.path.dirname(__file__)}"
        walk = os.walk(project_folder)
        for dirpath, dirnames, filenames in walk:
            for filename in filenames:
                if (filename.endswith(".xml") or filename.endswith(".sddraft")) and os.path.basename(filename) not in ["metadata outline.xml"]:
                    xml_files.append(os.path.join(dirpath, filename))
                else:
                    pass
                del filename
            del dirpath, dirnames, filenames
        for xml_file in xml_files:
            #arcpy.AddMessage(f"\tProcessing {os.path.basename(xml_file)}")
            pretty_format_xml_file(xml_file)
            del xml_file
        del xml_files
        del walk
        #arcpy.AddMessage("Pretty Print XMLs DONE")
        # Function variables
        del project_folder
        # Imports
        del pretty_format_xml_file

    except:
        traceback.print_exc()
    else:
        return True
    finally:
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: raise Warning(f"\n Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk

# function to update purpose and credits in metadata
def update_metadata(target_root, source_root):
    try:
        num_elements = 0

        UpdateIdPurp = False
        if UpdateIdPurp:
            # modify purpose element's text
            # there is only supposed to be one purpose element in metadata
            # replace purpose element text if element exists
            # if element doesn't exist, do nothing
            target_id_purp_elements = target_root.findall("./dataIdInfo/idPurp")
            for target_id_purp_element in target_id_purp_elements:
                if target_id_purp_element.text is not None:
                    print(f"Purpose: {target_id_purp_element.text}")
                del target_id_purp_element
            del target_id_purp_elements
            num_elements += 1
        del UpdateIdPurp

        UpdateIdAbs = False
        if UpdateIdAbs:
            # modify credit element's text
            # there is only supposed to be one credit element in metadata
            # replace credit element text if element exists
            # if element doesn't exist, do nothing
            target_abstract_elements = target_root.findall("./dataIdInfo/idAbs")
            for target_abstract_element in target_abstract_elements:
                if target_abstract_element.text is not None:
                    print(f"Description: {target_abstract_elements.text}")
                del target_abstract_element
            del target_abstract_elements
            num_elements += 1
        del UpdateIdAbs

        UpdateIdCredit = False
        if UpdateIdCredit:
            # modify credit element's text
            # there is only supposed to be one credit element in metadata
            # replace credit element text if element exists
            # if element doesn't exist, do nothing
            target_id_credit_elements = target_root.findall("./dataIdInfo/idCredit")
            source_id_credit_elements = source_root.findall("./dataIdInfo/idCredit")
            for target_id_credit_element in target_id_credit_elements:
                #if target_id_credit_element.text is not None:
                #print(f"Credits: {target_id_credit_element.text}")
                target_id_credit_element.text = source_id_credit_elements[0].text
                del target_id_credit_element
            del target_id_credit_elements, source_id_credit_elements
            num_elements += 1
        del UpdateIdCredit

        UpdateUseLimit = False
        if UpdateUseLimit:
            # modify credit element's text
            # there is only supposed to be one credit element in metadata
            # replace credit element text if element exists
            # if element doesn't exist, do nothing
            target_use_limit_elements = target_root.findall("./dataIdInfo/resConst/Consts/useLimit")
            source_use_limit_elements = source_root.findall("./dataIdInfo/resConst/Consts/useLimit")
            for target_use_limit_element in target_use_limit_elements:
                #if target_use_limit_element.text is not None:
                #print(f"Use Limits: {target_use_limit_element.text}")
                target_use_limit_element.text = source_use_limit_elements[0].text
                del target_use_limit_element
            del target_use_limit_elements, source_use_limit_elements
            num_elements += 1
        del UpdateUseLimit

        UpdateExDesc = False # Add extent description
        if UpdateExDesc:
            # modify credit element's text
            # there is only supposed to be one credit element in metadata
            # replace credit element text if element exists
            # if element doesn't exist, do nothing
            target_ex_desc_elements = target_root.findall("./dataIdInfo/dataExt/exDesc")
            source_ex_des_elements  = source_root.findall("./dataIdInfo/dataExt/exDesc")
            for target_ex_desc_element in target_ex_desc_elements:
                if target_ex_desc_element.text is not None:
                    temp_text = target_ex_desc_element.text
                    if source_ex_des_elements[0].text not in temp_text:
                        target_ex_desc_element.text = f"{temp_text}. {source_ex_des_elements[0].text}"
                    del temp_text
                else:
                    target_ex_desc_element.text = source_ex_des_elements[0].text
                del target_ex_desc_element
            del target_ex_desc_elements, source_ex_des_elements
            num_elements += 1
        del UpdateExDesc

        UpdateEaInfo = False
        if UpdateEaInfo:
            # Find the eainfo elements
            eainfo_target_child = target_root.find("eainfo/detailed")
            eainfo_source_child = source_root.find("eainfo/detailed")
            if eainfo_target_child is not None:
                # Replace child1 with child2
                parent = eainfo_target_child.getparent()
                parent.replace(eainfo_target_child, eainfo_source_child)
                del parent
            else:
                arcpy.AddWarning(f"\tFeature Class has no eainfo")
            del eainfo_target_child, eainfo_source_child
            num_elements += 1
        del UpdateEaInfo

        UpdateIdPoC = False
        if UpdateIdPoC:
            # Find the citRespPart elements
            idPoC_target_child = target_root.find('dataIdInfo/idPoC')
            idPoC_source_child = source_root.find('dataIdInfo/idPoC')
            if idPoC_target_child is not None:
                # Replace child1 with child2
                parent = idPoC_target_child.getparent()
                parent.replace(idPoC_target_child, idPoC_source_child)
                del parent
            else:
                arcpy.AddWarning(f"\tFeature Class has no idPoC")
            del idPoC_target_child, idPoC_source_child
            num_elements += 1
        del UpdateIdPoC

        UpdateCitRespParty = False
        if UpdateCitRespParty:
            # Find the citRespPart elements
            citRespParty_target_child = target_root.find('dataIdInfo/idCitation/citRespParty')
            citRespParty_source_child = source_root.find('dataIdInfo/idCitation/citRespParty')
            if citRespParty_target_child is not None:
                # Replace child1 with child2
                parent = citRespParty_target_child.getparent()
                parent.replace(citRespParty_target_child, citRespParty_source_child)
                del parent
            else:
                arcpy.AddWarning(f"\tFeature Class has no citRespParty")
            del citRespParty_target_child, citRespParty_source_child
            num_elements += 1
        del UpdateCitRespParty

        UpdateMdContact = False
        if UpdateMdContact:
            # Find the citRespPart elements
            mdContact_target_child = target_root.find('mdContact')
            mdContact_source_child = source_root.find('mdContact')
            if mdContact_target_child is not None: # and mdContact_source_child is not None:
                # Replace child1 with child2
                parent = mdContact_target_child.getparent()
                parent.replace(mdContact_target_child, mdContact_source_child)
                del parent
            else:
                arcpy.AddWarning(f"\tFeature Class has no mdContact")
            del mdContact_target_child, mdContact_source_child
            num_elements += 1
        del UpdateMdContact

        UpdateDistInfo = False
        if UpdateDistInfo:
            # Find the distInfo elements
            distInfo_target_child = target_root.find('distInfo')
            distInfo_source_child = source_root.find('distInfo')
            if distInfo_target_child is not None: # and distInfo_source_child is not None:
                #pass
                # Replace child1 with child2
                parent = distInfo_target_child.getparent()
                parent.replace(distInfo_target_child, distInfo_source_child)
                del parent
            else:
                arcpy.AddWarning(f"\tFeature Class has no distInfo")
            del distInfo_target_child, distInfo_source_child
            num_elements += 1
        del UpdateDistInfo

        UpdateRpCntInfos = False
        if UpdateRpCntInfos:
            from lxml import etree
            rpCntInfos = target_root.findall(".//rpCntInfo/cntOnlineRes")
            for rpCntInfo in rpCntInfos:
                children = [c for c in rpCntInfo.getchildren()]
                if children:
                    if children[1].tag != "protocol":
                        rpCntInfo.insert(1, etree.SubElement(rpCntInfo, "protocol"))
                        protocol = rpCntInfo.find("./protocol")
                        protocol.text = "REST Service"
                    if children[1].tag == "protocol" and children[1].text is not None:
                        protocol = rpCntInfo.find("./protocol")
                        protocol.text = "REST Service"
                del children
                del rpCntInfo
            del rpCntInfos
            # Imports
            del etree
            num_elements += 1
        del UpdateRpCntInfos

        UpdateLinkage = False
        if UpdateLinkage:
            new_item_name = target_root.find("./Esri/DataProperties/itemProps/itemName").text
            onLineSrcs = target_root.findall("./distInfo/distributor/distorTran/onLineSrc")
            for onLineSrc in onLineSrcs:
                if onLineSrc.find('./protocol').text == "ESRI REST Service":
                    old_linkage_element = onLineSrc.find('./linkage')
                    old_linkage = old_linkage_element.text
                    #print(old_linkage)
                    old_item_name = old_linkage[old_linkage.find("/services/")+len("/services/"):old_linkage.find("/FeatureServer")]
                    new_linkage = old_linkage.replace(old_item_name, new_item_name)
                    #print(new_linkage)
                    old_linkage_element.text = new_linkage
                    #print(old_linkage_element.text)
                    del old_linkage_element
                    del old_item_name, old_linkage, new_linkage
                del onLineSrc
            del onLineSrcs, new_item_name
            num_elements += 1
        del UpdateLinkage

        UpdateDqInfo = False
        if UpdateDqInfo:
            # Find the dqInfo elements
            dqInfo_target_child = target_root.find('dqInfo')
            dqInfo_source_child = source_root.find('dqInfo')
            if dqInfo_target_child is not None: # and dqInfo_source_child is not None:
                #pass
                # Replace child1 with child2
                parent = dqInfo_target_child.getparent()
                parent.replace(dqInfo_target_child, dqInfo_source_child)
                del parent
            else:
                arcpy.AddWarning(f"\tFeature Class has no dqInfo")
            del dqInfo_target_child, dqInfo_source_child
            num_elements += 1
        del UpdateDqInfo
        # Function parameters
        del target_root, source_root

    except:
        traceback.print_exc()
    else:
        return num_elements
    finally:
        del num_elements
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: raise Warning(f"\nWARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk

def main():
    try:
        # Imports
        from lxml import etree
        from arcpy import metadata as md
        from time import gmtime, localtime, strftime, time
        # Set a start time so that we can see how log things take
        start_time = time()
        print(f"{'-' * 90}")
        print(f"Python Script:  {os.path.basename(__file__)}")
        print(f"Location:       {os.path.dirname(__file__)}")
        print(f"Python Version: {sys.version} Environment: {os.path.basename(sys.exec_prefix)}")
        print(f"{'-' * 90}\n")

        from src.project_tools import pretty_format_xml_file

        project_folder = rf"{os.path.dirname(__file__)}"

        target_xmls = [rf"{project_folder}\Export\{f}" for f in os.listdir(rf"{project_folder}\Export") if f.endswith(".xml")]

        # get and save item metadata
        for target_xml in target_xmls:
            arcpy.AddMessage(f"Target Metadata: {os.path.basename(target_xml)}")
            source_xml = rf"{project_folder}\species_range_boilerplate.xml"
            pretty_format_xml_file(source_xml)

            source_md = md.Metadata(source_xml)
            source_xml_string = source_md.xml
            # create an ElementTree object from the metadata XML string
            source_root = etree.fromstring(source_xml_string)
            del source_xml, source_md, source_xml_string

            # get the item's metadata xml
            target_md = md.Metadata(target_xml)
            target_xml_string = target_md.xml
            # create an ElementTree object from the metadata XML string
            target_root = etree.fromstring(target_xml_string)

            try:
                # call the update_metadata function to modify the item's metadata
                changes = update_metadata(target_root, source_root)
            except Warning as w:
                print(f"{w}"); del w
            except Exception as e:
                print(f"ERROR: {e}"); del e

            if changes > 0:
                # get modified XML
                updated_target_xml_string = etree.tostring(target_root, encoding="utf-8")

                # import result back into metadata
                arcpy.AddMessage("Saving updated metadata with the item...")
                target_md.xml = updated_target_xml_string
                target_md.save()
                del updated_target_xml_string
            else:
                arcpy.AddMessage("No changes to save")

            del target_root, source_root, changes
            del target_md, target_xml_string
            del target_xml

        del project_folder
        del target_xmls

        try:
            pretty_format_xml_files()
        except Exception as e:
            print(e)

        arcpy.AddMessage('Finished updating metadata for all source metadata items')

        # Elapsed time
        end_time = time()
        elapse_time =  end_time - start_time
        print(f"\n{'-' * 90}")
        print(f"Python script: {os.path.basename(__file__)} successfully completed {strftime('%a %b %d %I:%M %p', localtime())}")
        print(u"Elapsed Time {0} (H:M:S)".format(strftime("%H:%M:%S", gmtime(elapse_time))))
        print(f"{'-' * 90}")
        del elapse_time, end_time, start_time
        del gmtime, localtime, strftime, time

        # Imports
        del md, etree, pretty_format_xml_file

    except:
        traceback.print_exc()
    else:
        return True
    finally:
        # Cleanup
        arcpy.management.ClearWorkspaceCache()
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: raise Warning(f"\n Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk

if __name__ == '__main__':
    try:
        main()
    except Warning as w:
        print(w)
