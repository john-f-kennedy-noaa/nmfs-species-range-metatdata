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

def create_export_folder(export_folder):
    try:
        # Test of the Export folder exists. If not, then create the folder
        if not arcpy.Exists(export_folder):
            arcpy.AddMessage(f"Creating the Export Folder: {os.path.basename(export_folder)}")
            # Execute CreateFolder
            arcpy.management.CreateFolder(os.path.dirname(export_folder), os.path.basename(export_folder))
            msg = "\tCreate the Export Folder:\n\t\t"+arcpy.GetMessages().replace("\n", "\n\t\t")+"\n"
            arcpy.AddMessage(f"{msg}"); del msg
        else:
            arcpy.AddMessage(f"The Export folder Exists: {os.path.basename(export_folder)}")

    except:
        traceback.print_exc()
        raise Exception

def create_schema_report(gdb=""):
    try:
        # Imports

        # Use all of the cores on the machine
        arcpy.env.parallelProcessingFactor = "100%"
        arcpy.env.overwriteOutput = True

        # Define variables
        project_folder = os.path.dirname(gdb)
        scratch_folder = rf"{project_folder}\Scratch"
        scratch_gdb    = rf"{scratch_folder}\scratch.gdb"
        schema_folder  = rf"{project_folder}\Schema"

        create_export_folder(schema_folder)

        arcpy.env.workspace = schema_folder
        fs = arcpy.ListFiles("*")
        for f in fs:
            arcpy.management.Delete(f)
            del f
        del fs

        # Set the workspace environment to local file geodatabase
        arcpy.env.workspace = project_gdb
        # Set the scratchWorkspace environment to local file geodatabase
        arcpy.env.scratchWorkspace = scratch_gdb

        # Clean-up variables
        del scratch_folder, scratch_gdb

        arcpy.AddMessage(f"\n{'--Start' * 10}--\n")

        arcpy.env.workspace = gdb

        fcs = arcpy.ListFeatureClasses()

        arcpy.AddMessage(f"Check feature classes\n")
        for fc in sorted(fcs):
            arcpy.AddMessage(f"{fc}")

            #arcpy.management.GenerateSchemaReport(f"{gdb}\{fc}", schema_folder, fc, ["JSON", "PDF", "HTML", "XLSX"])
            arcpy.management.GenerateSchemaReport(f"{gdb}\{fc}", schema_folder, fc, ["JSON", "HTML"])

            del fc

        del fcs

        arcpy.AddMessage(f"\n{'--End' * 10}--")

        del schema_folder

        del project_folder

        # Imports

        # Function parameters
        del gdb

    except KeyboardInterrupt:
        raise SystemExit
    except arcpy.ExecuteWarning:
        arcpy.AddWarning(arcpy.GetMessages())
    except arcpy.ExecuteError:
        arcpy.AddError(arcpy.GetMessages())
        traceback.print_exc()
        raise Exception
    except Exception as e:
        arcpy.AddError(str(e))
        raise Exception
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
            raise Exception(traceback.print_exc())
    finally:
        # Cleanup
        arcpy.management.ClearWorkspaceCache()

def schema_field_report(gdb=""):
    try:
        # Imports

        # Use all of the cores on the machine
        arcpy.env.parallelProcessingFactor = "100%"
        arcpy.env.overwriteOutput = True

        # Define variables
        project_folder = os.path.dirname(gdb)
        scratch_folder = rf"{project_folder}\Scratch"
        scratch_gdb    = rf"{scratch_folder}\scratch.gdb"
        #schema_folder  = rf"{project_folder}\Schema"
        #create_export_folder(schema_folder)
        #del schema_folder

        # Set the workspace environment to local file geodatabase
        arcpy.env.workspace = project_gdb
        # Set the scratchWorkspace environment to local file geodatabase
        arcpy.env.scratchWorkspace = scratch_gdb

        # Clean-up variables
        del scratch_folder, scratch_gdb

        arcpy.AddMessage(f"\n{'--Start' * 10}--\n")

        arcpy.env.workspace = gdb
        #print(gdb)

        fcs = arcpy.ListFeatureClasses()

        fc_field_report = {}

        arcpy.AddMessage(f"Check if feature classes exists in Project GDB\n")
        for fc in sorted(fcs):
            arcpy.AddMessage(f"{fc}")
            fc_field_report[fc] = {}

            #fc_path = rf"{source_gdb}\{fc}"

            #fields = [f for f in arcpy.ListFields(fc_path) if f.type not in ['Geometry', 'OID'] and not f.name.startswith('Shape_')]
            fields = [f for f in arcpy.ListFields(fc) if f.type not in ['Geometry', 'OID'] and not f.name.startswith('Shape_')]

            for field in fields:

                #arcpy.AddMessage(f"\t{field.name}\n\t\t{field.aliasName}\n\t\t{field.type}\n\t\t{field.length}")

                if field.type == "String":

                    #with arcpy.da.SearchCursor(fc_path, [field.name]) as cursor:
                    with arcpy.da.SearchCursor(fc, [field.name]) as cursor:
                        text_length = 0
                        for row in cursor:
                            if row[0] != None and len(row[0]) > text_length:
                                text_length = len(row[0])
                            else:
                                text_length = text_length
                            del row
                    del cursor

                    fc_field_report[fc][field.name] = [field.aliasName, field.type, field.length, text_length]
                    del text_length
                else:

                    fc_field_report[fc][field.name] = [field.aliasName, field.type, 0, 0]

                del field
            del fields
            #del fc_path
            del fc

        del fcs

        for fc in fc_field_report:

            field_report = fc_field_report[fc]
            fields  = []

            for field in field_report:
                fields.append(field)
                fields.append(field_report[field][0])
                fields.append(field_report[field][1])
                fields.append(field_report[field][2])
                fields.append(field_report[field][3])
                del field

            print(f"{fc}, {', '.join([str(f) for f in fields])}")

            del fields
            del field_report
            del fc
        del fc_field_report

        del project_folder

        arcpy.AddMessage(f"\n{'--End' * 10}--")

        # Imports

        # Function parameters
        del gdb

    except KeyboardInterrupt:
        raise SystemExit
    except arcpy.ExecuteWarning:
        arcpy.AddWarning(arcpy.GetMessages())
    except arcpy.ExecuteError:
        traceback.print_exc()
        arcpy.AddError(arcpy.GetMessages())
        raise Exception
    except Exception as e:
        arcpy.AddError(str(e))
        raise Exception
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
            raise Exception(traceback.print_exc())
    finally:
        # Cleanup
        arcpy.management.ClearWorkspaceCache()

def field_info_report(gdb=""):
    try:
        # Imports

        # Use all of the cores on the machine
        arcpy.env.parallelProcessingFactor = "100%"
        arcpy.env.overwriteOutput = True

        # Define variables
        project_folder = os.path.dirname(gdb)
        scratch_folder = rf"{project_folder}\Scratch"
        scratch_gdb    = rf"{scratch_folder}\scratch.gdb"
        #schema_folder  = rf"{project_folder}\Schema"
        #create_export_folder(schema_folder)
        #del schema_folder

        # Set the workspace environment to local file geodatabase
        arcpy.env.workspace = project_gdb
        # Set the scratchWorkspace environment to local file geodatabase
        arcpy.env.scratchWorkspace = scratch_gdb

        # Clean-up variables
        del scratch_folder, scratch_gdb

        arcpy.AddMessage(f"\n{'--Start' * 10}--\n")

        arcpy.env.workspace = gdb
        #print(gdb)

        new_field_order = {"ID"         : "ID",
                           "SCIENAME"   : "Scientific Name",
                           "COMNAME"    : "Common Name",
                           "LISTENTITY" : "Listed Entity",
                           "DPSESU"     : "Distinct Population Segment or Evolutionarily Significant Unit",
                           "LISTSTATUS" : "Listed Status",
                           "TAXON"      : "Taxon",
                           "LEADOFFICE" : "Lead Office",
                           "FEDREG"     : "Federal Register Rule",
                           "PUBDATE"    : "Publication Date",
                           "EFFECTDATE" : "Effective Date",
                           "CREATEDATE" : "Create Date",
                           "NOTES"      : "Notes",
                           "INPORTURL"  : "InPort URL",
                           "REFERENCE"  : "Reference",
                           "NMFSPAGE"   : "Species Webpage",
                           "PUBLIC"     : "Public Mapper",
                           "LIFESTAGE"  : "Lifestage",
                           "BEHAVIOR"   : "Behavior",
                           "FEATNAME"   : "Feature Name",
                          }

        fcs = arcpy.ListFeatureClasses()

        arcpy.AddMessage(f"Check Field Info\n")
        for fc in sorted(fcs):
            if fc == "AbaloneBlack_20210712":
                arcpy.AddMessage(f"{fc}")

                # Create a fieldinfo object
                fieldinfo = arcpy.FieldInfo()

                # Get the fields from the input
                fields = arcpy.ListFields(fc)

                # Iterate through the input fields and add them to fieldinfo
                for field in fields:
                    if field.type == "OID":
                        # Set the Population to have a ratio split policy
                        fieldinfo.addField(field.name, field.name, "VISIBLE", "NONE")
                    else:
                        fieldinfo.addField(field.name, field.name, "HIDDEN", "NONE")
                    del field
                del fields

                # Make a layer from the feature class
                layer = "temp_layer"
                arcpy.management.MakeFeatureLayer(fc, layer, field_info=fieldinfo)
                del fieldinfo

                arcpy.conversion.FeatureClassToFeatureClass(layer, gdb, fc+"_tmp")

                arcpy.management.Delete(layer)
                del layer

                fields = [f.name for f in arcpy.ListFields(fc) if f.type not in ['Geometry', 'OID'] and not f.name.startswith('Shape_')]

                fc_array = arcpy.da.TableToNumPyArray(fc, fields)
                print(fc_array.dtype)

                del fc_array, fields
            del fc
        del fcs

        del new_field_order

# FeatureclassToFeatureclass exporting only the object id field.  Then export
# the table to a numpy array (TableToNumPyArray), sort the fields there then use
# ExtendTable to join the sorted fields back to the newly created featureclass.


##            fc_field_report[fc] = {}
##
##            fc_path = rf"{source_gdb}\{fc}"
##
##            fields = [f for f in arcpy.ListFields(fc_path) if f.type not in ['Geometry', 'OID'] and not f.name.startswith('Shape_')]
##
##            for field in fields:
##
##                #arcpy.AddMessage(f"\t{field.name}\n\t\t{field.aliasName}\n\t\t{field.type}\n\t\t{field.length}")
##
##                if field.type == "String":
##
##                    with arcpy.da.SearchCursor(fc_path, [field.name]) as cursor:
##                        text_length = 0
##                        for row in cursor:
##                            if row[0] != None and len(row[0]) > text_length:
##                                text_length = len(row[0])
##                            else:
##                                text_length = text_length
##                            del row
##                    del cursor
##
##                    fc_field_report[fc][field.name] = [field.aliasName, field.type, field.length, text_length]
##                    del text_length
##                else:
##
##                    fc_field_report[fc][field.name] = [field.aliasName, field.type, 0, 0]
##
##                del field
##            del fields
##            del fc_path
##            del fc
##
##        del fcs
##
##        for fc in fc_field_report:
##
##            field_report = fc_field_report[fc]
##            fields  = []
##
##            for field in field_report:
##                fields.append(field)
##                fields.append(field_report[field][0])
##                fields.append(field_report[field][1])
##                fields.append(field_report[field][2])
##                fields.append(field_report[field][3])
##                del field
##
##            print(f"{fc}, {', '.join([str(f) for f in fields])}")
##
##            del fields
##            del field_report
##            del fc
##        del fc_field_report

        del project_folder

        arcpy.AddMessage(f"\n{'--End' * 10}--")

        # Imports

        # Function parameters
        del gdb

    except KeyboardInterrupt:
        raise SystemExit
    except arcpy.ExecuteWarning:
        arcpy.AddWarning(arcpy.GetMessages())
    except arcpy.ExecuteError:
        arcpy.AddError(arcpy.GetMessages())
        traceback.print_exc()
    except Exception as e:
        arcpy.AddError(str(e))
        traceback.print_exc()
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
            raise Exception(traceback.print_exc())
    finally:
        # Cleanup
        arcpy.management.ClearWorkspaceCache()


# Main function
def main():
    try:

        SchemaFieldReport = False
        if SchemaFieldReport:
            schema_field_report(gdb=project_gdb)
        del SchemaFieldReport

        CreateSchemaReport = False
        if CreateSchemaReport:
            create_schema_report(gdb=project_gdb)
        del CreateSchemaReport

        FieldInfoReport = False
        if FieldInfoReport:
            field_info_report(gdb=project_gdb)
        del FieldInfoReport

    except:
        traceback.print_exc()
        raise Exception

if __name__ == '__main__':
    try:
        from time import gmtime, localtime, strftime, time

        # Set a start time so that we can see how log things take
        start_time = time()

        print(f"{'-' * 90}")
        print(f"Python Script:  {os.path.basename(__file__)}")
        print(f"Location:       {os.path.dirname(__file__)}")
        print(f"Python Version: {sys.version} Environment: {os.path.basename(sys.exec_prefix)}")
        print(f"{'-' * 90}\n")
        project_folder = os.path.dirname(__file__)
        project_gdb    = rf"{project_folder}\National Mapper.gdb"
        #source_gdb     = rf"{project_folder}\NMFS_ESA_Range_20241121.gdb"
        source_gdb     = rf"{project_folder}\NMFS_ESA_Range.gdb"

        del project_folder

        main()

        del project_gdb, source_gdb

        # Elapsed time
        end_time = time()
        elapse_time =  end_time - start_time

        print(f"\n{'-' * 90}")
        print(f"Python script: {os.path.basename(__file__)} successfully completed {strftime('%a %b %d %I:%M %p', localtime())}")
        print(u"Elapsed Time {0} (H:M:S)".format(strftime("%H:%M:%S", gmtime(elapse_time))))
        print(f"{'-' * 90}")
        del elapse_time, end_time, start_time
        del gmtime, localtime, strftime, time

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