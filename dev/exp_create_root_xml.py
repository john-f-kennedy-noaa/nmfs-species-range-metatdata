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
    from io import StringIO
    # Create the root element
    root = etree.Element("metadata")
    root.set("{http://www.w3.org/XML/1998/namespace}lang", "en-US")
    tree = etree.ElementTree(root)
    # Create child elements and add them to the root
    #eainfo = etree.SubElement(root, "eainfo")

    xml = '''<eainfo>
                <detailed xmlns="" Name="" Sync="TRUE">
                    <enttyp>
                        <enttypl Sync="TRUE">Attribute Table Fields</enttypl>
                        <enttypt Sync="TRUE">Feature Class</enttypt>
                        <enttypc Sync="TRUE">1</enttypc>
                        <enttypd>A collection of geographic features with the same geometry type.</enttypd>
                        <enttypds>Esri</enttypds>
                    </enttyp>
                </detailed>
             </eainfo>'''

    _xml = etree.XML(xml)
    # Parse the XML
    parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
    _tree = etree.parse(StringIO(xml), parser=parser)
    _root = _tree.getroot()
    del parser

    # Append element
    eainfo = _root.xpath("./eainfo")
    root.append(_root)
    #root.insert(100, _root)
    # Serialize the tree to a string
    xml_string = etree.tostring(tree, pretty_print=True, method='xml', xml_declaration=True, encoding="utf-8").decode()
    print(xml_string)

if __name__ == '__main__':
    main()
