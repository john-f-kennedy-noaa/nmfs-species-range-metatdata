#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john.f.kennedy
#
# Created:     15/01/2025
# Copyright:   (c) john.f.kennedy 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Python Built-in's modules are loaded first
import os, sys
import traceback, inspect

# Third-party modules are loaded second
# import arcpy

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

def main(project_folder=""):
    try:
        from lxml import etree

        target_xml = rf'{project_folder}\Export\WhaleBlue_20201014.xml'
        del project_folder

        parser = etree.XMLParser(remove_blank_text=True)
        # Parse the XML
        target_tree = etree.parse(target_xml, parser=parser)
        target_root = target_tree.getroot()
        del parser
        #etree.indent(tree, space="    ")
        # Pretty print
        target_xml_string = etree.tostring(target_tree, pretty_print=True, method='html', encoding="utf-8").decode()
        #print(target_xml_string)

        target_elements = target_tree.find("./dqInfo").getchildren()

        def sort_function(target_element):
            try:
                tag_position_dict = {
                                     "dqScope": 0,
                                     "report" : {"DQConcConsis" : 1, "DQCompOm" : 2},
                                     "dataLineage" : 3,
                                    }

                #print(tag_position_dict["dqScope"])
                #print(tag_position_dict["report"]["DQConcConsis"])
                #print(tag_position_dict["report"]["DQCompOm"])
                #print(tag_position_dict["dataLineage"])

                if target_element.tag == "dqScope":
                    return tag_position_dict["dqScope"]
                if target_element.tag == "report":
                    if target_element.get("type") == "DQConcConsis":
                        return tag_position_dict["report"]["DQConcConsis"]
                    elif target_element.get("type") == "DQCompOm":
                        return tag_position_dict["report"]["DQCompOm"]
                if target_element.tag == "dataLineage":
                    return tag_position_dict["dataLineage"]
            except:
                traceback.print_exc()
            else:
                del tag_position_dict
            finally:
                pass

        target_elements[:] = sorted(target_elements, key=sort_function)

        for target_element in target_elements:
            print(target_element.tag)
            del target_element

        del sort_function

        # Variables
        del target_elements
        del target_xml, target_xml_string, target_tree, target_root

        # Imports
        del etree

    except:
        traceback.print_exc()
    else:
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: raise Warning(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
    finally:
        pass
        # Cleanup
        # arcpy.management.ClearWorkspaceCache()

if __name__ == '__main__':
    try:
        main(project_folder=rf"{os.path.dirname(os.path.dirname(__file__))}")
    except Warning as w:
        print(w)
