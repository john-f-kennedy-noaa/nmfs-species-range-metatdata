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

def getSortValue(elem):
    from lxml import etree
    if isinstance(elem, etree._Comment):
        # sort comment by its content
        return elem.text
    else:
        # sort entities by tag and then by name
        #return elem.tag + elem.attrib.get('name','')
        return elem.tag

def main(project_folder=""):
    try:
        # https://stackoverflow.com/questions/78713666/find-the-index-of-a-child-in-lxml

        from lxml import etree

        target_xml = rf'{project_folder}\Export\WhaleBlue_20201014.xml'
        del project_folder

        # Parse the XML
        tree = etree.parse(target_xml)
        root = tree.getroot()

        for parent in tree.xpath('//*[./*]'): # Search for parent elements
            parent[:] = sorted(parent, key=lambda x: getSortValue(x))
            del parent

        # https://lxml.de/apidoc/lxml.etree.html#lxml.etree.indent
        # import lxml.etree as ET
        # ET.indent(tree, space='    ')  # clean all indentations - use 4 spaces
        # ET.indent(tree, space='....')  # clean all indentations - use 4 dots - looks like TOC (Table Of Contents) in book :)
        # ET.indent(tree)   # clean all indentations - use (default) 2 spaces

        #etree.indent(tree, space='    ')
        #print(etree.tostring(tree, pretty_print=True, method='html', encoding='UTF-8').decode())

        #etree.indent(root, space='    ')
        #etree.dump(root)

        xml_string = etree.tostring(tree, pretty_print=True, method='html', encoding='UTF-8').decode()

        try:
            with open(target_xml, "w") as f:
                f.write(xml_string)
            del f
        except:
            arcpy.AddError(f"The metadata file: {os.path.basename(xml)} can not be overwritten!!")

        del xml_string


        #with open(filename_out,"wb") as file:
        #    file.write(etree.tostring(doc, pretty_print=True))

        del tree, root

        # Variables
        del target_xml

        # Imports
        del etree

    except:
        traceback.print_exc()
    else:
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: raise Warning(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
    finally:
        pass
        # Cleanup
        # arcpy.management.ClearWorkspaceCache()

if __name__ == '__main__':
    try:
        main(project_folder=rf"{os.path.dirname(os.path.dirname(__file__))}")
    except Warning as w:
        print(w)
