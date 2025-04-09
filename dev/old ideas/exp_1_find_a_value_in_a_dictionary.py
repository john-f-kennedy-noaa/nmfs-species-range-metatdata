#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john.f.kennedy
#
# Created:     24/01/2025
# Copyright:   (c) john.f.kennedy 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Python Built-in's modules are loaded first
import os, sys
import traceback, inspect

def main():
    try:
        # Imports
        from lxml import etree

        target_xml = '''<mdContact>
                          <editorSource>extermal</editorSource>
                          <editorDigest>7517deefd0d9d1960164ab982e5e8278568cfa8c</editorDigest>
                          <rpIndName>Jennifer Schultz</rpIndName>
                          <rpOrgName>NMFS Office Of Protected Resources</rpOrgName>
                          <rpPosName>Fisheries Biologist</rpPosName>
                          <rpCntInfo>
                            <cntAddress addressType="both">
                              <delPoint>1315 East West Highway</delPoint>
                              <city>Silver Spring</city>
                              <adminArea>MD</adminArea>
                              <postCode>20910-3282</postCode>
                              <eMailAdd>jennifer.schultz@noaa.gov</eMailAdd>
                              <country>US</country>
                            </cntAddress>
                            <cntPhone>
                              <voiceNum tddtty="">(301) 427-8400</voiceNum>
                              <faxNum>(301) 427-8400</faxNum>
                            </cntPhone>
                            <cntHours>0700 - 1800 EST/EDT</cntHours>
                            <cntOnlineRes>
                              <linkage>https://www.fisheries.noaa.gov/about/office-protected-resources</linkage>
                              <protocol>REST Service</protocol>
                              <orName>Fisheries OPR</orName>
                              <orDesc>NOAA Fisheries Office of Protected Resources</orDesc>
                              <orFunct>
                                <OnFunctCd value="002">value="002"</OnFunctCd>
                              </orFunct>
                            </cntOnlineRes>
                          </rpCntInfo>
                          <editorSave>True</editorSave>
                          <displayName>Jennifer Schultz</displayName>
                          <role>
                            <RoleCd value="005"/>
                          </role>
                        </mdContact>
                    '''

        contact_dict = {"Jeffrey A. Seminoff" : {"editorSource"                   : "extermal",
                                                 "editorDigest"                   : "",
                                                 "rpIndName"                      : "Jeffrey A. Seminoff",
                                                 "rpOrgName"                      : "UPDATE NEEDED",
                                                 "rpPosName"                      : "UPDATE NEEDED",
                                                 "rpCntInfo/cntAddress/delPoint"  : "8901 La Jolla Shores Drive",
                                                 "rpCntInfo/cntAddress/city"      : "La Jolla",
                                                 "rpCntInfo/cntAddress/adminArea" : "CA",
                                                 "rpCntInfo/cntAddress/postCode"  : "92037-1508",
                                                 "rpCntInfo/cntAddress/eMailAdd"  : "jeffrey.seminoff@noaa.gov",
                                                 "rpCntInfo/cntAddress/country"   : "US",
                                                 "rpCntInfo/cntPhone/voiceNum"    : "UPDATE NEEDED",
                                                 "rpCntInfo/cntPhone/faxNum"      : "UPDATE NEEDED",
                                                 "rpCntInfo/cntHours"             : "UPDATE NEEDED",
                                                 "rpCntInfo/cntOnlineRes/linkage"           : "https://UPDATE NEEDED",
                                                 "rpCntInfo/cntOnlineRes/protocol"          : "REST Service",
                                                 "rpCntInfo/cntOnlineRes/orName"            : "Fisheries",
                                                 "rpCntInfo/cntOnlineRes/orDesc"            : "NOAA Fisheries",
                                                 "rpCntInfo/cntOnlineRes/orFunct/OnFunctCd" : 'value="002"',
                                                 "displayName"                    : "Jeffrey A. Seminoff",
                                                 "editorSave"                     : "True",
                                                 #"role/RoleCd"                    : "",
                                                 },

            "Jennifer Schultz" : {"editorSource"                   : "extermal",
                                  "editorDigest"                   : "7517deefd0d9d1960164ab982e5e8278568cfa8c",
                                  "rpIndName"                      : "Jennifer Schultz",
                                  "rpOrgName"                      : "Office of Protected Resources, National Marine Fisheries Service",
                                  "rpPosName"                      : "Fisheries Biologist",
                                  "rpCntInfo/cntAddress/delPoint"  : "1315 East West Highway",
                                  "rpCntInfo/cntAddress/city"      : "Silver Spring",
                                  "rpCntInfo/cntAddress/adminArea" : "MD",
                                  "rpCntInfo/cntAddress/postCode"  : "20910-3282",
                                  "rpCntInfo/cntAddress/eMailAdd"  : "jennifer.schultz@noaa.gov",
                                  "rpCntInfo/cntAddress/country"   : "US",
                                  "rpCntInfo/cntPhone/voiceNum"    : "(301) 427-8400",
                                  "rpCntInfo/cntPhone/faxNum"      : "(301) 427-8400",
                                  "rpCntInfo/cntHours"             : "0700 - 1800 EST/EDT",
                                  "rpCntInfo/cntOnlineRes/linkage"           : "https://www.fisheries.noaa.gov/about/office-protected-resources",
                                  "rpCntInfo/cntOnlineRes/protocol"          : "REST Service",
                                  "rpCntInfo/cntOnlineRes/orName"            : "Fisheries OPR",
                                  "rpCntInfo/cntOnlineRes/orDesc"            : "NOAA Fisheries Office of Protected Resources",
                                  "rpCntInfo/cntOnlineRes/orFunct/OnFunctCd" : 'value="002"',
                                  "displayName"                    : "Jennifer Schultz",
                                  "editorSave"                     : "True",
                                  #"role/RoleCd"                    : "",
                                 },

            "Jonathan Molineaux" : {"editorSource"                   : "extermal",
                                    "editorDigest"                   : "12f8bd0167374224b1b5438e94e5c11e1f233005",
                                    "rpIndName"                      : "Jonathan Molineaux",
                                    "rpOrgName"                      : "Office of Protected Resources, National Marine Fisheries Service",
                                    "rpPosName"                      : "Fisheries Biologist",
                                    "rpCntInfo/cntAddress/delPoint"  : "1315 East West Highway",
                                    "rpCntInfo/cntAddress/city"      : "Silver Spring",
                                    "rpCntInfo/cntAddress/adminArea" : "MD",
                                    "rpCntInfo/cntAddress/postCode"  : "20910-3282",
                                    "rpCntInfo/cntAddress/eMailAdd"  : "jonathan.molineaux@noaa.gov",
                                    "rpCntInfo/cntAddress/country"   : "US",
                                    "rpCntInfo/cntPhone/voiceNum"    : "(301) 427-8400",
                                    "rpCntInfo/cntPhone/faxNum"      : "(301) 427-8400",
                                    "rpCntInfo/cntHours"             : "0700 - 1800 EST/EDT",
                                    "rpCntInfo/cntOnlineRes/linkage"           : "https://www.fisheries.noaa.gov/about/office-protected-resources",
                                    "rpCntInfo/cntOnlineRes/protocol"          : "REST Service",
                                    "rpCntInfo/cntOnlineRes/orName"            : "Fisheries OPR",
                                    "rpCntInfo/cntOnlineRes/orDesc"            : "NOAA Fisheries Office of Protected Resources",
                                    "rpCntInfo/cntOnlineRes/orFunct/OnFunctCd" : 'value="002"',
                                    "displayName"                    : "Jonathan Molineaux",
                                    "editorSave"                     : "True",
                                    #"role/RoleCd"                    : "",
                                   },

            "Marc Romano" : {"editorSource"                   : "extermal",
                             "editorDigest"                   : "",
                             "rpIndName"                      : "Marc Romano",
                             "rpOrgName"                      : "UPDATE NEEDED",
                             "rpPosName"                      : "UPDATE NEEDED",
                             "rpCntInfo/cntAddress/delPoint"  : "UPDATE NEEDED",
                             "rpCntInfo/cntAddress/city"      : "UPDATE NEEDED",
                             "rpCntInfo/cntAddress/adminArea" : "UPDATE NEEDED",
                             "rpCntInfo/cntAddress/postCode"  : "UPDATE NEEDED",
                             "rpCntInfo/cntAddress/eMailAdd"  : "marc.romano@noaa.gov",
                             "rpCntInfo/cntAddress/country"   : "US",
                             "rpCntInfo/cntPhone/voiceNum"    : "UPDATE NEEDED",
                             "rpCntInfo/cntPhone/faxNum"      : "UPDATE NEEDED",
                             "rpCntInfo/cntHours"             : "UPDATE NEEDED",
                             "rpCntInfo/cntOnlineRes/linkage"           : "UPDATE NEEDED",
                             "rpCntInfo/cntOnlineRes/protocol"          : "REST Service",
                             "rpCntInfo/cntOnlineRes/orName"            : "UPDATE NEEDED",
                             "rpCntInfo/cntOnlineRes/orDesc"            : "UPDATE NEEDED",
                             "rpCntInfo/cntOnlineRes/orFunct/OnFunctCd" : 'value="002"',
                             "displayName"                    : "Marc Romano",
                             "editorSave"                     : "True",
                             #"role/RoleCd"                    : "",
                            },

            "NMFS Office Of Protected Resources" : {"editorSource"                   : "extermal",
                               "editorDigest"                   : "",
                               "rpIndName"                      : "NMFS Office Of Protected Resources",
                               "rpOrgName"                      : "Department of Commerce (DOC), National Oceanic and Atmospheric Administration (NOAA), National Marine Fisheries Service (NMFS)",
                               "rpPosName"                      : "Biologist",
                               "rpCntInfo/cntAddress/delPoint"  : "1315 East West Highway",
                               "rpCntInfo/cntAddress/city"      : "Silver Spring",
                               "rpCntInfo/cntAddress/adminArea" : "MD",
                               "rpCntInfo/cntAddress/postCode"  : "20910-3282",
                               "rpCntInfo/cntAddress/eMailAdd"  : "nikki.wildart@noaa.gov",
                               "rpCntInfo/cntAddress/country"   : "US",
                               "rpCntInfo/cntPhone/voiceNum"    : "(301) 427-8443",
                               "rpCntInfo/cntPhone/faxNum"      : "(301) 427-8443",
                               "rpCntInfo/cntHours"             : "0700 - 1800 EST/EDT",
                               "rpCntInfo/cntOnlineRes/linkage"           : "https://www.fisheries.noaa.gov/about/office-protected-resources",
                               "rpCntInfo/cntOnlineRes/protocol"          : "REST Service",
                               "rpCntInfo/cntOnlineRes/orName"            : "Fisheries OPR",
                               "rpCntInfo/cntOnlineRes/orDesc"            : "NOAA Fisheries Office of Science and Technology",
                               "rpCntInfo/cntOnlineRes/orFunct/OnFunctCd" : 'value="002"',
                               "displayName"                    : "Department of Commerce (DOC), National Oceanic and Atmospheric Administration (NOAA), National Marine Fisheries Service (NMFS)",
                               "editorSave"                     : "True",
                               #"role/RoleCd"                    : "",
                              },

            "Nikki Wildart" : {"editorSource"                   : "extermal",
                               "editorDigest"                   : "7f5dd3d1346a40f0aee0e04601dff44733c88af1",
                               "rpIndName"                      : "Nikki Wildart",
                               "rpOrgName"                      : "Office of Protected Resources, National Marine Fisheries Service",
                               "rpPosName"                      : "Biologist",
                               "rpCntInfo/cntAddress/delPoint"  : "1315 East West Highway",
                               "rpCntInfo/cntAddress/city"      : "Silver Spring",
                               "rpCntInfo/cntAddress/adminArea" : "MD",
                               "rpCntInfo/cntAddress/postCode"  : "20910-3282",
                               "rpCntInfo/cntAddress/eMailAdd"  : "nikki.wildart@noaa.gov",
                               "rpCntInfo/cntAddress/country"   : "US",
                               "rpCntInfo/cntPhone/voiceNum"    : "(301) 427-8443",
                               "rpCntInfo/cntPhone/faxNum"      : "(301) 427-8443",
                               "rpCntInfo/cntHours"             : "0700 - 1800 EST/EDT",
                               "rpCntInfo/cntOnlineRes/linkage"           : "https://www.fisheries.noaa.gov/about/office-protected-resources",
                               "rpCntInfo/cntOnlineRes/protocol"          : "REST Service",
                               "rpCntInfo/cntOnlineRes/orName"            : "Fisheries OPR",
                               "rpCntInfo/cntOnlineRes/orDesc"            : "NOAA Fisheries Office of Science and Technology",
                               "rpCntInfo/cntOnlineRes/orFunct/OnFunctCd" : 'value="002"',
                               "displayName"                    : "Nikki Wildart",
                               "editorSave"                     : "True",
                               #"role/RoleCd"                    : "",
                              },

            "Shanna Dunn" : {"editorSource"                   : "extermal",
                             "editorDigest"                   : "",
                             "rpIndName"                      : "Shanna Dunn",
                             "rpOrgName"                      : "UPDATE NEEDED",
                             "rpPosName"                      : "UPDATE NEEDED",
                             "rpCntInfo/cntAddress/delPoint"  : "UPDATE NEEDED",
                             "rpCntInfo/cntAddress/city"      : "UPDATE NEEDED",
                             "rpCntInfo/cntAddress/adminArea" : "UPDATE NEEDED",
                             "rpCntInfo/cntAddress/postCode"  : "UPDATE NEEDED",
                             "rpCntInfo/cntAddress/eMailAdd"  : "shanna.dunn@noaa.gov",
                             "rpCntInfo/cntAddress/country"   : "US",
                             "rpCntInfo/cntPhone/voiceNum"    : "(555) 555-5555",
                             "rpCntInfo/cntPhone/faxNum"      : "(555) 555-5555",
                             "rpCntInfo/cntHours"             : "9-5",
                             "rpCntInfo/cntOnlineRes/linkage"           : "https://. . . ",
                             "rpCntInfo/cntOnlineRes/protocol"          : "REST Service",
                             "rpCntInfo/cntOnlineRes/orName"            : "UPDATE NEEDED",
                             "rpCntInfo/cntOnlineRes/orDesc"            : "UPDATE NEEDED",
                             "rpCntInfo/cntOnlineRes/orFunct/OnFunctCd" : 'value="002"',
                             "displayName"                    : "Shanna Dunn",
                             "editorSave"                     : "True",
                             #"role/RoleCd"                    : "",
                            },

            "Susan Wang" : {"editorSource"                   : "extermal",
                            "editorDigest"                   : "",
                            "rpIndName"                      : "Susan Wang",
                            "rpOrgName"                      : "Protected Resources Division, West Coast Region, National Marine Fisheries Service",
                            "rpPosName"                      : "Black Abalone Recovery Coordinator",
                            "rpCntInfo/cntAddress/delPoint"  : "501 West Ocean Boulevard, Suite 4200",
                            "rpCntInfo/cntAddress/city"      : "Long Beach",
                            "rpCntInfo/cntAddress/adminArea" : "CA",
                            "rpCntInfo/cntAddress/postCode"  : "90802",
                            "rpCntInfo/cntAddress/eMailAdd"  : "susan.wang@noaa.gov",
                            "rpCntInfo/cntAddress/country"   : "US",
                            "rpCntInfo/cntPhone/voiceNum"    : "(562) 980-4199",
                            "rpCntInfo/cntPhone/faxNum"      : "(562) 980-4199",
                            "rpCntInfo/cntHours"             : "0700 - 1800 PST/PDT",
                            "rpCntInfo/cntOnlineRes/linkage"           : "https://www.fisheries.noaa.gov/about/west-coast-region</linkage>",
                            "rpCntInfo/cntOnlineRes/protocol"          : "REST Service",
                            "rpCntInfo/cntOnlineRes/orName"            : "West Coast Region NOAA Fisheries",
                            "rpCntInfo/cntOnlineRes/orDesc"            : "About the West Coast Region of NOAA Fisheries",
                            "rpCntInfo/cntOnlineRes/orFunct/OnFunctCd" : 'value="002"',
                            "displayName"                    : "Susan Wang",
                            "editorSave"                     : "True",
                            #"role/RoleCd"                    : "",
                         },}

        Test_1 = False
        if Test_1:
            # Test 1
            select_element = "rpCntInfo/cntAddress/eMailAdd"
            select_text    = "susan.wang@noaa.gov"

            for contact in contact_dict:
                user_dict = contact_dict[contact]
                if select_text == user_dict[select_element]:
                    print(user_dict[select_element])
                del contact
                del user_dict

            del select_element, select_text
        del Test_1

        Test_2 = False
        if Test_2:
            # Test 2
            select_element = "eMailAdd"
            select_text    = "susan.wang@noaa.gov"

            for contact in contact_dict:
                user_dict = contact_dict[contact]
                select_element = [k for k in user_dict if select_element in k][0]
                if select_text == user_dict[select_element]:
                    print(user_dict[select_element])
                del contact

            del select_element, select_text
        del Test_2

        Test_3 = False
        if Test_3:
            # Test 3

            target_tree = etree.ElementTree(etree.fromstring(target_xml))
            #target_tree = etree.fromstring(target_xml_string)
            target_root = target_tree.getroot()
            #print(target_root.tag)

            select_elements = ["rpIndName", "eMailAdd", "rpOrgName",]
            select_element  = "rpOrgName"
            select_key      = ""

            found_elements = dict()
            for element in select_elements:
                found_element = target_root.find(f".//{element}")
                if not isinstance(found_element, type(None)) and found_element.text:
                    found_elements[found_element.tag] = found_element.text
                else:
                    pass
                del found_element
                del element

            #if found_elements:
            #    for found_element in found_elements:
            #        print(f"{found_element:<10}: '{found_elements[found_element]}'")
            #        del found_element
            #else:
            #    print("nothing found")

            user_dict = dict()
            if found_elements:
                for found_element in found_elements:
                    #print(f"{found_element:<10}: '{found_elements[found_element]}'")
                    for contact in contact_dict:
                        select_dict = contact_dict[contact]
                        se = [key for key in select_dict if (found_element in key or found_element == key) and select_dict[key] == found_elements[found_element]]
                        if se:
                            se = se[0]
                            print(f"{se:<41}: '{select_dict[se]}'")
                            user_dict = select_dict
                        del se
                        del select_dict
                        del contact
                    del found_element
            #if user_dict:
            #    print(user_dict)
            del user_dict

##                for contact in contact_dict:
##                    #print(f"Contact: {contact}")
##                    select_dict = contact_dict[contact]
##                    #print(select_dict)
##                    for found_element in found_elements:
##                        #print(f"{found_element:<10}: '{found_elements[found_element]}'")
##                        if found_element in select_dict:
##                            print(f"{found_element:<10}: '{found_elements[found_element]}'")
##                        del found_element
##                    #select_key = [k for k in select_dict if found_element in k]
##                    #if select_key: select_key = select_key[0]
##                    #print(select_key, select_dict[select_key])
##                    #if select_text == select_dict[select_element]:
##                    #    print(select_dict[select_element])
####                    for key in select_dict:
####                        if key in found_elements.keys() and select_dict[key] in found_elements.values():
####                            print(f"{key:<41}: '{select_dict[key]}'")
####                        del key
####                    for found_element in found_elements:
####                        print(f"{found_element:<10}: '{found_elements[found_element]}'")
####                        print(select_dict[found_element])
####
####                        del found_element
##
##
##                    del contact
##                    del select_dict

##            for contact in contact_dict:
##                print(f"Contact: {contact}")
##                select_dict = contact_dict[contact]
##                #print(select_dict)
##                select_key = [k for k in select_dict if select_element in k][0]
##                #if select_text == select_dict[select_element]:
##                #    print(select_dict[select_element])
##                del contact
##                del select_dict
            del found_elements
            del select_elements, select_element, select_key
            del target_tree, target_root
        del Test_3


        Test_4 = True
        if Test_4:
            # Test 4
            target_tree = etree.ElementTree(etree.fromstring(target_xml))
            #target_tree = etree.fromstring(target_xml_string)
            target_root = target_tree.getroot()
            #print(target_root.tag)

            select_elements = ["eMailAdd", "rpIndName", "rpOrgName",]
            select_element  = "rpOrgName"
            select_key      = ""

            #print(target_root.tag)
            #elements = target_tree.xpath(f".//parent::*[self::eMailAdd or self::rpIndName or self::rpOrgName]")
            elements = target_tree.xpath(f".//*[self::rpCntInfo/cntAddress/eMailAdd or self::rpIndName or self::rpOrgName]/ancestor::*")
            #elements = target_root.xpath(f".//eMailAdd | .//rpIndName | .//rpOrgName")
            #elements = target_root.xpath(f".//eMailAdd or .//rpIndName or .//rpOrgName")

            #elements = target_root.xpath("./*[parent::*[@tag='eMailAdd' or @tag='rpIndName' or @tag='rpOrgName']]")

            #print(elements)

            for element in elements:
                print(element.tag)
                del element
            del elements

            #if not isinstance(parent, type(None)):
            #    print(parent.tag)
            #else:
            #    print("didn't work")
            #del parent
##            found_elements = dict()
##            for element in select_elements:
##                found_element = target_root.find(f".//{element}")
##                if not isinstance(found_element, type(None)) and found_element.text:
##                    found_elements[found_element.tag] = found_element.text
##                else:
##                    pass
##                del found_element
##                del element

            #if found_elements:
            #    for found_element in found_elements:
            #        print(f"{found_element:<10}: '{found_elements[found_element]}'")
            #        del found_element
            #else:
            #    print("nothing found")

##            user_dict = dict()
##            if found_elements:
##                for found_element in found_elements:
##                    #print(f"{found_element:<10}: '{found_elements[found_element]}'")
##                    for contact in contact_dict:
##                        select_dict = contact_dict[contact]
##                        se = [key for key in select_dict if (found_element in key or found_element == key) and select_dict[key] == found_elements[found_element]]
##                        if se:
##                            se = se[0]
##                            print(f"{se:<41}: '{select_dict[se]}'")
##                            user_dict = select_dict
##                        del se
##                        del select_dict
##                        del contact
##                    del found_element
##            #if user_dict:
##            #    print(user_dict)
##            del user_dict

            #del found_elements
            del select_elements, select_element, select_key
            del target_tree, target_root
        del Test_4


        del contact_dict

        del target_xml

# Case #1
#     1) provide a tag for the select_element. Select one from: rpIndName,
#        rpOrgName, eMailAdd. All three will be used to search the XML for positives
#     2) search for select_elements in XML
#        i) if select_element tag is found and select_element text exists,
#           then return tag and text in a dictionary
#       ii) else: not sure, pass? break?
#     3)

        # Imports
        del etree

    except:
        traceback.print_exc()
    else:
        rk = [key for key in locals().keys() if not key.startswith('__') and key not in [""]]
        if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True

if __name__ == '__main__':
    main()

