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
import os, sys
import inspect, traceback

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

def main():
    try:
        from lxml import etree
        from src.project_tools import pretty_format_xml_file

        target_xml      = r"species_range_boilerplate.xml"
        target_xml_name = os.path.basename(target_xml)

        #parser = etree.XMLParser(remove_blank_text=True)
        # Parse the XML
        #tree = etree.parse("species_range_boilerplate.xml", parser=parser)
        # Pretty print
        #xml_string = etree.tostring(tree, pretty_print=True, encoding="utf-8").decode()
        #print(xml_string)

        parser = etree.XMLParser(remove_blank_text=True)
        target_tree = etree.parse(target_xml, parser=parser)
        target_root = target_tree.getroot()
        del parser
        # print(etree.tostring(tree.getroot(), pretty_print=True).decode(), end='')

        UpdateRpCntInfos = False
        if UpdateRpCntInfos:
            cntOnlineRess = target_root.findall(".//rpCntInfo/cntOnlineRes")
            for cntOnlineRes in cntOnlineRess:
                #print(etree.tostring(cntOnlineRes, pretty_print=True).decode(), end='')
                #print(etree.tostring(cntOnlineRes, pretty_print=False).decode(), end='')

                children = [c for c in cntOnlineRes.getchildren()]
                if children:
                    # <protocol>REST Service</protocol>
                    print(f"Before {cntOnlineRes.tag}")
                    for child in children:
                        print(f"\t{child.tag:<8} = {child.text}")
                        #print(f"\t{child}")
                    del child
                    if children[1].tag != "protocol":
                        cntOnlineRes.insert(1, etree.SubElement(cntOnlineRes, "protocol"))
                        protocol = cntOnlineRes.find("./protocol")
                        protocol.text = "REST Service"
                    if children[1].tag == "protocol" and children[1].text is not None:
                        protocol = cntOnlineRes.find("./protocol")
                        protocol.text = "REST Service"

                    #for child in children:
                    #    print(f"\t{child.tag}")
                    #    #print(f"\t{child}")
                del children

                children = [c for c in cntOnlineRes.getchildren()]
                if children:
                    print(f"After {cntOnlineRes.tag}")
                    for child in children:
                        print(f"\t{child.tag:<8} = {child.text}")
                        if child.tag == "protocol":
                            protocol = cntOnlineRes.find("./protocol")
                            ancestors = []
                            for ancestor in protocol.iterancestors():
                                #iterancestors(self, tag=None, *tags)
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
                del cntOnlineRes
            del cntOnlineRess
        del UpdateRpCntInfos

        UpdateRpCntInfos = False
        if UpdateRpCntInfos:
            contact_dict  = dict()
            contact_count = 0
            cntAddresss = target_root.findall(".//rpCntInfo/cntAddress")
            for cntAddress in cntAddresss:
                contact_count+=1
                contact_dict[contact_count] = {target_xml_name : {}}

                cntAddress.set("addressType", "both")

                # Get the parent element
                cntAddressParent = cntAddress.getparent()
                rpCntInfoParent = cntAddressParent.getparent()
                rpIndName = rpCntInfoParent.find("./rpIndName").text
                del cntAddressParent, rpCntInfoParent

                children = [c for c in cntAddress.getchildren()]

                cntAddress_children   = ('delPoint', 'city', 'adminArea', 'postCode', 'eMailAdd', 'country',)
                cntAddress_children_dict = {child : cntAddress_children.index(child) for child in cntAddress_children}
                #print(cntAddress_children_dict)
                del cntAddress_children

                new_cntAddress_children_dict = {child : cntAddress_children_dict[child]
                                                for child in cntAddress_children_dict
                                                if child not in [c.tag for c in cntAddress.getchildren()]}

                if new_cntAddress_children_dict:
                    for new_cntAddress_child in new_cntAddress_children_dict:
                        #print(new_cntAddress_child, new_cntAddress_children_dict[new_cntAddress_child])
                        cntAddress.insert(new_cntAddress_children_dict[new_cntAddress_child], etree.SubElement(cntAddress, f"{new_cntAddress_child}"))
                        new_cntAddress_child_elem = cntAddress.find(f"./{new_cntAddress_child}")
                        if new_cntAddress_child_elem.tag == "country":
                            new_cntAddress_child_elem.text = "US"
                        else:
                            new_cntAddress_child_elem.text = "UPDATE NEEDED"
                        del new_cntAddress_child_elem
                        del new_cntAddress_child

                del new_cntAddress_children_dict, cntAddress_children_dict
                del children

                children = [c for c in cntAddress.getchildren()]
                if children:
                    #print(f"After {cntAddress.tag}")
                    for child in children:
                        if rpIndName not in contact_dict[contact_count][os.path.basename(target_xml)]:
                            contact_dict[contact_count][os.path.basename(target_xml)] = {rpIndName : {}}
                        #    contact_dict[contact_count][os.path.basename(target_xml)][rpIndName][child.tag] = child.text
                        #    #print(f"\t{child.tag:<9} = {child.text}")
                        contact_dict[contact_count][os.path.basename(target_xml)][rpIndName][child.tag] = child.text
                        del child
                del children

                del rpIndName
                del cntAddress

            for count in contact_dict:
                for _target_xml in contact_dict[count]:
                    print(_target_xml)
                    for contact in contact_dict[count][_target_xml]:
                        print(f"\t{contact:<10}")
                        for address_part in contact_dict[count][_target_xml][contact]:
                            print(f"\t\t{address_part:<10}:  {contact_dict[count][_target_xml][contact][address_part]}")
                            del address_part
                        del contact
                    del _target_xml
                del count

            del cntAddresss, contact_dict, contact_count
        del UpdateRpCntInfos

        UpdateRpCntInfos = False
        if UpdateRpCntInfos:

            def remove_duplicate_elements(root):
                seen = {}
                for element in root.iter():
                    key = (element.tag, element.text, tuple(element.attrib.items()))
                    if key in seen:
                        element.getparent().remove(element)
                    else:
                        seen[key] = True
                    del key, element
                del seen, root

##        <RoleCd value="001"></RoleCd> -->> Resource Provider
##        <RoleCd value="002"></RoleCd> -->> Custodian
##        <RoleCd value="003"></RoleCd> -->> Owner
##        <RoleCd value="004"></RoleCd> -->> User
##        <RoleCd value="005"></RoleCd> -->> Distributor
##        <RoleCd value="006"></RoleCd> -->> Originator
##        <RoleCd value="007"></RoleCd> -->> Point of Contact
##        <RoleCd value="008"></RoleCd> -->> Principal Investigator
##        <RoleCd value="009"></RoleCd> -->> Processor
##        <RoleCd value="010"></RoleCd> -->> Publisher
##        <RoleCd value="011"></RoleCd> -->> Author
##        <RoleCd value="012"></RoleCd> -->> Collaborator
##        <RoleCd value="013"></RoleCd> -->> Editor
##        <RoleCd value="014"></RoleCd> -->> Mediator
##        <RoleCd value="015"></RoleCd> -->> Rights Holder

            contact_dict = {"Jeffrey A. Seminoff" : {"editorSource"                   : "",
                                                     "editorDigest"                   : "",
                                                     "rpIndName"                      : "Jeffrey A. Seminoff",
                                                     "rpOrgName"                      : "",
                                                     "rpPosName"                      : "",
                                                     "rpCntInfo/cntAddress/delPoint"  : "8901 La Jolla Shores Drive",
                                                     "rpCntInfo/cntAddress/city"      : "La Jolla",
                                                     "rpCntInfo/cntAddress/adminArea" : "CA",
                                                     "rpCntInfo/cntAddress/postCode"  : "92037-1508",
                                                     "rpCntInfo/cntAddress/eMailAdd"  : "jeffrey.seminoff@noaa.gov",
                                                     "rpCntInfo/cntAddress/country"   : "US",
                                                     "rpCntInfo/cntPhone/voiceNum"    : "",
                                                     "rpCntInfo/cntPhone/faxNum"      : "",
                                                     "rpCntInfo/cntHours"             : "",
                                                     "rpCntInfo/cntOnlineRes/linkage"           : "https://",
                                                     "rpCntInfo/cntOnlineRes/protocol"          : "REST Service",
                                                     "rpCntInfo/cntOnlineRes/orName"            : "Fisheries",
                                                     "rpCntInfo/cntOnlineRes/orDesc"            : "NOAA Fisheries",
                                                     "rpCntInfo/cntOnlineRes/orFunct/OnFunctCd" : 'value="002"',
                                                     "displayName"                    : "Jeffrey A. Seminoff",
                                                     "editorSave"                     : "True",
                                                     },

                "Jennifer Schultz" : {"editorSource"                   : "",
                                      "editorDigest"                   : "",
                                      "rpIndName"                      : "Jennifer Schultz",
                                      "rpOrgName"                      : "Office of Protected Resources, National Marine Fisheries Service",
                                      "rpPosName"                      : "Fisheries Biologist",
                                      "rpCntInfo/cntAddress/delPoint"  : "1315 East West Highway",
                                      "rpCntInfo/cntAddress/city"      : "Silver Spring",
                                      "rpCntInfo/cntAddress/country"   : "MD",
                                      "rpCntInfo/cntAddress/postCode"  : "",
                                      "rpCntInfo/cntAddress/eMailAdd"  : "jennifer.schultz@noaa.gov",
                                      "rpCntInfo/cntAddress/country"   : "US",
                                      "rpCntInfo/cntPhone/voiceNum"    : "",
                                      "rpCntInfo/cntPhone/faxNum"      : "",
                                      "rpCntInfo/cntHours"             : "0700 - 1800 EST/EDT",
                                      "rpCntInfo/cntOnlineRes/linkage"           : "https://www.fisheries.noaa.gov/about/office-protected-resources",
                                      "rpCntInfo/cntOnlineRes/protocol"          : "REST Service",
                                      "rpCntInfo/cntOnlineRes/orName"            : "Fisheries OPR",
                                      "rpCntInfo/cntOnlineRes/orDesc"            : "NOAA Fisheries Office of Protected Resources",
                                      "rpCntInfo/cntOnlineRes/orFunct/OnFunctCd" : 'value="002"',
                                      "displayName"                    : "Jennifer Schultz",
                                      "editorSave"                     : "True",
                                     },

                "Jonathan Molineaux" : {"editorSource"                   : "",
                                        "editorDigest"                   : "",
                                        "rpIndName"                      : "Jonathan Molineaux",
                                        "rpOrgName"                      : "Office of Protected Resources, National Marine Fisheries Service",
                                        "rpPosName"                      : "Fisheries Biologist",
                                        "rpCntInfo/cntAddress/delPoint"  : "1315 East West Highway",
                                        "rpCntInfo/cntAddress/city"      : "Silver Spring",
                                        "rpCntInfo/cntAddress/country"   : "MD",
                                        "rpCntInfo/cntAddress/postCode"  : "",
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
                                       },

                "Marc Romano" : {"editorSource"                   : "",
                                 "editorDigest"                   : "",
                                 "rpIndName"                      : "Marc Romano",
                                 "rpOrgName"                      : "",
                                 "rpPosName"                      : "",
                                 "rpCntInfo/cntAddress/delPoint"  : "UPDATE NEEDED",
                                 "rpCntInfo/cntAddress/city"      : "UPDATE NEEDED",
                                 "rpCntInfo/cntAddress/country"   : "UPDATE NEEDED",
                                 "rpCntInfo/cntAddress/postCode"  : "UPDATE NEEDED",
                                 "rpCntInfo/cntAddress/eMailAdd"  : "marc.romano@noaa.gov",
                                 "rpCntInfo/cntAddress/country"   : "US",
                                 "rpCntInfo/cntPhone/voiceNum"    : "",
                                 "rpCntInfo/cntPhone/faxNum"      : "",
                                 "rpCntInfo/cntHours"             : "",
                                 "rpCntInfo/cntOnlineRes/linkage"           : "",
                                 "rpCntInfo/cntOnlineRes/protocol"          : "REST Service",
                                 "rpCntInfo/cntOnlineRes/orName"            : "",
                                 "rpCntInfo/cntOnlineRes/orDesc"            : "",
                                 "rpCntInfo/cntOnlineRes/orFunct/OnFunctCd" : 'value="002"',
                                 "displayName"                    : "Marc Romano",
                                 "editorSave"                     : "True",
                                },

                "Nikki Wildart" : {"editorSource"                   : "",
                                   "editorDigest"                   : "",
                                   "rpIndName"                      : "Nikki Wildart",
                                   "rpOrgName"                      : "Office of Protected Resources, National Marine Fisheries Service",
                                   "rpPosName"                      : "Biologist",
                                   "rpCntInfo/cntAddress/delPoint"  : "1315 East West Highway",
                                   "rpCntInfo/cntAddress/city"      : "Silver Spring",
                                   "rpCntInfo/cntAddress/country"   : "MD",
                                   "rpCntInfo/cntAddress/postCode"  : "",
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
                                  },

                "Shanna Dunn" : {"editorSource"                   : "",
                                 "editorDigest"                   : "",
                                 "rpIndName"                      : "Shanna Dunn",
                                 "rpOrgName"                      : "",
                                 "rpPosName"                      : "",
                                 "rpCntInfo/cntAddress/delPoint"  : "UPDATE NEEDED",
                                 "rpCntInfo/cntAddress/city"      : "UPDATE NEEDED",
                                 "rpCntInfo/cntAddress/country"   : "UPDATE NEEDED",
                                 "rpCntInfo/cntAddress/postCode"  : "UPDATE NEEDED",
                                 "rpCntInfo/cntAddress/eMailAdd"  : "shanna.dunn@noaa.gov",
                                 "rpCntInfo/cntAddress/country"   : "US",
                                 "rpCntInfo/cntPhone/voiceNum"    : "",
                                 "rpCntInfo/cntPhone/faxNum"      : "",
                                 "rpCntInfo/cntHours"             : "",
                                 "rpCntInfo/cntOnlineRes/linkage"           : "",
                                 "rpCntInfo/cntOnlineRes/protocol"          : "REST Service",
                                 "rpCntInfo/cntOnlineRes/orName"            : "",
                                 "rpCntInfo/cntOnlineRes/orDesc"            : "",
                                 "rpCntInfo/cntOnlineRes/orFunct/OnFunctCd" : 'value="002"',
                                 "displayName"                    : "Shanna Dunn",
                                 "editorSave"                     : "True",
                                },

                "Susan Wang" : {"editorSource"                   : "",
                                "editorDigest"                   : "",
                                "rpIndName"                      : "Susan Wang",
                                "rpOrgName"                      : "Protected Resources Division, West Coast Region, National Marine Fisheries Service",
                                "rpPosName"                      : "Black Abalone Recovery Coordinator",
                                "rpCntInfo/cntAddress/delPoint"  : "501 West Ocean Boulevard, Suite 4200",
                                "rpCntInfo/cntAddress/city"      : "Long Beach",
                                "rpCntInfo/cntAddress/country"   : "CA",
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
                             },}

            print(target_xml_name)

            rpIndNames = target_root.findall(".//rpIndName")

            contact_parent_children = {"editorSource":0,"editorDigest":1,"rpIndName":2,"rpOrgName":3,"rpPosName":4,"rpCntInfo":5,"rpCntInfo/cntOnlineRes":6,"displayName":7,"editorSave":8,"role":9,}
            default_list = list(contact_parent_children.keys())

            for rpIndName in rpIndNames:
                print(f"\t{rpIndName.text}")

                contact_parent = rpIndName.getparent()

                current_list = [child.tag for child in contact_parent.iterchildren()]
                the_missing = [i for i in default_list if i not in current_list]
                new_list = current_list + the_missing

                #children =  list(contact_parent)
                #print(children)

##                for child in contact_parent.iterchildren():
##                    print(contact_parent.index(child))

                print(current_list)

                for key in contact_parent_children:
                    #print(key)
                    if key in current_list:
                        old_index = current_list.index(key)
                        new_index = contact_parent_children[key]
                        current_list.pop(old_index)
                        current_list.insert(new_index, key)
                        del old_index, new_index
                    del key
                #print(new_list)

                print(current_list)

##                for element in contact_parent:
####                    old_index = contact_parent.index(element)
####                    new_index = contact_parent_children[element.tag]
####                    contact_parent.pop(old_index)
####                    current_list.insert(new_index, element)
####                    del old_index, new_index
##                    del element
##
##                print(contact_parent)

                #for item in new_list:
                #    print(item)

                #for child in contact_parent.iterchildren():
                #    print(f"\t\t{child.tag}")
##                for child in contact_parent:
##                    print(f"\t\t{child.tag}")
##                    #if not child.tag in contact_parent_children:
##                    print(f"\t\t\t{[k for k in contact_parent_children] if }")
##
##                    del child
                del current_list, the_missing, new_list
                del contact_parent
                del rpIndName
            del contact_dict
            del rpIndNames

            #print(default_list)
            del default_list
            del contact_parent_children
##                rpIndName_dict = contact_dict[rpIndName.text]
##                key_list = list(rpIndName_dict.keys())
##                for key in key_list:
##                    value = rpIndName_dict[key]
##                    print(f"\t\tIndex: {key_list.index(key):<2} Key: {key:<31} Value: {value}")
##
##                    if key.split('/')[-1:][0] not in ["OnFunctCd"]:
##                        key_value = contact_parent.find(f"./{key}")
##                        # Check if key_value is not None, which means the element exists
##                        if key_value != None:
##                            if key_value.text:
##                                print(f"\t\t\t ./{key:<31}: {key_value.text}\n")
##                                if value != key_value.text:
##                                    pass
##                                    #key_value.text = value
##                            else:
##                                print("no text")
##                        # If key_value is equal to None, then the element is missing and needs to be inserted
##                        elif key_value == None:
##                            insert_key = key.split('/')[-1:][0]
##                            key_parent = key.split('/')[:-1]
##                            key_parent_element = contact_parent.find(f"./{key_parent}")
##                            key_parent_element.insert()
##
##                            #print(f"need to insert: {insert_key_element} at {'/'.join(key_element_parent)}")
##                            #print(key.split('/'))
##                            #print(f"\t\t\t ./{key} is missing")
##                            # .split('/')[-1:][0]
##                            del insert_key_element, key_parent, key_parent_element
##
##                    else:
##                        key_value = contact_parent.find(f"./{key}")
##                        if key_value != None:
##                            if key_value.text:
##                                print(f"\t\t\t ./{key:<31}: {key_value.text}\n")
##                                if value != key_value.text:
##                                    pass
##                                    #key_value.text = value
##                            else:
##                                print("no text")
##                                print(key.split('/')[-1:][0])
##                        # If key_value is equal to None, then the element is missing and needs to be inserted
##                        elif key_value == None:
##                            print(f"need to insert: {key.split('/')[-1:][0]} at {key.split('/')[:-1][-1:]}")
##                            #print(key.split('/')[-1:][0])
##                            #print(key.split('/'))
##
##
##                        #key_value.set(value.split("=")[0],value.split("=")[1] )
##
##
##                        print(rpIndName_dict.keys().posistion(key))
##
##                    if key_value:
##                        print(f"\t\tNot None {key_value.text}")
##                    else:
##                        print(f"\t\tNone {key_value}")
##                    del key_value
##                    del key, value
##                del key_list
##                del rpIndName_dict

                #print(contact_parent.tag)
                #print(len(contact_parent))
                #remove_duplicate_elements(contact_parent)

                #print(len(contact_parent))
                #for ele in contact_parent:
                #    print(f"\t\t{ele.tag}")
                #    del ele

##
##                print(f"Before {cntOnlineRes.tag}")
##                for child in children:
##                    print(f"\t{child.tag:<8} = {child.text}")
##                    #print(f"\t{child}")
##                del child
##                if children[1].tag != "protocol":
##                    cntOnlineRes.insert(1, etree.SubElement(cntOnlineRes, "protocol"))
##                    protocol = cntOnlineRes.find("./protocol")
##                    protocol.text = "REST Service"
##                if children[1].tag == "protocol" and children[1].text is not None:
##                    protocol = cntOnlineRes.find("./protocol")
##                    protocol.text = "REST Service"

##                cntAddress       = contact_parent.find("./rpCntInfo/cntAddress")
##
##                delPoint = cntAddress.find("./delPoint")
##                if delPoint:
##                    delPoint.text  = contact_dict[rpIndName.text]["delPoint"]
##                else:
##                    cntAddress.insert(0, etree.SubElement(cntAddress, "delPoint"))
##                    delPoint.text  = contact_dict[rpIndName.text]["delPoint"]
##
##                city           = cntAddress.find("./rpCntInfo/cntAddress/city")
##                city.text      = contact_dict[rpIndName.text]["city"]
##
##                adminArea      = cntAddress.find("./rpCntInfo/cntAddress/adminArea")
##                adminArea.text = contact_dict[rpIndName.text]["adminArea"]
##
##                postCode       = cntAddress.find("./rpCntInfo/cntAddress/postCode")
##                postCode.text  = contact_dict[rpIndName.text]["postCode"]
##
##                eMailAdd       = cntAddress.find("./rpCntInfo/cntAddress/eMailAdd")
##                eMailAdd.text  = contact_dict[rpIndName.text]["eMailAdd"]
##
##                country        = cntAddress.find("./rpCntInfo/cntAddress/country")
##                country.text   = contact_dict[rpIndName.text]["country"]
##
##                del delPoint, city, adminArea, postCode, eMailAdd, country
        del UpdateRpCntInfos

        UpdateRpCntInfos = True
        if UpdateRpCntInfos:

##        <RoleCd value="001"></RoleCd> -->> Resource Provider
##        <RoleCd value="002"></RoleCd> -->> Custodian
##        <RoleCd value="003"></RoleCd> -->> Owner
##        <RoleCd value="004"></RoleCd> -->> User
##        <RoleCd value="005"></RoleCd> -->> Distributor
##        <RoleCd value="006"></RoleCd> -->> Originator
##        <RoleCd value="007"></RoleCd> -->> Point of Contact
##        <RoleCd value="008"></RoleCd> -->> Principal Investigator
##        <RoleCd value="009"></RoleCd> -->> Processor
##        <RoleCd value="010"></RoleCd> -->> Publisher
##        <RoleCd value="011"></RoleCd> -->> Author
##        <RoleCd value="012"></RoleCd> -->> Collaborator
##        <RoleCd value="013"></RoleCd> -->> Editor
##        <RoleCd value="014"></RoleCd> -->> Mediator
##        <RoleCd value="015"></RoleCd> -->> Rights Holder

            contact_dict = {"Jeffrey A. Seminoff" : {"editorSource"                   : "",
                                                     "editorDigest"                   : "",
                                                     "rpIndName"                      : "Jeffrey A. Seminoff",
                                                     "rpOrgName"                      : "",
                                                     "rpPosName"                      : "",
                                                     "rpCntInfo/cntAddress/delPoint"  : "8901 La Jolla Shores Drive",
                                                     "rpCntInfo/cntAddress/city"      : "La Jolla",
                                                     "rpCntInfo/cntAddress/adminArea" : "CA",
                                                     "rpCntInfo/cntAddress/postCode"  : "92037-1508",
                                                     "rpCntInfo/cntAddress/eMailAdd"  : "jeffrey.seminoff@noaa.gov",
                                                     "rpCntInfo/cntAddress/country"   : "US",
                                                     "rpCntInfo/cntPhone/voiceNum"    : "",
                                                     "rpCntInfo/cntPhone/faxNum"      : "",
                                                     "rpCntInfo/cntHours"             : "",
                                                     "rpCntInfo/cntOnlineRes/linkage"           : "https://",
                                                     "rpCntInfo/cntOnlineRes/protocol"          : "REST Service",
                                                     "rpCntInfo/cntOnlineRes/orName"            : "Fisheries",
                                                     "rpCntInfo/cntOnlineRes/orDesc"            : "NOAA Fisheries",
                                                     "rpCntInfo/cntOnlineRes/orFunct/OnFunctCd" : 'value="002"',
                                                     "displayName"                    : "Jeffrey A. Seminoff",
                                                     "editorSave"                     : "True",
                                                     },

                "Jennifer Schultz" : {"editorSource"                   : "",
                                      "editorDigest"                   : "",
                                      "rpIndName"                      : "Jennifer Schultz",
                                      "rpOrgName"                      : "Office of Protected Resources, National Marine Fisheries Service",
                                      "rpPosName"                      : "Fisheries Biologist",
                                      "rpCntInfo/cntAddress/delPoint"  : "1315 East West Highway",
                                      "rpCntInfo/cntAddress/city"      : "Silver Spring",
                                      "rpCntInfo/cntAddress/adminArea"   : "MD",
                                      "rpCntInfo/cntAddress/postCode"  : "",
                                      "rpCntInfo/cntAddress/eMailAdd"  : "jennifer.schultz@noaa.gov",
                                      "rpCntInfo/cntAddress/country"   : "US",
                                      "rpCntInfo/cntPhone/voiceNum"    : "",
                                      "rpCntInfo/cntPhone/faxNum"      : "",
                                      "rpCntInfo/cntHours"             : "0700 - 1800 EST/EDT",
                                      "rpCntInfo/cntOnlineRes/linkage"           : "https://www.fisheries.noaa.gov/about/office-protected-resources",
                                      "rpCntInfo/cntOnlineRes/protocol"          : "REST Service",
                                      "rpCntInfo/cntOnlineRes/orName"            : "Fisheries OPR",
                                      "rpCntInfo/cntOnlineRes/orDesc"            : "NOAA Fisheries Office of Protected Resources",
                                      "rpCntInfo/cntOnlineRes/orFunct/OnFunctCd" : 'value="002"',
                                      "displayName"                    : "Jennifer Schultz",
                                      "editorSave"                     : "True",
                                     },

                "Jonathan Molineaux" : {"editorSource"                   : "",
                                        "editorDigest"                   : "",
                                        "rpIndName"                      : "Jonathan Molineaux",
                                        "rpOrgName"                      : "Office of Protected Resources, National Marine Fisheries Service",
                                        "rpPosName"                      : "Fisheries Biologist",
                                        "rpCntInfo/cntAddress/delPoint"  : "1315 East West Highway",
                                        "rpCntInfo/cntAddress/city"      : "Silver Spring",
                                        "rpCntInfo/cntAddress/adminArea" : "MD",
                                        "rpCntInfo/cntAddress/postCode"  : "",
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
                                       },

                "Marc Romano" : {"editorSource"                   : "",
                                 "editorDigest"                   : "",
                                 "rpIndName"                      : "Marc Romano",
                                 "rpOrgName"                      : "",
                                 "rpPosName"                      : "",
                                 "rpCntInfo/cntAddress/delPoint"  : "UPDATE NEEDED",
                                 "rpCntInfo/cntAddress/city"      : "UPDATE NEEDED",
                                 "rpCntInfo/cntAddress/adminArea" : "UPDATE NEEDED",
                                 "rpCntInfo/cntAddress/postCode"  : "UPDATE NEEDED",
                                 "rpCntInfo/cntAddress/eMailAdd"  : "marc.romano@noaa.gov",
                                 "rpCntInfo/cntAddress/country"   : "US",
                                 "rpCntInfo/cntPhone/voiceNum"    : "",
                                 "rpCntInfo/cntPhone/faxNum"      : "",
                                 "rpCntInfo/cntHours"             : "",
                                 "rpCntInfo/cntOnlineRes/linkage"           : "",
                                 "rpCntInfo/cntOnlineRes/protocol"          : "REST Service",
                                 "rpCntInfo/cntOnlineRes/orName"            : "",
                                 "rpCntInfo/cntOnlineRes/orDesc"            : "",
                                 "rpCntInfo/cntOnlineRes/orFunct/OnFunctCd" : 'value="002"',
                                 "displayName"                    : "Marc Romano",
                                 "editorSave"                     : "True",
                                },

                "Nikki Wildart" : {"editorSource"                   : "",
                                   "editorDigest"                   : "",
                                   "rpIndName"                      : "Nikki Wildart",
                                   "rpOrgName"                      : "Office of Protected Resources, National Marine Fisheries Service",
                                   "rpPosName"                      : "Biologist",
                                   "rpCntInfo/cntAddress/delPoint"  : "1315 East West Highway",
                                   "rpCntInfo/cntAddress/city"      : "Silver Spring",
                                   "rpCntInfo/cntAddress/adminArea"   : "MD",
                                   "rpCntInfo/cntAddress/postCode"  : "",
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
                                  },

                "Shanna Dunn" : {"editorSource"                   : "",
                                 "editorDigest"                   : "",
                                 "rpIndName"                      : "Shanna Dunn",
                                 "rpOrgName"                      : "",
                                 "rpPosName"                      : "",
                                 "rpCntInfo/cntAddress/delPoint"  : "UPDATE NEEDED",
                                 "rpCntInfo/cntAddress/city"      : "UPDATE NEEDED",
                                 "rpCntInfo/cntAddress/adminArea" : "UPDATE NEEDED",
                                 "rpCntInfo/cntAddress/postCode"  : "UPDATE NEEDED",
                                 "rpCntInfo/cntAddress/eMailAdd"  : "shanna.dunn@noaa.gov",
                                 "rpCntInfo/cntAddress/country"   : "US",
                                 "rpCntInfo/cntPhone/voiceNum"    : "",
                                 "rpCntInfo/cntPhone/faxNum"      : "",
                                 "rpCntInfo/cntHours"             : "",
                                 "rpCntInfo/cntOnlineRes/linkage"           : "",
                                 "rpCntInfo/cntOnlineRes/protocol"          : "REST Service",
                                 "rpCntInfo/cntOnlineRes/orName"            : "",
                                 "rpCntInfo/cntOnlineRes/orDesc"            : "",
                                 "rpCntInfo/cntOnlineRes/orFunct/OnFunctCd" : 'value="002"',
                                 "displayName"                    : "Shanna Dunn",
                                 "editorSave"                     : "True",
                                },

                "Susan Wang" : {"editorSource"                   : "",
                                "editorDigest"                   : "",
                                "rpIndName"                      : "Susan Wang",
                                "rpOrgName"                      : "Protected Resources Division, West Coast Region, National Marine Fisheries Service",
                                "rpPosName"                      : "Black Abalone Recovery Coordinator",
                                "rpCntInfo/cntAddress/delPoint"  : "501 West Ocean Boulevard, Suite 4200",
                                "rpCntInfo/cntAddress/city"      : "Long Beach",
                                "rpCntInfo/cntAddress/adminArea"   : "CA",
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
                             },}

            print(target_xml_name)

            rpIndNames = target_root.findall(".//rpIndName")

            contact_parent_children = {"editorSource":0,"editorDigest":1,"rpIndName":2,"rpOrgName":3,"rpPosName":4,"rpCntInfo":5,"rpCntInfo/cntOnlineRes":6,"displayName":7,"editorSave":8,"role":9,}
            default_list = list(contact_parent_children.keys())

            for rpIndName in rpIndNames:
                print(f"\t{rpIndName.text}")

                contact_parent = rpIndName.getparent()
                print(contact_parent.tag)
                #print(etree.tostring(contact_parent, pretty_print=True).decode(), end='')
                #print(etree.tostring(contact_parent).decode(), end='')
                for child in contact_parent.iterchildren():
                    #print(contact_parent.index(child))
                    print(etree.tostring(child, method='html', pretty_print=True).decode(), end='')
                    del child
                del contact_parent

                del rpIndName

            del contact_dict

            del rpIndNames

            del default_list

            del contact_parent_children

        del UpdateRpCntInfos



        # Write the XML to the file
        target_tree.write(target_xml)
        pretty_format_xml_file(target_xml)

        del target_xml, target_xml_name
        del target_tree, target_root

        # Imports
        del etree, pretty_format_xml_file

    except:
        traceback.print_exc()
    else:
        return True
    finally:
        # Cleanup
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: raise Warning(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk

if __name__ == '__main__':
    try:
        main()
    except Warning as w:
        print(w)
