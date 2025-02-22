#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john.f.kennedy
#
# Created:     19/02/2025
# Copyright:   (c) john.f.kennedy 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from lxml import etree

def main():
    # Create the first tree
    root1 = etree.Element("root1")
    element1 = etree.SubElement(root1, "element1")
    element1.text = "Text in element1"
    tree1 = etree.ElementTree(root1)

    print("Tree 1")
    print(etree.tostring(tree1, pretty_print=True, encoding="unicode"))

    # Create the second tree
    root2 = etree.Element("root2")
    element2 = etree.SubElement(root2, "element2")
    element2.text = "Text in element2"
    tree2 = etree.ElementTree(root2)

    print("Tree 2")
    print(etree.tostring(tree2, pretty_print=True, encoding="unicode"))


    # Find the node in the first tree where you want to append the second tree
    #target_node = tree1.find("element1")
    target_node1 = tree1.xpath("element1")

    print("target_node 1")
    print(etree.tostring(target_node1[0], pretty_print=True, encoding="unicode"))

    target_node2 = tree2.xpath("element2")

    print("target_node 2")
    print(etree.tostring(target_node2[0], pretty_print=True, encoding="unicode"))

    # Append the root of the second tree to the target node
    root1.append(target_node2[0])

    #print("target_node 1")
    #print(etree.tostring(target_node1[1], pretty_print=True, encoding="unicode"))

    # Print the merged tree
    print(etree.tostring(tree1, pretty_print=True, encoding="unicode"))

##<root1>
##    <element1>Text in element1
##        <root2>
##            <element2>Text in element2</element2>
##        </root2>
##    </element1>
##</root1>

if __name__ == '__main__':
    main()
