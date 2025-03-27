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

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

##def remove_duplicate_elements(root):
##    seen = {}
##    for element in root.iter():
##        key = (element.tag, element.text, tuple(element.attrib.items()))
##        if key in seen:
##            element.getparent().remove(element)
##        else:
##            seen[key] = True
##        del key, element
##    del seen, root
##
### function to update purpose and credits in metadata
##def update_metadata(target_tree, source_tree, target_xml_name):
##    try:
##        from lxml import etree
##        num_elements = 0
##        source_root = source_tree.getroot()
##        target_root = target_tree.getroot()
##
##        UpdateLinkage = False
##        if UpdateLinkage:
##            new_item_name = target_root.find("./Esri/DataProperties/itemProps/itemName").text
##            onLineSrcs = target_root.findall("./distInfo/distributor/distorTran/onLineSrc")
##            for onLineSrc in onLineSrcs:
##                if onLineSrc.find('./protocol').text == "ESRI REST Service":
##                    old_linkage_element = onLineSrc.find('./linkage')
##                    old_linkage = old_linkage_element.text
##                    #print(old_linkage, flush=True)
##                    old_item_name = old_linkage[old_linkage.find("/services/")+len("/services/"):old_linkage.find("/FeatureServer")]
##                    new_linkage = old_linkage.replace(old_item_name, new_item_name)
##                    #print(new_linkage, flush=True)
##                    old_linkage_element.text = new_linkage
##                    #print(old_linkage_element.text, flush=True)
##                    del old_linkage_element
##                    del old_item_name, old_linkage, new_linkage
##                del onLineSrc
##            del onLineSrcs, new_item_name
##            num_elements += 1
##        else:
##            pass
##        del UpdateLinkage

##        UpdateDetailedName = False
##        if UpdateDetailedName:
##            new_item_name = target_root.find("./Esri/DataProperties/itemProps/itemName").text
##            detailed = target_root.find("eainfo/detailed")
##            detailed.set("Name", new_item_name)
##            del detailed, new_item_name
##            num_elements += 1
##        else:
##            pass
##        del UpdateDetailedName
##
##        # metadata/dqScope
##
##        UpdateDqScope = False
##        if UpdateDqScope:
##            #print(etree.tostring(source_root, pretty_print=True).decode(), flush=True)
##            #find = etree.XPath("//rpIndName[contains(.,'Jennifer Schultz')]")
##            find = etree.XPath("//dqScope")
##            target_elements = find(target_root)
##            del find
##            if target_elements:
##                #print("\n", flush=True)
##                for target_element in target_elements:
##                    #print(etree.tostring(target_element, pretty_print=True).decode(), flush=True)
##                    print(f"\t{target_element.tag}", flush=True)
##                    new_xml_string = '<dqScope xmlns=""><scpLvl><ScopeCd value="005"></ScopeCd></scpLvl><scpLvlDesc xmlns=""><datasetSet>Feature Class</datasetSet></scpLvlDesc></dqScope>'
##                    new_element = etree.fromstring(new_xml_string)
##                    del new_xml_string
##
##                    # create an ElementTree object from the metadata XML string
##                    new_xml_string_tree = etree.ElementTree(new_element)
##                    new_xml_string_root = new_xml_string_tree.getroot()
##                    #print(etree.tostring(new_xml_string_tree, pretty_print=True).decode(), flush=True)
##                    new_element_x_path = new_xml_string_tree.getpath(new_xml_string_root)
##                    #print(f"\t\t{new_element_x_path}", flush=True)
##                    #print(new_xml_string_tree.xpath(new_element_x_path)[0], flush=True)
##
##                    old_element_x_path = target_tree.getpath(target_element)
##                    #print(f"\t\t{old_element_x_path}", flush=True)
##                    #print(target_tree.xpath(old_element_x_path), flush=True)
##
##                    target_element.getparent().replace(target_tree.xpath(old_element_x_path)[0], new_xml_string_tree.xpath(new_element_x_path)[0])
##
##                    del new_xml_string_tree, new_xml_string_root
##                    del old_element_x_path, new_element_x_path
##                    del new_element
##                    del target_element
##            else:
##                print("Element is missing", flush=True)
##            del target_elements
##            num_elements += 1
##        del UpdateDqScope
##
##        UpdateDqInfoReport = True
##        if UpdateDqInfoReport:
##            #print(etree.tostring(source_root, pretty_print=True).decode(), flush=True)
##            #find = etree.XPath("//rpIndName[contains(.,'Jennifer Schultz')]")
##            # Find element with specific attribute value
##            # element = root.xpath("//element[@attr1='value1']")
##            #print(etree.tostring(report, pretty_print=True).decode().replace("\n\t\t", "\n"), flush=True)
##
##            find = etree.XPath("./dqInfo/report[@type='DQConcConsis']") # DQConcConsis, DQCompOm
##            target_elements = find(target_root)
##            del find
##
##            if target_elements:
##                #print(etree.tostring(target_elements[0], pretty_print=True).decode(), flush=True)
##                print(f"\tUpdating: {target_elements[0].attrib['type']}", flush=True)
##                new_xml_string = '<report xmlns="" type="DQConcConsis" dimension="horizontal"><measDesc>Based on a review from species experts, we determined that all necessary features were included in the species range file. Attribute values confirmed and checked via team review.</measDesc><measResult><ConResult xmlns=""><conSpec xmlns=""><resTitle>UPDATE NEEDED. What document or online reference covers the specifications used.</resTitle><date><pubDate>2025-01-01T00:00:00</pubDate></date></conSpec><conExpl>Based on a review from species experts, we determined that all necessary features were included in the species range file. Attribute values confirmed and checked via team review.</conExpl><conPass>1</conPass></ConResult></measResult></report>'
##                new_element = etree.fromstring(new_xml_string)
##                del new_xml_string
##
##                # create an ElementTree object from the metadata XML string
##                new_xml_string_tree = etree.ElementTree(new_element)
##                new_xml_string_root = new_xml_string_tree.getroot()
##                #print(etree.tostring(new_xml_string_tree, pretty_print=True).decode(), flush=True)
##
##                new_element_x_path = new_xml_string_tree.getpath(new_xml_string_root)
##                #print(f"\t\t{new_element_x_path}", flush=True)
##                #print(new_xml_string_tree.xpath(new_element_x_path)[0], flush=True)
##
##                old_element_x_path = target_tree.getpath(target_elements[0])
##                #print(f"\t\t{old_element_x_path}", flush=True)
##                #print(target_tree.xpath(old_element_x_path)[0], flush=True)
##
##                target_elements[0].getparent().replace(target_tree.xpath(old_element_x_path)[0], new_xml_string_tree.xpath(new_element_x_path)[0])
##
##                del new_xml_string_tree, new_xml_string_root
##                del old_element_x_path, new_element_x_path
##                del new_element
##                num_elements += 1
##            else:
##                find = etree.XPath("./dqInfo")
##                perant_element = find(target_root)[0]
##                del find
##
##                print(f"\tInserting type='DQConcConsis'", flush=True)
##
##                new_xml_string = '<report xmlns="" type="DQConcConsis" dimension="horizontal"><measDesc>Based on a review from species experts, we determined that all necessary features were included in the species range file. Attribute values confirmed and checked via team review.</measDesc><measResult><ConResult xmlns=""><conSpec xmlns=""><resTitle>UPDATE NEEDED. What document or online reference covers the specifications used.</resTitle><date><pubDate>2025-01-01T00:00:00</pubDate></date></conSpec><conExpl>Based on a review from species experts, we determined that all necessary features were included in the species range file. Attribute values confirmed and checked via team review.</conExpl><conPass>1</conPass></ConResult></measResult></report>'
##                new_element = etree.fromstring(new_xml_string)
##                del new_xml_string
##
##                # create an ElementTree object from the metadata XML string
##                new_xml_string_tree = etree.ElementTree(new_element)
##                new_xml_string_root = new_xml_string_tree.getroot()
##                #print(etree.tostring(new_xml_string_tree, pretty_print=True).decode(), flush=True)
##                new_element_x_path = new_xml_string_tree.getpath(new_xml_string_root)
##                #print(f"\t\t{new_element_x_path}", flush=True)
##                #print(new_xml_string_tree.xpath(new_element_x_path)[0], flush=True)
##
##                #perant_element.insert(1, new_xml_string_root)
##                perant_element.append(new_element)
##
##                #print(etree.tostring(perant_element, pretty_print=True).decode(), flush=True)
##
##                del new_xml_string_tree, new_xml_string_root, new_element_x_path
##                del new_element
##
##                del perant_element
##                num_elements += 1
##
##            del target_elements
##
##            find = etree.XPath("./dqInfo/report[@type='DQCompOm']") # DQConcConsis, DQCompOm
##            target_elements = find(target_root)
##            del find
##
##            if target_elements:
##                #print(etree.tostring(target_elements[0], pretty_print=True).decode(), flush=True)
##                print(f"\tUpdating: {target_elements[0].attrib['type']}", flush=True)
##                new_xml_string = '<report xmlns="" type="DQCompOm" dimension="horizontal"><measDesc>Based on a review from species experts, we determined that all necessary features were included in the species range file. Attribute values confirmed and checked via team review.</measDesc><measResult><ConResult xmlns=""><conSpec xmlns=""><resTitle>UPDATE NEEDED. What document or online reference covers the specifications used.</resTitle><date><pubDate>2025-01-01T00:00:00</pubDate></date></conSpec><conExpl>Based on a review from species experts, we determined that all necessary features were included in the species range file. Attribute values confirmed and checked via team review.</conExpl><conPass>1</conPass></ConResult></measResult></report>'
##                new_element = etree.fromstring(new_xml_string)
##                del new_xml_string
##
##                # create an ElementTree object from the metadata XML string
##                new_xml_string_tree = etree.ElementTree(new_element)
##                new_xml_string_root = new_xml_string_tree.getroot()
##                #print(etree.tostring(new_xml_string_tree, pretty_print=True).decode(), flush=True)
##
##                new_element_x_path = new_xml_string_tree.getpath(new_xml_string_root)
##                #print(f"\t\t{new_element_x_path}", flush=True)
##                #print(new_xml_string_tree.xpath(new_element_x_path)[0], flush=True)
##
##                old_element_x_path = target_tree.getpath(target_elements[0])
##                #print(f"\t\t{old_element_x_path}", flush=True)
##                #print(target_tree.xpath(old_element_x_path)[0], flush=True)
##
##                target_elements[0].getparent().replace(target_tree.xpath(old_element_x_path)[0], new_xml_string_tree.xpath(new_element_x_path)[0])
##
##                del new_xml_string_tree, new_xml_string_root
##                del old_element_x_path, new_element_x_path
##                del new_element
##                num_elements += 1
##            else:
##                find = etree.XPath("./dqInfo")
##                perant_element = find(target_root)[0]
##                del find
##
##                print(f"\tInserting  type='DQCompOm'", flush=True)
##
##                new_xml_string = '<report xmlns="" type="DQCompOm" dimension="horizontal"><measDesc>Based on a review from species experts, we determined that all necessary features were included in the species range file. Attribute values confirmed and checked via team review.</measDesc><measResult><ConResult xmlns=""><conSpec xmlns=""><resTitle>UPDATE NEEDED. What document or online reference covers the specifications used.</resTitle><date><pubDate>2025-01-01T00:00:00</pubDate></date></conSpec><conExpl>Based on a review from species experts, we determined that all necessary features were included in the species range file. Attribute values confirmed and checked via team review.</conExpl><conPass>1</conPass></ConResult></measResult></report>'
##                new_element = etree.fromstring(new_xml_string)
##                del new_xml_string
##
##                # create an ElementTree object from the metadata XML string
##                new_xml_string_tree = etree.ElementTree(new_element)
##                new_xml_string_root = new_xml_string_tree.getroot()
##                #print(etree.tostring(new_xml_string_tree, pretty_print=True).decode(), flush=True)
##                new_element_x_path = new_xml_string_tree.getpath(new_xml_string_root)
##                #print(f"\t\t{new_element_x_path}", flush=True)
##                #print(new_xml_string_tree.xpath(new_element_x_path)[0], flush=True)
##
##                #perant_element.insert(2, new_xml_string_root)
##                perant_element.append(new_element)
##
##                #print(etree.tostring(perant_element, pretty_print=True).decode(), flush=True)
##
##                del new_xml_string_tree, new_xml_string_root, new_element_x_path
##                del new_element
##
##                del perant_element
##                num_elements += 1
##
##            del target_elements
##
##            # Track changes
##            num_elements += 1
##        del UpdateDqInfoReport
##
##
##        # This is the current one that appears to work.
##        InsertProcessStep = False
##        if InsertProcessStep:
##            pass
##        else:
##            pass
##        del InsertProcessStep
##
##        # Function parameters
##        del target_tree, source_tree
##        del target_root, source_root, target_xml_name
##
##        # Imports
##        del etree

    except:
        traceback.print_exc()
    else:
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: raise Warning(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return num_elements
    finally:
        del num_elements

def main(project_folder=""):
    try:
        # Imports
        from time import gmtime, localtime, strftime, time
        # Set a start time so that we can see how log things take
        start_time = time()
        print(f"{'-' * 80}", flush=True)
        print(f"Python Script:  {os.path.basename(__file__)}", flush=True)
        print(f"Location:       {os.path.dirname(__file__)}", flush=True)
        print(f"Python Version: {sys.version} Environment: {os.path.basename(sys.exec_prefix)}", flush=True)
        print(f"{'-' * 80}\n")

        # Imports
        from lxml import etree
        from arcpy import metadata as md
        from src.project_tools import pretty_format_xml_file

        #target_xmls = [rf"{project_folder}\Export\{f}" for f in os.listdir(rf"{project_folder}\Export") if f.endswith(".xml")]
        target_xmls = [rf"{project_folder}\Export\{f}" for f in os.listdir(rf"{project_folder}\Export")]
        #target_xmls = [rf"{project_folder}\Export\{f}" for f in os.listdir(rf"{project_folder}\Export") if f == "WhaleNorthAtlanticRight_20201215.xml"]
        #source_xml = rf"{project_folder}\species_range_boilerplate.xml"
        source_xml = rf"species_range_boilerplate.xml"
        pretty_format_xml_file(source_xml)

        warnings_and_errors = dict()

        # get and save item metadata
        for target_xml in target_xmls:
            target_xml_name = os.path.basename(target_xml)
            print(f"Target Metadata: {target_xml_name}", flush=True)
            #print(f"Target Metadata: {target_xml}", flush=True)
            source_md = md.Metadata(source_xml)
            source_xml_string = source_md.xml
            # create an ElementTree object from the metadata XML string
            source_tree = etree.ElementTree(etree.fromstring(source_xml_string))
            #source_tree = etree.fromstring(source_xml_string)
            source_root = source_tree.getroot()
            #del source_tree
            del source_md, source_xml_string

            # get the item's metadata xml
            target_md = md.Metadata(target_xml)
            target_xml_string = target_md.xml
            # create an ElementTree object from the metadata XML string
            target_tree = etree.ElementTree(etree.fromstring(target_xml_string))
            #target_tree = etree.fromstring(target_xml_string)
            target_root = target_tree.getroot()
            #print(target_root.tag, flush=True)
            #del target_tree

            #print(etree.tostring(target_root, pretty_print=True).decode(), flush=True)
            #print(etree.tostring(source_root, pretty_print=True).decode(), flush=True)

            try:
                pass
                # call the update_metadata function to modify the item's metadata
                changes = update_metadata(target_tree, source_tree, target_xml_name)
                #print(changes, flush=True)
            except Warning as w:
                #changes = 0
                warnings_and_errors[target_xml_name] = w
                print(f"{w}", flush=True); del w
            except Exception as e:
                #changes = 0
                warnings_and_errors[target_xml_name] = e
                print(f"ERROR: {e}", flush=True); del e
            except:
                traceback.print_exc()

            if "changes" in locals().keys():
                if changes > 0:
                    # get modified XML
                    #updated_target_xml_string = etree.tostring(target_root, encoding='UTF-8')
                    updated_target_xml_string = etree.tostring(target_tree, encoding='UTF-8')

                    # import result back into metadata
                    print("Saving updated metadata with the item...", flush=True)
                    target_md.xml = updated_target_xml_string
                    target_md.save()
                    del updated_target_xml_string
                    pretty_format_xml_file(target_xml)

                    print('Finished updating metadata for all source metadata items')

                else:
                    print("No changes to save")
            else:
                pass
                #print("some thing is wong!", flush=True)

            if "changes" in locals().keys(): del changes

            del target_tree, source_tree
            del target_root, source_root
            del target_md, target_xml_string
            del target_xml, target_xml_name

        sys.stdout.flush()

        del source_xml
        del project_folder
        del target_xmls

        PrintWarningsAndErrors = True
        if PrintWarningsAndErrors:
            if len(warnings_and_errors) > 0:
                for warnings_and_error in warnings_and_errors:
                    print(warnings_and_error, warnings_and_errors[warnings_and_error], flush=True)
                    del warnings_and_error
        del PrintWarningsAndErrors

        del warnings_and_errors

        #try:
        #    pretty_format_xml_files()
        #except Exception as e:
        #    print(e)

##
##            try:
##                with open(xml, "w") as f:
##                    f.write(xml_string)
##                del f
##            except:
##                arcpy.AddError(f"The metadata file: {os.path.basename(xml)} can not be overwritten!!")


        # Imports
        del md, etree, pretty_format_xml_file

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
        if rk: raise Warning(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        # Cleanup
        arcpy.management.ClearWorkspaceCache()

if __name__ == '__main__':
    try:
        main(project_folder=rf"{os.path.dirname(os.path.dirname(__file__))}")
    except Warning as w:
        print(w, flush=True)
    except:
        traceback.print_exc()
