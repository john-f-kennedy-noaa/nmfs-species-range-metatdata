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

def remove_duplicate_elements(root):
    seen = {}
    #for element in root.iter():
    for element in root.iterchildren():
        key = (element.tag, element.text, tuple(element.attrib.items()))
        if key in seen:
            element.getparent().remove(element)
        else:
            seen[key] = True
        del key, element
    del seen, root

def root_sort(target_xml=""):
    try:
        from lxml import objectify, etree

        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
        # Parse the XML
        target_tree = etree.parse(target_xml, parser=parser)
        target_root = target_tree.getroot()
        del parser
        #etree.indent(tree, space="    ")
        # Pretty print
        #target_xml_string = etree.tostring(target_tree, pretty_print=True, method='html', encoding='UTF-8').decode()
        #print(target_xml_string)

        global tag_position_dict
        # https://stackoverflow.com/questions/8385358/lxml-sorting-tag-order
        # lxml etree order children under parent
        #xml
        #etree.indent(xml, space="  ")
        #xml_string = etree.tostring(xml, pretty_print=True, method='html', encoding='UTF-8').decode()
        #print(xml_string)

        #doc = etree.XML(xml_string, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
        #for parent in target_tree.xpath('//*[./*]'): # Search for parent elements
        #    print(parent.tag)
            #parent[:] = sorted(parent,key=lambda x: tag_position_dict[x.tag])
        #etree.indent(target_tree, space="  ")
        #print(etree.tostring(doc, pretty_print=True))
        #print(etree.tostring(target_tree, pretty_print=True, method='html', encoding='UTF-8').decode())

        for parent in target_tree.xpath('//*[./*]'): # Search for parent elements
            if parent.tag in tag_position_dict:
                #print(parent.tag, tag_position_dict[parent.tag])
                # Get the second item element
                try:
                    print(f"'{parent.tag}'")
##                    #print(target_root.xpath(f"{parent.tag}"))
##                    #print(len(target_root.xpath(f"{parent.tag}")))
##                    #print(target_root.xpath(f"{parent.tag}"))
##                    #print(isinstance(target_root.xpath(f"{parent.tag}"), list))
##                    #print(type(target_root.xpath(f"{parent.tag}")))
##                    #if len(target_root.xpath(f"{parent.tag}")) > 0:
                    items = target_root.xpath(f".//{parent.tag}")
                    if items:
                        for item in items:
                            print(f"Item: {item.tag}")  # Access first item safely
                            print(f"Parent of Item: {item.getparent().tag}")
                            # Use getpath() to get the element path from the tree
                            element_get_path = target_tree.getpath(item)
                            #print(element_get_path)
                            elems = target_root.xpath(f"{element_get_path}")
                            for elem in elems:
                                print(f"new elements {elem} tag: {elem.tag} attrib: {elem.attrib} text: {elem.text}")
                                # Get the index of element within its parent (root)
                                #index_of_element = target_root.index(elem)
                                #print(f"Index of '{elem.tag}': {index_of_element}")  # Output: 1
                                #del index_of_element
                                # Use getpath() to get the element path from the tree
                                #element_get_path = target_tree.getpath(elem)
                                #print(element_get_path)
                                del elem
                            del element_get_path
                            del elems
                            del item
                    else:
                        print(f"No subitem found. items: {items} {parent.tag}")
                        elems = target_root.xpath(f".//{parent.tag}")
                        for elem in elems:
                            print(f"new elements {elem} tag: {elem.tag} attrib: {elem.attrib} text: {elem.text}")
                            del elem
                        del elems
                    del items
##                    parent_tag = target_root.xpath(f".//{parent.tag}")[0]
##                    # Get the index of element within its parent (root)
##                    index_of_parent_tag = target_root.index(parent_tag)
##                    print(f"Index of '{parent_tag.tag}': {index_of_parent_tag}")  # Output: 1
##                    del parent_tag, index_of_parent_tag
                except:
                    pass
##                    print(f"###--->>> '{parent.tag}' has an issue <<<---###")
##                    #print(f"'{parent.tag}'")
##                    #print(target_root.xpath(f"{parent.tag}"))
##                    #print(len(target_root.xpath(f"{parent.tag}")))
##                    # Use getpath() to get the element path from the tree
##                    element_get_path = target_tree.getpath(parent)
##                    print(f"{element_get_path}", flush=True)
##                    element_find_path = target_root.find(f".//{parent.tag}")[0]
##                    print(f"{element_find_path.tag}", flush=True)
##                    #element_x_path = target_tree.xpath(element_get_path.tag)
##                    #print(f"{element_x_path}", flush=True)
##                    #index_of_parent_tag = target_root.index(element_x_path)
##                    #print(f"Index of '{element_x_path.tag}': {index_of_parent_tag}")
##                    traceback.print_exc()



                    traceback.print_exc()
                    #print(target_root.index(parent))
                    #print(target_root.xpath(f"{parent.tag}"))
                    #print(len(target_root.xpath(f"{parent.tag}")))
                    #print(isinstance(target_root.xpath(f"{parent.tag}"), list))
                    #print(type(target_root.xpath(f"{parent.tag}")))

            del parent

##            else:
##                try:
##                    #print(f"'{parent.tag}'")
##                    #print(target_root.xpath(f"{parent.tag}"))
##                    #print(len(target_root.xpath(f"{parent.tag}")))
##                    #print(target_root.xpath(f"{parent.tag}"))
##                    #print(isinstance(target_root.xpath(f"{parent.tag}"), list))
##                    #print(type(target_root.xpath(f"{parent.tag}")))
##                    if len(target_root.xpath(f"{parent.tag}")) > 0:
##                        parent_tag = target_root.xpath(f"{parent.tag}")[0]
##                        # Get the index of element within its parent (root)
##                        index_of_parent_tag = target_root.index(parent_tag)
##                        print(f"Index of '{parent_tag.tag}': {index_of_parent_tag}")  # Output: 1
##                        del parent_tag, index_of_parent_tag
##                    else:
##                        print(f"'{parent.tag}'")
##                        print(target_root.find(f".//{parent.tag}"))
##                        print(target_root.xpath(f"{parent.tag}"))
##                        print(len(target_root.xpath(f"{parent.tag}")))
##                        print(target_root.index(parent))
##                except:
##                    pass
##                    #print(f"###--->>> '{parent.tag}' has an issue <<<---###")
##                    #print(f"'{parent.tag}'")
##                    #print(target_root.xpath(f"{parent.tag}"))
##                    #print(len(target_root.xpath(f"{parent.tag}")))
##                    #print(target_root.index(parent))



##        remove_duplicate_elements(target_root)
##
##        target_elements = target_root.getchildren()
##
##        # JFK 1/17//2025 11:13 am ET set the dictionary to global and simplified
##        # JFK 1/16/2025 5 pm ET created a function that uses a dictionary to find
##        # a position for a given tag
##        # JFK 1/16/2025 3 pm ET created a function that asigns a position to a tag
##        # a position for a given tag
##        def sort_function(element):
##            try:
##                global tag_position_dict
##
##                if element.tag not in tag_position_dict:
##                    print(f"{element.tag} is missing from dictionary")
##
##                # Root Position 0
##                if element.tag == "Esri":
##                    return tag_position_dict["Esri"]
##                # Root Position 1
##                if element.tag == "dataIdInfo":
##                    return tag_position_dict["dataIdInfo"]
##                # Root Position 2
##                if element.tag == "mdChar":
##                    return tag_position_dict["mdChar"]
##                # Root Position 3
##                if element.tag == "mdContact":
##                    return tag_position_dict["mdContact"]
##                # Root Position 4
##                if element.tag == "mdDateSt":
##                    return tag_position_dict["mdDateSt"]
##                # Root Position 5
##                if element.tag == "mdFileID":
##                    return tag_position_dict["mdFileID"]
##                # Root Position 6
##                if element.tag == "mdLang":
##                    return tag_position_dict["mdLang"]
##                # Root Position 7
##                if element.tag == "mdMaint":
##                    return tag_position_dict["mdMaint"]
##                # Root Position 8
##                if element.tag == "mdHrLv":
##                    return tag_position_dict["mdHrLv"]
##                # Root Position 9
##                if element.tag == "mdHrLvName":
##                    return tag_position_dict["mdHrLvName"]
##                # Root Position 10
##                if element.tag == "mdStanName":
##                    return tag_position_dict["mdStanName"]
##                # Root Position 11
##                if element.tag == "mdStanVer":
##                    return tag_position_dict["mdStanVer"]
##                # Root Position 12
##                if element.tag == "refSysInfo":
##                    return tag_position_dict["refSysInfo"]
##                # Root Position 13
##                if element.tag == "spatRepInfo":
##                    return tag_position_dict["spatRepInfo"]
##                # Root Position 14
##                if element.tag == "spdoinfo":
##                    return tag_position_dict["spdoinfo"]
##                # Root Position 15
##                if element.tag == "dqInfo":
##                    return tag_position_dict["dqInfo"]
##                # dqInfo Position 0
##                if element.tag == "dqScope":
##                    return tag_position_dict["dqScope"]
##                # dqInfo Position 1 & 2
##                if element.tag == "report":
##                    if element.get("type") == "DQConcConsis":
##                        return tag_position_dict["report"]["DQConcConsis"]
##                    elif element.get("type") == "DQCompOm":
##                        return tag_position_dict["report"]["DQCompOm"]
##                # dqInfo Position 3
##                if element.tag == "dataLineage":
##                    return tag_position_dict["dataLineage"]
##                # dataLineage Position 0
##                if element.tag == "statement":
##                    return tag_position_dict["statement"]
##                # dataLineage Position 1
##                if element.tag == "dataSource":
##                    return tag_position_dict["dataSource"]
##                # dataLineage Position ?
##                if element.tag == "prcStep":
##                    return tag_position_dict["prcStep"]
##                # Root Position 16
##                if element.tag == "distInfo":
##                    return tag_position_dict["distInfo"]
##                # Root Position 17
##                if element.tag == "eainfo":
##                    return tag_position_dict["eainfo"]
##                # Root Position 18
##                if element.tag == "Binary":
##                    return tag_position_dict["Binary"]
##                # Binary Position 0
##                if element.tag == "Thumbnail":
##                    return tag_position_dict["Thumbnail"]
##
##            except:
##                traceback.print_exc()
##            else:
##                pass
##            finally:
##                pass
##
##        #print([t.tag for t in target_elements])

##        target_elements[:] = sorted(target_elements, key=sort_function)
##
##        for target_element in target_elements:
##            #print(target_element.tag)
##            print(f"{target_element.tag:<11} : {tag_position_dict[target_element.tag]}")
##            del target_element

##        del sort_function

##        canvas = objectify.fromstring('''
##            <canvas>
##              <shape name="a" />
##              <shape name="b" />
##              <shape name="c" />
##            </canvas>
##        ''')
##
##        canvas.shape = [canvas.shape[1], canvas.shape[0], canvas.shape[2]]
##
##        print(etree.tostring(canvas, pretty_print=True))

        target_xml_string = etree.tostring(target_tree, pretty_print=True, method='html', encoding='UTF-8').decode()
        #print(target_xml_string)

##        with open(target_xml, "w") as f:
##            f.write(target_xml_string)
##        del f

        # Declared Variables
        #del target_elements
        del target_xml_string, target_tree, target_root

        # Imports
        del etree, objectify
        # Function parameters
        del target_xml

    except:
        traceback.print_exc()
    else:
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        pass

def dqInfo_sort(target_xml=""):
    try:
        from lxml import etree

        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
        # Parse the XML
        target_tree = etree.parse(target_xml, parser=parser)
        target_root = target_tree.getroot()
        del parser
        #etree.indent(tree, space="    ")
        # Pretty print
        target_xml_string = etree.tostring(target_tree, pretty_print=True, method='html', encoding='UTF-8').decode()
        #print(target_xml_string)

        target_elements = target_tree.find("./dqInfo").getchildren()

        # JFK 1/16/2025 5 pm ET created a function that uses a dictionary to find
        # a position for a given tag
        # JFK 1/16/2025 3 pm ET created a function that asigns a position to a tag
        # a position for a given tag
        def sort_function(element):
            try:
                global tag_position_dict

                if element.tag == "Esri"        : return tag_position_dict["Esri"]
                if element.tag == "dataIdInfo"  : return tag_position_dict["dataIdInfo"]
                if element.tag == "mdChar"      : return tag_position_dict["mdChar"]
                if element.tag == "mdContact"   : return tag_position_dict["mdContact"]
                if element.tag == "mdDateSt"    : return tag_position_dict["mdDateSt"]
                if element.tag == "mdFileID"    : return tag_position_dict["mdFileID"]
                if element.tag == "mdLang"      : return tag_position_dict["mdLang"]
                if element.tag == "mdMaint"     : return tag_position_dict["mdMaint"]
                if element.tag == "mdHrLv"      : return tag_position_dict["mdHrLv"]
                if element.tag == "mdHrLvName"  : return tag_position_dict["mdHrLvName"]
                if element.tag == "refSysInfo"  : return tag_position_dict["refSysInfo"]
                if element.tag == "spatRepInfo" : return tag_position_dict["spatRepInfo"]
                if element.tag == "spdoinfo"    : return tag_position_dict["spdoinfo"]
                if element.tag == "dqInfo"      : return tag_position_dict["dqInfo"]
                if element.tag == "dqScope"     : return tag_position_dict["dqScope"]
                if element.tag == "report":
                    if element.get("type") == "DQConcConsis":
                        return tag_position_dict["report"]["DQConcConsis"]
                    elif element.get("type") == "DQCompOm":
                        return tag_position_dict["report"]["DQCompOm"]
                if element.tag == "dataLineage" : return tag_position_dict["dataLineage"]
                if element.tag == "statement"   : return tag_position_dict["statement"]
                if element.tag == "dataSource"  : return tag_position_dict["dataSource"]
                if element.tag == "prcStep"     : return tag_position_dict["prcStep"]
                if element.tag == "distInfo"    : return tag_position_dict["distInfo"]
                if element.tag == "eainfo"      : return tag_position_dict["eainfo"]

            except:
                traceback.print_exc()
            else:
                del tag_position_dict
            finally:
                pass

        target_elements[:] = sorted(target_elements, key=sort_function)

        for target_element in target_elements:
            #print(target_element.tag)
            print(f"{target_element.tag:<11} : {tag_position_dict[target_element.tag]}")
            del target_element

        del sort_function

        # Declared Variables
        del target_elements
        del target_xml_string, target_tree, target_root

        # Imports
        del etree
        # Function parameters
        del target_xml

    except:
        traceback.print_exc()
    else:
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        pass

def dataLineage_sort(target_xml=""):
    try:
        from lxml import etree

        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
        # Parse the XML
        target_tree = etree.parse(target_xml, parser=parser)
        target_root = target_tree.getroot()
        del parser
        #etree.indent(tree, space="    ")
        # Pretty print
        target_xml_string = etree.tostring(target_tree, pretty_print=True, method='html', encoding='UTF-8').decode()
        #print(target_xml_string)

        target_elements = target_root.find(".//dataLineage").getchildren()

        # JFK 1/17//2025 11:13 am ET set the dictionary to global and simplified
        # JFK 1/16/2025 5 pm ET created a function that uses a dictionary to find
        # a position for a given tag
        # JFK 1/16/2025 3 pm ET created a function that asigns a position to a tag
        # a position for a given tag
        def sort_function(element):
            try:
                global tag_position_dict

                if element.tag in tag_position_dict:
                    if element.tag == "Esri"        : return tag_position_dict["Esri"]
                    if element.tag == "dataIdInfo"  : return tag_position_dict["dataIdInfo"]
                    if element.tag == "mdChar"      : return tag_position_dict["mdChar"]
                    if element.tag == "mdContact"   : return tag_position_dict["mdContact"]
                    if element.tag == "mdDateSt"    : return tag_position_dict["mdDateSt"]
                    if element.tag == "mdFileID"    : return tag_position_dict["mdFileID"]
                    if element.tag == "mdLang"      : return tag_position_dict["mdLang"]
                    if element.tag == "mdMaint"     : return tag_position_dict["mdMaint"]
                    if element.tag == "mdHrLv"      : return tag_position_dict["mdHrLv"]
                    if element.tag == "mdHrLvName"  : return tag_position_dict["mdHrLvName"]
                    if element.tag == "refSysInfo"  : return tag_position_dict["refSysInfo"]
                    if element.tag == "spatRepInfo" : return tag_position_dict["spatRepInfo"]
                    if element.tag == "spdoinfo"    : return tag_position_dict["spdoinfo"]
                    if element.tag == "dqInfo"      : return tag_position_dict["dqInfo"]
                    if element.tag == "dqScope"     : return tag_position_dict["dqScope"]
                    if element.tag == "report":
                        if element.get("type") == "DQConcConsis":
                            return tag_position_dict["report"]["DQConcConsis"]
                        elif element.get("type") == "DQCompOm":
                            return tag_position_dict["report"]["DQCompOm"]
                    if element.tag == "dataLineage" : return tag_position_dict["dataLineage"]
                    if element.tag == "statement"   : return tag_position_dict["statement"]
                    if element.tag == "dataSource"  : return tag_position_dict["dataSource"]
                    if element.tag == "prcStep"     : return tag_position_dict["prcStep"]
                    if element.tag == "distInfo"    : return tag_position_dict["distInfo"]
                    if element.tag == "eainfo"      : return tag_position_dict["eainfo"]
                else:
                    raise Exception(f"###--->>> '{element.tag}' not in tag_position_dict <<<---###")
            except Exception as e:
                print(e)
                #raise Exception(e)
            except:
                traceback.print_exc()
            else:
                del tag_position_dict
            finally:
                pass

        #target_elements[:] = sorted(target_elements, key=sort_function)

        for target_element in target_elements:
            print(target_element.tag)
            #print(f"{target_element.tag:<11} : {tag_position_dict[target_element.tag]}")
            del target_element

        del sort_function

        # Declared Variables
        del target_elements
        del target_xml_string, target_tree, target_root

        # Imports
        del etree
        # Function parameters
        del target_xml

    except Exception as e:
        pass #print(e)
    except:
        traceback.print_exc()
    else:
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__')]
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

        from src.project_tools import pretty_format_xml_file

        global tag_position_dict

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

        target_xmls = [rf"{project_folder}\Export\{f}" for f in os.listdir(rf"{project_folder}\Export") if f.endswith(".xml")]

        # get and save item metadata
        for target_xml in target_xmls:
            target_xml_name = os.path.basename(target_xml)
            print(f"Target Metadata: {target_xml_name}",flush=True)

            print(f"Processing XML File: '{os.path.basename(target_xml)}'",flush=True)

            RootSort = True
            if RootSort:
                print("###--->>> Output for 'RootSort' <<<---###",flush=True)
                root_sort(target_xml)
            else:
                pass
            del RootSort

    ##        DqInfoSort = False
    ##        if DqInfoSort:
    ##            print("###--->>> Output for 'DqInfoSort' <<<---###")
    ##            dqInfo_sort(target_xml)
    ##        else:
    ##            pass
    ##        del DqInfoSort
    ##
    ##        DataLineageSort = False
    ##        if DataLineageSort:
    ##            print("###--->>> Output for 'DataLineageSort' <<<---###")
    ##            dataLineage_sort(target_xml)
    ##        else:
    ##            pass
    ##        del DataLineageSort

            pretty_format_xml_file(target_xml)

            del target_xml, target_xml_name

        # Declared Variables
        del tag_position_dict
        del target_xmls
        del project_folder

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

    #except Warning as w:
    #    print(w)
    except:
        traceback.print_exc()
    else:
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: raise Warning(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        pass

if __name__ == '__main__':
    try:
        main(project_folder=rf"{os.path.dirname(os.path.dirname(__file__))}")
    except Warning as w:
        print(w)
