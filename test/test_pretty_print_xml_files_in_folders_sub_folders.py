#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john.f.kennedy
#
# Created:     05/01/2025
# Copyright:   (c) john.f.kennedy 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Python Built-in's modules are loaded first
import os, sys
import traceback
import inspect

# Third-party modules are loaded second
import arcpy

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

def main(project_folder=str()):
    try:
        # Imports
        from src.project_tools import parse_xml_file_format_and_save
        print("Pretty Print XMLs")
        xml_files = []

        print("Walking directories for XML files")

        walk = os.walk(project_folder)

        for dirpath, dirnames, filenames in walk:
            for filename in filenames:
                if (filename.endswith(".xml") or filename.endswith(".sddraft")) and os.path.basename(filename) not in ["metadata outline.xml"]:
                    xml_files.append(os.path.join(dirpath, filename))
                else:
                    pass
                del filename
            del dirpath, dirnames, filenames

        for xml_file in xml_files:
            print(f"\tProcessing {os.path.basename(xml_file)}")
            try:
                #pretty_format_xml_file(xml_file)
                parse_xml_file_format_and_save(xml_file)
            except Warning as w:
                print(f"{w} captured in the '{inspect.stack()[0][3]}' function")
            except Exception as e:
                print(f"{e} captured in the '{inspect.stack()[0][3]}' function")
            del xml_file
        del xml_files

        del walk

        print("Pretty Print XMLs DONE")

        # Function variables
        del project_folder
        # Imports
        del parse_xml_file_format_and_save

    except:
        traceback.print_exc()
        raise Exception(f"In function: '{inspect.stack()[0][3]}'")
    else:
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        # Cleanup
        arcpy.management.ClearWorkspaceCache()

if __name__ == '__main__':
    try:
        #project_folder = rf"{os.path.dirname(os.path.dirname(__file__))}"
        #project_folder = rf"{os.environ['USERPROFILE']}\Documents\ArcGIS\Projects\DisMap\ArcGIS-Analysis-Python"
        project_folder = rf"{os.environ['USERPROFILE']}\Documents\ArcGIS\Projects\ArcPy Studies\XML\nmfs-species-range-metatdata"
        main(project_folder=project_folder)
    except Warning as w:
        print(w)

