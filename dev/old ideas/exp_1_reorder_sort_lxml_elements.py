#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john.f.kennedy
#
# Created:     20/01/2025
# Copyright:   (c) john.f.kennedy 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
##    from lxml import objectify, etree
##
##    print("Use lxml objectify")
##    canvas = objectify.fromstring("""
##    <canvas>
##      <shape name="a" />
##      <shape name="b" />
##      <shape name="c" />
##    </canvas>
##        """)
##    canvas.shape = [canvas.shape[1], canvas.shape[0], canvas.shape[2]]
##    etree.indent(canvas, space="    ")
##    print(etree.tostring(canvas, pretty_print=True, method='html', encoding="utf-8").decode())
##
##    # Get the second item element
##    #item2 = tree.xpath("mdChar")[0]
##    # Get the index of item2 within its parent (root)
##    #index_of_item2 = tree.index(item2)
##    #print(f"Index of '{item2.tag}': {index_of_item2}")  # Output: 1
##
##
##    data = """<X>
##                <X03>3</X03>
##                <X02>2</X02>
##                <A>
##                    <A02>Y</A02>
##                    <A01>X</A01>
##                    <A03>Z</A03>
##                </A>
##                <X01>1</X01>
##                <B>
##                    <B01>Z</B01>
##                    <B02>X</B02>
##                    <B03>C</B03>
##                </B>
##              </X>"""

##    '''<X>
##         <A>
##            <A01>X</A01>
##            <A02>Y</A02>
##            <A03>Z</A03>
##         </A>
##         <B>
##            <B01>Z</B01>
##            <B02>X</B02>
##            <B03>C</B03>
##         </B>
##         <X01>1</X01>
##         <X02>2</X02>
##         <X03>3</X03>
##      </X>'''

##    doc = etree.XML(data,etree.XMLParser(remove_blank_text=True))
##    for parent in doc.xpath('//*[./*]'): # Search for parent elements
##        parent[:] = sorted(parent,key=lambda x: x.tag)
##
##        idx = lambda x: x.tag
##        #print(idx(parent))
##
##    etree.indent(doc, space="  ")
##    #print(etree.tostring(doc, pretty_print=True))
##    #print(etree.tostring(doc, pretty_print=True, method='html', encoding="utf-8").decode())
##
##    #print(doc.tag)
##    #print(type(doc))

##    from lxml import etree
##    # Parse an XML document
##    tree = etree.fromstring("<root><item1/><item2/><item3/></root>")
##    # Get the second item element
##    item2 = tree.xpath("item2")[0]
##    # Get the index of item2 within its parent (root)
##    index_of_item2 = tree.index(item2)
##    print(f"Index of 'item2': {index_of_item2}")  # Output: 1

# https://stackoverflow.com/questions/8385358/lxml-sorting-tag-order
# lxml etree order children under parent
##    xml_string = etree.tostring(xml, pretty_print=True, method='html', encoding="utf-8").decode()
##    #print(xml_string)
##
##    doc = etree.XML(xml_string, etree.XMLParser(remove_blank_text=True))
##
##    print(len(doc.xpath('//*[./*]')))
##    print(doc.xpath('//*[./*]'))
##
##    for parent in doc.xpath('//*[./*]'): # Search for parent elements
##        print(parent.tag)
##        parent[:] = sorted(parent,key=lambda x: tag_position_dict[x.tag])
##    etree.indent(doc, space="  ")
##    #print(etree.tostring(doc, pretty_print=True))
##    print(etree.tostring(doc, pretty_print=True, method='html', encoding="utf-8").decode())

    # xml = objectify.fromstring("""<metadata><Esri>Esri</Esri><eainfo>eainfo</eainfo><mdLang>mdLang</mdLang><mdChar>mdChar</mdChar><mdHrLv>mdHrLv</mdHrLv><mdHrLvName>dataset</mdHrLvName><mdDateSt>20250117</mdDateSt><mdStanName>ArcGIS Metadata</mdStanName><mdStanVer>1.0</mdStanVer><distInfo>distInfo</distInfo><dataIdInfo>dataIdInfo</dataIdInfo><mdMaint>mdMaint</mdMaint><dqInfo>dqInfo</dqInfo><spatRepInfo>spatRepInfo</spatRepInfo><refSysInfo>refSysInfo</refSysInfo><spdoinfo>spdoinfo</spdoinfo></metadata>""")

##    sort_order = dict()
##    for child in root.iterchildren():
##        #print(type(child))
##        sort_order[child.tag] = root.index(child)
##    #print(sort_order)


##    #xml
##    #etree.indent(xml, space="  ")
##    #print(xml_string)
##    doc = etree.XML(xml_string, etree.XMLParser(remove_blank_text=True))
##    for parent in doc.xpath('.'): # Search for parent elements
##        #print(type(parent))
##    #for parent in doc.xpath('//*[./*]'): # Search for parent elements
##        parent[:] = sorted(parent,key=lambda x: tag_position_dict[x.tag])
##    etree.indent(doc, space="  ")
##    #print(etree.tostring(doc, pretty_print=True, encoding="utf-8").decode())

##    # Parse an XML document
##    #tree = etree.fromstring("<root><item1/><item2/><item3/></root>")

##    from lxml import objectify, etree
##
##    xml = objectify.fromstring("""<metadata>
##    <Esri>Esri</Esri>
##    <eainfo>eainfo</eainfo>
##    <mdLang>mdLang</mdLang>
##    <mdChar>mdChar</mdChar>
##    <mdHrLv>mdHrLv</mdHrLv>
##    <mdHrLvName>dataset</mdHrLvName>
##    <mdDateSt>20250117</mdDateSt>
##    <mdStanName>ArcGIS Metadata</mdStanName>
##    <mdStanVer>1.0</mdStanVer>
##    <distInfo>distInfo</distInfo>
##    <dataIdInfo>dataIdInfo</dataIdInfo>
##    <mdMaint>mdMaint</mdMaint>
##    <dqInfo>dqInfo</dqInfo>
##    <spatRepInfo>spatRepInfo</spatRepInfo>
##    <refSysInfo>refSysInfo</refSysInfo>
##    <spdoinfo>spdoinfo</spdoinfo>
##    </metadata>""")

    from lxml import etree

##    xml_from_string = etree.fromstring("""<metadata>
##                                            <Esri>Esri</Esri>
##                                            <eainfo>eainfo</eainfo>
##                                            <mdLang>mdLang</mdLang>
##                                            <mdChar>mdChar</mdChar>
##                                            <mdHrLv>mdHrLv</mdHrLv>
##                                            <mdHrLvName>dataset</mdHrLvName>
##                                            <mdDateSt>20250117</mdDateSt>
##                                            <mdStanName>ArcGIS Metadata</mdStanName>
##                                            <mdStanVer>1.0</mdStanVer>
##                                            <distInfo>distInfo</distInfo>
##                                            <dataIdInfo>dataIdInfo</dataIdInfo>
##                                            <mdMaint>mdMaint</mdMaint>
##                                            <dqInfo>dqInfo</dqInfo>
##                                            <spatRepInfo>spatRepInfo</spatRepInfo>
##                                            <refSysInfo>refSysInfo</refSysInfo>
##                                            <spdoinfo>spdoinfo</spdoinfo>
##                                         </metadata>
##                                      """)

##    xml_string = """<metadata xml:lang="en">
##                    <Esri>Esri</Esri>
##                    <eainfo>eainfo</eainfo>
##                    <mdLang>mdLang</mdLang>
##                    <mdChar>mdChar</mdChar>
##                    <mdHrLv>mdHrLv</mdHrLv>
##                    <mdHrLvName>dataset</mdHrLvName>
##                    <mdDateSt>20250117</mdDateSt>
##                    <mdStanName>ArcGIS Metadata</mdStanName>
##                    <mdStanVer>1.0</mdStanVer>
##                    <distInfo>distInfo</distInfo>
##                    <dataIdInfo>dataIdInfo</dataIdInfo>
##                    <mdMaint>mdMaint</mdMaint>
##                    <dqInfo>dqInfo</dqInfo>
##                    <spatRepInfo>spatRepInfo</spatRepInfo>
##                    <refSysInfo>refSysInfo</refSysInfo>
##                    <spdoinfo>spdoinfo</spdoinfo>
##                  </metadata>
##               """

    xml_string = """<metadata xml:lang="en"><Esri>Esri</Esri><eainfo>eainfo</eainfo><mdLang>mdLang</mdLang><mdChar>mdChar</mdChar><mdHrLv>mdHrLv</mdHrLv><mdHrLvName>dataset</mdHrLvName><mdDateSt>20250117</mdDateSt><mdStanName>ArcGIS Metadata</mdStanName><mdStanVer>1.0</mdStanVer><distInfo>distInfo</distInfo><dataIdInfo>dataIdInfo</dataIdInfo><mdMaint>mdMaint</mdMaint><dqInfo>dqInfo</dqInfo><spatRepInfo>spatRepInfo</spatRepInfo><refSysInfo>refSysInfo</refSysInfo><spdoinfo>spdoinfo</spdoinfo></metadata>"""

    tag_position_dict = {
                     "dqScope"     : 0,
                     "report"      : {"DQConcConsis" : 1, "DQCompOm" : 2},
                     "dataLineage" : 3,
                     "Esri"        : 0,
                     "dataIdInfo"  : 1,
                     "mdChar"      : 2,
                     "mdContact"   : 3,
                     "mdDateSt"    : 4,
                     "mdFileID"    : 5,
                     "mdLang"      : 6,
                     "mdMaint"     : 7,
                     "mdHrLv"      : 8,
                     "mdHrLvName"  : 9,
                     "mdStanName"  : 10,
                     "mdStanVer"   : 11,
                     "refSysInfo"  : 12,
                     "spatRepInfo" : 13,
                     "spdoinfo"    : 14,
                     "dqInfo"      : 15,
                     "distInfo"    : 16,
                     "eainfo"      : 17,
                     "statement"   : 0,
                     "dataSource"  : 1,
                     "prcStep"     : 2,
                     "Binary"      : 18,
                     "Thumbnail"   : 0,
                    }


    root = etree.XML(xml_string)

    #print(etree.tostring(root))

    etree.indent(root, space="    ")
    print(etree.tostring(root, xml_declaration=True, encoding="utf-8").decode())

    for child in root.xpath("."):
        child[:] = sorted(child, key=lambda x: tag_position_dict[x.tag])

    etree.indent(root, space="    ")
    print(etree.tostring(root, xml_declaration=True, encoding="utf-8").decode())

    xml_file = r'C:\Users\john.f.kennedy\Documents\ArcGIS\Projects\ArcPy Studies\XML\nmfs-species-range-metatdata\Export 2025-01-27\_SeaTurtleGreen_20210129.xml'

    # Parse the XML
    parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
    tree = etree.parse(xml_file, parser=parser)
    root = tree.getroot()
    del parser

    etree.indent(root, space="    ")
    print(etree.tostring(root, xml_declaration=True, encoding="utf-8").decode())

    for child in root.xpath("."):
        child[:] = sorted(child, key=lambda x: tag_position_dict[x.tag])

    etree.indent(root, space="    ")
    print(etree.tostring(root, xml_declaration=True, encoding="utf-8").decode())


##    contact_xml_string = etree.fromstring(f'<{parent.tag}><editorSource>external</editorSource><editorDigest/><rpIndName/><rpOrgName/><rpPosName/><rpCntInfo><cntAddress addressType="both"><delPoint/><city/><adminArea/><postCode/><eMailAdd/><country>US</country></cntAddress><cntPhone><voiceNum tddtty=""></voiceNum><faxNum/></cntPhone><cntHours/><cntOnlineRes><linkage/><protocol/><orName/><orDesc/><orFunct><OnFunctCd value="002"></OnFunctCd></orFunct></cntOnlineRes></rpCntInfo><editorSave/><displayName/><role><RoleCd value="005"></RoleCd></role></{parent.tag}>')
##    # create an ElementTree object from the metadata XML string
##    contact_tree = etree.ElementTree(contact_xml_string)
##    contact_root = contact_tree.getroot()

##
##    xml_string = etree.tostring(xml, pretty_print=True, method='html', encoding="utf-8").decode()
##
##    print(etree.tostring(xml_string, pretty_print=True, encoding="utf-8").decode())
##
##    new_xml_string = etree.fromstring(xml_string)
##    # create an ElementTree object from the metadata XML string
##    tree = etree.ElementTree(new_xml_string)
##    root = tree.getroot()
##
##    for child in root.xpath("."):
##        child[:] = sorted(child, key=lambda x: tag_position_dict[x.tag])
##
##    #print(etree.tostring(root, pretty_print=True, encoding="utf-8").decode())


if __name__ == '__main__':
    main()
