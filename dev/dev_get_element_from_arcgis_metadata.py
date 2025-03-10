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

def get_element_from_arcgis_metadata(project_gdb="", metadata_element=""):
    try:
        # Imports
        from lxml import etree
        from io import StringIO
        # Third-party modules are loaded second
        import arcpy
        from arcpy import metadata as md
        import dev_create_folders

        # Project modules
        from src.project_tools import pretty_format_xml_file

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

        print(f"\n{'--Start' * 10}--\n")

        fcs = arcpy.ListFeatureClasses()

        #print(f"Get '{metadata_element}' from arcgis metadata and print xml\n")
        for fc in sorted(fcs):
            #print(f"Finding '{metadata_element}' in the '{fc}' metadata record")
            fc_path = rf"{project_gdb}\{fc}"

            dataset_md = md.Metadata(fc_path)
            dataset_md.synchronize('ALWAYS')
            dataset_md.save()
            dataset_md.reload()
            metadata_xml_string = dataset_md.xml
            del dataset_md

            # Parse the XML
            # parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
            # target_name = os.path.basename(fc_metadata_xml_file).replace(".xml", "")
            # target_tree = etree.parse(fc_metadata_xml_file, parser=parser)
            # target_root = target_tree.getroot()
            # del parser

            # Parse the XML file
            parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
            tree = etree.parse(StringIO(metadata_xml_string))
            del parser
            #print(etree.tostring(tree, encoding='UTF-8',  method='xml', pretty_print=True).decode())

            element = tree.xpath(f".//{metadata_element}")
            for elem in element:
                etree.indent(elem, space="  ")
                print(etree.tostring(elem, encoding='UTF-8',  method='xml', pretty_print=True).decode())
                del elem

            del element
            del tree

            del metadata_xml_string
            del fc, fc_path

        del fcs
        del project_folder

        print(f"\n{'--End' * 10}--")

        # Imports
        del etree, StringIO, md, pretty_format_xml_file, dev_create_folders
        # Function parameters
        del project_gdb, metadata_element

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

def main(project_gdb="", metadata_element=""):
    try:
        from time import gmtime, localtime, strftime, time
        # Set a start time so that we can see how log things take
        start_time = time()
        print(f"{'-' * 80}")
        print(f"Python Script:  {os.path.basename(__file__)}")
        print(f"Location:       {os.path.dirname(__file__)}")
        print(f"Python Version: {sys.version} Environment: {os.path.basename(sys.exec_prefix)}")
        print(f"{'-' * 80}\n")

        get_element_from_arcgis_metadata(project_gdb=project_gdb, metadata_element=metadata_element)

        # Variables

        # Function parameters
        del project_gdb, metadata_element

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
        # Imports
        from datetime import date

        # Append the location of this scrip to the System Path
        #sys.path.append(os.path.dirname(__file__))
        sys.path.append(os.path.dirname(os.path.dirname(__file__)))

        today = date.today()
        date_string = date.today().strftime("%Y-%m-%d")

        project_folder  = rf"{os.path.dirname(os.path.dirname(__file__))}"
        project_name    = "National Mapper"
        #project_name    = "NMFS_ESA_Range"
        project_gdb     = rf"{project_folder}\{project_name}.gdb"

        #metadata_element = "dqInfo"
        #metadata_element = "dqScope"
        #metadata_element = "dataIdInfo"
        metadata_element = "distInfo"

        main(project_gdb=project_gdb, metadata_element=metadata_element)

        # Variables
        del project_folder, project_name, project_gdb, metadata_element
        del today, date_string
        # Imports
        del date

    except:
        traceback.print_exc()
    else:
        pass
    finally:
        pass