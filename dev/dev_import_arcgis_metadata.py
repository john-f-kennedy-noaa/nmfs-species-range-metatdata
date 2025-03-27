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

def import_metadata(project_gdb="", metadata_folder=""):
    try:
        # Imports
        # Third-party modules are loaded second
        import arcpy
        from arcpy import metadata as md

        # Use all of the cores on the machine
        arcpy.env.parallelProcessingFactor = "100%"
        arcpy.env.overwriteOutput = True

        # Define variables
        project_folder = os.path.dirname(project_gdb)
        scratch_folder = rf"{project_folder}\Scratch"
        scratch_gdb    = rf"{scratch_folder}\scratch.gdb"

        # Set the workspace environment to local file geodatabase
        arcpy.env.workspace = project_gdb
        # Set the scratchWorkspace environment to local file geodatabase
        arcpy.env.scratchWorkspace = scratch_gdb

        # Clean-up variables
        del scratch_folder, scratch_gdb

        print(f"{'--Start' * 10}--\n")

        arcpy.env.workspace = project_gdb

        fcs = arcpy.ListFeatureClasses()

        print(f"Import and synchronize feature classes metadata from Project GDB\n")
        for fc in sorted(fcs):
            print(f"Importing the metadata record for: '{fc}'")

            fc_path = rf"{project_gdb}\{fc}"

            import_xml_metadata_path = rf"{metadata_folder}\{fc}.xml"

            dataset_md = md.Metadata(fc_path)
            dataset_md.synchronize('ALWAYS')
            dataset_md.save()
            dataset_md.importMetadata(import_xml_metadata_path)
            dataset_md.save()
            dataset_md.synchronize('SELECTIVE')
            dataset_md.save()
            dataset_md.title = fc
            dataset_md.save()
            dataset_md.synchronize('ALWAYS')
            dataset_md.save()
            del dataset_md

            del import_xml_metadata_path
            del fc, fc_path

        del fcs
        del project_folder

        print(f"\n{'--End' * 10}--")

        # Imports
        del md
        # Function parameters
        del project_gdb, metadata_folder

    except:
        traceback.print_exc()
    else:
        # Cleanup
        arcpy.management.ClearWorkspaceCache()
        # Imports
        del arcpy
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        pass

def main(project_gdb="", metadata_folder=""):
    try:
        from time import gmtime, localtime, strftime, time
        # Set a start time so that we can see how log things take
        start_time = time()
        print(f"{'-' * 80}")
        print(f"Python Script:  {os.path.basename(__file__)}")
        print(f"Location:       {os.path.dirname(__file__)}")
        print(f"Python Version: {sys.version} Environment: {os.path.basename(sys.exec_prefix)}")
        print(f"{'-' * 80}\n")

        import_metadata(project_gdb=project_gdb, metadata_folder=metadata_folder)

        # Declared Variables

        # Function parameters
        del project_gdb, metadata_folder

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
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        pass

if __name__ == '__main__':
    try:
        from datetime import date

        # Append the location of this scrip to the System Path
        #sys.path.append(os.path.dirname(__file__))
        sys.path.append(os.path.dirname(os.path.dirname(__file__)))

        today = date.today()
        date_string = today.strftime("%Y-%m-%d")

        project_folder  = rf"{os.path.dirname(os.path.dirname(__file__))}"
        project_name    = "National Mapper"
        project_gdb     = rf"{project_folder}\{project_name}.gdb"
        metadata_folder = f"Export {date_string}"

        main(project_gdb=project_gdb,metadata_folder=metadata_folder)

        # Declared Variables
        del project_folder, project_name, project_gdb, metadata_folder
        del today, date_string
        # Imports
        del date

    except:
        traceback.print_exc()
    else:
        pass
    finally:
        pass