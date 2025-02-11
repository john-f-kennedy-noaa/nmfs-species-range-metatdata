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

def contact_search_dictionary(target_xml_name, target_tree, search_expression):
    try:
        print(f"\tProcessing: {target_xml_name}")

        tag_text_dict = {}

        if target_tree.xpath(search_expression):
            record_count = 0
            for elem in target_tree.xpath(search_expression):
                parent = elem.getparent()
                rpIndNames = parent.findall("./rpIndName")
                for rpIndName in rpIndNames:
                    #tag_text_dict[target_xml_name][record_count] = {rpIndName : {}}
                    remove_duplicate_elements(rpIndName)
                    #print(f"\tFile: '{target_xml_name}' Record: '{record_count}' Parent: '{parent.tag}' Name: '{rpIndName}'")

                    #tag_text_dict[target_xml_name] = {record_count : {parent.tag : {rpIndName : {}}}}

                    parent_tag = parent.tag
                    user = rpIndName.text
                    tag_text_dict = {record_count : {target_xml_name : {parent_tag : {user :{}}}}}

                    descendants = parent.iterdescendants()

                    for descendant in descendants:
                        if descendant.text:
                            #print(f"\t\t{descendant.getroottree().getpath(descendant)} : {descendant.text}")
                            #print(f"\t\t{descendant.tag} : {descendant.text}")
                            #tag_text_dict[target_xml_name][record_count][parent.tag][rpIndName][descendant.tag] = descendant.text
                            #print(f"\tFile: '{target_xml_name}' Record: '{record_count}' Parent: '{parent.tag}' Name: '{rpIndName}' Descendant: '{descendant.tag}' Text: '{descendant.text}'")
                            #tag_text_dict[target_xml_name][record_count][parent.tag][rpIndName] = {descendant.tag : descendant.text}
                            #tag_text_dict[target_xml_name][record_count][parent.tag][rpIndName][descendant.tag] = descendant.text
                            #descendant_dict[target_xml_name][record_count][parent_tag][user][descendant.tag] = descendant.text
                            tag_text_dict[record_count][target_xml_name][parent_tag][user][descendant.tag] = descendant.text
                        del descendant
                    del descendants
                    del parent_tag
                    del user
                    del rpIndName

                # Variables
                del rpIndNames
                del parent
                del elem

##                for record_number in tag_text_dict:
##                    print(f"\t\tRecord Number: {record_number}")
##                    for xml_name in tag_text_dict[record_number]:
##                        print(f"\t\t\tXML Name: {xml_name}")
##                        for parent_tag in tag_text_dict[record_number][xml_name]:
##                            print(f"\t\t\t\tTag: {parent_tag}")
##                            for user in tag_text_dict[record_number][xml_name][parent_tag]:
##                                print(f"\t\t\t\t\tUser: {user}")
##                                for descendant in tag_text_dict[record_number][xml_name][parent_tag][user]:
##                                    print(f"\t\t\t\t\t\tElem: {descendant:<12} : {tag_text_dict[record_number][xml_name][parent_tag][user][descendant]}")
##                                    del descendant
##                                del user
##                            del parent_tag
##                        del record_number
##                    del xml_name

                record_count+=1
            del record_count
        else:
            print("something is wrong in not search_term")

        del target_xml_name

        # print(f"\tFile: '{target_xml_name}' Record: '{record_count}' Parent: '{parent.tag}' Name: '{rpIndName}' Descendant: '{descendant.tag}' Text: '{descendant.text}'")

        ReportTagTextDict = False
        if ReportTagTextDict:
            for target_xml_name in tag_text_dict:
                print(f"\tXML File Name: '{target_xml_name}'")
                for record_number in tag_text_dict[target_xml_name]:
                    print(f"\t\tRecord Number {record_number}")
                    for parent_tag in tag_text_dict[target_xml_name][record_number]:
                        print(f"\t\t\tParent: {parent_tag}")
                        for user in tag_text_dict[target_xml_name][record_number][parent_tag]:
                            print(f"\t\t\tContact: {user}")
                            for descendant in tag_text_dict[target_xml_name][record_number][parent_tag][user]:
                                print(f"\t\t\t\tElement: '{descendant}' : '{tag_text_dict[target_xml_name][record_number][parent_tag][user][descendant]}'")
                                del descendant
                            del user
                        del parent_tag
                    del record_number
                del target_xml_name
##            for target_xml_name in tag_text_dict:
##                print(f"\t\tXML File Name: {target_xml_name}")
##                for record_number in tag_text_dict[target_xml_name]:
##                    print(f"\t\t\tRecord Number: {record_number}")
##                    for parent_tag in tag_text_dict[target_xml_name][record_number]:
##                        print(f"\t\t\t\tTag: {parent_tag}")
##                        for user in tag_text_dict[target_xml_name][record_number][parent_tag]:
##                            print(f"\t\t\t\t\tUser: {user}")
##                            for descendant in tag_text_dict[target_xml_name][record_number][parent_tag][user]:
##                                print(f"\t\t\t\t\t\tElem: {descendant:<12} : {descendant_dict[target_xml_name][record_number][parent_tag][user][descendant]}")
##                                del descendant
##                            del user
##                        del parent_tag
##                    del record_number
##                del target_xml_name
        del ReportTagTextDict

        #del tag_text_dict

        # Function parameters
        del target_tree, search_expression

    except Warning as w:
        print(w)
    except:
        traceback.print_exc()
    else:
        rk = [key for key in locals().keys() if not key.startswith('__') and key not in ["tag_text_dict"]]
        if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return tag_text_dict
    finally:
        if "tag_text_dict" in locals().keys(): del tag_text_dict

def contact_search(target_xml, search_element="", search_term=""):
    try:
        from lxml import etree
        target_xml_name = os.path.basename(target_xml)
        print(f"Target Metadata: {target_xml_name}", flush=True)
        #del target_xml_name

        parser = etree.XMLParser(remove_blank_text=True)
        # Parse the XML
        target_tree = etree.parse(target_xml, parser=parser)
        target_root = target_tree.getroot()
        del parser
        #etree.indent(tree, space="    ")
        # Pretty print
        #target_xml_string = etree.tostring(target_tree, pretty_print=True, method='html', encoding="utf-8").decode()
        #print(target_xml_string,flush=True); del target_xml_string
        #foos = tree.xpath('.//ancestor::foo[bar[@attr="val"] and position() = 1]')
        #foos = tree.xpath('.//ancestor::foo[bar[@attr="val"]][1]')
        #for foo in foos:
        #    print(foo.attrib)

        if search_element in ["extermal", "editorDigest", "rpIndName", "rpOrgName", "rpPosName", "rpCntInfo", "displayName", "editorSave"]:
            if not search_term:
                search_expression = f".//{search_element}"
            elif search_term:
                #search_expression = f".//{search_element}[text()='{search_term}']"
                search_expression = f".//{search_element}[contains(.,'{search_term}')]"
            else:
                print(f"something is wrong in '{search_element}'")

        elif search_element in ["eMailAdd"]:
            if not search_term:
                search_expression = f".//rpCntInfo"
            elif search_term:
                #search_expression = f".//rpCntInfo[text()='{search_term}']"
                search_expression = f".//rpCntInfo[contains(.,'{search_term}')]"
        else:
            print(f"something is wrong in '{rpCntInfo}'")

        if "parent" in locals().keys(): del parent

        ContactSearchReport = False
        if ContactSearchReport:
            contact_search_report(target_tree, search_expression)
        del ContactSearchReport

        ContactSearchDictionary = True
        if ContactSearchDictionary:
            contract_dict = dict()
            try:
                tag_text_dict = contact_search_dictionary(target_xml_name, target_tree, search_expression)
                #contract_dict[target_xml_name] = tag_text_dict[target_xml_name]
                del tag_text_dict
            except:
                raise Exception

            ContractDictReport = False
            if ContractDictReport:
                for xml_name in contract_dict:
                    print(f"\tFile Name: {xml_name}")
                    #print(xml_name, contract_dict[xml_name])
                    # tag_text_dict[target_xml_name][record_count][rpIndName][child.tag]
                    for record_count in contract_dict[xml_name]:
                        print(f"\t\tRecord Number: {record_count}")
                        for user in contract_dict[xml_name][record_count]:
                            print(f"\t\t\tContact: {user}")
                            elems = contract_dict[xml_name][record_count][user]
                            for elem in elems:
                                print(f"\t\t\t\t{elem} : {elems[elem]}")
                                del elem
                            del elems
                            del user
                        del record_count
                    del xml_name
            del ContractDictReport

            del contract_dict
        del ContactSearchDictionary

        del search_expression

        # Variables
        #del elements
        del target_tree, target_root
        del target_xml_name
        # Imports
        del etree
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
            # Pretty Format
            #pretty_format_xml_file(target_xml)

            del target_xml

        # Variables
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