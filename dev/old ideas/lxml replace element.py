#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john.f.kennedy
#
# Created:     15/12/2024
# Copyright:   (c) john.f.kennedy 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Python Built-in's modules are loaded first
import os, sys
import traceback
import importlib
import inspect
from lxml import etree

# Third-party modules are loaded second
import arcpy

# Append the location of this scrip to the System Path
sys.path.append(os.path.dirname(__file__))

def update_eainfo():
    try:
        from copy import deepcopy

        # XML Files
        eainfo_old_xml_path = rf"eainfo_old_xml.xml"
        eainfo_new_xml_path = rf"eainfo_new_xml.xml"

        # Parse the XML file
        eainfo_old_tree = etree.parse(eainfo_old_xml_path)
        eainfo_new_tree = etree.parse(eainfo_new_xml_path)

        # Get the root element
        eainfo_old_root = eainfo_old_tree.getroot()
        eainfo_new_root = eainfo_new_tree.getroot()

        #print(eainfo_old_root.tag)
        #print(eainfo_old_root.find("eainfo").tag)
        #print(eainfo_new_root.tag)

        # Find the elements
        eainfo_old_child = eainfo_old_root.find("eainfo")
        eainfo_new_child = eainfo_new_root.find("eainfo")

        # Replace child1 with child2
        eainfo_old_root.replace(eainfo_old_child, eainfo_new_child)

        # Print the modified XML
        print(etree.tostring(eainfo_old_tree, pretty_print=True).decode())


##        # Find the elements
##        eainfo_old_parent = eainfo_old_tree.find("metadata")
##        eainfo_old_child  = eainfo_old_parent.find("/eainfo")
##
##        eainfo_new_child = eainfo_new_tree.find("metadata/eainfo")
##
##        # Replace child1 with child2
##        eainfo_old_parent.replace(eainfo_old_child, eainfo_new_child)
##
##        # Print the modified XML
##        print(etree.tostring(eainfo_old_tree, pretty_print=True).decode())

        del eainfo_old_xml_path, eainfo_old_tree, eainfo_old_root, eainfo_old_child, eainfo_new_child
        del eainfo_new_xml_path, eainfo_new_tree, eainfo_new_root

        # Imports
        del deepcopy

    except arcpy.ExecuteError:
        arcpy.AddError(arcpy.GetMessages())
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

def main():
    try:

        UpdateEainfo = True
        if UpdateEainfo:
            update_eainfo()
        del UpdateEainfo

    except Exception as e:
        print(e)
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
        project_gdb    = rf"{project_folder}\Metadata.gdb"
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

    except Exception as e:
        print(e)
    except:
        traceback.print_exc()
    else:
        leave_out_keys = ["leave_out_keys"]
        leave_out_keys.extend([name for name, obj in inspect.getmembers(sys.modules[__name__]) if inspect.isfunction(obj) or inspect.ismodule(obj)])
        remaining_keys = [key for key in locals().keys() if not key.startswith("__") and key not in leave_out_keys]
        if remaining_keys:
            arcpy.AddWarning(f"Remaining Keys: ##--> '{', '.join(remaining_keys)}' <--##")
        else:
            pass
        del leave_out_keys, remaining_keys
    finally:
        pass
