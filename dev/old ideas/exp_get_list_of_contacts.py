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

        #target_xml = rf'{project_folder}\Export\WhaleBlue_20201014.xml'
        #del project_folder

        target_xmls = [rf"{project_folder}\Export\{f}" for f in os.listdir(rf"{project_folder}\Export") if f.endswith(".xml")]

        # get and save item metadata
        for target_xml in target_xmls:

            def contact_search(target_xml, search_element="", search_term=""):
                try:
                    from lxml import etree
                    target_xml_name = os.path.basename(target_xml)
                    print(f"Target Metadata: {target_xml_name}", flush=True)
                    del target_xml_name

                    parser = etree.XMLParser(remove_blank_text=True)
                    # Parse the XML
                    target_tree = etree.parse(target_xml, parser=parser)
                    target_root = target_tree.getroot()
                    del parser
                    #etree.indent(tree, space="    ")
                    # Pretty print
                    #target_xml_string = etree.tostring(target_tree, pretty_print=True, method='html', encoding="utf-8").decode()
                    #print(target_xml_string,flush=True); del target_xml_string

                    if search_term:
                        #find = etree.XPath("//rpIndName[contains(.,'Jennifer Schultz')]")
                        find = etree.XPath(f"//{search_element}[contains(.,'{search_term}')]")
                    else:
                        find = etree.XPath(f".//{search_element}")

                    elements = find(target_root)

                    if "find" in locals().keys(): del find

                    for element in elements:
                        #print(element.tag)

                        if search_element == "rpIndName":
                            contact = element.getparent()
                        elif search_element == "eMailAdd":
                            contact = element.getparent().getparent().getparent()

                        print(f"\t{contact.tag}")
                        rpIndName = contact.find("./rpIndName")
                        user = rpIndName.text
                        print(f"\t{user}")
                        #print(f"\t\t{rpIndName.getroottree().getpath(rpIndName)}")
                        email = contact.find(".//eMailAdd").text
                        print(email)


                        descendants = contact.iterdescendants()
                        for descendant in descendants:

                            if descendant.text:
                                #print(f"\t\t{descendant.getroottree().getpath(descendant)}")
                                print(f"\t\t\t{descendant.tag} {descendant.text}")
                            if descendant.attrib:
                                #print(f"\t\t{descendant.getroottree().getpath(descendant)}")
                                print(f"\t\t\t{descendant.tag} {descendant.attrib}")
                            del descendant


                        if "contact" in locals().keys(): del contact
                        if "user" in locals().keys(): del user
                        if "rpIndName" in locals().keys(): del rpIndName

##
##                        # Iterate over all descendants of the root element
##                        for element in rpIndName.getparent().iterdescendants():
##                            #print(f"\t\t{element.getroottree().getpath(element)}")
##                            if element.text:
##                                print(f"\t\t\t{element.tag} {element.text}")
##                            if element.attrib:
##                                print(f"\t\t\t{element.tag} {element.attrib}")
##                            del element
##
##                        del user
##                        del rpIndName

                    # Variables
                    del elements
                    del target_tree, target_root
                    # Imports
                    del etree
                    # Function parameters
                    del target_xml, search_element, search_term

                except:
                    traceback.print_exc()
                else:
                    # While in development, leave here. For test, move to finally
                    #rk = [key for key in locals().keys() if not key.startswith('__')]
                    #if rk: raise Warning(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
                    return True
                finally:
                    pass

            #search_element = "rpIndName"
            search_element = "eMailAdd"
            search_term    = ""

            #contact_list = contact_search(target_xml, search_element, search_term)
            #del search_element, search_term, contact_search
            #del contact_list

            contact_search(target_xml, search_element=search_element, search_term=search_term)

            del search_element, search_term, contact_search

            #target_elements = target_tree.findall(".//rpIndName")
            #for target_element in target_elements:
            #    print(f"\t{target_element.getroottree().getpath(target_element)}")
            #    del target_element
            #CompleteTree = False
            #if CompleteTree:
            #    for element in target_tree.iter(): print(element.getroottree().getpath(element)); del element
            #else:
            #    pass
            #del CompleteTree

            # get xml path example
            # from lxml import etree
            # xml = '''<test><a/><b><i/><ii/></b></test>'''
            # tree = etree.fromstring(xml)
            # for element in tree.iter(): print(element.getroottree().getpath(element))
            # del xml, tree, element

            # Pretty Format
            #pretty_format_xml_file(target_xml)

            del target_xml

        # Variables
        del project_folder, target_xmls

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