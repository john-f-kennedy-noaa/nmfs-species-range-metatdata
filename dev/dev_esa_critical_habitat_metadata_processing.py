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

def main(project_gdb=""):
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

        #Imports
        from lxml import etree
        from io import StringIO, BytesIO
        #import copy
        #import arcpy
        from arcpy import metadata as md

        arcpy.env.overwriteOutput = True
        arcpy.env.parallelProcessingFactor = "100%"

        # Test if passed workspace exists, if not raise SystemExit
        if not arcpy.Exists(project_gdb):
            print(f"{os.path.basename(project_gdb)} is missing!!")
            print(f"{project_gdb}")

        project_folder = os.path.dirname(project_gdb)
        scratch_folder = rf"{project_folder}\Scratch"

        arcpy.env.workspace        = project_gdb
        arcpy.env.scratchWorkspace = rf"{scratch_folder}\scratch.gdb"

        import json
        json_path = rf"{project_folder}\root_dict.json"
        with open(json_path, "r") as json_file:
            root_dict = json.load(json_file)
        del json_file
        del json_path
        del json

        datasets = list()
        walk = arcpy.da.Walk(arcpy.env.workspace)
        for dirpath, dirnames, filenames in walk:
            for filename in filenames:
                datasets.append(os.path.join(dirpath, filename))
                del filename
            del dirpath, dirnames, filenames
        del walk

        del scratch_folder, project_folder

        print(f"Processing: {os.path.basename(arcpy.env.workspace)} in the '{inspect.stack()[0][3]}' function")

        # ALL
        for dataset_path in sorted(datasets):
        #for dataset_path in sorted([ds for ds in datasets if ds.endswith("20250501")]):
            dataset_name = os.path.basename(dataset_path)
            print(f"Dataset: {dataset_name}")
            del dataset_name

##            dataset_md = md.Metadata(dataset_path)
##            #dataset_md.synchronize("ALWAYS")
##            #dataset_md.save()
##            #dataset_md.reload()
##            dataset_md_xml = dataset_md.xml
##            del dataset_md
##
##            # Parse the XML
##            parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
##            target_tree = etree.parse(StringIO(dataset_md_xml), parser=parser)
##            target_root = target_tree.getroot()
##            del parser, dataset_md_xml



            PrintTargetTree = True
            if PrintTargetTree:
                dataset_md = md.Metadata(dataset_path)
                dataset_md.synchronize("ALWAYS")
                dataset_md.save()
                dataset_md.reload()
                # Parse the XML
                export_folder  = rf"{os.path.dirname(os.path.dirname(dataset_path))}\Export"
                _target_tree = etree.parse(StringIO(dataset_md.xml), parser=etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
                _target_root = _target_tree.getroot()
                _target_root[:] = sorted(_target_root, key=lambda x: root_dict[x.tag])
                etree.indent(_target_tree, "    ")
                _target_tree.write(rf"{export_folder}\{os.path.basename(dataset_path)}.xml", encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True)
                print(etree.tostring(_target_tree, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
                del _target_tree, _target_root, export_folder
                del dataset_md
            else:
                pass
            del PrintTargetTree

        CompactGDB = True
        if CompactGDB:
            print(f"Compact GDB")
            arcpy.management.Compact(project_gdb)
            print("\t"+arcpy.GetMessages().replace("\n", "\n\t")+"\n")
        else:
            pass
        del CompactGDB

        # Declared Varaiables
        del datasets, dataset_path, root_dict
        # Imports
        del etree, StringIO, BytesIO, md
        # Function Parameters
        del project_gdb
        # Elapsed time
        end_time = time()
        elapse_time =  end_time - start_time
        print(f"\n{'-' * 80}")
        print(f"Python script: {os.path.basename(__file__)}\nCompleted: {strftime('%a %b %d %I:%M %p', localtime())}")
        print(u"Elapsed Time {0} (H:M:S)".format(strftime("%H:%M:%S", gmtime(elapse_time))))
        print(f"{'-' * 80}")
        del elapse_time, end_time, start_time
        del gmtime, localtime, strftime, time

    except KeyboardInterrupt:
        raise SystemExit
    except Exception as e:
        raise Exception
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
        # Append the location of this scrip to the System Path
        sys.path.append(os.path.dirname(os.path.dirname(__file__)))

        # Imports
        # ###################### ESA ########################################
##        contacts = {"citRespParty"     : {"rpIndName" : "Nikki Wildart",                      "eMailAdd" : "nikki.wildart@noaa.gov"},
##                        "idPoC"        : {"rpIndName" : "Nikki Wildart",                      "eMailAdd" : "nikki.wildart@noaa.gov"},
##                        "distorCont"   : {"rpIndName" : "NMFS Office of Protected Resources", "eMailAdd" : "nikki.wildart@noaa.gov"},
##                        "mdContact"    : {"rpIndName" : "Nikki Wildart",                      "eMailAdd" : "nikki.wildart@noaa.gov"},
##                        "stepProc"     : [{"rpIndName" : "Nikki Wildart",                      "eMailAdd" : "nikki.wildart@noaa.gov"},
##                                          {"rpIndName" : "Dan Lawson",                         "eMailAdd" : "dan.lawson@noaa.gov"},
##                                          {"rpIndName" : "Jeffrey A. Seminoff",                "eMailAdd" : "jeffrey.seminoff@noaa.gov"},
##                                          {"rpIndName" : "Jennifer Schultz",                   "eMailAdd" : "jennifer.schultz@noaa.gov"},
##                                          {"rpIndName" : "Jonathan Molineaux",                 "eMailAdd" : "jonathan.molineaux@noaa.gov"},
##                                          {"rpIndName" : "Marc Romano",                        "eMailAdd" : "marc.romano@noaa.gov"},
##                                          {"rpIndName" : "Susan Wang",                         "eMailAdd" : "susan.wang@noaa.gov"},
##                                         ],
##                        }

##        contacts = {"citRespParty"     : [{"role"  : "Custodian",        "rpIndName" : "Nikki Wildart",       "eMailAdd" : "nikki.wildart@noaa.gov"},],
##                        "idPoC"        : [{"role"  : "Point of Contact", "rpIndName" : "Nikki Wildart",       "eMailAdd" : "nikki.wildart@noaa.gov"},],
##                        "distorCont"   : [{"role"  : "Distributor",      "rpIndName" : "Nikki Wildart",       "eMailAdd" : "nikki.wildart@noaa.gov"},],
##                        "mdContact"    : [{"role"  : "Author",           "rpIndName" : "Nikki Wildart",       "eMailAdd" : "nikki.wildart@noaa.gov"},],
##                        "stepProc"     : [{"role" : "Processor",        "rpIndName" : "Nikki Wildart",       "eMailAdd" : "nikki.wildart@noaa.gov"},
##                                          {"role" : "Processor",        "rpIndName" : "Dan Lawson",          "eMailAdd" : "dan.lawson@noaa.gov"},
##                                          {"role" : "Processor",        "rpIndName" : "Jeffrey A. Seminoff", "eMailAdd" : "jeffrey.seminoff@noaa.gov"},
##                                          {"role" : "Processor",        "rpIndName" : "Jennifer Schultz",    "eMailAdd" : "jennifer.schultz@noaa.gov"},
##                                          {"role" : "Processor",        "rpIndName" : "Jonathan Molineaux",  "eMailAdd" : "jonathan.molineaux@noaa.gov"},
##                                          {"role" : "Processor",        "rpIndName" : "Marc Romano",         "eMailAdd" : "marc.romano@noaa.gov"},
##                                          {"role" : "Processor",        "rpIndName" : "Susan Wang",          "eMailAdd" : "susan.wang@noaa.gov"},
##                                         ],
##                        }

        base_project_folder = rf"{os.path.dirname(os.path.dirname(__file__))}"
        project_name        = "NMFS_ESA_Critical_Habitat_FeatureClassTemplates2025"
        project_folder      = rf"{base_project_folder}"
        project_gdb         = rf"{project_folder}\{project_name}.gdb"

        main(project_gdb=project_gdb)

        # Declared Variables
        #del contacts, collective_title
        del project_gdb, project_name, project_folder, base_project_folder

        # Imports

    except KeyboardInterrupt:
        raise SystemExit
    except:
        traceback.print_exc()
    else:
        pass
    finally:
        pass
