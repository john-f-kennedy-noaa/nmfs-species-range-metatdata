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

def root_sort(target_xml=""):
    try:
        from lxml import etree

        parser = etree.XMLParser(remove_blank_text=True)
        # Parse the XML
        target_tree = etree.parse(target_xml, parser=parser)
        target_root = target_tree.getroot()
        del parser
        #etree.indent(tree, space="    ")
        # Pretty print
        target_xml_string = etree.tostring(target_tree, pretty_print=True, method='html', encoding="utf-8").decode()
        #print(target_xml_string)

        target_elements = target_root.getchildren()

        # JFK 1/17//2025 11:13 am ET set the dictionary to global and simplified
        # JFK 1/16/2025 5 pm ET created a function that uses a dictionary to find
        # a position for a given tag
        # JFK 1/16/2025 3 pm ET created a function that asigns a position to a tag
        # a position for a given tag
        def sort_function(element):
            try:
                global tag_position_dict

                if element.tag == "Esri":
                    return tag_position_dict["Esri"]
                if element.tag == "dataIdInfo":
                    return tag_position_dict["dataIdInfo"]
                if element.tag == "mdChar":     return tag_position_dict["mdChar"]
                if element.tag == "mdContact": return tag_position_dict["mdContact"]
                if element.tag == "mdDateSt": return tag_position_dict["mdDateSt"]
                if element.tag == "mdFileID": return tag_position_dict["mdFileID"]
                if element.tag == "mdLang": return tag_position_dict["mdLang"]
                if element.tag == "mdMaint": return tag_position_dict["mdMaint"]
                if element.tag == "mdHrLv": return tag_position_dict["mdHrLv"]
                if element.tag == "mdHrLvName": return tag_position_dict["mdHrLvName"]
                if element.tag == "refSysInfo": return tag_position_dict["refSysInfo"]
                if element.tag == "spatRepInfo": return tag_position_dict["spatRepInfo"]
                if element.tag == "spdoinfo": return tag_position_dict["spdoinfo"]
                if element.tag == "dqInfo": return tag_position_dict["dqInfo"]
                if element.tag == "dqScope": return tag_position_dict["dqScope"]
                if element.tag == "report":
                    if element.get("type") == "DQConcConsis":
                        return tag_position_dict["report"]["DQConcConsis"]
                    elif element.get("type") == "DQCompOm":
                        return tag_position_dict["report"]["DQCompOm"]
                if element.tag == "dataLineage":
                    return tag_position_dict["dataLineage"]
                if element.tag == "distInfo":
                    return tag_position_dict["distInfo"]
                if element.tag == "eainfo":
                    return tag_position_dict["eainfo"]

                #if element.tag in tag_position_dict:
                #    return tag_position_dict[element.tag]
                #else:
                #    print(f"WARNING!!! {element.tag} is missing from dictionary")

##                tag_position_dict = {
##                                     "dqScope": 0,
##                                     "report" : {"DQConcConsis" : 1, "DQCompOm" : 2},
##                                     "dataLineage" : 3,
##                                    }
##
##                #print(tag_position_dict["dqScope"])
##                #print(tag_position_dict["report"]["DQConcConsis"])
##                #print(tag_position_dict["report"]["DQCompOm"])
##                #print(tag_position_dict["dataLineage"])
##
##                if target_element.tag == "dqScope":
##                    return tag_position_dict["dqScope"]
##                if target_element.tag == "report":
##                    if target_element.get("type") == "DQConcConsis":
##                        return tag_position_dict["report"]["DQConcConsis"]
##                    elif target_element.get("type") == "DQCompOm":
##                        return tag_position_dict["report"]["DQCompOm"]
##                if target_element.tag == "dataLineage":
##                    return tag_position_dict["dataLineage"]
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

##        for target_element in target_elements:
##            print(f"{target_element.tag:<11} : {tag_position_dict[target_element.tag]}")
##            del target_element

        # Variables
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
        if rk: raise Warning(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        pass

def dqInfo_sort(target_xml=""):
    try:
        from lxml import etree

        parser = etree.XMLParser(remove_blank_text=True)
        # Parse the XML
        target_tree = etree.parse(target_xml, parser=parser)
        target_root = target_tree.getroot()
        del parser
        #etree.indent(tree, space="    ")
        # Pretty print
        target_xml_string = etree.tostring(target_tree, pretty_print=True, method='html', encoding="utf-8").decode()
        #print(target_xml_string)

        target_elements = target_tree.find("./dqInfo").getchildren()

        # JFK 1/16/2025 5 pm ET created a function that uses a dictionary to find
        # a position for a given tag
        # JFK 1/16/2025 3 pm ET created a function that asigns a position to a tag
        # a position for a given tag
        def sort_function(element):
            try:
                global tag_position_dict

                if element.tag == "Esri":
                    return tag_position_dict["Esri"]
                if element.tag == "dataIdInfo":
                    return tag_position_dict["dataIdInfo"]
                if element.tag == "mdChar":     return tag_position_dict["mdChar"]
                if element.tag == "mdContact": return tag_position_dict["mdContact"]
                if element.tag == "mdDateSt": return tag_position_dict["mdDateSt"]
                if element.tag == "mdFileID": return tag_position_dict["mdFileID"]
                if element.tag == "mdLang": return tag_position_dict["mdLang"]
                if element.tag == "mdMaint": return tag_position_dict["mdMaint"]
                if element.tag == "mdHrLv": return tag_position_dict["mdHrLv"]
                if element.tag == "mdHrLvName": return tag_position_dict["mdHrLvName"]
                if element.tag == "refSysInfo": return tag_position_dict["refSysInfo"]
                if element.tag == "spatRepInfo": return tag_position_dict["spatRepInfo"]
                if element.tag == "spdoinfo": return tag_position_dict["spdoinfo"]
                if element.tag == "dqInfo": return tag_position_dict["dqInfo"]
                if element.tag == "dqScope": return tag_position_dict["dqScope"]
                if element.tag == "report":
                    if element.get("type") == "DQConcConsis":
                        return tag_position_dict["report"]["DQConcConsis"]
                    elif element.get("type") == "DQCompOm":
                        return tag_position_dict["report"]["DQCompOm"]
                if element.tag == "dataLineage":
                    return tag_position_dict["dataLineage"]
                if element.tag == "distInfo":
                    return tag_position_dict["distInfo"]
                if element.tag == "eainfo":
                    return tag_position_dict["eainfo"]

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

        # Variables
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
        if rk: raise Warning(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        pass

def dataLineage_sort(target_xml=""):
    try:
        from lxml import etree

        parser = etree.XMLParser(remove_blank_text=True)
        # Parse the XML
        target_tree = etree.parse(target_xml, parser=parser)
        target_root = target_tree.getroot()
        del parser
        #etree.indent(tree, space="    ")
        # Pretty print
        target_xml_string = etree.tostring(target_tree, pretty_print=True, method='html', encoding="utf-8").decode()
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
                    if element.tag == "Esri":
                        return tag_position_dict["Esri"]
                    if element.tag == "dataIdInfo":
                        return tag_position_dict["dataIdInfo"]
                    if element.tag == "mdChar":     return tag_position_dict["mdChar"]
                    if element.tag == "mdContact": return tag_position_dict["mdContact"]
                    if element.tag == "mdDateSt": return tag_position_dict["mdDateSt"]
                    if element.tag == "mdFileID": return tag_position_dict["mdFileID"]
                    if element.tag == "mdLang": return tag_position_dict["mdLang"]
                    if element.tag == "mdMaint": return tag_position_dict["mdMaint"]
                    if element.tag == "mdHrLv": return tag_position_dict["mdHrLv"]
                    if element.tag == "mdHrLvName": return tag_position_dict["mdHrLvName"]
                    if element.tag == "refSysInfo": return tag_position_dict["refSysInfo"]
                    if element.tag == "spatRepInfo": return tag_position_dict["spatRepInfo"]
                    if element.tag == "spdoinfo": return tag_position_dict["spdoinfo"]
                    if element.tag == "dqInfo": return tag_position_dict["dqInfo"]
                    if element.tag == "dqScope": return tag_position_dict["dqScope"]
                    if element.tag == "report":
                        if element.get("type") == "DQConcConsis":
                            return tag_position_dict["report"]["DQConcConsis"]
                        elif element.get("type") == "DQCompOm":
                            return tag_position_dict["report"]["DQCompOm"]
                    if element.tag == "dataLineage":
                        return tag_position_dict["dataLineage"]
                    if element.tag == "statement":
                        return tag_position_dict["statement"]
                    if element.tag == "dataSource":
                        return tag_position_dict["dataSource"]
                    if element.tag == "prcStep":
                        print(element.getroottree().getpath(element))
                        return tag_position_dict["prcStep"]
                    if element.tag == "distInfo":
                        return tag_position_dict["distInfo"]
                    if element.tag == "eainfo":
                        return tag_position_dict["eainfo"]
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

        # Variables
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
        if rk: raise Warning(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
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

        target_xml = rf'{project_folder}\Export\WhaleBlue_20201014.xml'
        del project_folder

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
                             "refSysInfo"  : 10,
                             "spatRepInfo" : 11,
                             "spdoinfo"    : 12,
                             "dqInfo"      : 13,
                             "distInfo"    : 14,
                             "eainfo"      : 15,
                             "statement"   : 0,
                             "dataSource"  : 1,
                             "prcStep"     : 2,
                            }

        print(f"Processing XML File: '{os.path.basename(target_xml)}'")

        RootSort = False
        if RootSort:
            print("###--->>> Output for 'RootSort' <<<---###")
            root_sort(target_xml)
        else:
            pass
        del RootSort

        DqInfoSort = False
        if DqInfoSort:
            print("###--->>> Output for 'DqInfoSort' <<<---###")
            dqInfo_sort(target_xml)
        else:
            pass
        del DqInfoSort

        DataLineageSort = False
        if DataLineageSort:
            print("###--->>> Output for 'DataLineageSort' <<<---###")
            dataLineage_sort(target_xml)
        else:
            pass
        del DataLineageSort

        del tag_position_dict
        del target_xml

        # Imports

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

if __name__ == '__main__':
    try:
        main(project_folder=rf"{os.path.dirname(os.path.dirname(__file__))}")
    except Warning as w:
        print(w)
