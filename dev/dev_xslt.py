#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john.f.kennedy
#
# Created:     22/12/2024
# Copyright:   (c) john.f.kennedy 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Python Built-in's modules are loaded first
import os, sys
import traceback
import inspect

# Third-party modules are loaded second
import arcpy

# Append the location of this scrip to the System Path
sys.path.append(os.path.dirname(__file__))

def main():
    try:
        # Imports
        from lxml import etree
        from arcpy import metadata as md
        from io import StringIO

        project_folder = r"{os.environ['USERPROFILE']}\Documents\ArcGIS\Projects\National Mapper"

        arcpy.env.workspace = rf"{project_folder}\National Mapper.gdb"

        #for fc in arcpy.ListFeatureClasses():
        #    if fc == "AbaloneBlack_20210712"

        #set local variables
        #dir = arcpy.GetInstallInfo("desktop")["InstallDir"]
        #xslt = rf"{project_folder}\Metadata\Stylesheets\gpTools\generate metadata template.xslt"
        xslt = r"{os.environ['USERPROFILE']}\Documents\ArcGIS\Projects\ArcGIS-XML-to-InPort-XML\ArcGIS2InPort.xsl"

        dataset_md = md.Metadata("AbaloneBlack_20210712")

        metadata_xml_string = dataset_md.xml

        # Parse the XML file
        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)

        dataset_tree = etree.parse(StringIO(metadata_xml_string), parser=parser)
        xslt_tree    = etree.parse(xslt, parser=parser)

        del parser
        del metadata_xml_string

        # Get the root element
        dataset_root = dataset_tree.getroot()
        xslt_root    = xslt_tree.getroot()

        transform = etree.XSLT(xslt_root)

        result = transform(dataset_root)

        #print(bytes(result))

        etree.indent(result, space="    ")

        # Pretty print
        xml_string = etree.tostring(result, encoding='UTF-8',  method='xml', pretty_print=True).decode()

        # Write the pretty XML to a file
        with open(rf"{project_folder}\xlst_test.xml", "w") as f:
            f.write(xml_string)

        del f
        del xml_string

        del transform
        del result
        del dataset_md

        del dataset_tree, xslt_tree, dataset_root, xslt_root

##
##        # Imports
##        del etree
##        # Function parameters
##        del xml


        # Variables created in function
        del project_folder, xslt

        # Imports
        del etree, md, StringIO

    except:
        traceback.print_exc()
    else:
        try:
            remaining_keys = [key for key in locals().keys() if not key.startswith('__')]
            if remaining_keys:
                arcpy.AddWarning(f"Remaining Keys in '{inspect.stack()[0][3]}': ##--> '{', '.join(remaining_keys)}' <--## Line Number: {traceback.extract_stack()[-1].lineno}")
            else:
                pass
            del remaining_keys
        except:
            traceback.print_exc()
    finally:
        pass


if __name__ == '__main__':
    main()
