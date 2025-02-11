#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john.f.kennedy
#
# Created:     04/02/2025
# Copyright:   (c) john.f.kennedy 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from lxml import etree

def main():
    # Create the root element
    root = etree.Element("metadata")
    #root.set('xml:lang', "en")

    #root.attrib[QName("http://www.w3.org/XML/1998/namespace", "lang")] = "en-US"
    root.set("{http://www.w3.org/XML/1998/namespace}lang", "en-US")


    # Create child elements and add them to the root
    #child1 = etree.SubElement(root, "child1")
    #child1.text = "Child 1 text"

    #child2 = etree.SubElement(root, "child2")
    #child2.set("attribute", "value")

    # Serialize the tree to a string
    xml_string = etree.tostring(root, pretty_print=True, xml_declaration=True, encoding="utf-8").decode()

    print(xml_string)


if __name__ == '__main__':
    main()
