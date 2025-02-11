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
            arcpy.AddMessage(f"Creating the Project GDB: {os.path.basename(project_gdb)}")
            arcpy.management.CreateFileGDB(project_folder, os.path.basename(project_gdb))
            msg = "\tCreate the Project GDB:\n\t\t"+arcpy.GetMessages().replace("\n", "\n\t\t")+"\n"
            arcpy.AddMessage(f"{msg}"); del msg
        else:
            arcpy.AddMessage(f"The Project GDB Exists: {os.path.basename(project_gdb)}")

        # Test of the Scratch GDB exists. If not, then create the Scratch GDB
        scratch_folder = rf"{project_folder}\Scratch"
        scratch_gdb    = rf"{scratch_folder}\scratch.gdb"
        if not arcpy.Exists(scratch_gdb):
            arcpy.AddMessage(f"Creating the Scratch Folder: {os.path.basename(scratch_folder)}")
            # Execute CreateFolder
            arcpy.management.CreateFolder(project_folder, "Scratch")
            msg = "\tCreate the Scratch Folder:\n\t\t"+arcpy.GetMessages().replace("\n", "\n\t\t")+"\n"
            arcpy.AddMessage(f"{msg}"); del msg
            arcpy.AddMessage(f"Creating the Scratch GDB: {os.path.basename(scratch_gdb)}")
            arcpy.management.CreateFileGDB(scratch_folder, os.path.basename(scratch_gdb))
            msg = "\tCreate the Scratch GDB:\n\t\t"+arcpy.GetMessages().replace("\n", "\n\t\t")+"\n"
            arcpy.AddMessage(f"{msg}"); del msg
        else:
            arcpy.AddMessage(f"The Scratch GDB Exists: {os.path.basename(scratch_gdb)}")
        del scratch_folder, scratch_gdb

        del project_folder
        # Function parameters
        del project_gdb

    except:
        traceback.print_exc()
    else:
        return True
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        # Cleanup
        arcpy.management.ClearWorkspaceCache()
        # Imports
        del arcpy

def create_folders(project_folder, folders=[]):
    try:
        for folder in folders:
            directory_path = rf"{project_folder}\{folder}"
            # Test of the Export folder exists. If not, then create the folder
            if not os.path.isdir(directory_path):
                print(f"Creating Folder: {folder}")
                # Create the directory
                os.mkdir(directory_path)
            else:
                print(f"The {folder} folder exists")
            del folder
            del directory_path
        # Function parameters
        del folders, project_folder
    except:
        traceback.print_exc()
    else:
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        pass

def pretty_format_xml_file(xml=""):
    try:
        # Imports
        from lxml import etree

        #arcpy.AddMessage(f"###--->>> Converting metadata file: {os.path.basename(xml)} to pretty format")
        if os.path.isfile(xml):

            parser = etree.XMLParser(remove_blank_text=True)
            # Parse the XML
            tree = etree.parse(xml, parser=parser)

            etree.indent(tree, space="    ")

            # Pretty print
            xml_string = etree.tostring(tree, pretty_print=True, method='html', encoding="utf-8", xml_declaration=True).decode()

            xml_string = xml_string.replace(' code="0">\n', ' code="0">')
            xml_string = xml_string.replace(' code="4">\n', ' code="4">')
            xml_string = xml_string.replace(' code="4326">\n', ' code="4326">')

            xml_string = xml_string.replace(' country="US">\n', ' country="US">')

            xml_string = xml_string.replace(' Sync="TRUE">\n', ' Sync="TRUE">')
            xml_string = xml_string.replace(' Sync="FALSE">\n', ' Sync="FALSE">')
            xml_string = xml_string.replace(' Sync="TRUE">            <enttyp>', ' Sync="TRUE">\n            <enttyp>')

            xml_string = xml_string.replace(' value="001">\n', ' value="001">')
            xml_string = xml_string.replace(' value="002">\n', ' value="002">')
            xml_string = xml_string.replace(' value="003">\n', ' value="003">')
            xml_string = xml_string.replace(' value="004">\n', ' value="004">')
            xml_string = xml_string.replace(' value="005">\n', ' value="005">')
            xml_string = xml_string.replace(' value="006">\n', ' value="006">')
            xml_string = xml_string.replace(' value="007">\n', ' value="007">')
            xml_string = xml_string.replace(' value="008">\n', ' value="008">')
            xml_string = xml_string.replace(' value="009">\n', ' value="009">')
            xml_string = xml_string.replace(' value="010">\n', ' value="010">')
            xml_string = xml_string.replace(' value="011">\n', ' value="011">')
            xml_string = xml_string.replace(' value="012">\n', ' value="012">')
            xml_string = xml_string.replace(' value="013">\n', ' value="013">')
            xml_string = xml_string.replace(' value="014">\n', ' value="014">')
            xml_string = xml_string.replace(' value="015">\n', ' value="015">')
            xml_string = xml_string.replace(' value="031">\n', ' value="031">')

            xml_string = xml_string.replace(' value="eng">\n', ' value="eng">')
            xml_string = xml_string.replace(' value="US">\n', ' value="US">')

            xml_string = xml_string.replace('<RefSystem dimension="horizontal">\n', '<RefSystem dimension="horizontal">',)

            #xml_string = xml_string.replace("<attrdef>", '<attrdef Sync="TRUE">')
            #xml_string = xml_string.replace("<attrdefs>", '<attrdefs Sync="TRUE">')
            #xml_string = xml_string.replace("<udom>", '<udom Sync="TRUE">')
            xml_string = xml_string.replace('<UOM type="length">\n', '<UOM type="length">')

            try:
                with open(xml, "w") as f:
                    f.write(xml_string)
                del f
            except:
                arcpy.AddError(f"The metadata file: {os.path.basename(xml)} can not be overwritten!!")

            del xml_string
            del parser, tree

        else:
            print(f"\t###--->>> {os.path.basename(xml)} is missing!! <<<---###")

        # Imports
        del etree
        # Function parameters
        del xml

    except:
        traceback.print_exc()
        raise Exception(f"In function: '{inspect.stack()[0][3]}'")
    else:
        return True
    finally:
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk

def check_and_repair_geometry(fc_path):
    try:
        # Check Geometry
        fc  = os.path.basename(fc_path)
        gdb = os.path.dirname(fc_path)

        bad_geometry_fc = {}

        out_table = rf"{gdb}\CheckGeometryTable_{fc}"

        arcpy.AddMessage(f"Check Geometry for {fc}")
        result = arcpy.management.CheckGeometry(fc_path, out_table, "ESRI")
        msg = "\tCheck Geometry:\n\t\t"+arcpy.GetMessages().replace("\n", "\n\t\t")+"\n"
        arcpy.AddMessage(f"{msg}"); del msg

        if result[1] == "false":
            arcpy.management.Delete(out_table)
        elif result[1] == "true":
            ot = result[0]
            field_names = [f.name for f in arcpy.ListFields(ot) if f.type not in ['Geometry', 'OID']]

            with arcpy.da.SearchCursor(ot, field_names) as cursor:
                for row in cursor:
                    bad_geometry_fc[os.path.basename(row[0])] = {"CLASS" : row[0], "FEATURE_ID" : row[1], "PROBLEM" : row[2]}
                    del row
            del cursor
            arcpy.management.Delete(ot)
            del ot
            del field_names

            arcpy.AddMessage(f"Repair Geometry for {fc}")
            arcpy.management.RepairGeometry(fc_path)
            msg = "\tRepair Geometry:\n\t\t"+arcpy.GetMessages().replace("\n", "\n\t\t")+"\n"
            arcpy.AddMessage(f"{msg}"); del msg

        else:
            pass

        del out_table, result

        # Recalculate Feature Class Extent
        arcpy.AddMessage(f"Recalculate Feature Class Extent for {fc}")
        arcpy.management.RecalculateFeatureClassExtent(fc_path)
        msg = "\tRecalculate Feature Class Extent:\n\t\t"+arcpy.GetMessages().replace("\n", "\n\t\t")+"\n"
        arcpy.AddMessage(f"{msg}"); del msg

        del fc, gdb
        del fc_path

    except:
        traceback.print_exc()
        raise Exception(f"In function: '{inspect.stack()[0][3]}'")
    else:
        return bad_geometry_fc
    finally:
        del bad_geometry_fc
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk

def main():
    try:
        from time import gmtime, localtime, strftime, time
        # Set a start time so that we can see how log things take
        start_time = time()
        print(f"{'-' * 80}")
        print(f"Python Script:  {os.path.basename(__file__)}")
        print(f"Location:       {os.path.dirname(__file__)}")
        print(f"Python Version: {sys.version} Environment: {os.path.basename(sys.exec_prefix)}")
        print(f"{'-' * 80}\n")

        CreateProjectGDB = False
        if CreateProjectGDB:
            project_folder = rf"{os.path.dirname(os.path.dirname(__file__))}"
            project = "Metadata"
            project_gdb = rf"{project_folder}\{project}.gdb"
            try:
                create_project_gdb(project_gdb)
            except Warning as w:
                print(f"{w}"); del w
            except Exception as e:
                print(f"ERROR: {e}"); del e
            del project_folder, project, project_gdb
        del CreateProjectGDB

        CreateFoldersTest = False
        if CreateFoldersTest:
            project_folder = rf"{os.path.dirname(os.path.dirname(__file__))}"
            folders = ["Export", "Layers", "Publish"]
            try:
                create_folders(project_folder, folders)
            except Warning as w:
                print(f"{w}"); del w
            except Exception as e:
                print(f"ERROR: {e}"); del e
            del project_folder, folders
        del CreateFoldersTest

        PrettyFormatXmlFileTest = False
        if PrettyFormatXmlFileTest:
            project_folder = rf"{os.path.dirname(os.path.dirname(__file__))}"
            xml_file = rf"{project_folder}\Export\ConchQueen_20240522.xml"
            try:
                pretty_format_xml_file(xml_file)
            except Warning as w:
                print(f"{w}"); del w
            except Exception as e:
                print(f"ERROR: {e}"); del e
            del xml_file
            del project_folder
        del PrettyFormatXmlFileTest

        CheckAndRepairGeometry = False
        if CheckAndRepairGeometry:
            bad_geometry_fcs = dict()
            try:
                bad_geometry_fc = check_and_repair_geometry(destination_fc_path+"_tmp")
            except Warning as w:
                print(f"{w}"); del w
            except Exception as e:
                print(f"ERROR: {e}"); del e
            if bad_geometry_fc:
                for key in bad_geometry_fc:
                    if key not in bad_geometry_fcs:
                        bad_geometry_fcs[key] = bad_geometry_fc[key]
                    del key
            del bad_geometry_fc
            if bad_geometry_fcs:
                arcpy.AddMessage(f"Feature Classes with bad geometry")
                for bad_geometry_fc in sorted(bad_geometry_fcs):
                    arcpy.AddMessage(f"\tFeature Class: {bad_geometry_fc}\n\t\tFeature ID: {bad_geometry_fcs[bad_geometry_fc]['FEATURE_ID']}\n\t\tProblem: {bad_geometry_fcs[bad_geometry_fc]['PROBLEM']}")
                    del bad_geometry_fc
            del bad_geometry_fcs
        del CheckAndRepairGeometry

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
        if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk

if __name__ == '__main__':
    try:
        main()
    except Warning as w:
        print(w)

