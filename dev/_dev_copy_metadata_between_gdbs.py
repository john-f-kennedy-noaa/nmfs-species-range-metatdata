# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john.f.kennedy
#
# Created:     03/03/2024
# Copyright:   (c) john.f.kennedy 2024
# Licence:     <your licence>
# -------------------------------------------------------------------------------
import os, sys  # built-ins first
import traceback
import importlib
import inspect

import arcpy  # third-parties second

def main(source_gdb="", target_gdb=""):
    try:
        from time import gmtime, localtime, strftime, time
        # Set a start time so that we can see how log things take
        start_time = time()
        print(f"{'-' * 80}")
        print(f"Python Script:  {os.path.basename(__file__)}")
        print(f"Location:       ..\Documents\ArcGIS\Projects\..\{os.path.basename(os.path.dirname(__file__))}\{os.path.basename(__file__)}")
        print(f"Python Version: {sys.version}")
        print(f"Environment:    {os.path.basename(sys.exec_prefix)}")
        print(f"{'-' * 80}\n")

        from arcpy import metadata as md

        arcpy.env.workspace = source_gdb

        fcs = arcpy.ListFeatureClasses("*")

        for fc in fcs:
            print(f"Dataset: {fc}")
            source_dataset_md = md.Metadata(fc)
            target_dataset_md = md.Metadata(rf"{target_gdb}\{fc}")
            target_dataset_md.copy(target_dataset_md)
            target_dataset_md.save()
            target_dataset_md.synchronize("ALWAYS")
            target_dataset_md.save()
            del target_dataset_md
            del source_dataset_md
            del fc

        # Declared Varaiables
        del fcs
        # Imports
        del md
        # Function Parameters
        del source_gdb, target_gdb

        # Elapsed time
        end_time = time()
        elapse_time =  end_time - start_time

        print(f"\n{'-' * 80}")
        print(f"Python script: {os.path.basename(__file__)}\nCompleted: {strftime('%a %b %d %I:%M %p', localtime())}")
        print(u"Elapsed Time {0} (H:M:S)".format(strftime("%H:%M:%S", gmtime(elapse_time))))
        print(f"{'-' * 80}")
        del elapse_time, end_time, start_time
        del gmtime, localtime, strftime, time

    except Exception:
        traceback.print_exc()
    except:
        traceback.print_exc()
    else:
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        pass

if __name__ == "__main__":
    try:
        # Imports
        # Append the location of this scrip to the System Path
        #sys.path.append(os.path.dirname(__file__))
        sys.path.append(os.path.dirname(os.path.dirname(__file__)))

        project_folder = rf"{os.path.dirname(os.path.dirname(__file__))}"
        arcpy.env.workspace = project_folder

        #gdbs = arcpy.ListWorkspaces(wild_card="*", workspace_type="FileGDB")
        #for gdb in gdbs:
        #    print(gdb)
        #del gdbs

        source_gdb = rf"{project_folder}\NMFS_ESA_Range.gdb"
        target_gdb = rf"{project_folder}\NMFS_ESA_Range.gdb"

        main(source_gdb=source_gdb, target_gdb=target_gdb)

        # Declared Variables
        del source_gdb, target_gdb
        del project_folder
        # Imports
    except:
        traceback.print_exc()
    else:
        pass
    finally:
        pass
