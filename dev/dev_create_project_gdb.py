"""
This module contains . . .

Requires : Python 3.11
           ArcGIS Pro 3.x

Copyright 2025 NMFS
Licensed under the Apache License, Version 2.0 (the 'License');
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an 'AS IS' BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
# Python Built-in's modules are loaded first
import os, sys
import traceback, inspect

def create_project_gdb(project_gdb):
    try:
        # Third-party modules are loaded second
        import arcpy

        project_folder = os.path.dirname(project_gdb)
        # Test of the Project GDB exists. If not, then create the Project GDB
        if not arcpy.Exists(project_gdb):
            print(f"Creating the Project GDB: {os.path.basename(project_gdb)}")
            arcpy.management.CreateFileGDB(project_folder, os.path.basename(project_gdb))
            msg = "\tCreate the Project GDB:\n\t\t"+arcpy.GetMessages().replace("\n", "\n\t\t")+"\n"
            print(f"{msg}"); del msg
        else:
            print(f"The Project GDB Exists: {os.path.basename(project_gdb)}")

        # Test of the Scratch GDB exists. If not, then create the Scratch GDB
        scratch_folder = rf"{project_folder}\Scratch"
        scratch_gdb    = rf"{scratch_folder}\scratch.gdb"
        if not arcpy.Exists(scratch_gdb):
            print(f"Creating the Scratch Folder: {os.path.basename(scratch_folder)}")
            # Execute CreateFolder
            arcpy.management.CreateFolder(project_folder, "Scratch")
            msg = "\tCreate the Scratch Folder:\n\t\t"+arcpy.GetMessages().replace("\n", "\n\t\t")+"\n"
            print(f"{msg}"); del msg
            print(f"Creating the Scratch GDB: {os.path.basename(scratch_gdb)}")
            arcpy.management.CreateFileGDB(scratch_folder, os.path.basename(scratch_gdb))
            msg = "\tCreate the Scratch GDB:\n\t\t"+arcpy.GetMessages().replace("\n", "\n\t\t")+"\n"
            print(f"{msg}"); del msg
        else:
            print(f"The Scratch GDB Exists: {os.path.basename(scratch_gdb)}")
        del scratch_folder, scratch_gdb

        del project_folder
        # Function parameters
        del project_gdb

    except:
        traceback.print_exc()
    else:
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        # Cleanup
        arcpy.management.ClearWorkspaceCache()
        # Imports
        del arcpy

def main(project_folder="",project_name=""):
    try:
        from time import gmtime, localtime, strftime, time
        # Set a start time so that we can see how log things take
        start_time = time()
        print(f"{'-' * 80}")
        print(f"Python Script:  {os.path.basename(__file__)}")
        print(f"Location:       {os.path.dirname(__file__)}")
        print(f"Python Version: {sys.version} Environment: {os.path.basename(sys.exec_prefix)}")
        print(f"{'-' * 80}\n")


        project_gdb = rf"{project_folder}\{project_name}.gdb"
        try:
            create_project_gdb(project_gdb)
        except Warning as w:
            print(f"{w}"); del w
        except Exception as e:
            print(f"ERROR: {e}"); del e

        # Variables
        del project_gdb
        # Function parameters
        del project_folder, project_name

        # Elapsed time
        end_time = time()
        elapse_time =  end_time - start_time
        print(f"\n{'-' * 80}")
        print(f"Python script: {os.path.basename(__file__)} successfully completed {strftime('%a %b %d %I:%M %p', localtime())}")
        print(u"Elapsed Time {0} (H:M:S)".format(strftime("%H:%M:%S", gmtime(elapse_time))))
        print(f"{'-' * 80}")
        del elapse_time, end_time, start_time
        del gmtime, localtime, strftime, time

    except:
        traceback.print_exc()
    else:
        return True
    finally:
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: raise Warning(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk

if __name__ == '__main__':
    try:
        main(project_folder = rf"{os.path.dirname(os.path.dirname(__file__))}", project_name = "project")
    except Warning as w:
        print(w)
