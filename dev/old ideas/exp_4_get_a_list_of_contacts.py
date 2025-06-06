#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john.f.kennedy
#
# Created:     15/01/2025
# Copyright:   (c) john.f.kennedy 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Python Built-in's modules are loaded first
import os, sys
import traceback, inspect

# Third-party modules are loaded second
# import arcpy

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

def new_function():
    try:
        pass
    except:
        traceback.print_exc()
    else:
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        pass

def getSortValue(elem):
    from lxml import etree
    if isinstance(elem, etree._Comment):
        # sort comment by its content
        return elem.text
    else:
        # sort entities by tag and then by name
        #return elem.tag + elem.attrib.get('name','')
        return elem.tag

def remove_duplicate_elements(root):
    seen = {}
    for element in root.iter():
        key = (element.tag, element.text, tuple(element.attrib.items()))
        if key in seen:
            element.getparent().remove(element)
        else:
            seen[key] = True

def contact_search_report(target_tree, search_expression):
    try:
        if target_tree.xpath(search_expression):
            for elem in target_tree.xpath(search_expression):
                parent = elem.getparent()
                #remove_duplicate_elements(parent)
                print(f"\tParent: '{parent.tag}'")
                descendants = parent.iterdescendants()
                for descendant in descendants:
                    if descendant.text:
                        print(f"\t\t{descendant.getroottree().getpath(descendant)} : {descendant.text}")
                        #print(f"\t\t\t{child.tag} {child.text}")
##                    elif descendant.attrib:
##                        print(f"\t\tattrib: {descendant.getroottree().getpath(descendant)} : {descendant.attrib}")
##                    else:
##                        print(f"\t\tother: {descendant.getroottree().getpath(descendant)} : {descendant.tag}")
##                        #print(f"\t\t\t{child.tag} {child.attrib}")
                    del descendant
                del descendants
                del parent
                del elem
        else:
            print("something is wrong in not search_term")

        # Function parameters
        del target_tree, search_expression

    except:
        traceback.print_exc()
    else:
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: raise Warning(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        pass

def contact_search_dictionary_email(target_xml_name, target_tree, search_expression, search_element):
    try:
        # Imports
        from lxml import etree

        target_root = target_tree.getroot()

        print(f"\tProcessing: {target_xml_name}")

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

        if target_tree.xpath(search_expression):
            record_count = 0
            #print(f"File: '{target_xml_name}'")
            for elem in target_tree.xpath(search_expression):
                parent = elem.getparent()
                #remove_duplicate_elements(parent)
                print(f"\tRecord: '{record_count}' Parent: '{parent.tag}'")

                #target_tree_x_path = target_tree.getpath(parent)
                #print(target_tree_x_path); del target_tree_x_path

                #print(etree.tostring(parent, pretty_print=True).decode())

                select_element = parent.find(f".//{search_element}")
                #print(select_element.text)

                user_dict = dict()

                for contact in contact_dict:
                    select_dict = contact_dict[contact]
                    select_key = [k for k in select_dict if search_element in k][0]
                    if select_element.text == select_dict[select_key]:
                        #print(select_dict[select_key])
                        user_dict = contact_dict[contact]
                    del contact
                    del select_dict
                    del select_key

                del select_element

                children = parent.iterchildren()
                children_tags = []
                for child in children:
                    #print(child.tag, child.text)

                    contact_xml_string = etree.fromstring(f'<{parent.tag}><editorSource>external</editorSource><editorDigest/><rpIndName/><rpOrgName/><rpPosName/><rpCntInfo><cntAddress addressType="both"><delPoint/><city/><adminArea/><postCode/><eMailAdd/><country>US</country></cntAddress><cntPhone><voiceNum tddtty=""></voiceNum><faxNum/></cntPhone><cntHours/><cntOnlineRes><linkage/><protocol/><orName/><orDesc/><orFunct><OnFunctCd value="002"></OnFunctCd></orFunct></cntOnlineRes></rpCntInfo><editorSave/><displayName/><role><RoleCd value="005"></RoleCd></role></{parent.tag}>')
                    # create an ElementTree object from the metadata XML string
                    contact_tree = etree.ElementTree(contact_xml_string)
                    contact_root = contact_tree.getroot()
                    del contact_xml_string
                    #print(etree.tostring(contact_root, pretty_print=True).decode())

                    if child.text:
                        #print(f"\t\t{child.tag}: '{child.text}'")
                        contact_child = contact_root.find(f"./{child.tag}")
                        contact_child.text = child.text
                        del contact_child
                        if child.tag not in children_tags:
                            children_tags.append(child.tag)
                    else:
                        pass

                    #print(f"\t\t\t{children_tags}")
                    #print(etree.tostring(contact_root, pretty_print=True).decode())

                    #print(user_dict)
                    user_tags = [u for u in user_dict if u not in children_tags]
                    #print(f"\t\t\t{user_tags}")
                    for user_tag in user_tags:
                        #print(f"\t\t\t{user_tag}")
                        contact_child = contact_root.find(f"./{user_tag}")
                        contact_child.text = user_dict[user_tag]
                        del contact_child
                        del user_tag

                    del user_tags
                    del child

                del children_tags

                #print(contact_root.tag)
                #print(etree.tostring(contact_root, pretty_print=True).decode())

                #print(parent.tag, contact_root.tag)

                target_tree_x_path = target_tree.getpath(parent)
                #print(target_tree_x_path)
                #print(parent.xpath(target_tree_x_path)[0])

                contact_root_x_path = contact_tree.getpath(contact_root)
                #print(contact_tree.xpath(contact_root_x_path)[0])

                parent.getparent().replace(parent.xpath(target_tree_x_path)[0], contact_tree.xpath(contact_root_x_path)[0])

                del contact_root, contact_tree
                del target_tree_x_path, contact_root_x_path

                del children
                del user_dict

                # Declared Variables
                del parent
                del elem

                record_count+=1
            del record_count
        else:
            print("something is wrong in not search_term")

        del contact_dict
        del target_root

        # Imports
        del etree
        # Function parameters
        del target_xml_name, search_expression, search_element

    except Warning as w:
        print(w)
    except:
        traceback.print_exc()
    else:
        rk = [key for key in locals().keys() if not key.startswith('__') and key not in ["target_tree"]]
        if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return target_tree
    finally:
        if "target_tree" in locals().keys(): del target_tree

def contact_search_dictionary_name(target_xml_name, target_tree, search_expression, search_element):
    try:
        # Imports
        from lxml import etree

        target_root = target_tree.getroot()

        print(f"\tProcessing: {target_xml_name}")

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

        if target_tree.xpath(search_expression):
            record_count = 0
            #print(f"File: '{target_xml_name}'")
            for elem in target_tree.xpath(search_expression):
                parent = elem.getparent()
                #remove_duplicate_elements(parent)
                print(f"\tRecord: '{record_count}' Parent: '{parent.tag}'")

                #target_tree_x_path = target_tree.getpath(parent)
                #print(target_tree_x_path)

                rpIndNames = parent.findall("./rpIndName")
                for rpIndName in rpIndNames:

                    contact_xml_string = etree.fromstring(f'<{parent.tag}><editorSource>external</editorSource><editorDigest/><rpIndName/><rpOrgName/><rpPosName/><rpCntInfo><cntAddress addressType="both"><delPoint/><city/><adminArea/><postCode/><eMailAdd/><country>US</country></cntAddress><cntPhone><voiceNum tddtty=""></voiceNum><faxNum/></cntPhone><cntHours/><cntOnlineRes><linkage/><protocol/><orName/><orDesc/><orFunct><OnFunctCd value="002"></OnFunctCd></orFunct></cntOnlineRes></rpCntInfo><editorSave/><displayName/><role><RoleCd value="005"></RoleCd></role></{parent.tag}>')
                    # create an ElementTree object from the metadata XML string
                    contact_tree = etree.ElementTree(contact_xml_string)
                    contact_root = contact_tree.getroot()
                    del contact_xml_string
                    #print(etree.tostring(contact_root, pretty_print=True).decode())

                    #tag_text_dict[target_xml_name][record_count] = {rpIndName : {}}
                    print(f"\t\tName: '{rpIndName.text}'")
                    siblings = rpIndName.itersiblings()
                    sibling_tags = []
                    for sibling in siblings:
                        print(f"\t\t{sibling.tag}: '{sibling.text}'")
                        contact_sibling = contact_root.find(f"./{sibling.tag}")
                        contact_sibling.text = sibling.text
                        #print(contact_sibling.tag, contact_sibling.text)
                        del contact_sibling
                        sibling_tags.append(sibling.tag)
                        del sibling
                    del siblings

                    #print(f"\t\t\t{sibling_tags}")

                    user_dict = contact_dict[rpIndName.text]

                    user_tags = [u for u in user_dict if u not in sibling_tags]
                    #print(f"\t\t\t{user_tags}")
                    for user_tag in user_tags:
                        #print(f"\t\t\t{user_tag}")
                        contact_sibling = contact_root.find(f"./{user_tag}")
                        contact_sibling.text = user_dict[user_tag]
                        del contact_sibling
                        del user_tag

                    del user_tags, sibling_tags

                    #print(contact_root.tag)
                    #print(etree.tostring(contact_root, pretty_print=True).decode())

                    #print(parent.tag, contact_root.tag)

                    target_tree_x_path = target_tree.getpath(parent)
                    #print(target_tree_x_path)
                    #print(parent.xpath(target_tree_x_path)[0])

                    contact_root_x_path = contact_tree.getpath(contact_root)
                    #print(contact_tree.xpath(contact_root_x_path)[0])

                    parent.getparent().replace(parent.xpath(target_tree_x_path)[0], contact_tree.xpath(contact_root_x_path)[0])

                    del contact_root, contact_tree
                    del target_tree_x_path, contact_root_x_path

                    del user_dict
                    del rpIndName

                # Declared Variables
                del rpIndNames
                del parent
                del elem

                record_count+=1
            del record_count
        else:
            print("something is wrong in not search_term")

        del contact_dict
        del target_root

        # Imports
        del etree
        # Function parameters
        del target_xml_name, search_expression, search_element

    except Warning as w:
        print(w)
    except:
        traceback.print_exc()
    else:
        rk = [key for key in locals().keys() if not key.startswith('__') and key not in ["target_tree"]]
        if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return target_tree
    finally:
        if "target_tree" in locals().keys(): del target_tree

def contact_search_dictionary(target_xml_name, target_tree, search_expression, search_element):
    try:
        # Imports
        from lxml import etree

        target_root = target_tree.getroot()

        print(f"\tProcessing: {target_xml_name}")

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

            "NMFS Office Of Protected Resources" : {"editorSource" : "extermal",
                               "editorDigest"                   : "",
                               "rpIndName"                      : "NMFS Office Of Protected Resources",
                               "rpOrgName"                      : "NOAA Fisheries Office of Protected Resources",
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

            "NOAA Fisheries Office of Protected Resources" : {"editorSource" : "extermal",
                               "editorDigest"                   : "",
                               "rpIndName"                      : "NMFS Office Of Protected Resources",
                               "rpOrgName"                      : "NOAA Fisheries Office of Protected Resources",
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

            "Department of Commerce (DOC), National Oceanic and Atmospheric Administration (NOAA), National Marine Fisheries Service (NMFS)" : {"editorSource" : "extermal",
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
        #the_missing = list()

        elements = target_tree.xpath(f"//rpIndName/.. | //rpOrgName/..")
        for element in elements:
            print(element.tag)
            del element
        print(len(elements))
        del elements


##                target_tree_x_path = target_tree.getpath(parent)
##                #print(target_tree_x_path); del target_tree_x_path
##
##                #print(etree.tostring(parent, pretty_print=True).decode())
##
##                select_element = parent.find(f".//{search_element}")
##                #print(select_element.text)
##
##                user_dict = dict()
##
##                for contact in contact_dict:
##                    select_dict = contact_dict[contact]
##                    select_key = [k for k in select_dict if search_element in k][0]
##                    #print(f"select_element: {select_element.tag} {select_element.text}")
##                    #print(f"select_dict: {select_dict[select_key]}")
##                    if select_element.text == select_dict[select_key]:
##                        user_dict = contact_dict[contact]
##                    else:
##                        the_missing.append(select_element.text)
##                    del contact
##                    del select_dict
##                    del select_key
##                del select_element

                #print(user_dict)

##                contact_xml_string = etree.fromstring(f'<{parent.tag}><editorSource>external</editorSource><editorDigest/><rpIndName/><rpOrgName/><rpPosName/><rpCntInfo><cntAddress addressType="both"><delPoint/><city/><adminArea/><postCode/><eMailAdd/><country>US</country></cntAddress><cntPhone><voiceNum tddtty=""></voiceNum><faxNum/></cntPhone><cntHours/><cntOnlineRes><linkage/><protocol/><orName/><orDesc/><orFunct><OnFunctCd value="002"></OnFunctCd></orFunct></cntOnlineRes></rpCntInfo><editorSave/><displayName/><role><RoleCd value="005"></RoleCd></role></{parent.tag}>')
##                # create an ElementTree object from the metadata XML string
##                contact_tree = etree.ElementTree(contact_xml_string)
##                contact_root = contact_tree.getroot()
##                del contact_xml_string
##                #print(etree.tostring(contact_root, pretty_print=True).decode())

##                children = parent.iterchildren()
##                children_tags = []
##                for child in children:
##                    #print(child.tag, child.text)
##                    if child.text:
##                        #print(f"\t\t{child.tag}: '{child.text}'")
##                        contact_child = contact_root.find(f".//{child.tag}")
##                        contact_child.text = child.text
##                        #print(f"\t\t{contact_child.tag}: '{contact_child.text}'")
##                        del contact_child
##                        children_tags.append(child.tag)
##                    else:
##                        pass
##                    #print(f"\t\t\t{children_tags}")
##                    del child
##                del children

##                #print(user_dict)
##                user_tags = [u for u in user_dict if u not in children_tags]
##                print(f"\t\t\t{user_tags}")
##                for user_tag in user_tags:
##                    #print(f"\t\t\t{user_tag} {user_dict[user_tag]}")
##                    contact_child = contact_root.find(f".//{user_tag}")
##                    print(f"\t\t\t{contact_child.tag} {contact_child.text}")
##                    #contact_child.text = user_dict[user_tag]
##                    #del contact_child
##                    del user_tag
##                del user_tags
##
##                del children_tags

##                del user_dict

                #print(contact_root.tag)
                #print(etree.tostring(contact_root, pretty_print=True).decode())

                #print(parent.tag, contact_root.tag)

##                target_tree_x_path = target_tree.getpath(parent)
##                #print(target_tree_x_path)
##                #print(parent.xpath(target_tree_x_path)[0])
##
##                contact_root_x_path = contact_tree.getpath(contact_root)
##                #print(contact_tree.xpath(contact_root_x_path)[0])
##
##                #parent.getparent().replace(parent.xpath(target_tree_x_path)[0], contact_tree.xpath(contact_root_x_path)[0])
##
##                del contact_root, contact_tree
##                del target_tree_x_path, contact_root_x_path

##                # Declared Variables
##                del parent
##                del elem
##
##                record_count+=1
##            del record_count
##
##            if the_missing: print(list(set(the_missing)));
##            del the_missing
##
##        else:
##            print("something is wrong in not search_term")

        del contact_dict
        del target_root

        # Imports
        del etree
        # Function parameters
        del target_xml_name, search_expression, search_element

    except Warning as w:
        print(w)
    except:
        traceback.print_exc()
    else:
        rk = [key for key in locals().keys() if not key.startswith('__') and key not in ["target_tree"]]
        if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return target_tree
    finally:
        if "target_tree" in locals().keys(): del target_tree

def contact_search(target_xml, search_element="", search_term=""):
    try:
        # Imports
        from lxml import etree
        from src.project_tools import pretty_format_xml_file

        target_xml_name = os.path.basename(target_xml)
        print(f"Target Metadata: {target_xml_name}", flush=True)
        #del target_xml_name

        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
        # Parse the XML
        target_tree = etree.parse(target_xml, parser=parser)
        target_root = target_tree.getroot()
        del parser
        #etree.indent(tree, space="    ")
        # Pretty print
        #target_xml_string = etree.tostring(target_tree, pretty_print=True, method='html', encoding='UTF-8').decode()
        #print(target_xml_string,flush=True); del target_xml_string
        #foos = tree.xpath('.//ancestor::foo[bar[@attr="val"] and position() = 1]')
        #foos = tree.xpath('.//ancestor::foo[bar[@attr="val"]][1]')
        #for foo in foos:
        #    print(foo.attrib)

        #print(search_element)

        #if search_element in ["extermal", "editorDigest", "rpIndName", "rpOrgName", "rpPosName", "rpCntInfo", "displayName", "editorSave"]:
        if search_element in ["rpIndName", "rpOrgName"]:
            if not search_term:
                search_expression = f".//{search_element}"
            elif search_term:
                #search_expression = f".//{search_element}[text()='{search_term}']"
                search_expression = f".//{search_element}[contains(.,'{search_term}')]"
            else:
                print(f"something is wrong in '{search_element}'")

            #target_tree = contact_search_dictionary_name(target_xml_name, target_tree, search_expression, search_element)
            #target_tree = contact_search_dictionary_email(target_xml_name, target_tree, search_expression, search_element)
            target_tree = contact_search_dictionary(target_xml_name, target_tree, search_expression, search_element)

            etree.indent(target_root, space='    ')
            #etree.dump(target_root)
            target_xml_string = etree.tostring(target_tree, pretty_print=True, method='html', encoding='UTF-8').decode()
            #print(target_xml_string)

            try:
                with open(target_xml, "w") as f:
                    f.write(target_xml_string)
                del f
            except:
                print(f"The metadata file: {os.path.basename(xml)} can not be overwritten!!")

            del target_xml_string

        #elif search_element in ["delPoint", "city", "adminArea", "postCode", "eMailAdd", "country", "voiceNum", "faxNum", "cntHours", "linkage", "protocol", "orName", "orDesc", "OnFunctCd", "RoleCd"]:
        elif search_element in ["eMailAdd"]:
            if not search_term:
                search_expression = f".//rpCntInfo"
            elif search_term:
                #search_expression = f".//rpCntInfo[text()='{search_term}']"
                search_expression = f".//rpCntInfo[contains(.,'{search_term}')]"

            target_tree = contact_search_dictionary_email(target_xml_name, target_tree, search_expression, search_element)
            #target_tree = contact_search_dictionary(target_xml_name, target_tree, search_expression, search_element)

            etree.indent(target_root, space='    ')
            #etree.dump(target_root)
            target_xml_string = etree.tostring(target_tree, pretty_print=True, method='html', encoding='UTF-8').decode()
            #print(target_xml_string)

            try:
                with open(target_xml, "w") as f:
                    f.write(target_xml_string)
                del f
            except:
                print(f"The metadata file: {os.path.basename(xml)} can not be overwritten!!")

            del target_xml_string


        else:
            pass
            #print(f"something is wrong in '{search_element}'")

        if "parent" in locals().keys(): del parent

        ContactSearchReport = False
        if ContactSearchReport:
            contact_search_report(target_tree, search_expression)
        del ContactSearchReport

##        ContactSearchDictionary = False
##        if ContactSearchDictionary:
##            contract_dict = dict()
##            try:
##                #tag_text_dict = contact_search_dictionary(target_xml_name, target_tree, search_expression)
##                #contract_dict[target_xml_name] = tag_text_dict[target_xml_name]
##                #del tag_text_dict
##
##                #target_tree = contact_search_dictionary_name(target_xml_name, target_tree, search_expression)
##                target_tree = contact_search_dictionary_email(target_xml_name, target_tree, search_expression)
##
##                Reorder = False
##                if Reorder:
##                    # Reorder elements
##                    for parent in target_tree.xpath('//*[./*]'): # Search for parent elements
##                        parent[:] = sorted(parent, key=lambda x: getSortValue(x))
##                        del parent
##                del Reorder
##
##                etree.indent(target_root, space='    ')
##                #etree.dump(root)
##                target_xml_string = etree.tostring(target_tree, pretty_print=True, method='html', encoding='UTF-8').decode()
##                #print(target_xml_string)
##
##                try:
##                    with open(target_xml, "w") as f:
##                        f.write(target_xml_string)
##                    del f
##                except:
##                    print(f"The metadata file: {os.path.basename(xml)} can not be overwritten!!")
##
##                del target_xml_string
##
##                #pretty_format_xml_file(target_xml)
##
##            except:
##                raise Exception

##            ContractDictReport = False
##            if ContractDictReport:
##                for xml_name in contract_dict:
##                    print(f"\tFile Name: {xml_name}")
##                    #print(xml_name, contract_dict[xml_name])
##                    # tag_text_dict[target_xml_name][record_count][rpIndName][child.tag]
##                    for record_count in contract_dict[xml_name]:
##                        print(f"\t\tRecord Number: {record_count}")
##                        for user in contract_dict[xml_name][record_count]:
##                            print(f"\t\t\tContact: {user}")
##                            elems = contract_dict[xml_name][record_count][user]
##                            for elem in elems:
##                                print(f"\t\t\t\t{elem} : {elems[elem]}")
##                                del elem
##                            del elems
##                            del user
##                        del record_count
##                    del xml_name
##            del ContractDictReport
##
##            del contract_dict
##        del ContactSearchDictionary

        del search_expression

        # Declared Variables
        #del elements
        del target_tree, target_root
        del target_xml_name
        # Imports
        del etree, pretty_format_xml_file
        # Function parameters
        del target_xml, search_element, search_term

    except Warning as w:
        print(w)
    except:
        traceback.print_exc()
    else:
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__')]
        #if rk: raise Warning(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        pass

def main(project_folder=""):
    try:
        # Imports
        from time import gmtime, localtime, strftime, time
        # Set a start time so that we can see how log things take
        start_time = time()
        print(f"{'-' * 80}", flush=True)
        print(f"Python Script:  {os.path.basename(__file__)}", flush=True)
        print(f"Location:       {os.path.dirname(__file__)}", flush=True)
        print(f"Python Version: {sys.version} Environment: {os.path.basename(sys.exec_prefix)}", flush=True)
        print(f"{'-' * 80}\n")

        # Imports
        from src.project_tools import pretty_format_xml_file

        #target_xml = rf'{project_folder}\Export\WhaleBlue_20201014.xml'
        #target_xmls = [rf"{project_folder}\Export\AbaloneBlack_20210712.xml"]

        target_xmls = [rf"{project_folder}\Export\{f}" for f in os.listdir(rf"{project_folder}\Export") if f.endswith(".xml")]

        # get and save item metadata
        for target_xml in target_xmls:

            # Contact Search Tests
            # Test 1
            contact_search(target_xml, search_element="rpIndName", search_term="")
            # Test 2
            #contact_search(target_xml, search_element="rpIndName", search_term="Jennifer Schultz")
            # Test 3
            #contact_search(target_xml, search_element="rpIndName", search_term="Jennifer")
            # Test 4
            #contact_search(target_xml, search_element="eMailAdd", search_term="")
            # Test 5
            #contact_search(target_xml, search_element="eMailAdd", search_term="jennifer.schultz@noaa.gov")
            # Test 6
            #contact_search(target_xml, search_element="eMailAdd", search_term="jennifer")
            # Test 7
            #contact_search(target_xml, search_element="rpOrgName", search_term="")


            # Pretty Format
            #pretty_format_xml_file(target_xml)

            del target_xml

        # Declared Variables
        del project_folder, target_xmls

        # Imports
        del pretty_format_xml_file

        # Elapsed time
        end_time = time()
        elapse_time =  end_time - start_time
        print(flush=True)
        print(f"\n{'-' * 80}", flush=True)
        print(f"Python script: {os.path.basename(__file__)} successfully completed {strftime('%a %b %d %I:%M %p', localtime())}", flush=True)
        print(u"Elapsed Time {0} (H:M:S)".format(strftime("%H:%M:%S", gmtime(elapse_time))), flush=True)
        print(f"{'-' * 80}", flush=True)
        del elapse_time, end_time, start_time
        del gmtime, localtime, strftime, time

    except Warning as w:
        print(w)
    except:
        traceback.print_exc()
    else:
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: raise Warning(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        pass
        # Cleanup
        # arcpy.management.ClearWorkspaceCache()

if __name__ == '__main__':
    try:
        main(project_folder=rf"{os.path.dirname(os.path.dirname(__file__))}")
    except Warning as w:
        print(w)