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
import os, sys, traceback, inspect

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

def list_all_lements(metadata_xml=""):
    try:
        #from arcpy import metadata as md
        from lxml import etree

##        from lxml import etree
##
##        xml = etree.XML('''<html><body>
##                           <p>hi there</p><p>2nd paragraph</p>
##                           </body></html>''')
##
##        # If you want to visit all of the descendants
##        for element in xml.iter():
##            print element.tag
##
##        # Or, if you want to have a list of all the descendents
##        all_elements = list(xml.iter())
##        print [element.tag for element in all_elements]

        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)

        if os.path.isfile(metadata_xml):
            parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
            # Parse the XML File
            tree = etree.parse(metadata_xml, parser=parser)
            etree.indent(tree, space="    ")
        else:
            # Parse the XML Object
            tree = etree.parse(metadata_xml, parser=parser)
            del parser
            etree.indent(tree, space="    ")

        del parser

        # Pretty print
        #print(etree.tostring(tree, pretty_print=True, method='html', encoding='UTF-8').decode())

        # Or, if you want to have a list of all the descendents

        # If you want to visit all of the descendants
        for element in tree.iter():
            #print(element.tag)
            # Use getpath() to get the element path from the tree
            element_path = tree.getpath(element)
            print(element_path, flush=True)
            del  element_path

            # Get the element at the end of the path using xpath. Return list
            #print(tree.xpath(element_path)[0].text)

        del element

        #all_elements = list(tree.iter())
        #print([element.tag for element in all_elements])

        # Variables
        del tree

        # Imports
        del etree
        # Function parameters
        del metadata_xml

    except:
        traceback.print_exc()
    else:
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: raise Warning(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        pass

def list_children_of_parent(metadata_xml="", find_element=""):
    try:
        #from arcpy import metadata as md
        from lxml import etree

        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)

        if os.path.isfile(metadata_xml):
            print(os.path.basename(metadata_xml), flush=True)
            parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
            # Parse the XML File
            tree = etree.parse(metadata_xml, parser=parser)
            #etree.indent(tree, space="    ")
            root = tree.getroot().find(f"./{find_element}")
            #root = root.find("./dqInfo")
        else:
            # Parse the XML Object
            tree = etree.parse(metadata_xml, parser=parser)
            del parser
            #etree.indent(tree, space="    ")
            root = tree.getroot().find(f"./{find_element}")

        del parser, find_element

##            # get the item's metadata xml
##            target_md = md.Metadata(target_xml)
##            target_xml_string = target_md.xml
##            # create an ElementTree object from the metadata XML string
##            target_tree = etree.ElementTree(etree.fromstring(target_xml_string))
##            #target_tree = etree.fromstring(target_xml_string)
##            target_root = target_tree.getroot()

        # Pretty print
        #print(etree.tostring(tree, pretty_print=True, method='html', encoding='UTF-8').decode())

        if len(root) > 0:
            # If you want to visit all of the descendants
            print(f"\troot '{root.tag}' has descendants", flush=True)
            for element in root.iterdescendants():
                # Use getpath() to get the element path from the tree
                element_get_path = tree.getpath(element)
                element_x_path = tree.xpath(element_get_path)
                print(f"\t\t{element_get_path}", flush=True)
                xml_string = etree.tostring(element_x_path[0], method='html', encoding='UTF-8').decode().replace("\t", "")
                #print("\t\t\t" + xml_string, flush=True)
                #print(f"\t\t\t{xml_string}", flush=True)
                # Get the element at the end of the path using xpath. Return list
                #print(tree.xpath(element_path)[0].text)
                del xml_string
                del element_get_path, element_x_path
            del element
##        else:
##            print(f"root '{root.tag}' has {len(root)} descendants", flush=True)
##            if isinstance(root.text, list):
##                for txt in root.text:
##                    print(txt, flush=True)
##                    del txt
##            elif isinstance(root.text, str):
##                print(root.text, flush=True)



        # Variables
        del tree, root
        # Imports
        del etree
        # Function parameters
        del metadata_xml

    except:
        traceback.print_exc()
    else:
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk:
            raise Warning(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        pass

def main():
    try:
        # Imports
        from src.project_tools import pretty_format_xml_file

        project_folder = rf"{os.path.dirname(os.path.dirname(__file__))}"
        target_xmls = [rf"{project_folder}\Export\{f}" for f in os.listdir(rf"{project_folder}\Export") if f.endswith(".xml")]

        ListAllElements = False
        if ListAllElements:
            list_all_lements(metadata_xml=target_xml[0])
        else:
            pass
        del ListAllElements

        ListChildrenOfParent = False
        if ListChildrenOfParent:
            find_element = "dqInfo/dataLineage/dataSource"
            for target_xml in target_xmls:
                list_children_of_parent(metadata_xml=target_xml, find_element=find_element)
                del target_xml
            del find_element
        else:
            pass

        target_xml = "species_range_boilerplate.xml"
        find_element = "dqInfo/dataLineage/dataSource"
        list_children_of_parent(metadata_xml=target_xml, find_element=find_element)
        del target_xml, find_element

        del ListChildrenOfParent

        # Variables
        del target_xmls
        del project_folder
        # Imports
        del pretty_format_xml_file

    except Warning as w:
        print(w, flush=True)
    except:
        traceback.print_exc()
    else:
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: raise Warning(f"WARNING!!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        pass

if __name__ == '__main__':
    try:
        main()
    except Warning as w:
        print(w, flush=True)
    except:
        traceback.print_exc()
