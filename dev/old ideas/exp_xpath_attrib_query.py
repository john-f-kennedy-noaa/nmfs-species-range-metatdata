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
import traceback
import inspect

def main():
    try:
        from lxml import etree

        target_xml = r'{os.environ['USERPROFILE']}\Documents\ArcGIS\Projects\ArcPy Studies\XML\nmfs-species-range-metatdata\Export\WhaleBlue_20201014.xml'

        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
        # Parse the XML
        target_tree = etree.parse(target_xml, parser=parser)
        target_root = target_tree.getroot()
        del parser
        #etree.indent(tree, space="    ")
        # Pretty print
        target_xml_string = etree.tostring(target_tree, pretty_print=True, method='html', encoding='UTF-8').decode()
        #print(target_xml_string)

        find = etree.XPath("./dqInfo/report[1]") # DQConcConsis, DQCompOm
        target_elements = find(target_root)
        del find

        print(os.path.basename(target_xml), flush=True)

        if target_elements:
            for target_element in target_elements:
                print(f"\t{target_element.attrib}")
                print(f"\t{target_tree.getpath(target_element)}")
                #print(f"\t{etree.tostring(target_element)}")
                print("\n")
                del target_element
        else:
            print("target is missing")

        find = etree.XPath("./dqInfo/report[@type='DQConcConsis']") # DQConcConsis, DQCompOm
        target_elements = find(target_root)
        del find

        print(os.path.basename(target_xml), flush=True)

        if target_elements:
            for target_element in target_elements:
                print(f"\t{target_element.attrib}")
                print(f"\t{target_tree.getpath(target_element)}")
                #print(f"\t{etree.tostring(target_element)}")
                print("\n")
                del target_element
        else:
            print("target is missing")

        find = etree.XPath("./dqInfo/report[@type='DQCompOm']") # DQConcConsis, DQCompOm
        target_elements = find(target_root)
        del find

        if target_elements:
            for target_element in target_elements:
                print(f"\t{target_element.attrib}")
                print(f"\t{target_tree.getpath(target_element)}")
                #print(f"\t{etree.tostring(target_element)}")
                print("\n")
                del target_element
        else:
            print("target is missing")


        # Declared Variables
        del target_elements
        del target_xml, target_xml_string, target_tree, target_root

        # Imports
        del etree

    except:
        import traceback
        traceback.print_exc()
    else:
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: raise Warning(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk

if __name__ == '__main__':
    try:
        main()
    except Warning as w:
        print(w)
