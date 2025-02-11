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

def main(project_folder=str(), project=str()):
    try:
        # Imports
        from src.project_tools import create_project_gdb

        project_gdb = rf"{project_folder}\{project}.gdb"

        try:

            create_project_gdb(project_gdb)

        except Warning as w:
            print(f"{w}"); del w
        except Exception as e:
            print(f"ERROR: {e}"); del e

        # Function variables
        del project_folder, project, project_gdb
        # Imports
        del create_project_gdb

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
        project = "Metadata"
        main(project_folder=project_folder, project=project)
    except Warning as w:
        print(w)

