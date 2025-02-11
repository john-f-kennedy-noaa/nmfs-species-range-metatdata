#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john.f.kennedy
#
# Created:     25/01/2025
# Copyright:   (c) john.f.kennedy 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from lxml import etree

def find_nodes_with_duplicate_children(root):
    """
    Finds nodes in the XML tree that have at least two children with the same tag and attributes.
    Args:
        root: The root element of the XML tree.
    Returns:
        A list of parent elements that have duplicate children.
    """
    duplicate_parents = []
    for parent in root.iter():
        child_tags = set()
        for child in parent.iterchildren():
            child_key = (child.tag, tuple(child.attrib.items()))
            if child_key in child_tags:
                duplicate_parents.append(parent)
                break
            child_tags.add(child_key)
    return duplicate_parents

def main():

    # Example usage
    xml_string = "<root><child attr='value' /><child attr='value' /><other_child /></root>"
    tree = etree.fromstring(xml_string)
    result = find_nodes_with_duplicate_children(tree)
    print(result[0].tag)  # Output: [<Element root at 0x...>]

if __name__ == '__main__':
    main()
