#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john.f.kennedy
#
# Created:     03/03/2025
# Copyright:   (c) john.f.kennedy 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    from lxml import etree
    from copy import deepcopy

    # Create the first tree
    root1 = etree.Element("root1")
    element1 = etree.SubElement(root1, "element1")
    element1.text = "text1"
    tree1 = etree.ElementTree(root1)
    print(etree.tostring(tree1, pretty_print=True).decode())

    # Create the second tree
    root2 = etree.Element("root2")
    element2 = etree.SubElement(root2, "element2")
    element2.text = "text2"
    tree2 = etree.ElementTree(root2)
    print(etree.tostring(tree2, pretty_print=True).decode())

    # Append the second tree to the first tree (moving the element)
    root1.append(root2)
    print(etree.tostring(tree1, pretty_print=True).decode())
    # Expected output (root2 is moved):
    # <root1>
    #  <element1>text1</element1>
    #  <root2>
    #   <element2>text2</element2>
    #  </root2>
    # </root1>
    print(etree.tostring(tree2, pretty_print=True).decode())
    # Expected output (tree2 is now empty):
    # <root2/>

    # Create a copy of the second tree and append it
    root3 = etree.Element("root3")
    element3 = etree.SubElement(root3, "element3")
    element3.text = "text3"
    tree3 = etree.ElementTree(root3)
    print(etree.tostring(tree3, pretty_print=True).decode())

    root4 = etree.Element("root4")
    element4 = etree.SubElement(root4, "element4")
    element4.text = "text4"
    tree4 = etree.ElementTree(root4)
    print(etree.tostring(tree4, pretty_print=True).decode())

    root3.append(deepcopy(root4))

    print(etree.tostring(tree3, pretty_print=True).decode())
    # Expected output (root4 is copied):
    # <root3>
    #  <element3>text3</element3>
    #  <root4>
    #   <element4>text4</element4>
    #  </root4>
    # </root3>
    print(etree.tostring(tree4, pretty_print=True).decode())
    # Expected output (tree4 is unchanged):
    # <root4>
    #  <element4>text4</element4>
    # </root4>

if __name__ == '__main__':
    main()

