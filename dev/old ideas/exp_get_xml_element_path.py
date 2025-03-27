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
        if rk: raise Warning(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return num_elements
    finally:
        del num_elements

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
        from lxml import etree
        from src.project_tools import pretty_format_xml_file

        target_xml = rf'{project_folder}\Export\WhaleBlue_20201014.xml'
        del project_folder

        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
        # Parse the XML
        target_tree = etree.parse(target_xml, parser=parser)
        target_root = target_tree.getroot()
        del parser
        #etree.indent(tree, space="    ")
        # Pretty print
        #target_xml_string = etree.tostring(target_tree, pretty_print=True, method='html', encoding='UTF-8').decode()
        #print(target_xml_string); del target_xml_string

        target_elements = target_tree.find("./dqInfo").getchildren()

        for target_element in target_elements:
            print(target_element.getroottree().getpath(target_element))
            del target_element

        CompleteTree = True
        if CompleteTree:
            for element in target_tree.iter(): print(element.getroottree().getpath(element)); del element
        else:
            pass
        del CompleteTree

        # get xml path example
        # from lxml import etree
        # xml = '''<test><a/><b><i/><ii/></b></test>'''
        # tree = etree.fromstring(xml)
        # for element in tree.iter(): print(element.getroottree().getpath(element))
        # del xml, tree, element

        # Pretty Format
        pretty_format_xml_file(target_xml)

        # Declared Variables
        del target_elements
        del target_xml, target_tree, target_root

        # Imports
        del etree, pretty_format_xml_file

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