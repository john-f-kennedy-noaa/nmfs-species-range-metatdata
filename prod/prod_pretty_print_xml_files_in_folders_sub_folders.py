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
        from src.project_tools import pretty_format_xml_file

        arcpy.AddMessage("Pretty Print XMLs")
        xml_files = []

        arcpy.AddMessage("Walking directories for XML files")

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
            arcpy.AddMessage(f"\tProcessing {os.path.basename(xml_file)}")
            try:
                pretty_format_xml_file(xml_file)
            except Warning as w:
                print(f"{w} captured in the '{inspect.stack()[0][3]}' function")
            except Exception as e:
                print(f"{e} captured in the '{inspect.stack()[0][3]}' function")
            del xml_file
        del xml_files

        del walk

        arcpy.AddMessage("Pretty Print XMLs DONE")

        # Function variables
        del project_folder
        # Imports
        del pretty_format_xml_file

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
        project_folder = rf"{os.path.dirname(os.path.dirname(__file__))}"
        main(project_folder=project_folder)
    except Warning as w:
        print(w)

