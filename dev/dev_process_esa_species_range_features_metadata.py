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
import traceback, inspect
import importlib

# Third-party modules are loaded second
import arcpy

# Append the location of this scrip to the System Path
#sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

def check_repair_geometry(fc_path):
    try:
        # Check Geometry
        fc  = os.path.basename(fc_path)
        gdb = os.path.dirname(fc_path)

        bad_geometry_fcs = {}

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
                    bad_geometry_fcs[os.path.basename(row[0])] = {"CLASS" : row[0], "FEATURE_ID" : row[1], "PROBLEM" : row[2]}
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
    else:
        try:
            remaining_keys = [key for key in locals().keys() if not key.startswith('__') and "bad_geometry_fcs" not in key]
            if remaining_keys:
                arcpy.AddWarning(f"Remaining Keys in '{inspect.stack()[0][3]}': ##--> '{', '.join(remaining_keys)}' <--## Line Number: {traceback.extract_stack()[-1].lineno}")
            else:
                pass
            del remaining_keys
            return bad_geometry_fcs
        except:
            traceback.print_exc()
    finally:
        pass

def copy_feature_classes(project_gdb=str(), source_gdb=str()):
    try:
        # Imports

        # Use all of the cores on the machine
        arcpy.env.parallelProcessingFactor = "100%"
        arcpy.env.overwriteOutput = True

        # Define variables
        project_folder = os.path.dirname(project_gdb)
        scratch_folder = rf"{project_folder}\Scratch"
        scratch_gdb    = rf"{scratch_folder}\scratch.gdb"
        #export_folder  = rf"{project_folder}\Export"
        #layers_folder  = rf"{project_folder}\Layers"

        # Set the workspace environment to local file geodatabase
        arcpy.env.workspace = project_gdb
        # Set the scratchWorkspace environment to local file geodatabase
        arcpy.env.scratchWorkspace = scratch_gdb

        # Clean-up variables
        del scratch_folder, scratch_gdb

        arcpy.AddMessage(f"\n{'--Start' * 10}--\n")

        # work

        # Change workspace to get a list of source feature classes
        arcpy.env.workspace = source_gdb
        source_fcs = arcpy.ListFeatureClasses()
        #print(source_gdb)
        #print(source_fcs)

        # Change back to get a list of destination feature classes
        arcpy.env.workspace = project_gdb
        destination_fcs = arcpy.ListFeatureClasses()

        bad_geometry_fcs = {}

        if source_fcs:
            arcpy.AddMessage(f"Check if feature classes exists in Project GDB\n")
            for source_fc in sorted(source_fcs):
                #if source_fc == "AbaloneBlack_20210712":

                arcpy.AddMessage(f"Source Feature Class: {source_fc}")
                source_fc_path      = rf"{source_gdb}\{source_fc}"
                destination_fc      = source_fc
                destination_fc_path = rf"{project_gdb}\{destination_fc}"

                # Copy Features
                arcpy.AddMessage(f"\tCopy Features from '{source_fc}'")
                arcpy.management.CopyFeatures(source_fc_path, destination_fc_path+"_tmp")
                arcpy.AddMessage("\t\tCopy Features:\n\t\t\t"+arcpy.GetMessages().replace("\n", "\n\t\t\t")+"\n")

                fc_fields = [f for f in arcpy.ListFields(destination_fc_path+"_tmp") if f.type not in ['Geometry', 'OID'] and f.name not in ['Shape_Length', 'Shape_Area']]
                for fc_field in fc_fields:
                    if fc_field.name == "Shape_Leng":
                        arcpy.AddMessage(f"\t\tRemoving the 'Shape_Leng' field")
                        fc_fields.remove(fc_field)
                        arcpy.management.DeleteField(destination_fc_path+"_tmp", "Shape_Leng")

                    if fc_field.name in ["FR", "FRN"]:
                        arcpy.AddMessage(f"\t\tRenaming the 'FR' and 'FRN' fields to 'FEDREG'")
                        arcpy.management.AlterField(destination_fc_path+"_tmp", fc_field.name, "FEDREG")

                    if fc_field.name in ["NMFSWEBPAG"]:
                        arcpy.AddMessage(f"\t\tRenaming the 'NMFSWEBPAG' field to 'NMFSPAGE'")
                        arcpy.management.AlterField(destination_fc_path+"_tmp", fc_field.name, "NMFSPAGE")

                    if fc_field.name == "ID":
                        arcpy.AddMessage(f"\t\tChanging the field type for ID")
                        arcpy.management.AlterField(destination_fc_path+"_tmp", fc_field.name, "ID2")
                        arcpy.management.AddField(destination_fc_path+"_tmp", "ID", "TEXT", field_length = 10, field_alias = "Distinct Population Segment or Evolutionarily Significant Unit")
                        arcpy.management.CalculateField(
                                                        in_table        = destination_fc_path+"_tmp",
                                                        field           = "ID",
                                                        expression      = "str(int(!ID2!))",
                                                        expression_type = "PYTHON3",
                                                        code_block      = "",
                                                        field_type      = "TEXT",
                                                        enforce_domains = "NO_ENFORCE_DOMAINS"
                                                        )
                        arcpy.management.DeleteField(destination_fc_path+"_tmp", "ID2")

                    field_names = [f.name for f in arcpy.ListFields(destination_fc_path+"_tmp") if f.type not in ['Geometry', 'OID'] and f.name not in ['Shape_Length', 'Shape_Area']]
                    if "DPSESU" not in field_names:
                        arcpy.AddMessage(f"\t\tAdding the 'DPSESU' field")
                        arcpy.management.AddField(destination_fc_path+"_tmp", "DPSESU", "TEXT", field_length = 100, field_alias = "Distinct Population Segment or Evolutionarily Significant Unit")
                    if "FEDREGURL" not in field_names:
                        arcpy.AddMessage(f"\t\tAdding the 'FEDREGURL' field")
                        arcpy.management.AddField(destination_fc_path+"_tmp", "FEDREGURL", "TEXT", field_length = 500, field_alias = "Distinct Population Segment or Evolutionarily Significant Unit")
                    del field_names
                    del fc_field
                del fc_fields

                if source_fc.startswith("CoralMountainousStar") or source_fc.startswith("CoralPillar") or source_fc.startswith("CoralRoughCactus"):
                    arcpy.management.CalculateField(
                                                    in_table        = destination_fc_path+"_tmp",
                                                    field           = "FEDREG",
                                                    expression      = '"79 FR 53852"',
                                                    expression_type = "PYTHON3",
                                                    code_block      = "",
                                                    field_type      = "TEXT",
                                                    enforce_domains = "NO_ENFORCE_DOMAINS"
                                                   )

                new_field_alias = {"ID"         : "ID",
                                   "SCIENAME"   : "Scientific Name",
                                   "COMNAME"    : "Common Name",
                                   "LISTENTITY" : "Listed Entity",
                                   "DPSESU"     : "Distinct Population Segment or Evolutionarily Significant Unit",
                                   "LISTSTATUS" : "Listed Status",
                                   "TAXON"      : "Taxon",
                                   "LEADOFFICE" : "Lead Office",
                                   "FEDREG"     : "Federal Register Rule",
                                   "FEDREGURL"  : "Federal Register Rule URL",
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

                arcpy.AddMessage(f"Updating Field Alias")
                field_names = [f.name for f in arcpy.ListFields(destination_fc_path+"_tmp") if f.type not in ['Geometry', 'OID'] and f.name not in ['Shape_Length', 'Shape_Area']]
                for field_name in field_names:
                    #print(len(new_field_alias[field_name]))
                    arcpy.management.AlterField(destination_fc_path+"_tmp", field_name, field_name, new_field_alias[field_name])
                    del field_name
                del field_names
                del new_field_alias

                bad_geometry_fc = check_repair_geometry(destination_fc_path+"_tmp")

                if bad_geometry_fc:
                    for key in bad_geometry_fc:
                        if key not in bad_geometry_fcs:
                            bad_geometry_fcs[key] = bad_geometry_fc[key]
                        del key

                del bad_geometry_fc

    ##        field_description = [
    ##                             ["FeatureClass", "TEXT", "Feature Class", 50, "#", "#"],
    ##                             ["ID",           "TEXT", "ID", 10, "#", "#"],
    ##                             ["SCIENAME",     "TEXT", "Scientific Name", 50, "#", "#"],
    ##                             ["COMNAME",      "TEXT", "Common Name", 50, "#", "#"],
    ##                             ["LISTENTITY",   "TEXT", "Listed Entity", 100, "#", "#"],
    ##                             ["DPSESU",       "TEXT", "Distinct Population Segment or Evolutionarily Significant Unit", 100, "#", "#"],
    ##                             ["LISTSTATUS",   "TEXT", "Listed Status", 50, "#", "#"],
    ##                             ["TAXON",        "TEXT", "Taxon", 50, "#", "#"],
    ##                             ["LEADOFFICE",   "TEXT", "Lead Office", 50, "#", "#"],
    ##                             ["FEDREG",       "TEXT", "Federal Register Rule", 50, "#", "#"],
    ##                             ["FEDREGURL",    "TEXT", "Federal Register Rule URL", 500, "#", "#"],
    ##                             ["PUBDATE",      "TEXT", "Publication Date", 25, "#", "#"],
    ##                             ["EFFECTDATE",   "TEXT", "Effective Date", 25, "#", "#"],
    ##                             ["CREATEDATE",   "TEXT", "Create Date", 25, "#", "#"],
    ##                             ["NOTES",        "TEXT", "Notes", 500, "#", "#"],
    ##                             ["INPORTURL",    "TEXT", "InPort URL", 250, "#", "#"],
    ##                             ["REFERENCE",    "TEXT", "Reference", 1000, "#", "#"],
    ##                             ["NMFSPAGE",     "TEXT", "Species Webpage", 250, "#", "#"],
    ##                             ["PUBLIC",       "TEXT", "Public Mapper", 5, "#", "#"],
    ##                             ["LIFESTAGE",    "TEXT", "Lifestage", 50, "#", "#"],
    ##                             ["BEHAVIOR",     "TEXT", "Behavior", 50, "#", "#"],
    ##                             ["FEATNAME",     "TEXT", "Feature Name", 250, "#", "#"],
    ##                            ]

                arcpy.AddMessage(f"\tExport Features for '{source_fc}'")
                arcpy.conversion.ExportFeatures(
                                                in_features             = destination_fc_path+"_tmp",
                                                out_features            = destination_fc_path,
                                                where_clause            = "",
                                                use_field_alias_as_name = "NOT_USE_ALIAS",
                                                field_mapping           = rf'ID "ID" true true false 10 Text 0 0,First,#,{destination_fc_path+"_tmp"},ID,0,9;SCIENAME "Scientific Name" true true false 50 Text 0 0,First,#,{destination_fc_path+"_tmp"},SCIENAME,0,49;COMNAME "Common Name" true true false 50 Text 0 0,First,#,{destination_fc_path+"_tmp"},COMNAME,0,49;LISTENTITY "Listed Entity" true true false 100 Text 0 0,First,#,{destination_fc_path+"_tmp"},LISTENTITY,0,99;DPSESU "Distinct Population Segment or Evolutionarily Significant Unit" true true false 100 Text 0 0,First,#,{destination_fc_path+"_tmp"},DPSESU,0,99;LISTSTATUS "Listed Status" true true false 50 Text 0 0,First,#,{destination_fc_path+"_tmp"},LISTSTATUS,0,49;TAXON "Taxon" true true false 50 Text 0 0,First,#,{destination_fc_path+"_tmp"},TAXON,0,49;LEADOFFICE "Lead Office" true true false 50 Text 0 0,First,#,{destination_fc_path+"_tmp"},LEADOFFICE,0,49;FEDREG "Federal Register Rule" true true false 50 Text 0 0,First,#,{destination_fc_path+"_tmp"},FEDREG,0,49;FEDREGURL "Federal Register Rule URL" true true false 500 Text 0 0,First,#,{destination_fc_path+"_tmp"},FEDREGURL,0,499;PUBDATE "Publication Date" true true false 25 Text 0 0,First,#,{destination_fc_path+"_tmp"},PUBDATE,0,24;EFFECTDATE "Effective Date" true true false 25 Text 0 0,First,#,{destination_fc_path+"_tmp"},EFFECTDATE,0,24;CREATEDATE "Create Date" true true false 25 Text 0 0,First,#,{destination_fc_path+"_tmp"},CREATEDATE,0,24;NOTES "Notes" true true false 500 Text 0 0,First,#,{destination_fc_path+"_tmp"},NOTES,0,499;INPORTURL "InPort URL" true true false 250 Text 0 0,First,#,{destination_fc_path+"_tmp"},INPORTURL,0,249;REFERENCE "Reference" true true false 1000 Text 0 0,First,#,{destination_fc_path+"_tmp"},REFERENCE,0,999;NMFSPAGE "Species Webpage" true true false 250 Text 0 0,First,#,{destination_fc_path+"_tmp"},NMFSPAGE,0,249;PUBLIC "Public Mapper" true true false 5 Text 0 0,First,#,{destination_fc_path+"_tmp"},PUBLIC,0,4;LIFESTAGE "Lifestage" true true false 50 Text 0 0,First,#,{destination_fc_path+"_tmp"},LIFESTAGE,0,49;BEHAVIOR "Behavior" true true false 50 Text 0 0,First,#,{destination_fc_path+"_tmp"},BEHAVIOR,0,49;FEATNAME "Feature Name" true true false 250 Text 0 0,First,#,{destination_fc_path+"_tmp"},FEATNAME,0,249;Shape_Length "Shape_Length" false true true 8 Double 0 0,First,#,{destination_fc_path+"_tmp"},Shape_Length,-1,-1;Shape_Area "Shape_Area" false true true 8 Double 0 0,First,#,{destination_fc_path+"_tmp"},Shape_Area,-1,-1',
                                                sort_field              = None
                                               )
                arcpy.AddMessage("\t\tExport Features:\n\t\t\t"+arcpy.GetMessages().replace("\n", "\n\t\t\t")+"\n")

                arcpy.management.Delete(destination_fc_path+"_tmp")

                del destination_fc, destination_fc_path
                del source_fc_path
                del source_fc
        else:
            print("No source fcs to process")

        arcpy.AddMessage(f"\tCompact GDB")
        arcpy.management.Compact(project_gdb)
        arcpy.AddMessage("\t\tCompact GDB:\n\t\t\t"+arcpy.GetMessages().replace("\n", "\n\t\t\t")+"\n")

        if bad_geometry_fcs:
            arcpy.AddMessage(f"Feature Classes with bad geometry")
            for bad_geometry_fc in sorted(bad_geometry_fcs):
                arcpy.AddMessage(f"\tFeature Class: {bad_geometry_fc}\n\t\tFeature ID: {bad_geometry_fcs[bad_geometry_fc]['FEATURE_ID']}\n\t\tProblem: {bad_geometry_fcs[bad_geometry_fc]['PROBLEM']}")
                del bad_geometry_fc

##            Feature Classes with bad geometry
##                Feature Class: CoralLobedStar_20210730
##                    Feature ID: 1
##                    Problem: self intersections
##                Feature Class: CoralMountainousStar_20210801
##                    Feature ID: 1
##                    Problem: self intersections
##                Feature Class: RockfishYelloweye_20240502
##                    Feature ID: 1
##                    Problem: self intersections
##                Feature Class: SealRinged_20210228
##                    Feature ID: 2
##                    Problem: self intersections

        del bad_geometry_fcs

        del source_fcs

        del destination_fcs
        del project_folder

        arcpy.AddMessage(f"\n{'--End' * 10}--")

        # Imports

        # Function parameters
        del project_gdb, source_gdb

    #except Exception as e:
    #    raise Exception(e)
    except arcpy.ExecuteWarning:
        arcpy.AddWarning(arcpy.GetMessages())
    except arcpy.ExecuteError:
        arcpy.AddError(arcpy.GetMessages())
    except:
        traceback.print_exc()
    else:
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: raise Warning(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        # Cleanup
        arcpy.management.ClearWorkspaceCache()

def create_species_range_table(project_gdb="", version=""):
    try:
        # Imports

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

        arcpy.AddMessage(f"\n{'--Start' * 10}--\n")

        fcs = arcpy.ListFeatureClasses("*")

        species_range_table = arcpy.management.CreateTable(project_gdb, f"SpeciesRangeTable{version}")

        field_description = [
                             ["FeatureClass", "TEXT", "Feature Class", 50, "#", "#"],
                             ["ID",           "TEXT", "ID", 10, "#", "#"],
                             ["SCIENAME",     "TEXT", "Scientific Name", 50, "#", "#"],
                             ["COMNAME",      "TEXT", "Common Name", 50, "#", "#"],
                             ["LISTENTITY",   "TEXT", "Listed Entity", 100, "#", "#"],
                             ["DPSESU",       "TEXT", "Distinct Population Segment or Evolutionarily Significant Unit", 100, "#", "#"],
                             ["LISTSTATUS",   "TEXT", "Listed Status", 50, "#", "#"],
                             ["TAXON",        "TEXT", "Taxon", 50, "#", "#"],
                             ["LEADOFFICE",   "TEXT", "Lead Office", 50, "#", "#"],
                             ["FEDREG",       "TEXT", "Federal Register Rule", 50, "#", "#"],
                             ["FEDREGURL",    "TEXT", "Federal Register Rule URL", 500, "#", "#"],
                             ["PUBDATE",      "TEXT", "Publication Date", 25, "#", "#"],
                             ["EFFECTDATE",   "TEXT", "Effective Date", 25, "#", "#"],
                             ["CREATEDATE",   "TEXT", "Create Date", 25, "#", "#"],
                             ["NOTES",        "TEXT", "Notes", 500, "#", "#"],
                             ["INPORTURL",    "TEXT", "InPort URL", 250, "#", "#"],
                             ["REFERENCE",    "TEXT", "Reference", 1000, "#", "#"],
                             ["NMFSPAGE",     "TEXT", "Species Webpage", 250, "#", "#"],
                             ["PUBLIC",       "TEXT", "Public Mapper", 5, "#", "#"],
                             ["LIFESTAGE",    "TEXT", "Lifestage", 50, "#", "#"],
                             ["BEHAVIOR",     "TEXT", "Behavior", 50, "#", "#"],
                             ["FEATNAME",     "TEXT", "Feature Name", 250, "#", "#"],
                            ]

        arcpy.management.AddFields(species_range_table, field_description, None)

        del field_description

        #max_length = 0
        arcpy.AddMessage(f"Crate new feature classes in Project GDB\n")
        for fc in sorted(fcs):
            arcpy.AddMessage(f"Feature Class: '{fc}'")
            #if len(fc) > max_length:
            #    max_length = len(fc)
            #arcpy.AddMessage(f"\tCopy Template Feature Class with source name to project GDB")
            #arcpy.management.CopyFeatures(species_range_template, rf"{project_gdb}\{source_fc}")
            #arcpy.AddMessage("\t\tCopy Features:\n\t\t\t"+arcpy.GetMessages().replace("\n", "\n\t\t\t")+"\n")

            fields = [f.name for f in arcpy.ListFields(fc) if f.type not in ['Geometry', 'OID'] and f.name not in ['Shape_Length', 'Shape_Area']]
            with arcpy.da.SearchCursor(fc, fields) as cursor:
                for row in cursor:
                    species_range_table_row = [fc]
                    species_range_table_row.extend(row)
                    #print(f"\t{fc} : {row}")
                    #print(f"\t{species_range_table_row}")

                    insert_fields = [f.name for f in arcpy.ListFields(species_range_table) if f.type not in ['Geometry', 'OID']]
                    #print(insert_fields)
                    # Open an InsertCursor using a context manager
                    with arcpy.da.InsertCursor(species_range_table, insert_fields) as insert_cursor:
                        insert_cursor.insertRow(species_range_table_row)

                    del insert_cursor
                    del insert_fields
                    del species_range_table_row
                    del row
            del fields, cursor
            del fc

        #print(max_length)
        #del max_length

        del species_range_table

        species_range_table = rf"{project_gdb}\SpeciesRangeTable{version}"

        arcpy.AddMessage(f"Table To Excel")
        arcpy.conversion.TableToExcel(
                                      Input_Table                        = species_range_table,
                                      Output_Excel_File                  = rf"{project_folder}\{os.path.basename(species_range_table)}.xlsx",
                                      #Use_field_alias_as_column_header   = "ALIAS",
                                      Use_field_alias_as_column_header   = "NAME",
                                      #Use_domain_and_subtype_description = "DESCRIPTION"
                                      Use_domain_and_subtype_description = "CODE"
                                     )
        arcpy.AddMessage("\tTable to Excel:\n\t\t"+arcpy.GetMessages().replace("\n", "\n\t\t")+"\n")

        del species_range_table, version
        arcpy.management.Compact(project_gdb)
        del fcs
        del project_folder

        arcpy.AddMessage(f"\n{'--End' * 10}--")

        # Imports

        # Function parameters
        del project_gdb

    except:
        traceback.print_exc()
    else:
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: raise Warning(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        # Cleanup
        arcpy.management.ClearWorkspaceCache()

def import_species_range_table(project_gdb="", version=""):
    try:
        # Imports

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

        arcpy.AddMessage(f"\n{'--Start' * 10}--\n")

        species_range_table_xlsx = rf"{project_folder}\SpeciesRangeTable {version}.xlsx"
        species_range_table      = rf"{project_gdb}\SpeciesRangeTable{version}"

        del version

        ExcelToTable = False
        if ExcelToTable:
            arcpy.AddMessage(f"Excel To Table")
            arcpy.conversion.ExcelToTable(
                                          Input_Excel_File = species_range_table_xlsx,
                                          Output_Table     = species_range_table,
                                          Sheet            = "SpeciesRangeTable",
                                          field_names_row  = 1,
                                          cell_range       = "B2:W103"
                                         )
        del ExcelToTable

        del species_range_table_xlsx

        field_report = {}

        CreateFieldLengthReport = False
        if CreateFieldLengthReport:
            arcpy.AddMessage(f"Create field length report")

            arcpy.AddMessage(f"Get list of field names")
            fields = [f for f in arcpy.ListFields(species_range_table) if f.type not in ['OID']]

            arcpy.AddMessage(f"Loop over fields")
            count = 0
            for field in fields:
                count+=1

                #arcpy.AddMessage(f"\t{field.name}\n\t\t{field.aliasName}\n\t\t{field.type}\n\t\t{field.length}")

                if field.type == "String":

                    with arcpy.da.SearchCursor(species_range_table, [field.name]) as cursor:
                        text_length = 0
                        for row in cursor:
                            if row[0] != None and len(row[0]) > text_length:
                                text_length = len(row[0])
                            else:
                                text_length = text_length
                            del row
                    del cursor

                    field_report[field.name] = {"Field Name" : f"{field.name}", "Alias" : f"{field.aliasName}", "Type" : f"{field.type}", "Field Length" : f"{field.length}", "Text Length" : f"{text_length}"}
                    del text_length
                else:
                    field_report[field.name] = {"Field Name" : f"{field.name}", "Alias" : f"{field.aliasName}", "Type" : f"{field.type}", "Field Length" : f"{field.length}", "Text Length" : f"{text_length}"}
                del field
            del fields
            del count

            arcpy.AddMessage(f"Create the CSV file")
            # Feature Class,Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Length, Text Length,,,,,,,,,,
            f = open(f"species ranges field name type length report {version}.csv","w")

            for field in field_report:
                field_info = field_report[field]
                for key in field_info:
                    f.write(f"{key}, {field_info[key]}" + "\n")
                    del key
                f.write("\n")
                del field_info
                del field
            del field_report
            # Python will convert \n to os.linesep
            f.close()
            del f
        del CreateFieldLengthReport
        del field_report

        arcpy.AddMessage("Process Feature Classes")

        fcs = arcpy.ListFeatureClasses("*")

        for fc in sorted(fcs):
            arcpy.AddMessage(f"\tFeature Class: '{fc}'")

            fc_fields = [f.name for f in arcpy.ListFields(fc) if f.type not in ['Geometry', 'OID'] and f.name not in ['Shape_Length', 'Shape_Area']]
            with arcpy.da.SearchCursor(fc, fc_fields) as fc_cursor:
                for fc_row in fc_cursor:
                    range_id = fc_row[0]
                    print(f"\t\tFeaure Class: {fc}, ID: {range_id}")

                    tb_fields = [f.name for f in arcpy.ListFields(species_range_table) if f.type not in ['Geometry', 'OID']]
                    with arcpy.da.SearchCursor(species_range_table, tb_fields, f"FeatureClass = '{fc}' and ID = '{range_id}'") as tb_cursor:
                        for tb_row in tb_cursor:
                            print(f"\t\t\t{tb_row[2:3]}")

                            with arcpy.da.UpdateCursor(fc, fc_fields[1:], f"ID = '{range_id}'") as update_cursor:
                                for update_row in update_cursor:
                                    update_cursor.updateRow(tb_row[2:])
                                    del update_row
                            del update_cursor

                            del tb_row
                    del tb_cursor
                    del tb_fields

                    del range_id
                    del fc_row
            del fc_fields, fc_cursor
            del fc

        del species_range_table
        del fcs

##        #print(max_length)
##        #del max_length
##
##        del species_range_table
##
##        species_range_table = rf"{gdb}\SpeciesRangeTable"
##
##        arcpy.AddMessage(f"Table To Excel")
##        arcpy.conversion.TableToExcel(
##                                      Input_Table                        = species_range_table,
##                                      Output_Excel_File                  = rf"{project_folder}\{os.path.basename(species_range_table)} Out.xlsx",
##                                      #Use_field_alias_as_column_header   = "ALIAS",
##                                      Use_field_alias_as_column_header   = "NAME",
##                                      #Use_domain_and_subtype_description = "DESCRIPTION"
##                                      Use_domain_and_subtype_description = "CODE"
##                                     )
##        arcpy.AddMessage("\tTable to Excel:\n\t\t"+arcpy.GetMessages().replace("\n", "\n\t\t")+"\n")
##
##        del species_range_table
##
##
##        del fcs

        del project_folder

        arcpy.management.Compact(project_gdb)

        arcpy.AddMessage(f"\n{'--End' * 10}--")

        # Imports

        # Function parameters
        del project_gdb

    except:
        traceback.print_exc()
    else:
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: raise Warning(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        # Cleanup
        arcpy.management.ClearWorkspaceCache()

##def export_metadata(project_gdb=""):
##    try:
##        # Imports
##        from arcpy import metadata as md
##        from src.project_tools import pretty_format_xml_file
##
##        # Use all of the cores on the machine
##        arcpy.env.parallelProcessingFactor = "100%"
##        arcpy.env.overwriteOutput = True
##
##        # Define variables
##        project_folder = os.path.dirname(project_gdb)
##        scratch_folder = rf"{project_folder}\Scratch"
##        scratch_gdb    = rf"{scratch_folder}\scratch.gdb"
##        export_folder  = rf"{project_folder}\Export"
##
##        # Set the workspace environment to local file geodatabase
##        arcpy.env.workspace = project_gdb
##        # Set the scratchWorkspace environment to local file geodatabase
##        arcpy.env.scratchWorkspace = scratch_gdb
##
##        # Clean-up variables
##        del scratch_folder, scratch_gdb
##
##        arcpy.AddMessage(f"\n{'--Start' * 10}--\n")
##
##        fcs = arcpy.ListFeatureClasses()
##
##        arcpy.AddMessage(f"Synchronize and export feature classes metadata from Project GDB\n")
##        for fc in sorted(fcs):
##            arcpy.AddMessage(f"Exporting the metadata record for: '{fc}'")
##
##            fc_path = rf"{project_gdb}\{fc}"
##
##            export_xml_metadata_path = rf"{export_folder}\{fc}.xml"
##
##            dataset_md = md.Metadata(fc_path)
##            dataset_md.synchronize("ALWAYS")
##            dataset_md.save()
##            dataset_md.reload()
##            dataset_md.saveAsXML(export_xml_metadata_path, "REMOVE_ALL_SENSITIVE_INFO")
##            #if dataset_md.thumbnailUri:
##            #    arcpy.management.Copy(dataset_md.thumbnailUri, rf"{export_folder}\{fc} Thumbnail.jpg")
##            #    arcpy.management.Copy(dataset_md.thumbnailUri, rf"{export_folder}\{fc} Browse Graphic.jpg")
##
##            del dataset_md
##
##            if arcpy.Exists(export_xml_metadata_path):
##                pretty_format_xml_file(export_xml_metadata_path)
##            else:
##                pass
##
##            del export_xml_metadata_path
##            del fc, fc_path
##
##        del fcs
##        del project_folder, export_folder
##
##        arcpy.AddMessage(f"\n{'--End' * 10}--")
##
##        # Imports
##        del md, pretty_format_xml_file
##        # Function parameters
##        del project_gdb
##
##    #except Exception as e:
##    #    raise Exception(e)
##    except arcpy.ExecuteWarning:
##        arcpy.AddWarning(arcpy.GetMessages())
##    except arcpy.ExecuteError:
##        arcpy.AddError(arcpy.GetMessages())
##    except:
##        traceback.print_exc()
##    else:
##        # While in development, leave here. For test, move to finally
##        rk = [key for key in locals().keys() if not key.startswith('__')]
##        if rk: raise Warning(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
##        return True
##    finally:
##        # Cleanup
##        arcpy.management.ClearWorkspaceCache()

##def import_metadata(project_gdb=""):
##    try:
##        # Imports
##        from arcpy import metadata as md
##
##        # Use all of the cores on the machine
##        arcpy.env.parallelProcessingFactor = "100%"
##        arcpy.env.overwriteOutput = True
##
##        # Define variables
##        project_folder = os.path.dirname(project_gdb)
##        scratch_folder = rf"{project_folder}\Scratch"
##        scratch_gdb    = rf"{scratch_folder}\scratch.gdb"
##        export_folder  = rf"{project_folder}\Export"
##
##        # Set the workspace environment to local file geodatabase
##        arcpy.env.workspace = project_gdb
##        # Set the scratchWorkspace environment to local file geodatabase
##        arcpy.env.scratchWorkspace = scratch_gdb
##
##        # Clean-up variables
##        del scratch_folder, scratch_gdb
##
##        arcpy.AddMessage(f"\n{'--Start' * 10}--\n")
##
##        arcpy.env.workspace = project_gdb
##
##        fcs = arcpy.ListFeatureClasses()
##
##        arcpy.AddMessage(f"Import and synchronize feature classes metadata from Project GDB\n")
##        for fc in sorted(fcs):
##            arcpy.AddMessage(f"Importing the metadata record for: '{fc}'")
##
##            fc_path = rf"{project_gdb}\{fc}"
##
##            import_xml_metadata_path = rf"{export_folder}\{fc}.xml"
##            #import_xml_metadata_path = rf"{project_folder}\SpeciesRangeMetadataTemplate.xml"
##
##            #import_xml_md = md.Metadata(import_xml_metadata_path)
##
##            dataset_md = md.Metadata(fc_path)
##            dataset_md.synchronize('ALWAYS')
##            dataset_md.save()
##
##            #if not dataset_md.isReadOnly:
##            #dataset_md.copy(import_xml_md)
##            dataset_md.importMetadata(import_xml_metadata_path)
##            dataset_md.save()
##            dataset_md.synchronize('SELECTIVE')
##            dataset_md.save()
##            dataset_md.title = dataset_md.title.replace("_", " ")
##            dataset_md.save()
##            dataset_md.synchronize('ALWAYS')
##            dataset_md.save()
##            del dataset_md
##            #del import_xml_md
##
##            del import_xml_metadata_path
##            del fc, fc_path
##
##        del fcs
##        del project_folder, export_folder
##
##        arcpy.AddMessage(f"\n{'--End' * 10}--")
##
##        # Imports
##        del md
##        # Function parameters
##        del project_gdb
##
##    except KeyboardInterrupt:
##        raise SystemExit
##    except arcpy.ExecuteWarning:
##        arcpy.AddWarning(arcpy.GetMessages())
##        traceback.print_exc()
##    except arcpy.ExecuteError:
##        arcpy.AddError(arcpy.GetMessages())
##        traceback.print_exc()
##        raise Exception
##    except Exception as e:
##        arcpy.AddError(str(e))
##        traceback.print_exc()
##        raise Exception
##    except:
##        traceback.print_exc()
##    else:
##        try:
##            remaining_keys = [key for key in locals().keys() if not key.startswith('__')]
##            if remaining_keys:
##                arcpy.AddWarning(f"Remaining Keys in '{inspect.stack()[0][3]}': ##--> '{', '.join(remaining_keys)}' <--## Line Number: {traceback.extract_stack()[-1].lineno}")
##            else:
##                pass
##            del remaining_keys
##        except:
##            raise Exception(traceback.print_exc())
##    finally:
##        pass

def schema_field_report(project_gdb=""):
    try:
        # Imports

        # Use all of the cores on the machine
        arcpy.env.parallelProcessingFactor = "100%"
        arcpy.env.overwriteOutput = True

        # Define variables
        project_folder = os.path.dirname(project_gdb)
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

        fcs = arcpy.ListFeatureClasses()

        fc_field_report = {}

        header = []

        arcpy.AddMessage(f"Check if feature classes exists in Project GDB\n")
        for fc in sorted(fcs):
            arcpy.AddMessage(f"{fc}")
            fc_field_report[fc] = {}

            #fc_path = rf"{source_gdb}\{fc}"

            #fields = [f for f in arcpy.ListFields(fc_path) if f.type not in ['Geometry', 'OID'] and not f.name.startswith('Shape_')]
            fields = [f for f in arcpy.ListFields(fc) if f.type not in ['Geometry', 'OID'] and not f.name.startswith('Shape_')]

            if not header:
                header.append("Feature Class")
                header.extend(["Field Name", "Alias", "Type", "Field Length", "Text Length"] * len(fields))

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

        # Feature Class,Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Field Length, Text Length, Field, Alias, Type,Length, Text Length,,,,,,,,,,
        f = open('species ranges field name type length report 20241209.csv','w')
        f.write(", ".join(header) + '\n') #Give your csv text here.


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

            #print(f"{fc}, {', '.join([str(f) for f in fields])}")

            f.write(f"{fc}, {', '.join([str(f) for f in fields])}" + "\n")

            del fields
            del field_report
            del fc
        del fc_field_report

        ## Python will convert \n to os.linesep
        f.close()

        del f

        del header
        del project_folder

        arcpy.AddMessage(f"\n{'--End' * 10}--")

        # Imports

        # Function parameters
        del project_gdb

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

##def update_metadata(project_gdb=""):
##    try:
##        # Imports
##        from arcpy import metadata as md
##        from lxml import etree
##        from io import StringIO
##
##        # Use all of the cores on the machine
##        arcpy.env.parallelProcessingFactor = "100%"
##        arcpy.env.overwriteOutput = True
##
##        # Define variables
##        project_folder = os.path.dirname(project_gdb)
##        scratch_folder = rf"{project_folder}\Scratch"
##        scratch_gdb    = rf"{scratch_folder}\scratch.gdb"
##        export_folder  = rf"{project_folder}\Export"
##
##        create_export_folder(export_folder)
##
##        # Set the workspace environment to local file geodatabase
##        arcpy.env.workspace = project_gdb
##        # Set the scratchWorkspace environment to local file geodatabase
##        arcpy.env.scratchWorkspace = scratch_gdb
##
##        # Clean-up variables
##        del scratch_folder, scratch_gdb
##
##        arcpy.AddMessage(f"\n{'--Start' * 10}--\n")
##
##        fcs = arcpy.ListFeatureClasses()
##
##        arcpy.AddMessage(f"Synchronize and export feature classes metadata from Project GDB\n")
##        for fc in sorted(fcs):
##            #if fc == "AbaloneBlack_20210712":
##            arcpy.AddMessage(f"Updating the metadata record for: '{fc}'")
##
##            fc_path = rf"{project_gdb}\{fc}"
##
##            # XML Files
##            metadata_template = rf"{project_folder}\SpeciesRangeMetadataTemplate.xml"
##
##            export_xml_metadata_path         = rf"{export_folder}\{fc}.xml"
##            export_xml_metadata_path_updated = rf"{export_folder}\{fc}_Updated.xml"
##
##            dataset_md = md.Metadata(fc_path)
##            dataset_md.synchronize("ALWAYS")
##            dataset_md.save()
##            dataset_md.reload()
##
##            dataset_md.saveAsXML(export_xml_metadata_path, "REMOVE_ALL_SENSITIVE_INFO")
##            dataset_md.saveAsXML(export_xml_metadata_path_updated, "REMOVE_ALL_SENSITIVE_INFO")
##            del dataset_md
##
##            # get the item's metadata xml
##            #metadata_xml_string = dataset_md.xml
##            # Parse the XML file and get the tree
##            #old_tree = etree.parse(StringIO(metadata_xml_string))
##            old_tree = etree.parse(export_xml_metadata_path_updated)
##            new_tree = etree.parse(metadata_template)
##            #del metadata_xml_string
##
##            # Get the root element
##            old_root = old_tree.getroot()
##            new_root = new_tree.getroot()
##
##            # Find the eainfo elements
##            eainfo_old_child = old_root.find("eainfo/detailed")
##            eainfo_new_child = new_root.find("eainfo/detailed")
##            if eainfo_old_child is not None:
##                # Replace child1 with child2
##                parent = eainfo_old_child.getparent()
##                parent.replace(eainfo_old_child, eainfo_new_child)
##                del parent
##            else:
##                arcpy.AddWarning(f"\tFeature Class '{fc}' has no detailed")
##            del eainfo_old_child, eainfo_new_child
##
##            # Find the citRespPart elements
##            idPoC_old_child = old_root.find('dataIdInfo/idPoC')
##            idPoC_new_child = new_root.find('dataIdInfo/idPoC')
##            if idPoC_old_child is not None:
##                # Replace child1 with child2
##                parent = idPoC_old_child.getparent()
##                parent.replace(idPoC_old_child, idPoC_new_child)
##                del parent
##            else:
##                arcpy.AddWarning(f"\tFeature Class '{fc}' has no idPoC")
##            del idPoC_old_child, idPoC_new_child
##
##            # Find the citRespPart elements
##            citRespParty_old_child = old_root.find('dataIdInfo/idCitation/citRespParty')
##            citRespParty_new_child = new_root.find('dataIdInfo/idCitation/citRespParty')
##            if citRespParty_old_child is not None: # and citRespParty_new_child is not None :
##                # Replace child1 with child2
##                parent = citRespParty_old_child.getparent()
##                parent.replace(citRespParty_old_child, citRespParty_new_child)
##                del parent
##            else:
##                arcpy.AddWarning(f"\tFeature Class '{fc}' has no citRespParty")
##            del citRespParty_old_child, citRespParty_new_child
##
##            # Find the citRespPart elements
##            mdContact_old_child = old_root.find('mdContact')
##            mdContact_new_child = new_root.find('mdContact')
##            if mdContact_old_child is not None: # and mdContact_new_child is not None:
##                # Replace child1 with child2
##                parent = mdContact_old_child.getparent()
##                parent.replace(mdContact_old_child, mdContact_new_child)
##                del parent
##            else:
##                arcpy.AddWarning(f"\tFeature Class '{fc}' has no mdContact")
##            del mdContact_old_child, mdContact_new_child
##
##            # Find the distInfo elements
##            distInfo_old_child = old_root.find('distInfo')
##            distInfo_new_child = new_root.find('distInfo')
##            if distInfo_old_child is not None: # and distInfo_new_child is not None:
##                #pass
##                # Replace child1 with child2
##                parent = distInfo_old_child.getparent()
##                parent.replace(distInfo_old_child, distInfo_new_child)
##                del parent
##            else:
##                arcpy.AddWarning(f"\tFeature Class '{fc}' has no distInfo")
##            del distInfo_old_child, distInfo_new_child
##
##            # Find the dqInfo elements
##            dqInfo_old_child = old_root.find('dqInfo')
##            dqInfo_new_child = new_root.find('dqInfo')
##            if dqInfo_old_child is not None: # and dqInfo_new_child is not None:
##                #pass
##                # Replace child1 with child2
##                parent = dqInfo_old_child.getparent()
##                parent.replace(dqInfo_old_child, dqInfo_new_child)
##                del parent
##            else:
##                arcpy.AddWarning(f"\tFeature Class '{fc}' has no dqInfo")
##            del dqInfo_old_child, dqInfo_new_child
##
##            # get modified XML
##            updated_xml_string = etree.tostring(old_root, encoding='UTF-8')
##            del old_root
##
##            with open(export_xml_metadata_path_updated, 'wb') as f:
##                f.write(updated_xml_string)
##            del f
##
##            del updated_xml_string
##
##            del old_tree, new_tree, new_root
##
##            #if dataset_md.thumbnailUri:
##            #    arcpy.management.Copy(dataset_md.thumbnailUri, rf"{export_folder}\{fc} Thumbnail.jpg")
##            #    arcpy.management.Copy(dataset_md.thumbnailUri, rf"{export_folder}\{fc} Browse Graphic.jpg")
##
##            if arcpy.Exists(export_xml_metadata_path):
##                pretty_format_xml_file(export_xml_metadata_path)
##            else:
##                pass
##
##            if arcpy.Exists(export_xml_metadata_path_updated):
##                pretty_format_xml_file(export_xml_metadata_path_updated)
##            else:
##                pass
##
##            if arcpy.Exists(metadata_template):
##                pretty_format_xml_file(metadata_template)
##            else:
##                pass
##
##            del metadata_template
##            del export_xml_metadata_path, export_xml_metadata_path_updated
##            del fc_path
##
##            #
##            del fc
##        del fcs
##        del project_folder, export_folder
##
##        arcpy.AddMessage(f"\n{'--End' * 10}--")
##
##        # Imports
##        del md, StringIO, etree
##        # Function parameters
##        del project_gdb
##
##    except KeyboardInterrupt:
##        raise SystemExit
##    except arcpy.ExecuteWarning:
##        arcpy.AddWarning(arcpy.GetMessages())
##    except arcpy.ExecuteError:
##        traceback.print_exc()
##        arcpy.AddError(arcpy.GetMessages())
##    except Exception:
##        traceback.print_exc()
##    except:
##        traceback.print_exc()
##    else:
##        try:
##            remaining_keys = [key for key in locals().keys() if not key.startswith('__')]
##            if remaining_keys:
##                arcpy.AddWarning(f"Remaining Keys in '{inspect.stack()[0][3]}': ##--> '{', '.join(remaining_keys)}' <--## Line Number: {traceback.extract_stack()[-1].lineno}")
##            else:
##                pass
##            del remaining_keys
##        except:
##            raise Exception(traceback.print_exc())
##    finally:
##        pass

def feature_sharing_draft_report(sd_draft=""):
    try:
        import xml.dom.minidom as DOM

        docs = DOM.parse(sd_draft)
        key_list = docs.getElementsByTagName("Key")
        value_list = docs.getElementsByTagName("Value")

        for i in range(key_list.length):
            value = f"Value: {value_list[i].firstChild.nodeValue}" if value_list[i].firstChild else f"Value is missing"

            arcpy.AddMessage(f"\t\tKey: {key_list[i].firstChild.nodeValue:<45} {value}")
            # arcpy.AddMessage(f"\t\tKey: {key_list[i].firstChild.nodeValue:<45} {value[:50]}")
            del i

        del DOM, key_list, value_list, docs
        del sd_draft

    except KeyboardInterrupt:
        raise SystemExit
    except arcpy.ExecuteWarning:
        arcpy.AddWarning(arcpy.GetMessages())
        traceback.print_exc()
    except arcpy.ExecuteError:
        arcpy.AddError(arcpy.GetMessages())
        traceback.print_exc()
    except Exception as e:
        print(e)
        traceback.print_exc()
    except:
        traceback.print_exc()
    else:
        try:
            leave_out_keys = ["leave_out_keys", "results"]
            remaining_keys = [key for key in locals().keys() if not key.startswith('__') and key not in leave_out_keys]
            if remaining_keys:
                arcpy.AddWarning(f"Remaining Keys in '{inspect.stack()[0][3]}': ##--> '{', '.join(remaining_keys)}' <--## Line Number: {traceback.extract_stack()[-1].lineno}")
            del leave_out_keys, remaining_keys
            return results if "results" in locals().keys() else ["NOTE!! The 'results' variable not yet set!!"]
        except:
            raise SystemExit(traceback.print_exc())
    finally:
        if "results" in locals().keys(): del results
        # Cleanup
        arcpy.management.ClearWorkspaceCache()

def create_feature_class_layers(project_gdb=""):
    try:
        # Import
        from arcpy import metadata as md

        # Set History and Metadata logs, set serverity and message level
        arcpy.SetLogHistory(True) # Look in %AppData%\Roaming\Esri\ArcGISPro\ArcToolbox\History
        arcpy.SetLogMetadata(True)
        arcpy.SetSeverityLevel(1) # 0—A tool will not throw an exception, even if the tool produces an error or warning.
                                  # 1—If a tool produces a warning or an error, it will throw an exception.
                                  # 2—If a tool produces an error, it will throw an exception. This is the default.
        arcpy.SetMessageLevels(['NORMAL']) # NORMAL, COMMANDSYNTAX, DIAGNOSTICS, PROJECTIONTRANSFORMATION

        # Set basic workkpace variables
        project_folder    = os.path.dirname(project_gdb)
        project_file      = rf"{project_folder}\{os.path.basename(project_folder)}.aprx"
        scratch_folder    = rf"{project_folder}\Scratch"
        scratch_workspace = rf"{project_folder}\Scratch\scratch.gdb"

        # Set basic workkpace variables
        arcpy.env.workspace                = project_gdb
        arcpy.env.scratchWorkspace         = scratch_workspace
        arcpy.env.overwriteOutput          = True
        arcpy.env.parallelProcessingFactor = "100%"

        del project_folder, scratch_folder, scratch_workspace

        arcpy.AddMessage(f"{'-' * 80}\n")

        aprx = arcpy.mp.ArcGISProject(project_file)
        home_folder = aprx.homeFolder
        del project_file

        datasets = arcpy.ListFeatureClasses("*")

        for dataset in sorted(datasets):

            feature_service_title = dataset.replace("_", " ")

            arcpy.AddMessage(f"Dataset: {dataset}")
            arcpy.AddMessage(f"\tTitle: {feature_service_title}")

            feature_class_path = rf"{project_gdb}\{dataset}"

            arcpy.AddMessage(f"\tMake Feature Layer")
            feature_class_layer = arcpy.management.MakeFeatureLayer(feature_class_path, feature_service_title)
            feature_class_layer_file = rf"{home_folder}\Layers\{feature_class_layer}.lyrx"

            arcpy.AddMessage(f"\tSave Layer File")
            _result = arcpy.management.SaveToLayerFile(
                                                       in_layer         = feature_class_layer,
                                                       out_layer        = feature_class_layer_file,
                                                       is_relative_path = "RELATIVE",
                                                       version          = "CURRENT"
                                                      )
            del _result

            arcpy.management.Delete(feature_class_layer)
            del feature_class_layer

            layer_file = arcpy.mp.LayerFile(feature_class_layer_file)

            # aprx.listBasemaps() to get a list of available basemaps
            #
            #    ['Charted Territory Map',
            #     'Colored Pencil Map',
            #     'Community Map',
            #     'Dark Gray Canvas',
            #     'Firefly Imagery Hybrid',
            #     'GEBCO Basemap (NOAA NCEI Visualization)',
            #     'GEBCO Basemap/Contours (NOAA NCEI Visualization)',
            #     'GEBCO Gray Basemap (NOAA NCEI Visualization)',
            #     'GEBCO Gray Basemap/Contours (NOAA NCEI Visualization)',
            #     'Human Geography Dark Map',
            #     'Human Geography Map',
            #     'Imagery',
            #     'Imagery Hybrid',
            #     'Light Gray Canvas',
            #     'Mid-Century Map',
            #     'Modern Antique Map',
            #     'National Geographic Style Map',
            #     'Navigation',
            #     'Navigation (Dark)',
            #     'Newspaper Map',
            #     'NOAA Charts',
            #     'NOAA ENC® Charts',
            #     'Nova Map',
            #     'Oceans',
            #     'OpenStreetMap',
            #     'Streets',
            #     'Streets (Night)',
            #     'Terrain with Labels',
            #     'Topographic']

            if aprx.listMaps(feature_service_title):
                aprx.deleteItem(aprx.listMaps(feature_service_title)[0])
                aprx.save()
            else:
                pass

            arcpy.AddMessage(f"\tCreating Map: {feature_service_title}")
            aprx.createMap(f"{feature_service_title}", "Map")
            aprx.save()

            current_map = aprx.listMaps(feature_service_title)[0]

            basemap = "Terrain with Labels"
            current_map.addLayer(layer_file)
            current_map.addBasemap(basemap)
            aprx.save()
            del basemap

            fc_md = md.Metadata(feature_class_path)

            if not fc_md.thumbnailUri:
                arcpy.AddMessage(f"\t\tCreate map thumbnail and update metadata")
                current_map_view = current_map.defaultView
                current_map_view.exportToPNG(
                                             rf"{home_folder}\Layers\{feature_service_title}.png",
                                             width=288,
                                             height=192,
                                             resolution=96,
                                             color_mode="24-BIT_TRUE_COLOR",
                                             embed_color_profile=True,
                                            )
                del current_map_view

                fc_md.thumbnailUri = rf"{home_folder}\Layers\{feature_service_title}.png"
                fc_md.save()

            del fc_md

            in_md = md.Metadata(feature_class_path)
            layer_file.metadata.copy(in_md)
            layer_file.metadata.save()
            layer_file.save()
            current_map.metadata.copy(in_md)
            current_map.metadata.save()
            aprx.save()
            del in_md

            arcpy.AddMessage(f"\t\tLayer File Path:     {layer_file.filePath}")
            arcpy.AddMessage(f"\t\tLayer File Version:  {layer_file.version}")
            arcpy.AddMessage(f"\t\tLayer File Metadata:")
            arcpy.AddMessage(f"\t\t\tLayer File Title:              {layer_file.metadata.title}")
            #arcpy.AddMessage(f"\t\t\tLayer File Tags:               {layer_file.metadata.tags}")
            #arcpy.AddMessage(f"\t\t\tLayer File Summary:            {layer_file.metadata.summary}")
            #arcpy.AddMessage(f"\t\t\tLayer File Description:        {layer_file.metadata.description}")
            #arcpy.AddMessage(f"\t\t\tLayer File Credits:            {layer_file.metadata.credits}")
            #arcpy.AddMessage(f"\t\t\tLayer File Access Constraints: {layer_file.metadata.accessConstraints}")

            arcpy.AddMessage(f"\t\tList of layers or tables in Layer File:")
            if current_map.listLayers(feature_service_title):
                layer = current_map.listLayers(feature_service_title)[0]
            elif current_map.listTables(feature_service_title):
                layer = current_map.listTables(feature_service_title)[0]
            else:
                arcpy.AddWarning(f"Something wrong")

            in_md = md.Metadata(feature_class_path)
            layer.metadata.copy(in_md)
            layer.metadata.save()
            layer_file.save()
            aprx.save()
            del in_md

            arcpy.AddMessage(f"\t\t\tLayer Name: {layer.name}")
            arcpy.AddMessage(f"\t\t\tLayer Metadata:")#
            arcpy.AddMessage(f"\t\t\t\tLayer Title:              {layer.metadata.title}")
            #arcpy.AddMessage(f"\t\t\t\tLayer Tags:               {layer.metadata.tags}")
            #arcpy.AddMessage(f"\t\t\t\tLayer Summary:            {layer.metadata.summary}")
            #arcpy.AddMessage(f"\t\t\t\tLayer Description:        {layer.metadata.description}")
            #arcpy.AddMessage(f"\t\t\t\tLayer Credits:            {layer.metadata.credits}")
            #arcpy.AddMessage(f"\t\t\t\tLayer Access Constraints: {layer.metadata.accessConstraints}")
            del layer
            del layer_file
            del feature_class_layer_file
            del feature_class_path

            aprx.deleteItem(current_map)
            del current_map
            aprx.save()

            del feature_service_title
            del dataset

        del datasets

        arcpy.AddMessage(f"\n{'-' * 90}\n")

        # Declared Variables set in function
        del aprx
        del home_folder

        # Imports
        del md

        # Function Parameters
        del project_gdb

    except KeyboardInterrupt:
        raise SystemExit
    except arcpy.ExecuteWarning:
        arcpy.AddWarning(arcpy.GetMessages())
        traceback.print_exc()
    except arcpy.ExecuteError:
        arcpy.AddError(arcpy.GetMessages())
        traceback.print_exc()
    except Exception as e:
        print(e)
        traceback.print_exc()
    except:
        traceback.print_exc()
    else:
        try:
            remaining_keys = [key for key in locals().keys() if not key.startswith('__')]
            if remaining_keys:
                arcpy.AddWarning(f"Remaining Keys in '{inspect.stack()[0][3]}': ##--> '{', '.join(remaining_keys)}' <--## Line Number: {traceback.extract_stack()[-1].lineno}")
            del remaining_keys
        except:
            traceback.print_exc()
            raise SystemExit
    finally:
        # Cleanup
        arcpy.management.ClearWorkspaceCache()

def get_feature_service_list():
    try:
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        del urllib3

        import datetime as dt
        from arcgis.gis import GIS

        gis = GIS("pro")

        day_start = dt.datetime(2024, 12, 30, 0, 0, 0, 0)
        day_end = dt.datetime(2025, 1, 10, 23, 59, 59, 999999)

        start_timestamp = int(day_start.timestamp() * 1000)
        end_timestamp = int(day_end.timestamp() * 1000)

        del day_start, day_end

        titles = [item.title for item in gis.content.search(query=f"owner:{gis.users.me.username}", item_type="Feature Service", max_items=1000) if item.created > start_timestamp and item.created < end_timestamp]

        #for title in sorted(titles):
        #    print(title)
        #    del title

        del end_timestamp, start_timestamp

        #del titles

        # Declared Variables
        del gis

        # Imports
        del GIS, dt

    except:
        traceback.print_exc()
    else:
        return titles
    finally:
        try:
            if "titles" in locals().keys(): del titles
            remaining_keys = [key for key in locals().keys() if not key.startswith('__')]
            if remaining_keys:
                arcpy.AddWarning(f"Remaining Keys in '{inspect.stack()[0][3]}': ##--> '{', '.join(remaining_keys)}' <--## Line Number: {traceback.extract_stack()[-1].lineno}")
            del remaining_keys
            # Cleanup
            arcpy.management.ClearWorkspaceCache()
        except:
            traceback.print_exc()

def create_feature_class_services(project_gdb=""):
    try:
        # Import
        from arcpy import metadata as md

        # Set History and Metadata logs, set serverity and message level
        arcpy.SetLogHistory(True) # Look in %AppData%\Roaming\Esri\ArcGISPro\ArcToolbox\History
        arcpy.SetLogMetadata(True)
        arcpy.SetSeverityLevel(1) # 0—A tool will not throw an exception, even if the tool produces an error or warning.
                                  # 1—If a tool produces a warning or an error, it will throw an exception.
                                  # 2—If a tool produces an error, it will throw an exception. This is the default.
        arcpy.SetMessageLevels(['NORMAL']) # NORMAL, COMMANDSYNTAX, DIAGNOSTICS, PROJECTIONTRANSFORMATION

        # Set basic workkpace variables
        project_folder    = os.path.dirname(project_gdb)
        project_file      = rf"{project_folder}\{os.path.basename(project_folder)}.aprx"
        scratch_folder    = rf"{project_folder}\Scratch"
        scratch_workspace = rf"{project_folder}\Scratch\scratch.gdb"

        # Set basic workkpace variables
        arcpy.env.workspace                = project_gdb
        arcpy.env.scratchWorkspace         = scratch_workspace
        arcpy.env.overwriteOutput          = True
        arcpy.env.parallelProcessingFactor = "100%"

        del project_folder, scratch_folder, scratch_workspace

        arcpy.AddMessage(f"\n{'-' * 90}\n")

        feature_service_list = get_feature_service_list()

        #for feature_service in feature_service_list:
        #    arcpy.AddMessage(feature_service)
        #    del feature_service

        aprx = arcpy.mp.ArcGISProject(project_file)
        home_folder = aprx.homeFolder

        #feature_service_list.append("SealGuadalupeFur_20210228")
        datasets = [ds for ds in arcpy.ListFeatureClasses("*") if ds not in feature_service_list]

        feature_service_errors = {}

        #print(datasets)

        for dataset in sorted(datasets):

            feature_service       = dataset
            feature_service_title = feature_service.replace("_", " ")

            arcpy.AddMessage(f"Dataset: {dataset}")
            arcpy.AddMessage(f"\tFS:  {feature_service}")
            arcpy.AddMessage(f"\tFST: {feature_service_title}")

            feature_class_layer_file = rf"{home_folder}\Layers\{feature_service_title}.lyrx"

            layer_file = arcpy.mp.LayerFile(feature_class_layer_file)

            del feature_class_layer_file

            # aprx.listBasemaps() to get a list of available basemaps
            #
            #    ['Charted Territory Map',
            #     'Colored Pencil Map',
            #     'Community Map',
            #     'Dark Gray Canvas',
            #     'Firefly Imagery Hybrid',
            #     'GEBCO Basemap (NOAA NCEI Visualization)',
            #     'GEBCO Basemap/Contours (NOAA NCEI Visualization)',
            #     'GEBCO Gray Basemap (NOAA NCEI Visualization)',
            #     'GEBCO Gray Basemap/Contours (NOAA NCEI Visualization)',
            #     'Human Geography Dark Map',
            #     'Human Geography Map',
            #     'Imagery',
            #     'Imagery Hybrid',
            #     'Light Gray Canvas',
            #     'Mid-Century Map',
            #     'Modern Antique Map',
            #     'National Geographic Style Map',
            #     'Navigation',
            #     'Navigation (Dark)',
            #     'Newspaper Map',
            #     'NOAA Charts',
            #     'NOAA ENC® Charts',
            #     'Nova Map',
            #     'Oceans',
            #     'OpenStreetMap',
            #     'Streets',
            #     'Streets (Night)',
            #     'Terrain with Labels',
            #     'Topographic']

            if aprx.listMaps(feature_service_title):
                aprx.deleteItem(aprx.listMaps(feature_service_title)[0])
                aprx.save()

            arcpy.AddMessage(f"\tCreating Map: {feature_service_title}")
            aprx.createMap(feature_service_title, "Map")
            aprx.save()

            current_map = aprx.listMaps(feature_service_title)[0]

            in_md = md.Metadata(rf"{project_gdb}\{dataset}")
            current_map.metadata.copy(in_md)
            current_map.metadata.save()
            aprx.save()

            current_map.addLayer(layer_file)
            aprx.save()

            del layer_file

            arcpy.AddMessage(f"\t\tList of layers or tables in Layer File:")
            if current_map.listLayers(feature_service_title):
                lyr = current_map.listLayers(feature_service_title)[0]
            elif current_map.listTables(feature_service_title):
                lyr = current_map.listTables(feature_service_title)[0]
            else:
                arcpy.AddWarning(f"Something wrong")

            in_md = md.Metadata(rf"{project_gdb}\{dataset}")
            lyr.metadata.copy(in_md)
            lyr.metadata.save()
            aprx.save()
            del in_md

            arcpy.AddMessage(f"\tGet Web Layer Sharing Draft")
            # Get Web Layer Sharing Draft
            server_type = "HOSTING_SERVER"  # FEDERATED_SERVER
            #            m.getWebLayerSharingDraft (server_type, service_type, service_name, {layers_and_tables})
            # sddraft = m.getWebLayerSharingDraft(server_type, "FEATURE", service_name, [selected_layer, selected_table])
            # https://pro.arcgis.com/en/pro-app/latest/arcpy/sharing/featuresharingdraft-class.htm#GUID-8E27A3ED-A705-4ACF-8C7D-AA861327AD26
            sddraft = current_map.getWebLayerSharingDraft(server_type=server_type, service_type="FEATURE", service_name=feature_service, layers_and_tables=lyr)
            del server_type

            sddraft.allowExporting = False
            sddraft.offline = False
            sddraft.offlineTarget = None
            sddraft.credits                  = lyr.metadata.credits
            sddraft.description              = lyr.metadata.description
            sddraft.summary                  = lyr.metadata.summary
            sddraft.tags                     = lyr.metadata.tags
            sddraft.useLimitations           = lyr.metadata.accessConstraints
            sddraft.overwriteExistingService = True
            sddraft.portalFolder = f"ESA Species Range"

            del lyr

            arcpy.AddMessage(f"\t\tAllow Exporting:            {sddraft.allowExporting}")
            arcpy.AddMessage(f"\t\tCheck Unique ID Assignment: {sddraft.checkUniqueIDAssignment}")
            arcpy.AddMessage(f"\t\tOffline:                    {sddraft.offline}")
            arcpy.AddMessage(f"\t\tOffline Target:             {sddraft.offlineTarget}")
            arcpy.AddMessage(f"\t\tOverwrite Existing Service: {sddraft.overwriteExistingService}")
            arcpy.AddMessage(f"\t\tPortal Folder:              {sddraft.portalFolder}")
            arcpy.AddMessage(f"\t\tServer Type:                {sddraft.serverType}")
            arcpy.AddMessage(f"\t\tService Name:               {sddraft.serviceName}")
            #arcpy.AddMessage(f"\t\tCredits:                    {sddraft.credits}")
            #arcpy.AddMessage(f"\t\tDescription:                {sddraft.description}")
            #arcpy.AddMessage(f"\t\tSummary:                    {sddraft.summary}")
            #arcpy.AddMessage(f"\t\tTags:                       {sddraft.tags}")
            #arcpy.AddMessage(f"\t\tUse Limitations:            {sddraft.useLimitations}")

            arcpy.AddMessage(f"\tExport to SD Draft")
            # Create Service Definition Draft file
            sddraft.exportToSDDraft(rf"{home_folder}\Publish\{feature_service}.sddraft")

            del sddraft

            sd_draft = rf"{home_folder}\Publish\{feature_service}.sddraft"

            arcpy.AddMessage(f"\tModify SD Draft")
            # https://pro.arcgis.com/en/pro-app/latest/arcpy/sharing/featuresharingdraft-class.htm
            import xml.dom.minidom as DOM

            docs = DOM.parse(sd_draft)
            key_list = docs.getElementsByTagName("Key")
            value_list = docs.getElementsByTagName("Value")

            for i in range(key_list.length):
                if key_list[i].firstChild.nodeValue == "maxRecordCount":
                    arcpy.AddMessage(f"\t\tUpdating maxRecordCount from 2000 to 10000")
                    value_list[i].firstChild.nodeValue = 10000
                if key_list[i].firstChild.nodeValue == "ServiceTitle":
                    arcpy.AddMessage(f"\t\tUpdating ServiceTitle from {value_list[i].firstChild.nodeValue} to {feature_service}")
                    value_list[i].firstChild.nodeValue = feature_service
                # Doesn't work
                #if key_list[i].firstChild.nodeValue == "GeodataServiceName":
                #    arcpy.AddMessage(f"\t\tUpdating GeodataServiceName from {value_list[i].firstChild.nodeValue} to {feature_service}")
                #    value_list[i].firstChild.nodeValue = feature_service
                del i

            # Write to the .sddraft file
            f = open(sd_draft, "w")
            docs.writexml(f)
            f.close()
            del f

            del DOM, docs, key_list, value_list

            FeatureSharingDraftReport = False
            if FeatureSharingDraftReport:
                arcpy.AddMessage(f"\tReport for {os.path.basename(sd_draft)} SD File")
                feature_sharing_draft_report(sd_draft)
            del FeatureSharingDraftReport

            try:
                arcpy.AddMessage(f"\tCreate/Stage {os.path.basename(sd_draft)} SD File")
                arcpy.server.StageService(in_service_definition_draft=sd_draft, out_service_definition=sd_draft.replace("sddraft", "sd"), staging_version=5)
            except arcpy.ExecuteError:
                arcpy.AddError(arcpy.GetMessages(2))

            UploadServiceDefinition = True if dataset not in ["SealGuadalupeFur_20210228"] else False
            if UploadServiceDefinition:
                try:
                    arcpy.AddMessage(f"\tUpload {os.path.basename(sd_draft).replace('sddraft', 'sd')} Service Definition")
                    arcpy.server.UploadServiceDefinition(
                                                         in_sd_file      = sd_draft.replace("sddraft", "sd"),
                                                         in_server       = "HOSTING_SERVER",  # in_service_name = "", #in_cluster      = "",
                                                         in_folder_type  = "FROM_SERVICE_DEFINITION",  # EXISTING #in_folder       = "",
                                                         in_startupType  = "STARTED",
                                                         in_override     = "OVERRIDE_DEFINITION",
                                                         in_my_contents  = "NO_SHARE_ONLINE",
                                                         in_public       = "PRIVATE",
                                                         in_organization = "NO_SHARE_ORGANIZATION",  # in_groups       = ""
                                                        )
                except arcpy.ExecuteError:
                    arcpy.AddError(arcpy.GetMessages(2))
                    feature_service_errors[dataset] = arcpy.GetMessages(2)
                    #raise Exception
            else:
                pass
            del UploadServiceDefinition

            del sd_draft

            #aprx.deleteItem(current_map)
            del current_map
            aprx.save()

            del feature_service
            del dataset
        del datasets
        #del datasets_dict

        aprx.save()

        current_maps = aprx.listMaps()

        if current_maps:
            arcpy.AddMessage(f"\nCurrent Maps\n")
            #for current_map in current_maps:
            #    arcpy.AddMessage(f"\tProject Map: {current_map.name}")
            #    del current_map
        else:
            arcpy.AddWarning("No maps in Project")

        arcpy.AddMessage(f"\n{'-' * 90}\n")

        del current_maps

        # Declared Variables set in function for aprx
        del home_folder
        # Save aprx one more time and then delete
        aprx.save()
        del aprx
        #del project

        for feature_service_error in feature_service_errors:
            arcpy.AddMessage(feature_service_error, feature_service_errors[feature_service_error])
            del feature_service_error
        del feature_service_errors

        # Declared Variables set in function
        del project_file, feature_service_list

        # Imports
        del md

        # Function Parameters
        del project_gdb

    except KeyboardInterrupt:
        raise SystemExit
    except arcpy.ExecuteWarning:
        arcpy.AddWarning(arcpy.GetMessages())
        traceback.print_exc()
    except arcpy.ExecuteError:
        arcpy.AddError(arcpy.GetMessages())
        traceback.print_exc()
    except Exception as e:
        print(e)
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
            traceback.print_exc()
    finally:
        pass

def update_existing_contacts(project_gdb=""):
    try:
        # Imports
        from lxml import etree
        from io import StringIO
        import copy
        from arcpy import metadata as md

        arcpy.env.overwriteOutput          = True
        arcpy.env.parallelProcessingFactor = "100%"
        arcpy.SetLogMetadata(True)
        arcpy.SetSeverityLevel(2)
        arcpy.SetMessageLevels(['NORMAL']) # NORMAL, COMMANDSYNTAX, DIAGNOSTICS, PROJECTIONTRANSFORMATION

        project_folder = os.path.dirname(project_gdb)
        scratch_folder      = rf"{project_folder}\Scratch"
# Moved dictionaries to JSON
##        root_dict = {"Esri"       :  0, "dataIdInfo" :  1, "mdChar"      :  2,
##                     "mdContact"  :  3, "mdDateSt"   :  4, "mdFileID"    :  5,
##                     "mdLang"     :  6, "mdMaint"    :  7, "mdHrLv"      :  8,
##                     "mdHrLvName" :  9, "refSysInfo" : 10, "spatRepInfo" : 11,
##                     "spdoinfo"   : 12, "dqInfo"     : 13, "distInfo"    : 14,
##                     "eainfo"     : 15, "contInfo"   : 16, "spref"       : 17,
##                     "spatRepInfo" : 18, "dataSetFn" : 19, "Binary"      : 100,}
# Moved dictionaries to JSON
##        RoleCd_dict = {"001" : "Resource Provider", "002" : "Custodian",
##                       "003" : "Owner",             "004" : "User",
##                       "005" : "Distributor",       "006" : "Originator",
##                       "007" : "Point of Contact",  "008" : "Principal Investigator",
##                       "009" : "Processor",         "010" : "Publisher",
##                       "011" : "Author",            "012" : "Collaborator",
##                       "013" : "Editor",            "014" : "Mediator",
##                       "015" : "Rights Holder",}

        workspaces = [project_gdb]

        contacts_xml = rf"{os.environ['USERPROFILE']}\Documents\ArcGIS\Descriptions\contacts.xml"
        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
        contacts_xml_tree = etree.parse(contacts_xml, parser=parser) # To parse from a string, use the fromstring() function instead.
        del parser
        del contacts_xml
        contacts_xml_root = contacts_xml_tree.getroot()
        #etree.indent(contacts_xml_root, space="  ")
        #print(etree.tostring(contacts_xml_root, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())

        for workspace in workspaces:

            arcpy.env.workspace        = workspace
            arcpy.env.scratchWorkspace = rf"{scratch_folder}\scratch.gdb"

            datasets = list()

            walk = arcpy.da.Walk(workspace)

            for dirpath, dirnames, filenames in walk:
                for filename in filenames:
                    datasets.append(os.path.join(dirpath, filename))
                    del filename
                del dirpath, dirnames, filenames
            del walk

            for dataset_path in sorted(datasets):
                #print(dataset_path)
                dataset_name = os.path.basename(dataset_path)

                #print(f"Dataset Name:     {dataset_name}")
                #print(f"\tDataset Location: {os.path.basename(os.path.dirname(dataset_path))}")

                dataset_md = md.Metadata(dataset_path)
                dataset_md_xml = dataset_md.xml
                del dataset_md

                # Parse the XML
                parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
                tree = etree.parse(StringIO(dataset_md_xml), parser=parser)
                root = tree.getroot()
                del parser, dataset_md_xml

                # print(etree.tostring(tree, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
                # etree.indent(tree, space='   ')
                # tree.write(xml_file, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True)

                print(f"Dataset Name: {dataset_name}")

                contact_parents = root.xpath(f".//eMailAdd/text()/ancestor::*//rpIndName/text()/ancestor::*//rpIndName/..")
                #contact_parents = copy.deepcopy(root.xpath(f".//eMailAdd/text()/ancestor::*//rpIndName/text()/ancestor::*//rpIndName/.."))
                #contact_parents = root.xpath(f".//eMailAdd/text()/ancestor::rpCntInfo/..")

                if len(contact_parents) > 0:
                    #count = 0
                    for contact_parent in contact_parents:
                        #count+=1
                        old_contact_parent = contact_parent.tag
                        print(f"\tContact Parent: {old_contact_parent}")
                        #print(etree.tostring(contact_parent, encoding='UTF-8',  method='xml', pretty_print=True).decode())


                        if isinstance(contact_parent.find(f"./rpCntInfo"), type(None)):
                            _xml = etree.XML('<rpCntInfo><cntAddress addressType="both"><delPoint></delPoint><city></city><adminArea></adminArea> \
                                              <postCode></postCode><eMailAdd></eMailAdd><country></country></cntAddress><cntPhone><voiceNum tddtty=""></voiceNum> \
                                              <faxNum></faxNum></cntPhone><cntHours></cntHours><cntOnlineRes><linkage></linkage><protocol>REST Service</protocol> \
                                              <orName></orName><orDesc></orDesc><orFunct><OnFunctCd value="002"></OnFunctCd></orFunct></cntOnlineRes></rpCntInfo>')
                            # Append element
                            contact_parent.append(_xml)
                            del _xml

                        if not isinstance(contact_parent.find(f".//eMailAdd"), type(None)):
                            email_address = contact_parent.find(f".//eMailAdd")
                            #print(f"\t\tEmail Address: {email_address}")
                            if not email_address.text:
                                _user_name = contact_parent.find(f"./rpIndName").text
                                _email_address = _user_name.lower().replace(" ", ".") + "@noaa.gov"
                                email_address.text = _email_address
                                del _email_address, _user_name
                            else:
                                pass
                        else:
                            pass
                            _rpCntInfo = contact_parent.find(f".//rpCntInfo")
                            _cntAddress = _rpCntInfo.find(f".//cntAddress")
                            _user_name = contact_parent.find(f"./rpIndName").text
                            #print(f"\t\tUser Name:     {_user_name}")
                            _email_address = _user_name.lower().replace(" ", ".") + "@noaa.gov"
                            _xml = etree.XML(f'<eMailAdd>{_email_address}</eMailAdd>')
                            # Append element
                            _cntAddress.append(_xml)
                            del _xml, _user_name, _cntAddress, _rpCntInfo

                        if old_contact_parent == "citRespParty":
                            if not isinstance(contact_parent.find(f"./role"), type(None)):
                                user_role = contact_parent.find(f".//RoleCd")
                                user_role.set("value", "002")
                            else:
                                _xml = etree.XML('<role><RoleCd value="002"/></role>')
                                # Append element
                                contact_parent.append(_xml)
                                del _xml

                        if old_contact_parent == "idPoC":
                            if not isinstance(contact_parent.find(f"./role"), type(None)):
                                user_role = contact_parent.find(f".//RoleCd")
                                user_role.set("value", "007")
                            else:
                                _xml = etree.XML('<role><RoleCd value="007"/></role>')
                                # Append element
                                contact_parent.append(_xml)
                                del _xml

                        if old_contact_parent == "distorCont":
                            if not isinstance(contact_parent.find(f"./role"), type(None)):
                                user_role = contact_parent.find(f".//RoleCd")
                                user_role.set("value", "005")
                            else:
                                _xml = etree.XML('<role><RoleCd value="005"/></role>')
                                # Append element
                                contact_parent.append(_xml)
                                del _xml

                        if old_contact_parent == "mdContact":
                            if not isinstance(contact_parent.find(f"./role"), type(None)):
                                user_role = contact_parent.find(f".//RoleCd")
                                user_role.set("value", "011")
                            else:
                                _xml = etree.XML('<role><RoleCd value="011"/></role>')
                                # Append element
                                contact_parent.append(_xml)
                                del _xml

                        if old_contact_parent == "stepProc":
                            if not isinstance(contact_parent.find(f"./role"), type(None)):
                                user_role = contact_parent.find(f".//RoleCd")
                                user_role.set("value", "009")
                            else:
                                _xml = etree.XML('<role><RoleCd value="009"/></role>')
                                # Append element
                                contact_parent.append(_xml)
                                del _xml

                        if not isinstance(contact_parent.find(f"./rpIndName"), type(None)):
                            user_name = contact_parent.find(f"./rpIndName").text
                            print(f"\t\tUser Name:     {user_name}")
                        else:
                            user_name = ""

                        if not isinstance(contact_parent.find(f".//eMailAdd"), type(None)):
                            email_address = contact_parent.find(f".//eMailAdd").text
                            print(f"\t\tEmail Address: {email_address}")
                        else:
                            email_address = ""
                        if not isinstance(contact_parent.find(f".//RoleCd"), type(None)):
                            user_role = contact_parent.find(f".//RoleCd")
                            print(f"\t\tRole:          {user_role.attrib}")
                        else:
                            user_role = ""

                        contact_root = root.xpath(f".//eMailAdd[text()='{email_address}']/ancestor::{old_contact_parent}/rpIndName[text()='{user_name}']/..")
                        #contact_root = copy.deepcopy(root.xpath(f".//eMailAdd[text()='{email_address}']/ancestor::{old_contact_parent}/rpIndName[text()='{user_name}']/.."))
                        #print(etree.tostring(contact_root[0], encoding='UTF-8',  method='xml', pretty_print=True).decode())
                        #print(etree.tostring(contact_root[0], encoding='UTF-8',  method='xml', pretty_print=True).decode())

                        new_contact_root = contacts_xml_root.xpath(f".//eMailAdd[text()='{email_address}']/ancestor::contact/rpIndName[text()='{user_name}']/ancestor::contact/editorSave[text()='True']/..")

                        if len(new_contact_root) == 1:
                            new_contact = copy.deepcopy(new_contact_root[0])
                            new_contact.tag = old_contact_parent
                            #new_contact.append(contact_root[0].find(f".//role"))
                            #print(etree.tostring(new_contact, encoding='UTF-8',  method='xml', pretty_print=True).decode())

                            contact_root[0].getparent().replace(contact_root[0], new_contact)
                            #print(etree.tostring(contact_root[0], encoding='UTF-8',  method='xml', pretty_print=True).decode())

                            del new_contact

                        del new_contact_root, contact_root
                        del user_role, email_address, user_name
                        del old_contact_parent, contact_parent

                dataset_md = md.Metadata(dataset_path)
                dataset_md.xml = etree.tostring(tree, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode()
                dataset_md.save()
                dataset_md.synchronize("ALWAYS")
                del dataset_md

                del contact_parents
                del dataset_name, dataset_path
                del root, tree
            del datasets
            del workspace

        # Declared Variables set in function
        del contacts_xml_root, contacts_xml_tree
        del RoleCd_dict, root_dict
        del project_folder, scratch_folder
        del workspaces

        # Imports
        del md, etree, StringIO, copy

        # Function Parameters
        del project_gdb

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

def change_existing_contacts(project_gdb="", assigned_contacts=""):
    try:
        # Imports
        from lxml import etree
        from io import StringIO
        import copy
        from arcpy import metadata as md

        # Project modules
        from src.project_tools import pretty_format_xml_file

        arcpy.env.overwriteOutput          = True
        arcpy.env.parallelProcessingFactor = "100%"
        arcpy.SetLogMetadata(True)
        arcpy.SetSeverityLevel(2)
        arcpy.SetMessageLevels(['NORMAL']) # NORMAL, COMMANDSYNTAX, DIAGNOSTICS, PROJECTIONTRANSFORMATION

        project_folder = os.path.dirname(project_gdb)
        scratch_folder      = rf"{project_folder}\Scratch"
# Moved dictionaries to JSON
##        root_dict = {"Esri"       :  0, "dataIdInfo" :  1, "mdChar"      :  2,
##                     "mdContact"  :  3, "mdDateSt"   :  4, "mdFileID"    :  5,
##                     "mdLang"     :  6, "mdMaint"    :  7, "mdHrLv"      :  8,
##                     "mdHrLvName" :  9, "refSysInfo" : 10, "spatRepInfo" : 11,
##                     "spdoinfo"   : 12, "dqInfo"     : 13, "distInfo"    : 14,
##                     "eainfo"     : 15, "contInfo"   : 16, "spref"       : 17,
##                     "spatRepInfo" : 18, "dataSetFn" : 19, "Binary"      : 100,}
# Moved dictionaries to JSON
##        RoleCd_dict = {"001" : "Resource Provider", "002" : "Custodian",
##                       "003" : "Owner",             "004" : "User",
##                       "005" : "Distributor",       "006" : "Originator",
##                       "007" : "Point of Contact",  "008" : "Principal Investigator",
##                       "009" : "Processor",         "010" : "Publisher",
##                       "011" : "Author",            "012" : "Collaborator",
##                       "013" : "Editor",            "014" : "Mediator",
##                       "015" : "Rights Holder",}

        workspaces = [project_gdb]

        contacts_xml = rf"{os.environ['USERPROFILE']}\Documents\ArcGIS\Descriptions\contacts.xml"
        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
        contacts_xml_tree = etree.parse(contacts_xml, parser=parser) # To parse from a string, use the fromstring() function instead.
        del parser
        del contacts_xml
        contacts_xml_root = contacts_xml_tree.getroot()
        #etree.indent(contacts_xml_root, space="  ")
        #print(etree.tostring(contacts_xml_root, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())

        for workspace in workspaces:

            arcpy.env.workspace        = workspace
            arcpy.env.scratchWorkspace = rf"{scratch_folder}\scratch.gdb"

            datasets = list()

            walk = arcpy.da.Walk(workspace)

            for dirpath, dirnames, filenames in walk:
                for filename in filenames:
                    datasets.append(os.path.join(dirpath, filename))
                    del filename
                del dirpath, dirnames, filenames
            del walk

            for dataset_path in sorted(datasets):
                #print(dataset_path)
                dataset_name = os.path.basename(dataset_path)

                #print(f"Dataset Name:     {dataset_name}")
                #print(f"\tDataset Location: {os.path.basename(os.path.dirname(dataset_path))}")

                dataset_md = md.Metadata(dataset_path)
                dataset_md_xml = dataset_md.xml
                del dataset_md

                # Parse the XML
                parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
                tree = etree.parse(StringIO(dataset_md_xml), parser=parser)
                root = tree.getroot()
                del parser, dataset_md_xml

                # print(etree.tostring(tree, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
                # etree.indent(tree, space='   ')
                # tree.write(xml_file, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True)

                print(f"Dataset Name: {dataset_name}")

                for assigned_contact in assigned_contacts:
                    if assigned_contact in ["citRespParty", "idPoC", "mdContact"]:
                        email_address = assigned_contacts[assigned_contact]
                        print(f"\t\tProcessing: {assigned_contact} Email: {email_address}")
                        contact_parents = root.xpath(f".//{assigned_contact}")
                        new_contact_root = contacts_xml_root.xpath(f".//eMailAdd[text()='{email_address}']/ancestor::contact/editorSave[text()='True']/..")
                        print(new_contact_root)
                        if len(new_contact_root) == 1:
                            new_contact = copy.deepcopy(new_contact_root[0])
                            new_contact.tag = assigned_contact
                            #contact_root[0].getparent().replace(contact_root[0], new_contact)
                            print(etree.tostring(contact_root[0], encoding='UTF-8',  method='xml', pretty_print=True).decode())
                            del new_contact
                        del new_contact_root

                        del email_address

##                        for contact_parent in contact_parents:
##                            print(contact_parent.tag)
##                            del contact_parent
                        del contact_parents

                    elif assigned_contact in ["distorCont", "stepProc"]:
                        print(f"\t\tProcessing: {assigned_contact} Email: {assigned_contacts[assigned_contact]}")
                        contact_parents = root.xpath(f".//{assigned_contact}")
##                        for contact_parent in contact_parents:
##                            print(contact_parent.tag)
##                            del contact_parent
                        del contact_parents
                    else:
                        pass

                    del assigned_contact


##                    for contact_parent in contact_parents:
##                        if isinstance(contact_parent, type(None)):
##                            print(f"\t\t###--->>> {assigned_contact} is missing!! <<<---###")
##                        elif not isinstance(contact_parent, type(None)):
##                            if assigned_contact in ["citRespParty", "idPoC", "mdContact"]:
##                                print(f"\t\tProcessing: {assigned_contact}")
##                                for contact in contact_parent:
##                                    print(contact.tag)
##                                email_address = contact_parent.find(f".//eMailAdd")
##                                if isinstance(email_address, type(None)):
##                                    print(f"\t\t\tEmail Address is missing")
##                                    kids = contact_parent.iterchildren()
##                                    for kid in kids:
##                                        print(f"\t\t\t\t\t{kid.tag}: {kid.text}")
##                                        del kid
##                                    del kids
##                                elif not isinstance(contact_parent, type(None)):
##                                    print(f"\t\t\tEmail Address: {email_address.text}")
##
##                                del email_address
##
##                            elif assigned_contact in ["distorCont", "stepProc"]:
##                                print(f"\t\tProcessing: {assigned_contact}")
##                                email_address = contact_parent.find(f".//eMailAdd")pIndName
##                                if isinstance(email_address, type(None)):
##                                    print(f"\t\t\tEmail Address is missing")
##                                    kids = contact_parent.iterchildren()
##                                    for kid in kids:
##                                        print(f"\t\t\t\t\t{kid.tag}: {kid.text}")
##                                        del kid
##                                    del kids
##                                elif not isinstance(contact_parent, type(None)):
##                                    print(f"\t\t\tEmail Address: {email_address.text}")
##                                del email_address


                      #  {"citRespParty" : {"Resource Citation Contacts" : "nikki.wildart@noaa.gov"},
                      #   "idPoC"        : {"Points of Contact"          : "nikki.wildart@noaa.gov"},
                      #   "distorCont"   : {"Distribution Contacts"      : "nikki.wildart@noaa.gov"},
                      #   "mdContact"    : {"Metadata Contacts"          : "nikki.wildart@noaa.gov"},
                      #   "stepProc"     : {"Step Processors"            : "nikki.wildart@noaa.gov",},
                      #          }


##                            print(f"\t\tProcessing: {assigned_contact}")
##                            #print(etree.tostring(contact_parent, encoding='UTF-8',  method='xml', pretty_print=True).decode())
##                            rpIndNames = contact_parent.xpath(f".//rpIndName")
##                            if len(rpIndNames) == 0:
##                                print(f"\t\t\trpIndName is missing")
##                                kids = contact_parent.iterchildren()
##                                for kid in kids:
##                                    print(kid.tag)
##                                    del kid
##                                del kids
##
##                            elif len(rpIndNames) > 0:
##                                print(f"\t\t\tThere are {len(rpIndNames)} rpIndName")
##                                for rpIndName in rpIndNames:
##                                    print(f"\t\t\t\tContact: {rpIndName.text}")
##
##                                    del rpIndName
##                            del rpIndNames

                    #"citRespParty"
                    #"idPoC"
                    #"distorCont"
                    #"mdContact"
                    #"stepProc"

##                        else:
##                            pass
##
##                        del contact_parent
##                    del assigned_contact

                    #del contact_parents
##                contact_parents = root.xpath(f".//eMailAdd/text()/ancestor::*//rpIndName/text()/ancestor::*//rpIndName/..")
##
##                if len(contact_parents) > 0:
##                    #count = 0
##                    for contact_parent in contact_parents:
##                        #count+=1
##                        old_contact_parent = contact_parent.tag
##                        print(f"\tContact Parent: {old_contact_parent}")
##                        #print(etree.tostring(contact_parent, encoding='UTF-8',  method='xml', pretty_print=True).decode())
##
##
##                        if isinstance(contact_parent.find(f"./rpCntInfo"), type(None)):
##                            _xml = etree.XML('<rpCntInfo><cntAddress addressType="both"><delPoint></delPoint><city></city><adminArea></adminArea> \
##                                              <postCode></postCode><eMailAdd></eMailAdd><country></country></cntAddress><cntPhone><voiceNum tddtty=""></voiceNum> \
##                                              <faxNum></faxNum></cntPhone><cntHours></cntHours><cntOnlineRes><linkage></linkage><protocol>REST Service</protocol> \
##                                              <orName></orName><orDesc></orDesc><orFunct><OnFunctCd value="002"></OnFunctCd></orFunct></cntOnlineRes></rpCntInfo>')
##                            # Append element
##                            contact_parent.append(_xml)
##                            del _xml
##
##                        if not isinstance(contact_parent.find(f".//eMailAdd"), type(None)):
##                            email_address = contact_parent.find(f".//eMailAdd")
##                            #print(f"\t\tEmail Address: {email_address}")
##                            if not email_address.text:
##                                _user_name = contact_parent.find(f"./rpIndName").text
##                                _email_address = _user_name.lower().replace(" ", ".") + "@noaa.gov"
##                                email_address.text = _email_address
##                                del _email_address, _user_name
##                            else:
##                                pass
##                        else:
##                            pass
##                            _rpCntInfo = contact_parent.find(f".//rpCntInfo")
##                            _cntAddress = _rpCntInfo.find(f".//cntAddress")
##                            _user_name = contact_parent.find(f"./rpIndName").text
##                            #print(f"\t\tUser Name:     {_user_name}")
##                            _email_address = _user_name.lower().replace(" ", ".") + "@noaa.gov"
##                            _xml = etree.XML(f'<eMailAdd>{_email_address}</eMailAdd>')
##                            # Append element
##                            _cntAddress.append(_xml)
##                            del _xml, _user_name, _cntAddress, _rpCntInfo
##
##                        if old_contact_parent == "citRespParty":
##                            if not isinstance(contact_parent.find(f"./role"), type(None)):
##                                user_role = contact_parent.find(f".//RoleCd")
##                                user_role.set("value", "002")
##                            else:
##                                _xml = etree.XML('<role><RoleCd value="002"/></role>')
##                                # Append element
##                                contact_parent.append(_xml)
##                                del _xml
##
##                        if old_contact_parent == "idPoC":
##                            if not isinstance(contact_parent.find(f"./role"), type(None)):
##                                user_role = contact_parent.find(f".//RoleCd")
##                                user_role.set("value", "007")
##                            else:
##                                _xml = etree.XML('<role><RoleCd value="007"/></role>')
##                                # Append element
##                                contact_parent.append(_xml)
##                                del _xml
##
##                        if old_contact_parent == "distorCont":
##                            if not isinstance(contact_parent.find(f"./role"), type(None)):
##                                user_role = contact_parent.find(f".//RoleCd")
##                                user_role.set("value", "005")
##                            else:
##                                _xml = etree.XML('<role><RoleCd value="005"/></role>')
##                                # Append element
##                                contact_parent.append(_xml)
##                                del _xml
##
##                        if old_contact_parent == "mdContact":
##                            if not isinstance(contact_parent.find(f"./role"), type(None)):
##                                user_role = contact_parent.find(f".//RoleCd")
##                                user_role.set("value", "011")
##                            else:
##                                _xml = etree.XML('<role><RoleCd value="011"/></role>')
##                                # Append element
##                                contact_parent.append(_xml)
##                                del _xml
##
##                        if old_contact_parent == "stepProc":
##                            if not isinstance(contact_parent.find(f"./role"), type(None)):
##                                user_role = contact_parent.find(f".//RoleCd")
##                                user_role.set("value", "009")
##                            else:
##                                _xml = etree.XML('<role><RoleCd value="009"/></role>')
##                                # Append element
##                                contact_parent.append(_xml)
##                                del _xml
##
##
##                        #if count == 1:
##                        #    _xml = etree.XML('<role><RoleCd value="011"/></role>')
##                        #    # Append element
##                        #    contact_root[0].append(_xml)
##                        #    # Change element name
##                        #    contact_parent.tag = "mdContact"
##                        #    del _xml
##                        #elif count == 2:
##                        #    _xml = etree.XML('<role><RoleCd value="005"/></role>')
##                        #    contact_root[0].append(_xml)
##                        #    contact_parent.tag = "distributor"
##                        #    del _xml
##                        #elif count == 3:
##                        #    _xml = etree.XML('<role><RoleCd value="002"/></role>')
##                        #    contact_root[0].append(_xml)
##                        #    contact_parent.tag = "citRespParty"
##                        #    del _xml
##                        #elif count == 4:
##                        #    _xml = etree.XML('<role><RoleCd value="007"/></role>')
##                        #    contact_root[0].append(_xml)
##                        #    contact_parent.tag = "idPoC"
##                        #    del _xml
##
##                        if not isinstance(contact_parent.find(f"./rpIndName"), type(None)):
##                            user_name = contact_parent.find(f"./rpIndName").text
##                            print(f"\t\tUser Name:     {user_name}")
##                        else:
##                            user_name = ""
##
##                        if not isinstance(contact_parent.find(f".//eMailAdd"), type(None)):
##                            email_address = contact_parent.find(f".//eMailAdd").text
##                            print(f"\t\tEmail Address: {email_address}")
##                        else:
##                            email_address = ""
##                        if not isinstance(contact_parent.find(f".//RoleCd"), type(None)):
##                            user_role = contact_parent.find(f".//RoleCd")
##                            print(f"\t\tRole:          {user_role.attrib}")
##                        else:
##                            user_role = ""
##
##                        contact_root = root.xpath(f".//eMailAdd[text()='{email_address}']/ancestor::{old_contact_parent}/rpIndName[text()='{user_name}']/..")
##                        #contact_root = copy.deepcopy(root.xpath(f".//eMailAdd[text()='{email_address}']/ancestor::{old_contact_parent}/rpIndName[text()='{user_name}']/.."))
##                        #print(etree.tostring(contact_root[0], encoding='UTF-8',  method='xml', pretty_print=True).decode())
##
##                        new_contact_root = contacts_xml_root.xpath(f".//eMailAdd[text()='{email_address}']/ancestor::contact/rpIndName[text()='{user_name}']/ancestor::contact/editorSave[text()='True']/..")
##
##                        if len(new_contact_root) == 1:
##                            new_contact = copy.deepcopy(new_contact_root[0])
##                            new_contact.tag = old_contact_parent
##                            #new_contact.append(contact_root[0].find(f".//role"))
##                            #print(etree.tostring(new_contact, encoding='UTF-8',  method='xml', pretty_print=True).decode())
##
##                            contact_root[0].getparent().replace(contact_root[0], new_contact)
##                            #print(etree.tostring(contact_root[0], encoding='UTF-8',  method='xml', pretty_print=True).decode())
##
##                            del new_contact
##
##                        del new_contact_root, contact_root
##                        del user_role, email_address, user_name
##                        del old_contact_parent, contact_parent
##
##                dataset_md = md.Metadata(dataset_path)
##                dataset_md.xml = etree.tostring(tree, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode()
##                dataset_md.save()
##                dataset_md.synchronize("ALWAYS")
##                del dataset_md
##
##                del contact_parents
                del dataset_name, dataset_path
                del root, tree
            del datasets
            del workspace

        # Declared Variables set in function
        del contacts_xml_root, contacts_xml_tree
        del RoleCd_dict, root_dict
        del project_folder, scratch_folder
        del workspaces

        # Imports
        del md, etree, StringIO, copy, pretty_format_xml_file

        # Function Parameters
        del project_gdb, assigned_contacts

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

# Main function
def main(project_folder=str()):
    try:
        from time import gmtime, localtime, strftime, time
        # Set a start time so that we can see how log things take
        start_time = time()
        print(f"{'-' * 80}")
        print(f"Python Script:  {os.path.basename(__file__)}")
        print(f"Location:       {os.path.dirname(__file__)}")
        print(f"Python Version: {sys.version} Environment: {os.path.basename(sys.exec_prefix)}")
        print(f"{'-' * 80}\n")
        project_gdb     = rf"{project_folder}\National Mapper.gdb"
        #source_zip_file = rf"{project_folder}\NMFS_ESA_Range.gdb (20241121).zip"
        #source_zip_file = rf"{project_folder}\NMFS_ESA_Range.gdb (20241209).zip"
        #source_gdb      = rf"{project_folder}\NMFS_ESA_Range_20241121.gdb"
        source_gdb      = rf"{project_folder}\NMFS_ESA_Range.gdb"

        version = "20241212"

        CreateGdbsAndFolder = False
        if CreateGdbsAndFolder:
            try:
                # Imports
                from src.project_tools import create_project_gdb, create_folders
                create_project_gdb(project_gdb)
                folders = ["Export", "Layers", "Publish", "dev", "test", "prod"]
                create_folders(project_folder, folders)
                del folders
                # Imports
                del create_project_gdb, create_folders
            except Warning as w:
                print(w, flush=True); del w
        else:
            pass
        del CreateGdbsAndFolder

        ExtractSourceZipFile = False
        if ExtractSourceZipFile:
            os.chdir(project_folder)
            source_zip_file = rf"{project_folder}\NMFS_ESA_Range.gdb (20241209).zip"
            print(f"\nExtracting '{os.path.basename(source_zip_file)}' zip file", flush=True)
            from zipfile import ZipFile
            with ZipFile(source_zip_file, mode="r") as archive:
                for file in sorted(archive.namelist()):
                    archive.extract(file, ".")
                    del file
            del archive
            del source_zip_file
            del ZipFile
        del ExtractSourceZipFile

        CopyFeatureClasses = False
        if CopyFeatureClasses:
            try:
                copy_feature_classes(project_gdb=project_gdb, source_gdb=source_gdb)
            except Exception as e:
                raise Exception(e)
        del CopyFeatureClasses

        CreateSpeciesRangeTable = False
        if CreateSpeciesRangeTable:
            create_species_range_table(project_gdb=project_gdb, version=version)
        del CreateSpeciesRangeTable

        ImportSpeciesRangeTable = False
        if ImportSpeciesRangeTable:
            import_species_range_table(project_gdb=project_gdb, version=version)
        del ImportSpeciesRangeTable

        SchemaFieldReport = False
        if SchemaFieldReport:
            schema_field_report(project_gdb=project_gdb)
        del SchemaFieldReport

        # Move to single py script
        #ExportMetadata = False
        #if ExportMetadata:
        #    try:
        #        export_metadata(project_gdb=project_gdb)
        #    except Exception as e:
        #        print(e)
        #del ExportMetadata

        # This is being replaced
        ImportMetadata = False
        if ImportMetadata:
            #_project_folder = os.path.dirname(project_gdb)
            #_project_gdb = rf"{project_folder}\Metadata Folder\National Mapper.gdb"
            try:
                import_metadata(project_gdb=project_gdb)
            except Exception as e:
                print(e)
            #del _project_folder, _project_gdb
        del ImportMetadata

##        # This is being replaced
##        UpdateMetadata = False
##        if UpdateMetadata:
##            #project_folder = os.path.dirname(project_gdb)
##            #project_gdb = rf"{project_folder}\Metadata Folder\National Mapper.gdb"
##            try:
##                update_metadata(project_gdb=project_gdb)cvt
##            except Exception as e:
##                print(e)
##        del UpdateMetadata

        UpdateExistingContacts = False
        if UpdateExistingContacts:
            update_existing_contacts(project_gdb=project_gdb)
        else:
            pass
        del UpdateExistingContacts

        ChangeExistingContacts = True
        if ChangeExistingContacts:
            #assigned_contacts = {"citRespParty" : {"Resource Citation Contacts" : "nikki.wildart@noaa.gov"},
            #                     "idPoC"        : {"Points of Contact"          : "nikki.wildart@noaa.gov"},
            #                     "distorCont"   : {"Distribution Contacts"      : "nikki.wildart@noaa.gov"},
            #                     "mdContact"    : {"Metadata Contacts"          : "nikki.wildart@noaa.gov"},
            #                     "stepProc"     : {"Step Processors"            : "nikki.wildart@noaa.gov",},
            #                    }
            assigned_contacts = {"citRespParty" : {"pIndName" : "Nikki Wildart", "eMailAdd" : "nikki.wildart@noaa.gov"},
                                 "idPoC"        : {"pIndName" : "Nikki Wildart", "eMailAdd" : "nikki.wildart@noaa.gov"},
                                 "distorCont"   : {"pIndName" : "Nikki Wildart", "eMailAdd" : "nikki.wildart@noaa.gov"},
                                 "mdContact"    : {"pIndName" : "Nikki Wildart", "eMailAdd" : "nikki.wildart@noaa.gov"},
                                 "stepProc"     : {"pIndName" : "Nikki Wildart", "eMailAdd" : "nikki.wildart@noaa.gov"},
                                }
            change_existing_contacts(project_gdb=project_gdb, assigned_contacts=assigned_contacts)
            del assigned_contacts
        else:
            pass
        del ChangeExistingContacts

        CreateFeatureClassLayers = False
        if CreateFeatureClassLayers:
            create_feature_class_layers(project_gdb)
        del CreateFeatureClassLayers

        CreateFeaturClasseServices = False
        if CreateFeaturClasseServices:
            #folders = ["Export", "Layers", "Publish"]
            #create_folders(project_folder, folders)
            create_feature_class_services(project_gdb)
            #del folders
        del CreateFeaturClasseServices

        # This is being replaced
        # UpdateMetadataFromPublishedMd = False
        # if UpdateMetadataFromPublishedMd:
        #    update_metadata_from_published_md(project_file, project)
        # del UpdateMetadataFromPublishedMd

        CreateMaps = False
        if CreateMaps:
            result = create_maps(project_file, project)
            arcpy.AddMessage(result)
            del result
        del CreateMaps

        #CreateFeatureClasses = False
        #if CreateFeatureClasses:
        #    create_feature_classes(project_gdb=project_gdb, source_gdb=source_gdb)
        #del CreateFeatureClasses

        # Declared Variables
        del project_gdb, source_gdb, version
        # Imports
        del project_folder

        # Elapsed time
        end_time = time()
        elapse_time =  end_time - start_time
        print(flush=True)
        print(f"\n{'-' * 80}", flush=True)
        print(f"Python script: {os.path.basename(__file__)} successfully completed {strftime('%a %b %d %I:%M %p', localtime())}", flush=True)
        print(u"Elapsed Time {0} (H:M:S)".format(strftime("%H:%M:%S", gmtime(elapse_time))), flush=True)
        print(f"{'-' * 80}", flush=True)
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
        # Cleanup
        arcpy.management.ClearWorkspaceCache()

if __name__ == '__main__':
    try:
        main(project_folder=rf"{os.path.dirname(os.path.dirname(__file__))}")
    except:
        traceback.print_exc()
