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

def zip_data(source_folder, selected_files, out_zip_file):
    try:
        # Imports
        from zipfile import ZipFile

        os.chdir(source_folder)

        print(f"Zipping up files into: '{os.path.basename(out_zip_file)}'")

        selected_files = selected_files.split(";")

        source_files = [f for f in os.listdir(source_folder) if f in selected_files]

        with ZipFile(out_zip_file, mode="w") as archive:
            for source_file in source_files:
                archive.write(source_file)
                del source_file
        del archive

        print(f"Done zipping up files into '{os.path.basename(out_zip_file)}'")

        results = out_zip_file
        del out_zip_file

        # Declared Variables

        # Imports
        del ZipFile

        # Function parameters
        del input_zip_file, output_folder
        del source_folder, selected_files, source_files

    except:
        traceback.print_exc()
    else:
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        pass

def main(input_zip_file="", output_folder=""):
    try:
        from time import gmtime, localtime, strftime, time
        # Set a start time so that we can see how log things take
        start_time = time()
        print(f"{'-' * 80}")
        print(f"Python Script:  {os.path.basename(__file__)}")
        print(f"Location:       {os.path.dirname(__file__)}")
        print(f"Python Version: {sys.version} Environment: {os.path.basename(sys.exec_prefix)}")
        print(f"{'-' * 80}\n")


        base_project_folder = os.path.dirname(os.path.dirname(__file__))

        #in_project = "July 1 2024"
        in_project = "December 1 2024"
        in_data_path = rf"{base_project_folder}\{in_project}\CSV Data"
        del in_project

        out_project = "December 1 2024"
        out_data_path = rf"{base_project_folder}\{out_project}\CSV Data"
        del out_project

        selected_files = ["AI_IDW.csv", "Datasets.csv", "EBS_IDW.csv",
                          "ENBS_IDW.csv", "GMEX_IDW.csv",
                          "GOA_IDW.csv", "HI_IDW.csv", "NBS_IDW.csv",
                          "NEUS_FAL_IDW.csv", "NEUS_SPR_IDW.csv",
                          "SEUS_FAL_IDW.csv", "SEUS_SPR_IDW.csv",
                          "SEUS_SUM_IDW.csv", "Species_Filter.csv",
                          "WC_ANN_IDW.csv", "WC_GFDL.csv", "WC_GLMME.csv",
                          "WC_TRI_IDW.csv", "field_definitions.json",
                          "metadata_dictionary.json", "table_definitions.json"
                         ]
        selected_files = ";".join(selected_files)

        main(in_data_path, out_data_path, selected_files)

        del in_data_path, out_data_path, selected_files
        del base_project_folder

        zip_data(input_zip_file, output_folder)

        # Declared Variables

        # Function parameters
        del input_zip_file, output_folder

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
        project_folder = rf"{os.path.dirname(os.path.dirname(__file__))}"
        zip_file_name  = "NMFS_ESA_Range.gdb (20241209).zip"
        main(input_zip_file = rf"{project_folder}\{zip_file_name}", output_folder=project_folder)
        del project_folder, zip_file_name
    except Warning as w:
        print(w)
