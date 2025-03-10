# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        Step 1 Export Metadata
# Purpose:     Process metadata recprds
#
# Author:      john.f.kennedy
#
# Created:     11/20/2024
# Copyright:   (c) john.f.kennedy 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Python Built-in's modules are loaded first
import os, sys
import traceback
import importlib
import inspect

# Third-party modules are loaded second
import arcpy

# Append the location of this scrip to the System Path
sys.path.append(os.path.dirname(__file__))

def create_folder(folder):
    try:
        # Test if the folder exists. If not, then create the folder
        if not arcpy.Exists(folder):
            arcpy.AddMessage(f"Creating Folder: {os.path.basename(folder)}")
            # Execute CreateFolder
            arcpy.management.CreateFolder(os.path.dirname(folder), os.path.basename(folder))
            msg = "\tCreate Folder:\n\t\t"+arcpy.GetMessages().replace("\n", "\n\t\t")+"\n"
            arcpy.AddMessage(f"{msg}"); del msg
        else:
            arcpy.AddMessage(f"The folder '{os.path.basename(folder)}' exists")

    except:
        traceback.print_exc()
        raise Exception

def create_gdb(gdb):
    try:
        # Test of the Project GDB exists. If not, then create the Project GDB
        if not arcpy.Exists(gdb):
            arcpy.AddMessage(f"Creating the Project GDB: {os.path.basename(gdb)}")
            arcpy.management.CreateFileGDB(os.path.dirname(gdb), os.path.basename(gdb))
            msg = "\tCreate the GDB:\n\t\t"+arcpy.GetMessages().replace("\n", "\n\t\t")+"\n"
            arcpy.AddMessage(f"{msg}"); del msg
        else:
            arcpy.AddMessage(f"The GDB '{os.path.basename(gdb)}' exists")
    except:
        traceback.print_exc()
        raise Exception

def pretty_print(xml):
    try:
        # Imports
        from lxml import etree

        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
        # Parse the XML
        tree = etree.parse(xml, parser=parser)

        etree.indent(tree, space="    ")

        # Pretty print
        xml_string = etree.tostring(tree, encoding='UTF-8',  method='xml', pretty_print=True).decode()

        xml_string = xml_string.replace(' Sync="TRUE">\n', ' Sync="TRUE">')
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
        xml_string = xml_string.replace(' value="eng">\n', ' value="eng">')
        xml_string = xml_string.replace(' value="USA">\n', ' value="USA">')
        xml_string = xml_string.replace(' code="4326">\n', ' code="4326">')
        xml_string = xml_string.replace(' code="4">\n', ' code="4">')

        xml_string = xml_string.replace('Sync="TRUE">            <enttyp>', 'Sync="TRUE">\n            <enttyp>>')

        del parser, tree

        # Write the pretty XML to a file
        with open(xml, "w") as f:
            f.write(xml_string)

        del f
        del xml_string

        # Imports
        del etree
        # Function parameters
        del xml

    except:
        traceback.print_exc()
        raise Exception
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
            raise Exception
    finally:
        pass

def update_metadata_xml(gdb=""):
    try:
        # Imports
        from arcpy import metadata as md
        from lxml import etree
        from io import StringIO
        #from copy import deepcopy

        # Use all of the cores on the machine
        arcpy.env.parallelProcessingFactor = "100%"
        arcpy.env.overwriteOutput = True

        # Define variables
        project_folder = os.path.dirname(gdb)
        scratch_folder = rf"{project_folder}\Scratch"
        scratch_gdb    = rf"{scratch_folder}\scratch.gdb"

        # Set the workspace environment to local file geodatabase
        arcpy.env.workspace = gdb
        # Set the scratchWorkspace environment to local file geodatabase
        arcpy.env.scratchWorkspace = scratch_gdb

        # Clean-up variables
        del scratch_folder, scratch_gdb

        arcpy.AddMessage(f"\n{'--Start' * 10}--\n")

        fcs = [f for f in arcpy.ListFeatureClasses() if f not in ["WhaleNorthAtlanticRight_20201215"]]

        for fc in fcs:
            arcpy.AddMessage(fc)

            # XML Files
            fc_metadata_xml         = rf"{project_folder}\{os.path.basename(fc)}.xml"
            fc_metadata_xml_updated = rf"{project_folder}\{os.path.basename(fc)} UPDATED.xml"
            metadata_template       = rf"{project_folder}\SpeciesRangeMetadataTemplate.xml"

            arcpy.AddMessage("\tExport Metadata")

            dataset_md = md.Metadata(fc)
            dataset_md.synchronize('ALWAYS')
            dataset_md.save()
            dataset_md.reload()

            dataset_md.saveAsXML(fc_metadata_xml, "REMOVE_ALL_SENSITIVE_INFO")
            dataset_md.saveAsXML(fc_metadata_xml_updated, "REMOVE_ALL_SENSITIVE_INFO")

            del dataset_md
            del fc

            dataset_md = md.Metadata(fc_metadata_xml_updated)

            metadata_xml_string = dataset_md.xml

            # Parse the XML file
            old_tree = etree.parse(StringIO(metadata_xml_string))
            new_tree = etree.parse(metadata_template)

            del metadata_xml_string

            # Get the root element
            old_root = old_tree.getroot()
            new_root = new_tree.getroot()

            #print(eainfo_old_root.tag)
            #print(eainfo_old_root.find("eainfo").tag)
            #print(eainfo_new_root.tag)

            # Find the elements
            eainfo_old_child = old_root.find("eainfo")
            eainfo_new_child = new_root.find("eainfo")

            # Replace child1 with child2
            old_root.replace(eainfo_old_child, eainfo_new_child)

            # Print the modified XML
            #print(etree.tostring(eainfo_old_tree, pretty_print=True).decode())

            #root = ET.fromstring(metadata_xml_string)
            #del metadata_xml_string

            # get modified XML
            updated_xml_string = etree.tostring(old_root, encoding='UTF-8')

            # import result back into metadata
            arcpy.AddMessage("\tSaving updated metadata with the item...")
            dataset_md.xml = updated_xml_string
            dataset_md.save()
            dataset_md.reload()
            dataset_md.saveAsXML(fc_metadata_xml_updated, "REMOVE_ALL_SENSITIVE_INFO")
            del dataset_md, updated_xml_string

            del eainfo_old_child, eainfo_new_child

            del old_tree, new_tree, old_root, new_root


            pretty_print(fc_metadata_xml)
            pretty_print(fc_metadata_xml_updated)

            del fc_metadata_xml, fc_metadata_xml_updated

            pretty_print(metadata_template)
            del metadata_template

        del fcs

        arcpy.AddMessage("Compact GDB")
        arcpy.management.Compact(gdb)

        arcpy.AddMessage(f"\n{'--End' * 10}--")

        #
        del project_folder

        # Imports
        del md, etree, StringIO

        # Function parameters
        del gdb

    except arcpy.ExecuteError:
        arcpy.AddError(arcpy.GetMessages())
        traceback.print_exc()
        raise Exception
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
            raise Exception
    finally:
        # Cleanup
        arcpy.management.ClearWorkspaceCache()

# Main function
def main():
    try:
        CheckFolderExists = False
        if CheckFolderExists:
            # Folder / GDB setup
            create_folder(project_folder)
            create_folder(scratch_folder)
            create_gdb(project_gdb)
            create_gdb(scratch_gdb)
        del CheckFolderExists

        UpdateMetadataXml = True
        if UpdateMetadataXml:
            update_metadata_xml(gdb=project_gdb)
        del UpdateMetadataXml

    except Exception:
        #print(e)
        pass
    except:
        traceback.print_exc()
        #raise Exception

if __name__ == '__main__':
    try:
        from time import gmtime, localtime, strftime, time

        # Set a start time so that we can see how log things take
        start_time = time()

        print(f"{'-' * 80}")
        print(f"Python Script:  {os.path.basename(__file__)}")
        print(f"Location:       {os.path.dirname(__file__)}")
        print(f"Python Version: {sys.version} Environment: {os.path.basename(sys.exec_prefix)}")
        print(f"{'-' * 80}\n")
        current_folder = os.path.dirname(__file__)
        project_folder = rf"{current_folder}\Metadata Folder"
        #project_gdb    = rf"{project_folder}\Metadata.gdb"
        project_gdb    = rf"{project_folder}\National Mapper.gdb"
        scratch_folder = rf"{project_folder}\Scratch"
        scratch_gdb    = rf"{scratch_folder}\scratch.gdb"

        main()

        del current_folder
        del project_folder, project_gdb
        del scratch_folder, scratch_gdb

        # Elapsed time
        end_time = time()
        elapse_time =  end_time - start_time

        print(f"\n{'-' * 80}")
        print(f"Python script: {os.path.basename(__file__)} successfully completed {strftime('%a %b %d %I:%M %p', localtime())}")
        print(u"Elapsed Time {0} (H:M:S)".format(strftime("%H:%M:%S", gmtime(elapse_time))))
        print(f"{'-' * 80}")
        del elapse_time, end_time, start_time
        del gmtime, localtime, strftime, time

    except Exception:
        pass
    except:
        traceback.print_exc()
    else:
        ["leave_out_keys"].extend([name for name, obj in inspect.getmembers(sys.modules[__name__]) if inspect.isfunction(obj) or inspect.ismodule(obj)])
        remaining_keys = [key for key in locals().keys() if not key.startswith("__") and key not in leave_out_keys]
        if remaining_keys:
            arcpy.AddWarning(f"Remaining Keys: ##--> '{', '.join(remaining_keys)}' <--##")
        else:
            pass # No Remaining Keys
        del leave_out_keys, remaining_keys
    finally:
        pass