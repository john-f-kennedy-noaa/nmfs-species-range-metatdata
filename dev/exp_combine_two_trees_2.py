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
    try:

        from lxml import etree
        from copy import deepcopy
        from io import BytesIO

        _xml_1 = '''<measResult>
                    <ConResult>
                        <conSpec>
                            <resTitle>Specification Title.</resTitle>
                            <date>
                                <pubDate>2021-07-12T10:03:34</pubDate>
                            </date>
                        </conSpec>
                    </ConResult>
                </measResult>'''

        _xml_2 = '''<measResult>
                    <ConResult>
                        <conSpec>
                            <resTitle>Specification Title.</resTitle>
                            <resAltTitle></resAltTitle>
                            <collTitle></collTitle>
                            <date>
                                <createDate></createDate>
                                <pubDate></pubDate>
                                <reviseDate></reviseDate>
                            </date>
                        </conSpec>
                        <conExpl>Results reviewed by team members</conExpl>
                        <conPass>1</conPass>
                    </ConResult>
                </measResult>'''



        _root_1 = etree.XML(_xml_1, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
        _root_2 = etree.XML(_xml_2, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))

        #print(etree.tostring(_root_1, pretty_print=True).decode())
        #print(etree.tostring(_root_2, pretty_print=True).decode())

    ##    for descendent in _root_1.iterdescendants():
    ##        ancestors = ""
    ##        for ancestor in descendent.iterancestors():
    ##            ancestors = f"/{ancestor.tag}" + ancestors
    ##            del ancestor
    ##        #print(ancestors)
    ##        #print(descendent.tag)
    ##        del ancestors


    ##    for descendent in _root_2.iterdescendants():
    ##        ancestors = ""
    ##        for ancestor in descendent.iterancestors():
    ##            ancestors = f"/{ancestor.tag}" + ancestors
    ##            del ancestor
    ##        #print(ancestors)
    ##        #print(descendent.tag)
    ##        del ancestors

    ##        xml_file = BytesIO(b'''<measResult>
    ##                <ConResult>
    ##                    <conSpec>
    ##                        <resTitle>Specification Title.</resTitle>
    ##                        <date>
    ##                            <pubDate></pubDate>
    ##                        </date>
    ##                    </conSpec>
    ##                </ConResult>
    ##            </measResult>''')
    ##
    ##    for event, element in etree.iterparse(xml_file):
    ##        #print(f"{event}, {element.tag:>4}, {element.text}")
    ##
    ##        ancestors = ""
    ##        for ancestor in element.iterancestors():
    ##            ancestors = f"/{ancestor.tag}" + ancestors
    ##            del ancestor
    ##
    ##        element_path = f"{ancestors}/{element.tag}"
    ##        #print(element_path)
    ##
    ##        #__element = _root_1.xpath(f"{element_path}")
    ##        #for __elem in __element:
    ##        #    print(f"__elem: {__elem.tag}")

        xml_file = BytesIO(b'''<measResult>
                                <ConResult>
                                    <conSpec>
                                        <resTitle>Specification Title.</resTitle>
                                        <resAltTitle>Alt Specification Title.</resAltTitle>
                                        <collTitle>Collection Specification Title.</collTitle>
                                        <date>
                                            <createDate>2021-07-12T10:03:34</createDate>
                                            <pubDate>2021-07-12T10:03:34</pubDate>
                                            <reviseDate>2025-03-01T19:22:37</reviseDate>
                                        </date>
                                    </conSpec>
                                    <conExpl>Results reviewed by team members</conExpl>
                                    <conPass>1</conPass>
                                </ConResult>
                            </measResult>''')

        #print("##################################################################")

        for event, element in etree.iterparse(xml_file):
            #print(f"{event}, {element.tag:>4}, {element.text} {isinstance(element.text, type(None))}")

            if isinstance(element.text, type(None)):
                #print(f"{event}, {element.tag:>4}, {element.text} {isinstance(element.text, type(None))}")
                ancestors = ""
                _root = element
                while _root.getparent() is not None:
                    _root = _root.getparent()
                    ancestors = f"/{_root.tag}" + ancestors
                element_path = f"{ancestors}/{element.tag}"
                print(f"element_path: {element_path}")

                _element = _root_1.xpath(f"{element_path}")
                if len(_element) == 0:
                    #print(f"append: {element.tag}")
                    #print(ancestors)
                    parent = _root_1.xpath(f"{ancestors}")[0]
                    parent.append(element)
                    del parent
                elif len(_element) == 1:
                    print("udate?")
                    print(_element[0].tag)
                else: pass
                #for __elem in __element:
                #    print(__elem.tag)
                del _element

                del element_path
                del ancestors
            elif not isinstance(element.text, type(None)):
                #print(f"{event}, {element.tag:>4}, {element.text} {isinstance(element.text, type(None))}")
                ancestors = ""
                _root = element
                while _root.getparent() is not None:
                    _root = _root.getparent()
                    ancestors = f"/{_root.tag}" + ancestors
                element_path = f"{ancestors}/{element.tag}"
                print(f"element_path: {element_path}")

                _element = _root_1.xpath(f"{element_path}")
                if len(_element) == 0:
                    #print(f"append: {element.tag}")
                    #print(ancestors)
                    parent = _root_1.xpath(f"{ancestors}")[0]
                    parent.append(element)
                    del parent
                elif len(_element) == 1 and not isinstance(_element[0].text, type(None)):
                    pass
                    print(f"udate?\n\tTag: {_element[0].tag}, Text: {_element[0].text}")
                else: pass
                #for __elem in __element:
                #    print(__elem.tag)
                del _element

                del element_path
                del ancestors
            else:
                pass
    ##        ancestors = ""
    ##        for ancestor in element.iterancestors():
    ##            ancestors = f"/{ancestor.tag}" + ancestors
    ##            del ancestor
    ##        element_path = f"{ancestors}/{element.tag}"
    ##        print(f"element_path: {element_path}")
    ##        del ancestors

    ##        __element = _root_1.xpath(f"{element_path}")
    ##        for __elem in __element:
    ##            ancestors = ""
    ##            for ancestor in __elem.iterancestors():
    ##                ancestors = f"/{ancestor.tag}" + ancestors
    ##                del ancestor
    ##            __elem_path = f"{ancestors}/{__elem.tag}"
    ##            del ancestors
    ##            print(f"__elem_path: {__elem_path}")

        etree.indent(_root_1, space=' ')
        _xml = etree.tostring(_root_1, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True)
        # This allows for sorting
        doc = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
        print(etree.tostring(doc, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
        del doc

        #print(etree.tostring(_root_1, pretty_print=True).decode())
        #print(etree.tostring(_root_2, pretty_print=True).decode())
        #print(etree.tostring(_root_1, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
        #print(etree.tostring(_root_2, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())

    except Exception:
        traceback.print_exc()
    except:
        traceback.print_exc()

if __name__ == '__main__':
    main()

