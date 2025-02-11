#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john.f.kennedy
#
# Created:     13/01/2025
# Copyright:   (c) john.f.kennedy 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    try:
    ##    from lxml import etree
    ##    a  = etree.Element("a")
    ##    b  = etree.SubElement(a, "b")
    ##    c  = etree.SubElement(a, "c")
    ##    d1 = etree.SubElement(c, "d")
    ##    d2 = etree.SubElement(c, "d")
    ##
    ##    tree = etree.ElementTree(c)
    ##    print(tree.getpath(d2))
    ##
    ##    print(tree.getpath(d2))
    ##    print(tree.xpath(tree.getpath(d2)) == [d2])
        from lxml import etree

##        original_xml = "<root><dc><batman alias='dark_knight' /></dc></root>"
##        modified_tag = "<batman alias='not_dark_knight' />"
##        x_path = '/root/dc/batman'
##        original_obj = etree.fromstring(original_xml)
##        modified_obj = etree.fromstring(modified_tag)
##
##        #original_obj.replace(original_obj.xpath(x_path)[0], modified_obj)
##
##        batman = original_obj.xpath(x_path)[0]
##        #print(batman)
##        batman.getparent().replace(batman, modified_obj)
##
##        print(etree.tostring(original_obj, pretty_print=True).decode())
##
##        print(etree.tostring(batman, pretty_print=True).decode())

        xml_string = "<root><child1><grandchild></grandchild></child1><child2></child2></root>"

        tree = etree.fromstring(xml_string)
        print(etree.tostring(tree, pretty_print=True).decode())

        # Incorrect: Trying to replace 'child2' with 'grandchild' which is not a direct child
        #child2_element = tree.xpath("child2")[0]
        #print(child2_element)
        #grandchild_element = tree.xpath("child1/grandchild")
        #child2_element.replace(grandchild_element)

        # Correct: Replace 'grandchild' with 'new_element' which is a child of 'child1'
        grandchild_element = tree.xpath("child1/grandchild")[0]
        child1_element = tree.xpath("child1")[0]
        new_element = etree.Element("new_element")
        child1_element.replace(grandchild_element, new_element)

        print(etree.tostring(tree, pretty_print=True).decode())

    except:
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()
