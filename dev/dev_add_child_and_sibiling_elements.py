#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john.f.kennedy
#
# Created:     07/01/2025
# Copyright:   (c) john.f.kennedy 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    try:
        import traceback
        from lxml import etree
        from src.project_tools import pretty_format_xml_file

        target_xml = r"C:\Users\john.f.kennedy\Documents\ArcGIS\Projects\ArcPy Studies\XML\nmfs-species-range-metatdata\species_range_boilerplate.xml"
        target_tree = etree.parse(target_xml)
        target_root = target_tree.getroot()
        # print(etree.tostring(tree.getroot(), pretty_print=True).decode(), end='')

        UpdateRpCntInfos = True
        if UpdateRpCntInfos:
            rpCntInfos = target_root.findall(".//rpCntInfo/cntOnlineRes")
            for rpCntInfo in rpCntInfos:
                #print(etree.tostring(rpCntInfo, pretty_print=True).decode(), end='')
                #print(etree.tostring(rpCntInfo, pretty_print=False).decode(), end='')

                children = [c for c in rpCntInfo.getchildren()]
                if children:
                    # <protocol>REST Service</protocol>
                    print(f"Before {rpCntInfo.tag}")
                    for child in children:
                        print(f"\t{child.tag:<8} = {child.text}")
                        #print(f"\t{child}")
                    del child
                    if children[1].tag != "protocol":
                        rpCntInfo.insert(1, etree.SubElement(rpCntInfo, "protocol"))
                        protocol = rpCntInfo.find("./protocol")
                        protocol.text = "REST Service"
                    if children[1].tag == "protocol" and children[1].text is not None:
                        protocol = rpCntInfo.find("./protocol")
                        protocol.text = "REST Service"

                    #for child in children:
                    #    print(f"\t{child.tag}")
                    #    #print(f"\t{child}")
                del children

                children = [c for c in rpCntInfo.getchildren()]
                if children:
                    # <protocol>REST Service</protocol>
                    print(f"After {rpCntInfo.tag}")
                    for child in children:
                        print(f"\t{child.tag:<8} = {child.text}")
                        if child.tag == "protocol":
                            protocol = rpCntInfo.find("./protocol")
                            ancestors = []
                            for ancestor in protocol.iterancestors():
                                if not ancestor.tag == "metadata":
                                    ancestors.append(ancestor.tag)
                                del ancestor
                            #print(ancestors, isinstance(ancestors, list))
                            ancestors_path = "./" + "/".join(list(reversed(ancestors))) + "/protocol"
                            print(ancestors_path)
                            print(target_root.find(ancestors_path).text)

                            del ancestors

                            #ancestor_tags = [ancestor.tag for ancestor in protocol.iterancestors()]
                            #if isinstance(ancestor_tags, list):
                            #    ancestors = ancestor_tags.reverse()
                            #    print(ancestors)
                            #if ancestors:
                            #    ancestors = list(ancestors.reverse())
                            #    print(ancestors, type(ancestors))
                                #print("/".join(ancestors))
                                #print(ancestor.tag)
                            #del ancestor
                del rpCntInfo

            del rpCntInfos
        del UpdateRpCntInfos
        #protocol = target_root.xpath('.//protocol[text()="ESRI REST Service"]')
        #print(protocol[0].text)

        #print(target_tree.find('.//protocol[text()="ESRI REST Service"]').tag)

        # Exact text match
        #e = root.xpath('.//a[text()="TEXT A"]')
        # Text contain a match
        #e = root.xpath('.//a[contains(text(),"TEXT A")]')
        # Text starts with a match
        #e = root.xpath('.//a[starts-with(text(),"TEXT A")]')

        # Write the XML to the file
        target_tree.write(target_xml)
        pretty_format_xml_file(target_xml)

        del target_xml, target_tree, target_root
        del traceback, etree, pretty_format_xml_file

    ##    for _, element in etree.iterparse(target_xml, tag='onLineSrc'):
    ##        print(f"{element.findtext('ESRI REST Service')}") #, element[1].text))
    ##        element.clear(keep_tail=True)
    except:
        traceback.print_exc()

if __name__ == '__main__':
    main()
