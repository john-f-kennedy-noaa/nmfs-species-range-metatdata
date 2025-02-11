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

    xml = '''<metadata xml:lang="en">
        <Esri>
            <CreaDate>20191125</CreaDate>
            <CreaTime>10235000</CreaTime>
            <ArcGISFormat>1.0</ArcGISFormat>
            <ArcGISstyle>ISO 19139 Metadata Implementation Specification</ArcGISstyle>
            <SyncOnce>FALSE</SyncOnce>
            <DataProperties>
                <itemProps>
                    <itemName Sync="TRUE">WhaleBlue_20201014</itemName>
                    <imsContentType Sync="TRUE" export="False">002</imsContentType>
                    <itemSize Sync="TRUE">0.000</itemSize>
                    <nativeExtBox>
                        <westBL Sync="TRUE">-179.999989</westBL>
                        <eastBL Sync="TRUE">179.999989</eastBL>
                        <southBL Sync="TRUE">-87.997582</southBL>
                        <northBL Sync="TRUE">78.378549</northBL>
                        <exTypeCode Sync="TRUE">1</exTypeCode>
                    </nativeExtBox>
                </itemProps>
                <coordRef>
                    <type Sync="TRUE">Geographic</type>
                    <geogcsn Sync="TRUE">GCS_WGS_1984</geogcsn>
                    <csUnits Sync="TRUE">Angular Unit: Degree (0.017453)</csUnits>
                    <peXml Sync="TRUE">&lt;GeographicCoordinateSystem xsi:type='typens:GeographicCoordinateSystem' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xmlns:xs='http://www.w3.org/2001/XMLSchema' xmlns:typens='http://www.esri.com/schemas/ArcGIS/3.4.0'&gt;&lt;WKT&gt;GEOGCS[&amp;quot;GCS_WGS_1984&amp;quot;,DATUM[&amp;quot;D_WGS_1984&amp;quot;,SPHEROID[&amp;quot;WGS_1984&amp;quot;,6378137.0,298.257223563]],PRIMEM[&amp;quot;Greenwich&amp;quot;,0.0],UNIT[&amp;quot;Degree&amp;quot;,0.0174532925199433],AUTHORITY[&amp;quot;EPSG&amp;quot;,4326]]&lt;/WKT&gt;&lt;XOrigin&gt;-400&lt;/XOrigin&gt;&lt;YOrigin&gt;-400&lt;/YOrigin&gt;&lt;XYScale&gt;1111948722.2222221&lt;/XYScale&gt;&lt;ZOrigin&gt;-100000&lt;/ZOrigin&gt;&lt;ZScale&gt;10000&lt;/ZScale&gt;&lt;MOrigin&gt;-100000&lt;/MOrigin&gt;&lt;MScale&gt;10000&lt;/MScale&gt;&lt;XYTolerance&gt;8.983152841195215e-09&lt;/XYTolerance&gt;&lt;ZTolerance&gt;0.001&lt;/ZTolerance&gt;&lt;MTolerance&gt;0.001&lt;/MTolerance&gt;&lt;HighPrecision&gt;true&lt;/HighPrecision&gt;&lt;LeftLongitude&gt;-180&lt;/LeftLongitude&gt;&lt;WKID&gt;4326&lt;/WKID&gt;&lt;LatestWKID&gt;4326&lt;/LatestWKID&gt;&lt;/GeographicCoordinateSystem&gt;</peXml>
                </coordRef>
            </DataProperties>
            <SyncDate>20250117</SyncDate>
            <SyncTime>19300100</SyncTime>
            <ModDate>20250117</ModDate>
            <ModTime>19300100</ModTime>
            <scaleRange>
                <minScale>150000000</minScale>
                <maxScale>5000</maxScale>
            </scaleRange>
            <ArcGISProfile>ISO19139</ArcGISProfile>
        </Esri>
        <dataIdInfo>
            <envirDesc Sync="FALSE">Esri ArcGIS 13.4.0.55405</envirDesc>
            <dataLang>
                <languageCode value="eng" Sync="TRUE"></languageCode>
                <countryCode value="USA" Sync="TRUE"></countryCode>
            </dataLang>
            <idCitation>
                <resTitle Sync="FALSE">WhaleBlue_20201014</resTitle>
                <presForm>
                    <PresFormCd value="005" Sync="TRUE"></PresFormCd>
                    <fgdcGeoform>vector digital data</fgdcGeoform>
                </presForm>
                <resAltTitle>WhaleBlue_20201014</resAltTitle>
                <date>
                    <createDate>2020-10-14T00:00:00</createDate>
                </date>
            </idCitation>
            <spatRpType>
                <SpatRepTypCd value="001" Sync="TRUE"></SpatRepTypCd>
            </spatRpType>
            <idPurp>The following map depicts the geographic range for ESA-listed blue whales.</idPurp>
            <dataChar>
                <CharSetCd value="004"></CharSetCd>
            </dataChar>
            <resMaint>
                <maintFreq>
                    <MaintFreqCd value="009"></MaintFreqCd>
                </maintFreq>
            </resMaint>
            <idAbs>&lt;DIV STYLE="text-align:Left;"&gt;&lt;DIV&gt;&lt;DIV&gt;&lt;P&gt;&lt;SPAN&gt;&lt;SPAN&gt;This dataset was developed to show those areas potentially used by Endangered Species Act (ESA) and/or Marine Mammal Protection Act (MMPA) listed species under National Marine Fisheries Service (NMFS) jurisdiction. &lt;/SPAN&gt;&lt;/SPAN&gt;&lt;SPAN&gt;&lt;SPAN&gt;The data was created by digitizing range information from public and agency sources.  These sources include OBIS the Ocean Biogeographic System (iobis.org), natural history guidebooks (National Audubon Society. 2002. Guide to Marine Mammals of the World), recovery and conservation plans, listing actions and status reports, and other agency sources.  All resulting range polygons were then reviewed and approved by expert NMFS biologists specializing in the species and were finally approved by NMFS Office of Protected Resources management team.  Range data include information on the range of all life stages.  Offshore distances are approximate for some species as sampling and distribution information in deeper waters are often based on more limited and fragmentary evidence and studies. &lt;/SPAN&gt;&lt;/SPAN&gt;&lt;SPAN&gt;&lt;SPAN&gt;The data DO NOT constitute a legal or regulatory description of range and are only provided for general guidance to members of the public or action agencies considering the development of projects that may affect species protected by either of these two laws.&lt;/SPAN&gt;&lt;/SPAN&gt;&lt;/P&gt;&lt;/DIV&gt;&lt;/DIV&gt;&lt;/DIV&gt;</idAbs>
            <searchKeys>
                <keyword>blue whale</keyword>
                <keyword>species range</keyword>
                <keyword>NMFS</keyword>
                <keyword>ESA</keyword>
            </searchKeys>
            <idCredit>NMFS Office of Protected Resources</idCredit>
            <idPoC>
                <rpIndName>Jonathan Molineaux</rpIndName>
                <rpOrgName>NMFS Office of Protected Resources</rpOrgName>
                <rpPosName>Fisheries Biologist</rpPosName>
                <role>
                    <RoleCd value="007"></RoleCd>
                </role>
            </idPoC>
            <tpCat>
                <TopicCatCd value="007"></TopicCatCd>
            </tpCat>
            <tpCat>
                <TopicCatCd value="014"></TopicCatCd>
            </tpCat>
            <dataExt>
                <geoEle>
                    <GeoBndBox esriExtentType="search">
                        <exTypeCode Sync="TRUE">1</exTypeCode>
                        <westBL Sync="TRUE">-179.999989</westBL>
                        <eastBL Sync="TRUE">179.999989</eastBL>
                        <northBL Sync="TRUE">78.378549</northBL>
                        <southBL Sync="TRUE">-87.997582</southBL>
                    </GeoBndBox>
                </geoEle>
            </dataExt>
        </dataIdInfo>
    </metadata>'''

    tree = etree.XML(xml)

    etree.indent(tree, space="    ")

    ##print(etree.tostring(tree, pretty_print=True, method='html', encoding="utf-8").decode())

    ##for elem in tree.xpath('.//rpIndName'):
    ##    print(f"Tag: {elem.tag} Parent: {elem.getparent().tag}")
    ## #Tag: rpIndName Parent: idPoC

    ##for elem in tree.xpath('//rpIndName/self::*'):
    ##    print(f"Name: {elem.text}")
    ## # Name: Jonathan Molineaux

    ##for elem in tree.xpath('//rpIndName//ancestor::*'):
    ##    if elem.tag == "name":
    ##        print(f"Self: {elem.tag}")
    ##    else:
    ##        print(f"Ancestor: {elem.tag}")
    ## #Ancestor: metadata
    ## #Ancestor: dataIdInfo
    ## #Ancestor: idPoC
    ## #Ancestor: rpIndName

    ##for elem in tree.xpath('//rpIndName//ancestor-or-self::*'):
    ##    if elem.tag == "name":
    ##        print(f"Self: {elem.tag}")
    ##    else:
    ##        print(f"Ancestor: {elem.tag}")
    ## #Ancestor: metadata
    ## #Ancestor: dataIdInfo
    ## #Ancestor: idPoC
    ## #Ancestor: rpIndName

    ##for elem in tree.xpath('//rpIndName/../preceding::*'): # Find the selected element ('group') and then the siblings of the proceeding element ('chart')
    ##    if elem.tag == "name":
    ##        print(f"Tag: '{elem.tag}' Text: '{elem.text}'")
    ##    else:
    ##        print(f"Ancestor: '{elem.tag}'")

    ##for elem in tree.xpath('//rpIndName/../preceding-sibling::*'): # Find the selected element ('group') and then the siblings of the proceeding element ('chart')
    ##    if elem.tag == "name":
    ##        print(f"Tag: '{elem.tag}' Text: '{elem.text}'")
    ##    else:
    ##        print(f"Ancestor: '{elem.tag}'")
    ##
    ## #Ancestor: 'envirDesc'
    ## #Ancestor: 'dataLang'
    ## #Ancestor: 'idCitation'
    ## #Ancestor: 'spatRpType'
    ## #Ancestor: 'idPurp'
    ## #Ancestor: 'dataChar'
    ## #Ancestor: 'resMaint'
    ## #Ancestor: 'idAbs'
    ## #Ancestor: 'searchKeys'
    ## #Ancestor: 'idCredit'

    for elem in tree.xpath(f".//*[self::rpCntInfo/cntAddress/eMailAdd or self::rpIndName or self::rpOrgName]/parent::*"):
        #print(f"Tag: '{elem.tag}' Text: '{elem.text}'")
        print(elem.tag)

#target_tree.xpath(f".//*[self::rpCntInfo/cntAddress/eMailAdd or self::rpIndName or self::rpOrgName]/ancestor::*")


##    # Example usage
##    #xml_string = "<root><child attr='value' /><child attr='value' /><other_child /></root>"
##    #tree = etree.fromstring(xml_string)
##    result = find_nodes_with_duplicate_children(tree)
##    print(result)  # Output: [<Element root at 0x...>]

if __name__ == '__main__':
    main()
