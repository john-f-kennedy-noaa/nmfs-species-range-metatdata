#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john.f.kennedy
#
# Created:     31/01/2025
# Copyright:   (c) john.f.kennedy 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    datainfo_dict = {"idCitation"   : 0,
                        "resTitle"      : 1,
                        "resAltTitle"   : 2,
                        "collTitle"     : 3,
                        "presForm"      : 4,
                        "PresFormCd"        : 0,
                        "fgdcGeoform"       : 1,
                        "date"          : 5,
                        "createDate"        : 0,
                        "pubDate"           : 1,
                        "revisedDate"       : 2,
                        "citRespParty"  : 6,
                        "editorSource"      : 0,
                        "editorDigest"      : 1,
                        "rpIndName"         : 2,
                        "rpOrgName"         : 3,
                        "rpPosName"         : 4,
                        "rpCntInfo"         : 5,
                        "cntAddress"            : 0,
                        "delPoint"                  : 0,
                        "city"                      : 1,
                        "adminArea"                 : 2,
                        "postCode"                  : 3,
                        "eMailAdd"                  : 4,
                        "country"                   : 5,
                        "cntPhone"              : 1,
                        "voiceNum"                  : 0,
                        "faxNum"                    : 1,
                        "cntHours"              : 2,
                        "cntOnlineRes"          : 3,
                        "linkage"                   : 0,
                        "protocol"                  : 1,
                        "orName"                    : 2,
                        "orDesc"                    : 3,
                        "orFunct"                   : 4,
                        "OnFunctCd"                     : 0,
                        "editorSave"    : 6,
                        "displayName"   : 7,
                        "role"          : 8,
                        "RoleCd"            : 0,
                    "searchKeys"    : 1,
                    "keyword"           : 0,
                    "idPurp"        : 3,
                    "idAbs"         : 4,
                    "idCredit"      : 5,
                    "resConst"      : 6,
                    "Consts"            : 0,
                    "useLimit"              : 0,
                    "legalLimit"            : 1,
                    "securitryLimit"        : 2,
                    "envirDesc"     : 7,
                    "dataLang"      : 8,
                    "languageCode"      : 0,
                    "countryCode"       : 1,
                    "spatRpType"    : 9,
                    "SpatRepTypCd"      : 0,
                    "dataExt"       : 10,
                    "geoEle"            : 0,
                    "GeoBndBox"             : 0,
                    "exTypeCode"                : 0,
                    "westBL"                    : 1,
                    "eastBL"                    : 2,
                    "northBL"                   : 3,
                    "southBL"                   : 4,
                    "tpCat"         : 11,
                    "TopicCatCd"        : 0,
                    }

    dataIdInfo_dict = {"idCitation"   : 0,
                      "searchKeys"    : 1,
                      "idPurp"        : 2,
                      "idAbs"         : 3,
                      "idCredit"      : 4,
                      "resConst"      : 5,
                      "envirDesc"     : 6,
                      "dataLang"      : 7,
                      "spatRpType"    : 8,
                      "dataExt"       : 9,
                      "tpCat"         : 10,
                      }

    metadata_detail_dict = {}

    idCitation_dict = {"idCitation" : 0,
                            "resTitle"      : 1,
                            "resAltTitle"   : 2,
                            "collTitle"     : 3,
                            "presForm"      : 4,
                                "PresFormCd"  : 0,
                                "fgdcGeoform" : 1,
                            "date"          : 5,
                                "createDate"  : 0,
                                "pubDate"     : 1,
                                "revisedDate" : 2,
                            "citRespParty"  : 6,
                        }

    contact_dict = {"editorSource" : 0,
                    "editorDigest" : 1,
                    "rpIndName"    : 2,
                    "rpOrgName"    : 3,
                    "rpPosName"    : 4,
                    "rpCntInfo"    : 5,
                    "cntAddress"     : 0,
                    "delPoint"          : 0,
                    "city"              : 1,
                    "adminArea"         : 2,
                    "postCode"          : 3,
                    "eMailAdd"          : 4,
                    "country"           : 5,
                    "cntPhone"          : 1,
                    "voiceNum"              : 0,
                    "faxNum"                : 1,
                    "cntHours"              : 2,
                    "cntOnlineRes"          : 3,
                    "linkage"                   : 0,
                    "protocol"                  : 1,
                    "orName"                    : 2,
                    "orDesc"                    : 3,
                    "orFunct"                   : 4,
                    "OnFunctCd"                     : 0,
                    "editorSave"   : 6,
                    "displayName"  : 7,
                    "role"         : 8,
                        "RoleCd"     : 0,
                    }



    esri_root ={"CreaDate" : 0,
                "CreaTime" : 1,
                "ArcGISFormat" : 2,
                "ArcGISstyle" : 3,
                "SyncOnce" : 4,
                "DataProperties" : 5,
                    "itemProps" : 0,
                        "itemName" : 0,
                        "imsContentType" : 1,
                        "nativeExtBox" : 2,
                            "westBL" : 0,
                            "eastBL" : 1,
                            "southBL" : 2,
                            "northBL" : 3,
                            "exTypeCode" : 4,
                    "coordRef" : 1,
                        "type" : 0,
                        "geogcsn" : 2,
                        "csUnits" : 3,
                        "peXml" : 4,
                "SyncDate" : 6,
                "SyncTime" : 7,
                "ModDate" : 8,
                "ModTime" : 9,
                "scaleRange" : 10,
                "minScale" : 11,
                "maxScale" : 12,
                "ArcGISProfile" : 13,
                }

    #for key in esri_root:
    #    print(f"{key:<20} {esri_root[key]}")

    from lxml import etree

    xml = '''<citRespParty>
                <editorSource>extermal</editorSource>
                <editorDigest>9cc0fe80de5687cc4d79f50f3a254f2c3ceb08ce</editorDigest>
                <rpIndName>Nikki Wildart</rpIndName>
                <rpOrgName>Office of Protected Resources, National Marine Fisheries Service</rpOrgName>
                <rpPosName>Biologist</rpPosName>
                <rpCntInfo>
                    <cntAddress addressType="both">
                        <delPoint>1315 East West Highway</delPoint>
                        <city>Silver Spring</city>
                        <adminArea>MD</adminArea>
                        <postCode>20910-3282</postCode>
                        <eMailAdd>nikki.wildart@noaa.gov</eMailAdd>
                        <country>US</country>
                    </cntAddress>
                    <cntPhone>
                        <voiceNum tddtty="">(301) 427-8443</voiceNum>
                        <faxNum>(301) 427-8443</faxNum>
                    </cntPhone>
                    <cntHours>0700 - 1800 EST/EDT</cntHours>
                    <cntOnlineRes>
                        <linkage>https://www.fisheries.noaa.gov/about/office-protected-resources</linkage>
                        <protocol>REST Service</protocol>
                        <orName>Fisheries OPR</orName>
                        <orDesc>NOAA Fisheries Office of Science and Technology</orDesc>
                        <orFunct>
                            <OnFunctCd value="002"></OnFunctCd>
                        </orFunct>
                    </cntOnlineRes>
                </rpCntInfo>
                <editorSave>True</editorSave>
                <displayName>Nikki Wildart</displayName>
                <role>
                    <RoleCd value="002"></RoleCd>
                </role>
    </citRespParty>'''

    # Create an XML string
    citRespParty_root = etree.XML(xml)

    # Parse your XML document
    #tree = etree.fromstring(xml)
    # Find all 'item' elements and print their position
    #for index, item in enumerate(citRespParty_root.xpath(".//")):
    #    print(f"Found '{item.tag}' at position {index+1}: {item.text}")

    xml = '''<dqInfo>
                <dqScope xmlns="">
                    <scpLvl>
                        <ScopeCd value="005"></ScopeCd>
                    </scpLvl>
                    <scpLvlDesc xmlns="">
                        <datasetSet>Feature Class</datasetSet>
                    </scpLvlDesc>
                </dqScope>
                <report type="DQConcConsis" dimension="horizontal">
                    <measDesc>Based on a review from species' experts, we determined that all necessary features were included in the species' range file.</measDesc>
                </report>
                <report type="DQCompOm" dimension="horizontal">
                    <measDesc>Based on a review from species' experts, we determined that all necessary features were included in the species' range file.</measDesc>
                </report>
                <dataLineage>
                    <statement></statement>
                    <dataSource type="">
                        <srcDesc></srcDesc>
                        <srcCitatn>
                            <resTitle></resTitle>
                            <date>
                                <createDate></createDate>
                            </date>
                        </srcCitatn>
                    </dataSource>
                    <prcStep>
                        <stepDesc></stepDesc>
                        <stepProc>
                            <editorSource>extermal</editorSource>
                            <editorDigest></editorDigest>
                            <rpIndName></rpIndName>
                            <rpOrgName></rpOrgName>
                            <rpPosName></rpPosName>
                            <rpCntInfo>
                                <cntAddress addressType="both">
                                    <delPoint></delPoint>
                                    <city></city>
                                    <adminArea></adminArea>
                                    <postCode></postCode>
                                    <eMailAdd></eMailAdd>
                                    <country></country>
                                </cntAddress>
                                <cntPhone>
                                    <voiceNum tddtty=""></voiceNum>
                                    <faxNum></faxNum>
                                </cntPhone>
                                <cntHours></cntHours>
                                <cntOnlineRes>
                                    <linkage></linkage>
                                    <protocol>REST Service</protocol>
                                    <orName></orName>
                                    <orDesc></orDesc>
                                    <orFunct>
                                        <OnFunctCd value="002"></OnFunctCd>
                                    </orFunct>
                                </cntOnlineRes>
                            </rpCntInfo>
                            <editorSave>True</editorSave>
                            <displayName></displayName>
                            <role>
                                <RoleCd value="009"></RoleCd>
                            </role>
                        </stepProc>
                        <stepDateTm></stepDateTm>
                    </prcStep>
                </dataLineage>
            </dqInfo>
            '''

    <dqScope> 0
        <scpLvl> 0
            <ScopeCd> 0

        <scpLvlDesc> 1
            <datasetSet> 0

    <report> 1
        <measDesc> 0
    <report> 2
        <measDesc> 0

    <dataLineage> 3
        <statement>  0
        <dataSource> 1
            <srcDesc>   0
            <srcCitatn> 1
                <resTitle> 0
                <date> 1
                    <createDate> 0
        <prcStep>    2
            <stepDesc> 0
            <stepProc> 1
                <editorSource> 0
                <editorDigest> 1
                <rpIndName>    2
                <rpOrgName>    3
                <rpPosName>    4
                <rpCntInfo>    5
                    <cntAddress> 0
                        <delPoint>  0
                        <city>      1
                        <adminArea> 2
                        <postCode>  3
                        <eMailAdd>  4
                        <country>   5

                    <cntPhone>     1
                        <voiceNum>   0
                        <faxNum>     1

                    <cntHours>     2
                    <cntOnlineRes> 3
                        <linkage>  0
                        <protocol> 1
                        <orName>   2
                        <orDesc>   3
                        <orFunct>  4
                            <OnFunctCd>
                <editorSave>    6
                <displayName>   7
                <role>          8
                    <RoleCd>    0
            <stepDateTm>  2




    "dqScope" : 0,
        "scpLvl" : 0,
            "ScopeCd" : 0,
        "scpLvlDesc" : 1,
            "datasetSet" : 0,
    "report" : 1,
        "measDesc" : 0,
    "report" : 2,
        "measDesc" : 0,
    "dataLineage" : 3,
        "statement" : 0,
        "dataSource" : 1,
            "srcDesc" : 0,
            "srcCitatn" : 1,
                "resTitle" : 0,
                "date" : 1,
                    "createDate" : 0,
        "prcStep" : 2,
            "stepDesc" : 0,
            "stepProc" : 1,
            "stepDateTm" : 2,



if __name__ == '__main__':
    main()
