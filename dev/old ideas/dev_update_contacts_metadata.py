#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john.f.kennedy
#
# Created:     24/11/2024
# Copyright:   (c) john.f.kennedy 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Python Built-in's modules are loaded first
import os, sys
import traceback, inspect

# Third-party modules are loaded second
import arcpy

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

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

# function to update purpose and credits in metadata
#def update_metadata(target_root, source_root, target_xml_name):
def update_metadata(target_tree, source_tree, target_xml_name):
    try:
        from lxml import etree

        num_elements = 0

        source_root = source_tree.getroot()
        target_root = target_tree.getroot()

        # Just prints purpose
        UpdateIdPurp = False
        if UpdateIdPurp:
            # modify purpose element's text
            # there is only supposed to be one purpose element in metadata
            # replace purpose element text if element exists
            # if element doesn't exist, do nothing
            target_id_purp_elements = target_root.findall("./dataIdInfo/idPurp")
            for target_id_purp_element in target_id_purp_elements:
                if target_id_purp_element.text is not None:
                    print(f"Purpose: {target_id_purp_element.text}")
                del target_id_purp_element
            del target_id_purp_elements
            num_elements += 1
        del UpdateIdPurp

        # Just prints abstract
        UpdateIdAbs = False
        if UpdateIdAbs:
            # modify credit element's text
            # there is only supposed to be one credit element in metadata
            # replace credit element text if element exists
            # if element doesn't exist, do nothing
            target_abstract_elements = target_root.findall("./dataIdInfo/idAbs")
            for target_abstract_element in target_abstract_elements:
                if target_abstract_element.text is not None:
                    print(f"Description: {target_abstract_elements.text}")
                del target_abstract_element
            del target_abstract_elements
            num_elements += 1
        del UpdateIdAbs

        UpdateIdCredit = False
        if UpdateIdCredit:
            # modify credit element's text
            # there is only supposed to be one credit element in metadata
            # replace credit element text if element exists
            # if element doesn't exist, do nothing
            target_id_credit_elements = target_root.findall("./dataIdInfo/idCredit")
            source_id_credit_elements = source_root.findall("./dataIdInfo/idCredit")
            for target_id_credit_element in target_id_credit_elements:
                #if target_id_credit_element.text is not None:
                #print(f"Credits: {target_id_credit_element.text}")
                target_id_credit_element.text = source_id_credit_elements[0].text
                del target_id_credit_element
            del target_id_credit_elements, source_id_credit_elements
            num_elements += 1
        del UpdateIdCredit

        UpdateUseLimit = False
        if UpdateUseLimit:
            # modify credit element's text
            # there is only supposed to be one credit element in metadata
            # replace credit element text if element exists
            # if element doesn't exist, do nothing
            target_use_limit_elements = target_root.findall("./dataIdInfo/resConst/Consts/useLimit")
            source_use_limit_elements = source_root.findall("./dataIdInfo/resConst/Consts/useLimit")
            for target_use_limit_element in target_use_limit_elements:
                #if target_use_limit_element.text is not None:
                #print(f"Use Limits: {target_use_limit_element.text}")
                target_use_limit_element.text = source_use_limit_elements[0].text
                del target_use_limit_element
            del target_use_limit_elements, source_use_limit_elements
            num_elements += 1
        del UpdateUseLimit

        # Don't use
        UpdateExDesc = False # Add extent description
        if UpdateExDesc:
            # modify credit element's text
            # there is only supposed to be one credit element in metadata
            # replace credit element text if element exists
            # if element doesn't exist, do nothing
            target_ex_desc_elements = target_root.findall("./dataIdInfo/dataExt/exDesc")
            source_ex_des_elements  = source_root.findall("./dataIdInfo/dataExt/exDesc")
            for target_ex_desc_element in target_ex_desc_elements:
                if target_ex_desc_element.text is not None:
                    temp_text = target_ex_desc_element.text
                    if source_ex_des_elements[0].text not in temp_text:
                        target_ex_desc_element.text = f"{temp_text}. {source_ex_des_elements[0].text}"
                    del temp_text
                else:
                    target_ex_desc_element.text = source_ex_des_elements[0].text
                del target_ex_desc_element
            del target_ex_desc_elements, source_ex_des_elements
            num_elements += 1
        del UpdateExDesc

        UpdateEaInfo = False
        if UpdateEaInfo:
            # Find the eainfo elements
            eainfo_target_child = target_root.find("eainfo/detailed")
            eainfo_source_child = source_root.find("eainfo/detailed")
            if eainfo_target_child is not None:
                # Replace child1 with child2
                parent = eainfo_target_child.getparent()
                parent.replace(eainfo_target_child, eainfo_source_child)
                del parent
            else:
                arcpy.AddWarning(f"\tFeature Class has no eainfo")
            del eainfo_target_child, eainfo_source_child
            num_elements += 1
        del UpdateEaInfo

        UpdateIdPoC = False
        if UpdateIdPoC:
            # Find the citRespPart elements
            idPoC_target_child = target_root.find('dataIdInfo/idPoC')
            idPoC_source_child = source_root.find('dataIdInfo/idPoC')
            if idPoC_target_child is not None:
                # Replace child1 with child2
                parent = idPoC_target_child.getparent()
                parent.replace(idPoC_target_child, idPoC_source_child)
                del parent
            else:
                arcpy.AddWarning(f"\tFeature Class has no idPoC")
            del idPoC_target_child, idPoC_source_child
            num_elements += 1
        del UpdateIdPoC

        UpdateCitRespParty = False
        if UpdateCitRespParty:
            # Find the citRespPart elements
            citRespParty_target_child = target_root.find('dataIdInfo/idCitation/citRespParty')
            citRespParty_source_child = source_root.find('dataIdInfo/idCitation/citRespParty')
            if citRespParty_target_child is not None:
                # Replace child1 with child2
                parent = citRespParty_target_child.getparent()
                parent.replace(citRespParty_target_child, citRespParty_source_child)
                del parent
            else:
                arcpy.AddWarning(f"\tFeature Class has no citRespParty")
            del citRespParty_target_child, citRespParty_source_child
            num_elements += 1
        del UpdateCitRespParty

        UpdateMdContact = False
        if UpdateMdContact:
            # Find the citRespPart elements
            mdContact_target_child = target_root.find('mdContact')
            mdContact_source_child = source_root.find('mdContact')
            if mdContact_target_child is not None: # and mdContact_source_child is not None:
                # Replace child1 with child2
                parent = mdContact_target_child.getparent()
                parent.replace(mdContact_target_child, mdContact_source_child)
                del parent
            else:
                arcpy.AddWarning(f"\tFeature Class has no mdContact")
            del mdContact_target_child, mdContact_source_child
            num_elements += 1
        del UpdateMdContact

        UpdateDistInfo = False
        if UpdateDistInfo:
            # Find the distInfo elements
            distInfo_target_child = target_root.find('distInfo')
            distInfo_source_child = source_root.find('distInfo')
            if distInfo_target_child is not None: # and distInfo_source_child is not None:
                #pass
                # Replace child1 with child2
                parent = distInfo_target_child.getparent()
                parent.replace(distInfo_target_child, distInfo_source_child)
                del parent
            else:
                arcpy.AddWarning(f"\tFeature Class has no distInfo")
            del distInfo_target_child, distInfo_source_child
            num_elements += 1
        del UpdateDistInfo

        # Updated in a new way below
        UpdateRpCntInfos = False
        if UpdateRpCntInfos:
            rpCntInfos = target_root.findall(".//rpCntInfo/cntOnlineRes")
            for rpCntInfo in rpCntInfos:
                children = [c for c in rpCntInfo.getchildren()]
                if children:
                    if children[1].tag != "protocol":
                        rpCntInfo.insert(1, etree.SubElement(rpCntInfo, "protocol"))
                        protocol = rpCntInfo.find("./protocol")
                        protocol.text = "REST Service"
                    if children[1].tag == "protocol" and children[1].text is not None:
                        protocol = rpCntInfo.find("./protocol")
                        protocol.text = "REST Service"
                del children
                del rpCntInfo
            del rpCntInfos
            num_elements += 1
        del UpdateRpCntInfos

        # Updated in a new way below
        UpdateLinkage = False
        if UpdateLinkage:
            new_item_name = target_root.find("./Esri/DataProperties/itemProps/itemName").text
            onLineSrcs = target_root.findall("./distInfo/distributor/distorTran/onLineSrc")
            for onLineSrc in onLineSrcs:
                if onLineSrc.find('./protocol').text == "ESRI REST Service":
                    old_linkage_element = onLineSrc.find('./linkage')
                    old_linkage = old_linkage_element.text
                    #print(old_linkage)
                    old_item_name = old_linkage[old_linkage.find("/services/")+len("/services/"):old_linkage.find("/FeatureServer")]
                    new_linkage = old_linkage.replace(old_item_name, new_item_name)
                    #print(new_linkage)
                    old_linkage_element.text = new_linkage
                    #print(old_linkage_element.text)
                    del old_linkage_element
                    del old_item_name, old_linkage, new_linkage
                del onLineSrc
            del onLineSrcs, new_item_name
            num_elements += 1
        del UpdateLinkage

        # Have to think about this one
        UpdateDqInfo = False
        if UpdateDqInfo:
            # Find the dqInfo elements
            dqInfo_target_child = target_root.find('dqInfo')
            dqInfo_source_child = source_root.find('dqInfo')
            if dqInfo_target_child is not None: # and dqInfo_source_child is not None:
                #pass
                # Replace child1 with child2
                parent = dqInfo_target_child.getparent()
                parent.replace(dqInfo_target_child, dqInfo_source_child)
                del parent
            else:
                arcpy.AddWarning(f"\tFeature Class has no dqInfo")
            del dqInfo_target_child, dqInfo_source_child
            num_elements += 1
        del UpdateDqInfo

        # Updated in a new way below
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

                contact_dict[contact_count][os.path.basename(target_xml_name)][rpIndName] = {}

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
                        contact_dict[contact_count][os.path.basename(target_xml_name)][rpIndName][child.tag] = child.text
                        #print(f"\t{child.tag:<9} = {child.text}")
                        del child
                del children

                del rpIndName
                del cntAddress

            for count in contact_dict:
                for _target_xml_name in contact_dict[count]:
                    print(_target_xml_name)
                    for contact in contact_dict[count][_target_xml_name]:
                        print(f"\t{contact:<10}")
                        for address_part in contact_dict[count][_target_xml_name][contact]:
                            print(f"\t\t{address_part:<10}:  {contact_dict[count][_target_xml_name][contact][address_part]}")
                            del address_part
                        del contact
                    del _target_xml_name
                del count

            del cntAddresss, contact_dict, contact_count
        del UpdateRpCntInfos

        # Doesn't work
        UpdateRpCntInfos = False
        if UpdateRpCntInfos:
            num_elements = 0

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

            contact_dict = {"Jeffrey A. Seminoff" : {"editorSource"                   : "extermal",
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

                "Jennifer Schultz" : {"editorSource"                   : "extermal",
                                      "editorDigest"                   : "7517deefd0d9d1960164ab982e5e8278568cfa8c",
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

                "Jonathan Molineaux" : {"editorSource"                   : "extermal",
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

                "Marc Romano" : {"editorSource"                   : "extermal",
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

                "Nikki Wildart" : {"editorSource"                   : "extermal",
                                   "editorDigest"                   : "9cc0fe80de5687cc4d79f50f3a254f2c3ceb08ce",
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

                "Shanna Dunn" : {"editorSource"                   : "extermal",
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

                "Susan Wang" : {"editorSource"                   : "extermal",
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


            rpIndNames = target_root.findall(".//rpIndName")

            tag_text_dict = {target_xml_name : {}}

            for rpIndName in rpIndNames:
                user = rpIndName.text
                #print(user)
                contact_parent = rpIndName.getparent()

                FullRecord = False
                if FullRecord:
                    if user in contact_dict:
                        print(f"{user}")
                        user_dict = contact_dict[user]
                        for key in user_dict:
                            #print(f"\t{key}")
                            element = contact_parent.find(f"./{key}")
                            #element.text = user_dict[key]
                            if len(element):
                                try:
                                    print(f"\t./{key} : {element.text}")
                                except:
                                    print(f"\t./{key} is empty or missing")
                            del element
                            del key
                        del user_dict
                del FullRecord

                SelectedElement = False
                if SelectedElement:
                    #if user in contact_dict:
                    key = "editorDigest"
                    element = contact_parent.find(f"./{key}")
                    #print(type(element))
                    #if not isinstance(element, 'NoneType'):
                        #if len(element.text) > 0:
                    #if element is not None:
                    if not isinstance(element, type(None)):
                        if element.text:
                            #print(f"{user}")
                            #print(f"\t./{key} : {element.text}")
                            ancestors = []
                            for ancestor in element.iterancestors():
                                #iterancestors(self, tag=None, *tags)
                                if not ancestor.tag == "metadata":
                                    ancestors.append(ancestor.tag)
                                del ancestor
                            #print(ancestors, isinstance(ancestors, list))
                            ancestors_path = "./" + "/".join(list(reversed(ancestors))) + f"/{element.tag}"
                            #print(f"\t{ancestors_path} --> {target_root.find(ancestors_path).text}")

                            #print(tag_text_dict[target_xml_name])
                            if ancestors_path not in tag_text_dict[target_xml_name]:
                                tag_text_dict[target_xml_name][ancestors_path] = {user : element.text}
                            del ancestors_path
                            del ancestors
                        else:
                            pass
                            #print(f"\t./{key} is empty")
                    else:
                        pass
                        #print(f"\t./{key} is missing")
                    #else:
                    #    pass
                    #print(f"\t./{key} is missing")

                    del key, element

                del SelectedElement

                del user
                del contact_parent
                del rpIndName

            for file_name in tag_text_dict:
                element_dict = tag_text_dict[file_name]
                print(file_name)
                for key in element_dict:
                    print(f"\t{key} : {element_dict[key]}")
                    del key
                del element_dict
                del file_name

            del tag_text_dict
            del contact_dict
            del rpIndNames
        del UpdateRpCntInfos

        # Doesn't work
        # Updated in a new way below
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

            contact_dict = {"Jeffrey A. Seminoff" : {"editorSource"                   : "extermal",
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
                                                     "role/RoleCd"                    : "",
                                                     },

                "Jennifer Schultz" : {"editorSource"                   : "extermal",
                                      "editorDigest"                   : "7517deefd0d9d1960164ab982e5e8278568cfa8c",
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
                                      "role/RoleCd"                    : "",
                                     },

                "Jonathan Molineaux" : {"editorSource"                   : "extermal",
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
                                        "role/RoleCd"                    : "",
                                       },

                "Marc Romano" : {"editorSource"                   : "extermal",
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
                                 "role/RoleCd"                    : "",
                                },

                "Nikki Wildart" : {"editorSource"                   : "extermal",
                                   "editorDigest"                   : "9cc0fe80de5687cc4d79f50f3a254f2c3ceb08ce",
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
                                   "role/RoleCd"                    : "",
                                  },

                "Shanna Dunn" : {"editorSource"                   : "extermal",
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
                                 "role/RoleCd"                    : "",
                                },

                "Susan Wang" : {"editorSource"                   : "extermal",
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
                                "rpCntInfo/cntOnlineRes/orFunct/OnFunctCd" : "",
                                "displayName"                    : "Susan Wang",
                                "editorSave"                     : "True",
                                "role/RoleCd"                    : "",
                             },}
            rpIndNames = target_root.findall(".//rpIndName")
            for rpIndName in rpIndNames:
                user = rpIndName.text
                #print(user)
                contact_parent = rpIndName.getparent()
                print(target_root.getpath(rpIndName))

                remove_duplicate_elements(contact_parent)

                ancestors = []
                for ancestor in contact_parent.iterancestors():
                    #if not ancestor.tag == "metadata":
                    #    ancestors.append(ancestor.tag)
                    ancestors.append(ancestor.tag)
                    del ancestor
                #ancestors_path_left = "./" + "/".join(list(reversed(ancestors))) + f"/{contact_parent.tag}"
                #ancestors_path_right = "./" + "/".join(list(ancestors)) + f"/{contact_parent.tag}"
                #ancestors_path_left = "<" + "><".join(list(reversed(ancestors)))  + ">" + f"<{contact_parent.tag}>"
                #ancestors_path_right = f"</{contact_parent.tag}>" + "</" + "></".join(list(ancestors))  + ">"
                #print(ancestors_path_left)
                #print(ancestors_path_right)
                #print(ancestors_path_left + ancestors_path_right)
                #del ancestors_path_left, ancestors_path_right
                ancestors_path = "/".join(list(reversed(ancestors))) + f"/{contact_parent.tag}"
                #ancestors_path = "<" + "><".join(list(reversed(ancestors)))  + ">" + f"<{contact_parent.tag}>" + '<editorSource>external</editorSource><editorDigest/><rpIndName/><rpOrgName/><rpPosName/><rpCntInfo><cntAddress addressType="both"><delPoint/><city/><adminArea/><postCode/><eMailAdd/><country>US</country></cntAddress><cntPhone><voiceNum tddtty=""></voiceNum><faxNum/></cntPhone><cntHours/><cntOnlineRes><linkage/><protocol/><orName/><orDesc/><orFunct><OnFunctCd value="002"></OnFunctCd></orFunct></cntOnlineRes></rpCntInfo><editorSave/><displayName/><role><RoleCd value="005"></RoleCd></role>' + f"</{contact_parent.tag}>" + "</" + "></".join(list(ancestors))  + ">"
                print(ancestors_path)
                ancestors_xml = "<" + "><".join(list(reversed(ancestors)))  + ">" + f"<{contact_parent.tag}>"
                ancestors_xml = ancestors_xml.replace("<>", "")
                #print(ancestors_xml)
                #print(ancestors)
                #contact_root = etree.XML(f'<{contact_parent.tag}><editorSource/><editorDigest/><rpIndName/><rpOrgName/><rpPosName/><rpCntInfo><cntAddress addressType="both"><delPoint/><city/><adminArea/><postCode/><eMailAdd/><country>US</country></cntAddress><cntPhone><voiceNum tddtty=""></voiceNum><faxNum/></cntPhone><cntHours/><cntOnlineRes><linkage/><protocol/><orName/><orDesc/><orFunct><OnFunctCd value="002"></OnFunctCd></orFunct></cntOnlineRes></rpCntInfo><editorSave/><displayName/><role><RoleCd value="005"></RoleCd></role></{contact_parent.tag}>')
                #contact_root = etree.XML(f'<{contact_parent.tag}><editorSource>external</editorSource><editorDigest/><rpIndName/><rpOrgName/><rpPosName/><rpCntInfo><cntAddress addressType="both"><delPoint/><city/><adminArea/><postCode/><eMailAdd/><country>US</country></cntAddress><cntPhone><voiceNum tddtty=""></voiceNum><faxNum/></cntPhone><cntHours/><cntOnlineRes><linkage/><protocol/><orName/><orDesc/><orFunct><OnFunctCd value="002"></OnFunctCd></orFunct></cntOnlineRes></rpCntInfo><editorSave/><displayName/><role><RoleCd value="005"></RoleCd></role></{contact_parent.tag}>')
                ancestors_path = "<" + "><".join(list(reversed(ancestors)))  + ">" + f"<{contact_parent.tag}>" + '<editorSource>external</editorSource><editorDigest/><rpIndName/><rpOrgName/><rpPosName/><rpCntInfo><cntAddress addressType="both"><delPoint/><city/><adminArea/><postCode/><eMailAdd/><country>US</country></cntAddress><cntPhone><voiceNum tddtty=""></voiceNum><faxNum/></cntPhone><cntHours/><cntOnlineRes><linkage/><protocol/><orName/><orDesc/><orFunct><OnFunctCd value="002"></OnFunctCd></orFunct></cntOnlineRes></rpCntInfo><editorSave/><displayName/><role><RoleCd value="005"></RoleCd></role>' + f"</{contact_parent.tag}>" + "</" + "></".join(list(ancestors))  + ">"
                contact_root = etree.fromstring(ancestors_path)
                #print(contact_root.tag)
                #print(target_root.tag)
                del ancestors_path
                #print(etree.tostring(contact_root, pretty_print=True).decode())
                del ancestors_xml
                for user in contact_dict:
                    user_dict = contact_dict[user]
                    for key in user_dict:
                        element = contact_root.find(f"./{key}")
                        if not isinstance(element, type(None)):
                            #if element.text:
                            if element.tag not in ["OnFunctCd", "RoleCd"]:
                                element.text = user_dict[key]
                            else:
                                if element.tag == "RoleCd":
                                    RoleCd = contact_parent.find(f"./{key}")
                                    element.set("value", RoleCd.attrib["value"])
                                    del RoleCd
                                elif element.tag == "OnFunctCd":
                                    pass
                        del element
                        del key
                    del user_dict
                #print(etree.tostring(contact_parent, pretty_print=True).decode())
                #print(etree.tostring(contact_root, encoding='UTF-8', xml_declaration=True, pretty_print=True).decode())
                #print(f"{contact_parent.tag}, {contact_root.tag}")
                #contact_parent.replace(contact_parent, contact_root)
##                ancestors = []
##                for ancestor in contact_parent.iterancestors():
##                    if not ancestor.tag == "metadata":
##                        ancestors.append(ancestor.tag)
##                    del ancestor
##                ancestors_path = "./" + "/".join(list(reversed(ancestors))) + f"/{contact_parent.tag}"
##                #print(ancestors_path)
##                ancestors_xml = "<" + "><".join(list(reversed(ancestors)))  + ">" + f"<{contact_parent.tag>}"
##                print(ancestors_xml)
##
##                del ancestors_xml
                #target_root_child = target_root.find(ancestors_path)
                #print(etree.tostring(target_root_child, encoding='UTF-8', xml_declaration=True, pretty_print=True).decode())
                #print(etree.tostring(target_root_child, pretty_print=True).decode())
                #target_root.replace(target_root_child, contact_root)
                #del target_root_child
                #del ancestors_path
                del ancestors
                del contact_root
                del user
                del contact_parent
                del rpIndName
            del remove_duplicate_elements
            del contact_dict
            del rpIndNames
            num_elements += 1
        del UpdateRpCntInfos


        # This is the current one that appears to work.
        UpdateRpCntInfos = False
        if UpdateRpCntInfos:

            #source_root = source_tree.getroot()
            #target_root = target_tree.getroot()

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

            contact_dict = {"Jeffrey A. Seminoff" : {"editorSource"                   : "extermal",
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
                                                     "role/RoleCd"                    : "",
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
                                      "role/RoleCd"                    : "",
                                     },

                "John F Kennedy" : {"editorSource"                  : "extermal",
                                   "editorDigest"                   : "7292bfe65733cdc0b913cf7ccdc01a2bff9590b1",
                                   "rpIndName"                      : "John F Kennedy",
                                   "rpOrgName"                      : "NMFS Office of Science and Technology",
                                   "rpPosName"                      : "GIS Specialist",
                                   "rpCntInfo/cntAddress/delPoint"  : "1315 East West Highway",
                                   "rpCntInfo/cntAddress/city"      : "Silver Spring",
                                   "rpCntInfo/cntAddress/adminArea" : "MD",
                                   "rpCntInfo/cntAddress/postCode"  : "20910-3282",
                                   "rpCntInfo/cntAddress/eMailAdd"  : "john.f.kennedy@noaa.gov",
                                   "rpCntInfo/cntAddress/country"   : "US",
                                   "rpCntInfo/cntPhone/voiceNum"    : "(301) 427-8149",
                                   "rpCntInfo/cntPhone/faxNum"      : "(301) 713-4137",
                                   "rpCntInfo/cntHours"             : "0700 - 1800 EST/EDT",
                                   "rpCntInfo/cntOnlineRes/linkage"           : "http://www.st.nmfs.noaa.gov",
                                   "rpCntInfo/cntOnlineRes/protocol"          : "REST Service",
                                   "rpCntInfo/cntOnlineRes/orName"            : "Fisheries OST",
                                   "rpCntInfo/cntOnlineRes/orDesc"            : "NOAA Fisheries Office of Science and Technology",
                                   "rpCntInfo/cntOnlineRes/orFunct/OnFunctCd" : 'value="002"',
                                   "displayName"                    : "John F Kennedy",
                                   "editorSave"                     : "True",
                                   "role/RoleCd"                    : "",
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
                                        "role/RoleCd"                    : "",
                                       },

                "Marc Romano" : {"editorSource"                   : "extermal",
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
                                 "role/RoleCd"                    : "",
                                },

                "Nikki Wildart" : {"editorSource"                   : "extermal",
                                   "editorDigest"                   : "9cc0fe80de5687cc4d79f50f3a254f2c3ceb08ce",
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
                                   "role/RoleCd"                    : "",
                                  },

                "Shanna Dunn" : {"editorSource"                   : "extermal",
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
                                 "role/RoleCd"                    : "",
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
                                "rpCntInfo/cntOnlineRes/orFunct/OnFunctCd" : "",
                                "displayName"                    : "Susan Wang",
                                "editorSave"                     : "True",
                                "role/RoleCd"                    : "",
                             },}

            #print(etree.tostring(target_root, pretty_print=True).decode())
            #print(etree.tostring(source_root, pretty_print=True).decode())

            #find = etree.XPath("//rpIndName[contains(.,'Jennifer Schultz')]")
            #rpIndNames = target_root.findall(".//rpIndName")
            #rpIndNames = find(target_root)
            #for rpIndName in rpIndNames:
            #    print(rpIndName.text)
            #    print(target_tree.getpath(rpIndName))
            #    del rpIndName
            #del rpIndNames
            #del find

            #>>> a  = etree.Element("a")
            #>>> b  = etree.SubElement(a, "b")
            #>>> c  = etree.SubElement(a, "c")
            #>>> d1 = etree.SubElement(c, "d")
            #>>> d2 = etree.SubElement(c, "d")
            #>>> tree = etree.ElementTree(c)
            #>>> print(tree.getpath(d2))
            #/c/d[2]
            #>>> tree.xpath(tree.getpath(d2)) == [d2]
            #True
            #tree = etree.ElementTree(c)
            #print(tree.getpath(d2))
            #print(tree.getpath(d2))
            #print(tree.xpath(tree.getpath(d2)) == [d2])

            #rpIndNames = target_root.findall(".//rpIndName")
            #find = etree.XPath("//rpIndName[contains(.,'Jennifer Schultz')]")
            find = etree.XPath("//rpIndName")
            rpIndNames = find(target_root)
            del find

            for rpIndName in rpIndNames:
                user = rpIndName.text
                print(user)
                contact_parent = rpIndName.getparent()
                #print(target_tree.getpath(rpIndName))
                #target_tree_x_path = target_tree.getpath(contact_parent)
                #rpIndName

##                ancestors = []
##                for ancestor in contact_parent.iterancestors():
##                    #if not ancestor.tag == "metadata":
##                    #    ancestors.append(ancestor.tag)
##                    ancestors.append(ancestor.tag)
##                    del ancestor
                #ancestors_path_left = "./" + "/".join(list(reversed(ancestors))) + f"/{contact_parent.tag}"
                #ancestors_path_right = "./" + "/".join(list(ancestors)) + f"/{contact_parent.tag}"
                #ancestors_path_left = "<" + "><".join(list(reversed(ancestors)))  + ">" + f"<{contact_parent.tag}>"
                #ancestors_path_right = f"</{contact_parent.tag}>" + "</" + "></".join(list(ancestors))  + ">"
                #print(ancestors_path_left)
                #print(ancestors_path_right)
                #print(ancestors_path_left + ancestors_path_right)
                #del ancestors_path_left, ancestors_path_right
                #ancestors_path = "/".join(list(reversed(ancestors))) + f"/{contact_parent.tag}"
                #ancestors_path = "<" + "><".join(list(reversed(ancestors)))  + ">" + f"<{contact_parent.tag}>" + '<editorSource>external</editorSource><editorDigest/><rpIndName/><rpOrgName/><rpPosName/><rpCntInfo><cntAddress addressType="both"><delPoint/><city/><adminArea/><postCode/><eMailAdd/><country>US</country></cntAddress><cntPhone><voiceNum tddtty=""></voiceNum><faxNum/></cntPhone><cntHours/><cntOnlineRes><linkage/><protocol/><orName/><orDesc/><orFunct><OnFunctCd value="002"></OnFunctCd></orFunct></cntOnlineRes></rpCntInfo><editorSave/><displayName/><role><RoleCd value="005"></RoleCd></role>' + f"</{contact_parent.tag}>" + "</" + "></".join(list(ancestors))  + ">"
                #print(ancestors_path)
                #ancestors_xml = "<" + "><".join(list(reversed(ancestors)))  + ">" + f"<{contact_parent.tag}>"
                #ancestors_xml = ancestors_xml.replace("<>", "")
                #print(ancestors_xml)
                #print(ancestors)
                #contact_root = etree.XML(f'<{contact_parent.tag}><editorSource/><editorDigest/><rpIndName/><rpOrgName/><rpPosName/><rpCntInfo><cntAddress addressType="both"><delPoint/><city/><adminArea/><postCode/><eMailAdd/><country>US</country></cntAddress><cntPhone><voiceNum tddtty=""></voiceNum><faxNum/></cntPhone><cntHours/><cntOnlineRes><linkage/><protocol/><orName/><orDesc/><orFunct><OnFunctCd value="002"></OnFunctCd></orFunct></cntOnlineRes></rpCntInfo><editorSave/><displayName/><role><RoleCd value="005"></RoleCd></role></{contact_parent.tag}>')
                #contact_root = etree.XML(f'<{contact_parent.tag}><editorSource>external</editorSource><editorDigest/><rpIndName/><rpOrgName/><rpPosName/><rpCntInfo><cntAddress addressType="both"><delPoint/><city/><adminArea/><postCode/><eMailAdd/><country>US</country></cntAddress><cntPhone><voiceNum tddtty=""></voiceNum><faxNum/></cntPhone><cntHours/><cntOnlineRes><linkage/><protocol/><orName/><orDesc/><orFunct><OnFunctCd value="002"></OnFunctCd></orFunct></cntOnlineRes></rpCntInfo><editorSave/><displayName/><role><RoleCd value="005"></RoleCd></role></{contact_parent.tag}>')
                #ancestors_path = "<" + "><".join(list(reversed(ancestors)))  + ">" + f"<{contact_parent.tag}>" + '<editorSource>external</editorSource><editorDigest/><rpIndName/><rpOrgName/><rpPosName/><rpCntInfo><cntAddress addressType="both"><delPoint/><city/><adminArea/><postCode/><eMailAdd/><country>US</country></cntAddress><cntPhone><voiceNum tddtty=""></voiceNum><faxNum/></cntPhone><cntHours/><cntOnlineRes><linkage/><protocol/><orName/><orDesc/><orFunct><OnFunctCd value="002"></OnFunctCd></orFunct></cntOnlineRes></rpCntInfo><editorSave/><displayName/><role><RoleCd value="005"></RoleCd></role>' + f"</{contact_parent.tag}>" + "</" + "></".join(list(ancestors))  + ">"
                contact_xml_string = etree.fromstring(f'<{contact_parent.tag}><editorSource>external</editorSource><editorDigest/><rpIndName/><rpOrgName/><rpPosName/><rpCntInfo><cntAddress addressType="both"><delPoint/><city/><adminArea/><postCode/><eMailAdd/><country>US</country></cntAddress><cntPhone><voiceNum tddtty=""></voiceNum><faxNum/></cntPhone><cntHours/><cntOnlineRes><linkage/><protocol/><orName/><orDesc/><orFunct><OnFunctCd value="002"></OnFunctCd></orFunct></cntOnlineRes></rpCntInfo><editorSave/><displayName/><role><RoleCd value="005"></RoleCd></role></{contact_parent.tag}>')
                #contact_xml_string = etree.fromstring(f'<editorSource>external</editorSource><editorDigest/><rpIndName/><rpOrgName/><rpPosName/><rpCntInfo><cntAddress addressType="both"><delPoint/><city/><adminArea/><postCode/><eMailAdd/><country>US</country></cntAddress><cntPhone><voiceNum tddtty=""></voiceNum><faxNum/></cntPhone><cntHours/><cntOnlineRes><linkage/><protocol/><orName/><orDesc/><orFunct><OnFunctCd value="002"></OnFunctCd></orFunct></cntOnlineRes></rpCntInfo><editorSave/><displayName/><role><RoleCd value="005"></RoleCd></role>')
                # create an ElementTree object from the metadata XML string
                contact_tree = etree.ElementTree(contact_xml_string)
                contact_root = contact_tree.getroot()
                del contact_xml_string

                #print(contact_root.tag)
                #print(target_root.tag)
                #del ancestors_path
                #print(etree.tostring(contact_root, pretty_print=True).decode())
                #del ancestors_xml

                user_dict = contact_dict[user]
                for key in user_dict:
                    element = contact_root.find(f"./{key}")
                    if not isinstance(element, type(None)):
                        #if element.text:
                        if element.tag not in ["OnFunctCd", "RoleCd"]:
                            element.text = user_dict[key]
                        else:
                            if element.tag == "RoleCd":
                                RoleCd = contact_parent.find(f"./{key}")
                                element.set("value", RoleCd.attrib["value"])
                                del RoleCd
                            elif element.tag == "OnFunctCd":
                                pass
                    del element
                    del key
                del user_dict
                #print(etree.tostring(contact_parent, pretty_print=True).decode())
                #print(etree.tostring(contact_root, encoding='UTF-8', xml_declaration=True, pretty_print=True).decode())
                #print(etree.tostring(contact_root, pretty_print=True).decode())
                #print(f"{contact_parent.tag}, {contact_root.tag}")
                #target_root.replace(contact_parent, contact_root)
                #target_root.replace(contact_parent.xpath(x_path)[0], contact_root)

    ##            original_xml = "<root><dc><batman alias='dark_knight' /></dc></root>"
    ##            modified_tag = "<batman alias='not_dark_knight' />"
    ##            x_path = '/root/dc/batman'
    ##            original_obj = etree.fromstring(original_xml)
    ##            modified_obj = etree.fromstring(modified_tag)
    ##            #original_obj.replace(original_obj.xpath(x_path)[0], modified_obj)
    ##            batman = original_obj.xpath(x_path)[0]
    ##            batman.getparent().replace(batman, modified_obj)

                target_tree_x_path = target_tree.getpath(contact_parent)
                #print(target_tree_x_path)
                #print(contact_parent.xpath(target_tree_x_path)[0])


                #rpIndName.getparent().replace(contact_parent.xpath(target_tree_x_path)[0], contact_root)
                contact_root_x_path = contact_tree.getpath(contact_root)
                #print(contact_tree.xpath(contact_root_x_path)[0])

                try:
                    contact_parent.getparent().replace(contact_parent.xpath(target_tree_x_path)[0], contact_tree.xpath(contact_root_x_path)[0])
                except:
                    print(user)
                    print(contact_parent.xpath(target_tree_x_path))
                    print(contact_tree.xpath(contact_root_x_path))
                    traceback.print_exc()

                del contact_root_x_path

##                # Correct: Replace 'grandchild' with 'new_element' which is a child of 'child1'
##                grandchild_element = tree.xpath("child1/grandchild")[0]
##                child1_element = tree.xpath("child1")[0]
##                new_element = etree.Element("new_element")
##                child1_element.replace(grandchild_element, new_element)

                del contact_tree

                    #>>> a  = etree.Element("a")
                    #>>> b  = etree.SubElement(a, "b")
                    #>>> c  = etree.SubElement(a, "c")
                    #>>> d1 = etree.SubElement(c, "d")
                    #>>> d2 = etree.SubElement(c, "d")
                    #>>> tree = etree.ElementTree(c)
                    #>>> print(tree.getpath(d2))
                    #/c/d[2]
                    #>>> tree.xpath(tree.getpath(d2)) == [d2]
                    #True
                    #tree = etree.ElementTree(c)
                    #print(tree.getpath(d2))
                    #print(tree.getpath(d2))
                    #print(tree.xpath(tree.getpath(d2)) == [d2])

##            find = etree.XPath("//rpIndName[contains(.,'Jennifer Schultz')]")
##            ##rpIndNames = target_root.findall(".//rpIndName")
##            rpIndNames = find(target_root)
##            for rpIndName in rpIndNames:
##                #print(rpIndName.text)
##                x_path = target_tree.getpath(rpIndName)
##                print(x_path)
##
##                rp_ind_name = rpIndName.xpath(x_path)[0]
##
##                #print(rp_ind_name.getparent().tag)
##                rp_ind_name.getparent().replace(rp_ind_name, rp_ind_name)
##
##                del x_path
##                del rpIndName
##            del rpIndNames
##            del find

##            original_xml = "<root><dc><batman alias='dark_knight' /></dc></root>"
##            modified_tag = "<batman alias='not_dark_knight' />"
##            x_path = '/root/dc/batman'
##            original_obj = etree.fromstring(original_xml)
##            modified_obj = etree.fromstring(modified_tag)
##            #original_obj.replace(original_obj.xpath(x_path)[0], modified_obj)
##            batman = original_obj.xpath(x_path)[0]
##            batman.getparent().replace(batman, modified_obj)

                #rpIndName.getparent().replace(contact_parent.xpath(target_tree_x_path)[0], contact_root)
                #contact_root_x_path = contact_root.getpath()
                #print(contact_root_x_path)

                #print(x_path)
                #print(etree.tostring(target_tree, pretty_print=True).decode())

                del target_tree_x_path


##                ancestors = []
##                for ancestor in contact_parent.iterancestors():
##                    if not ancestor.tag == "metadata":
##                        ancestors.append(ancestor.tag)
##                    del ancestor
##                ancestors_path = "./" + "/".join(list(reversed(ancestors))) + f"/{contact_parent.tag}"
##                #print(ancestors_path)
##                ancestors_xml = "<" + "><".join(list(reversed(ancestors)))  + ">" + f"<{contact_parent.tag>}"
##                print(ancestors_xml)
##
##                del ancestors_xml
                #target_root_child = target_root.find(ancestors_path)
                #print(etree.tostring(target_root_child, encoding='UTF-8', xml_declaration=True, pretty_print=True).decode())
                #print(etree.tostring(target_root_child, pretty_print=True).decode())
                #target_root.replace(target_root_child, contact_root)
                #del target_root_child
                #del ancestors_path
                #del ancestors
                del user
                del contact_parent, contact_root
                del rpIndName
            del contact_dict
            del rpIndNames
            num_elements += 1
        del UpdateRpCntInfos

        # Function parameters
        del target_tree, source_tree
        del target_root, source_root, target_xml_name

        # Imports
        del etree

    except:
        traceback.print_exc()
    else:
        return num_elements
    finally:
        del num_elements
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: raise Warning(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk

def main(project_folder=list()):
    try:
        # Imports
        from lxml import etree
        from arcpy import metadata as md
        from time import gmtime, localtime, strftime, time
        # Imports
        from src.project_tools import pretty_format_xml_file
        # Set a start time so that we can see how log things take
        start_time = time()
        print(f"{'-' * 80}")
        print(f"Python Script:  {os.path.basename(__file__)}")
        print(f"Location:       {os.path.dirname(__file__)}")
        print(f"Python Version: {sys.version} Environment: {os.path.basename(sys.exec_prefix)}")
        print(f"{'-' * 80}\n")

        from src.project_tools import pretty_format_xml_file

        target_xmls = [rf"{project_folder}\Export\{f}" for f in os.listdir(rf"{project_folder}\Export") if f.endswith(".xml")]
        #source_xml = rf"{project_folder}\species_range_boilerplate.xml"
        source_xml = rf"species_range_boilerplate.xml"
        pretty_format_xml_file(source_xml)

        warnings_and_errors = dict()

        # get and save item metadata
        for target_xml in target_xmls:
            target_xml_name = os.path.basename(target_xml)
            arcpy.AddMessage(f"Target Metadata: {target_xml_name}")
            #arcpy.AddMessage(f"Target Metadata: {target_xml}")
            source_md = md.Metadata(source_xml)
            source_xml_string = source_md.xml
            # create an ElementTree object from the metadata XML string
            source_tree = etree.ElementTree(etree.fromstring(source_xml_string))
            #source_tree = etree.fromstring(source_xml_string)
            source_root = source_tree.getroot()
            #del source_tree
            del source_md, source_xml_string

            # get the item's metadata xml
            target_md = md.Metadata(target_xml)
            target_xml_string = target_md.xml
            # create an ElementTree object from the metadata XML string
            target_tree = etree.ElementTree(etree.fromstring(target_xml_string))
            #target_tree = etree.fromstring(target_xml_string)
            target_root = target_tree.getroot()
            #print(target_root.tag)
            #del target_tree

            #print(etree.tostring(target_root, pretty_print=True).decode())
            #print(etree.tostring(source_root, pretty_print=True).decode())

            try:
                pass
                # call the update_metadata function to modify the item's metadata
                #changes = update_metadata(target_root, source_root, target_xml_name)
                changes = update_metadata(target_tree, source_tree, target_xml_name)
                #print(changes)
            except Warning as w:
                #changes = 0
                warnings_and_errors[target_xml_name] = w
                print(f"{w}"); del w
            except Exception as e:
                #changes = 0
                warnings_and_errors[target_xml_name] = e
                print(f"ERROR: {e}"); del e
            except:
                traceback.print_exc()

            if "changes" in locals().keys():
                if changes > 0:
                    # get modified XML
                    #updated_target_xml_string = etree.tostring(target_root, encoding='UTF-8')
                    updated_target_xml_string = etree.tostring(target_tree, encoding='UTF-8')

                    # import result back into metadata
                    arcpy.AddMessage("Saving updated metadata with the item...")
                    target_md.xml = updated_target_xml_string
                    target_md.save()
                    del updated_target_xml_string
                    pretty_format_xml_file(target_xml)

                    arcpy.AddMessage('Finished updating metadata for all source metadata items')

                else:
                    arcpy.AddMessage("No changes to save")
            else:
                pass
                #print("some thing is wong!")

            if "changes" in locals().keys(): del changes

            del target_tree, source_tree
            del target_root, source_root
            del target_md, target_xml_string
            del target_xml, target_xml_name

        del source_xml
        del project_folder
        del target_xmls

        PrintWarningsAndErrors = False
        if PrintWarningsAndErrors:
            if warnings_and_errors:
                for warnings_and_error in warnings_and_errors:
                    print(warnings_and_error, warnings_and_errors[warnings_and_error])
                    del warnings_and_error
        del PrintWarningsAndErrors

        del warnings_and_errors

        #try:
        #    pretty_format_xml_files()
        #except Exception as e:
        #    print(e)

        # Elapsed time
        end_time = time()
        elapse_time =  end_time - start_time
        print(f"\n{'-' * 80}")
        print(f"Python script: {os.path.basename(__file__)} successfully completed {strftime('%a %b %d %I:%M %p', localtime())}")
        print(u"Elapsed Time {0} (H:M:S)".format(strftime("%H:%M:%S", gmtime(elapse_time))))
        print(f"{'-' * 80}")
        del elapse_time, end_time, start_time
        del gmtime, localtime, strftime, time

        # Imports
        del md, etree, pretty_format_xml_file

    except:
        traceback.print_exc()
    else:
        return True
    finally:
        # Cleanup
        arcpy.management.ClearWorkspaceCache()
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: raise Warning(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk

if __name__ == '__main__':
    try:
        main(project_folder=rf"{os.path.dirname(os.path.dirname(__file__))}")
    except Warning as w:
        print(w)
