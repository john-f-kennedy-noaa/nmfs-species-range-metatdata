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

def remove_duplicate_elements(root):
    seen = {}
    for element in root.iter():
        key = (element.tag, element.text, tuple(element.attrib.items()))
        if key in seen:
            element.getparent().remove(element)
        else:
            seen[key] = True
        del key, element
    del seen, root

# function to update purpose and credits in metadata
#def update_metadata(target_root, source_root, target_xml_name):
def update_metadata(target_tree, source_tree, target_xml_name):
    try:
        from lxml import etree

        num_elements = 0

        source_root = source_tree.getroot()
        target_root = target_tree.getroot()

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

        # Function parameters
        del target_tree, source_tree
        del target_root, source_root, target_xml_name

        # Imports
        del etree

    except:
        traceback.print_exc()
    else:
        return num_elements
    finally:
        del num_elements
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: raise Warning(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk

def main(project_folder=list()):
    try:
        # Imports
        from lxml import etree
        from arcpy import metadata as md
        from time import gmtime, localtime, strftime, time
        # Imports
        from src.project_tools import pretty_format_xml_file
        # Set a start time so that we can see how log things take
        start_time = time()
        print(f"{'-' * 80}")
        print(f"Python Script:  {os.path.basename(__file__)}")
        print(f"Location:       {os.path.dirname(__file__)}")
        print(f"Python Version: {sys.version} Environment: {os.path.basename(sys.exec_prefix)}")
        print(f"{'-' * 80}\n")

        from src.project_tools import pretty_format_xml_file

        target_xmls = [rf"{project_folder}\Export\{f}" for f in os.listdir(rf"{project_folder}\Export") if f.endswith(".xml")]
        #source_xml = rf"{project_folder}\species_range_boilerplate.xml"
        source_xml = rf"species_range_boilerplate.xml"
        pretty_format_xml_file(source_xml)

        warnings_and_errors = dict()

        # get and save item metadata
        for target_xml in target_xmls:
            target_xml_name = os.path.basename(target_xml)
            arcpy.AddMessage(f"Target Metadata: {target_xml_name}")
            #arcpy.AddMessage(f"Target Metadata: {target_xml}")
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
            #print(target_root.tag)
            #del target_tree

            #print(etree.tostring(target_root, pretty_print=True).decode())
            #print(etree.tostring(source_root, pretty_print=True).decode())

            try:
                pass
                # call the update_metadata function to modify the item's metadata
                #changes = update_metadata(target_root, source_root, target_xml_name)
                changes = update_metadata(target_tree, source_tree, target_xml_name)
                #print(changes)
            except Warning as w:
                #changes = 0
                warnings_and_errors[target_xml_name] = w
                print(f"{w}"); del w
            except Exception as e:
                #changes = 0
                warnings_and_errors[target_xml_name] = e
                print(f"ERROR: {e}"); del e
            except:
                traceback.print_exc()

            if "changes" in locals().keys():
                if changes > 0:
                    # get modified XML
                    #updated_target_xml_string = etree.tostring(target_root, encoding='UTF-8')
                    updated_target_xml_string = etree.tostring(target_tree, encoding='UTF-8')

                    # import result back into metadata
                    arcpy.AddMessage("Saving updated metadata with the item...")
                    target_md.xml = updated_target_xml_string
                    target_md.save()
                    del updated_target_xml_string
                    pretty_format_xml_file(target_xml)

                    arcpy.AddMessage('Finished updating metadata for all source metadata items')

                else:
                    arcpy.AddMessage("No changes to save")
            else:
                pass
                #print("some thing is wong!")

            if "changes" in locals().keys(): del changes

            del target_tree, source_tree
            del target_root, source_root
            del target_md, target_xml_string
            del target_xml, target_xml_name

        del source_xml
        del project_folder
        del target_xmls

        PrintWarningsAndErrors = False
        if PrintWarningsAndErrors:
            if warnings_and_errors:
                for warnings_and_error in warnings_and_errors:
                    print(warnings_and_error, warnings_and_errors[warnings_and_error])
                    del warnings_and_error
        del PrintWarningsAndErrors

        del warnings_and_errors

        #try:
        #    pretty_format_xml_files()
        #except Exception as e:
        #    print(e)

        # Elapsed time
        end_time = time()
        elapse_time =  end_time - start_time
        print(f"\n{'-' * 80}")
        print(f"Python script: {os.path.basename(__file__)} successfully completed {strftime('%a %b %d %I:%M %p', localtime())}")
        print(u"Elapsed Time {0} (H:M:S)".format(strftime("%H:%M:%S", gmtime(elapse_time))))
        print(f"{'-' * 80}")
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
        if rk: raise Warning(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk

if __name__ == '__main__':
    try:
        project_folder = rf"{os.path.dirname(os.path.dirname(__file__))}"
        main(project_folder)
    except Warning as w:
        print(w)
