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

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

def main(project_folder=str(), folders=list()):
    try:
        # Imports
        from src.project_tools import create_folders

        try:

            create_folders(project_folder, folders)

        except Warning as w:
            print(f"{w}"); del w
        except Exception as e:
            print(f"ERROR: {e}"); del e

        # Function variables
        del project_folder, folders
        # Imports
        del create_folders

    except:
        traceback.print_exc()
    else:
        return True
    finally:
        # Cleanup
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: raise Warning(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk

if __name__ == '__main__':
    try:
        #project_folder = rf"{os.path.dirname(os.path.dirname(__file__))}"
        project_folder = r"C:\Users\john.f.kennedy\Documents\ArcGIS\Projects\DisMAP-ArcGIS-Analysis"
        #folders = ["Export", "Layers", "Publish", "dev", "test", "prod"]
        folders = ["build", "data", "dev", "dist", "helpDoc", "prod", "samples", "src", "test"]
        main(project_folder=project_folder, folders=folders)
        del project_folder, folders
    except Warning as w:
        print(w)

