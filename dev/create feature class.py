#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john.f.kennedy
#
# Created:     03/01/2025
# Copyright:   (c) john.f.kennedy 2025
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

def create_feature_classes1(project_gdb="", source_gdb=""):
    try:
        # Imports

        # Use all of the cores on the machine
        arcpy.env.parallelProcessingFactor = "100%"
        arcpy.env.overwriteOutput = True

        # Define variables
        project_folder = os.path.dirname(project_gdb)
        scratch_folder = rf"{project_folder}\Scratch"
        scratch_gdb    = rf"{scratch_folder}\scratch.gdb"

        create_project_gdb(project_gdb)
        create_scratch_gdb(scratch_gdb)

        # Set the workspace environment to local file geodatabase
        arcpy.env.workspace = project_gdb
        # Set the scratchWorkspace environment to local file geodatabase
        arcpy.env.scratchWorkspace = scratch_gdb

        # Clean-up variables
        del scratch_folder, scratch_gdb

        arcpy.AddMessage(f"\n{'--Start' * 10}--\n")

        # work

        arcpy.env.workspace = source_gdb

        source_fcs = arcpy.ListFeatureClasses()

        arcpy.env.workspace = project_gdb

        species_range_template = arcpy.management.CreateFeatureclass(project_gdb, "SpeciesRangeTemplate", geometry_type='POLYGON')

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

        arcpy.management.AddFields(species_range_template, field_description, None)

        del field_description

        arcpy.AddMessage(f"Crate new feature classes in Project GDB\n")
        for source_fc in sorted(source_fcs):
            arcpy.AddMessage(f"Source Feature Class: '{source_fc}'")
            arcpy.AddMessage(f"\tCopy Template Feature Class with source name to project GDB")
            arcpy.management.CopyFeatures(species_range_template, rf"{project_gdb}\{source_fc}")
            arcpy.AddMessage("\t\tCopy Features:\n\t\t\t"+arcpy.GetMessages().replace("\n", "\n\t\t\t")+"\n")

            del source_fc

##            source_fc_path      = rf"{source_gdb}\{source_fc}"
##            destination_fc      = source_fc
##            destination_fc_path = rf"{project_gdb}\{destination_fc}"
##            #if not arcpy.Exists(destination_fc_path):
##            # Copy Features
##            arcpy.AddMessage(f"\tCopy Features from '{source_fc}'")
##            #arcpy.management.CopyFeatures(source_fc_path, destination_fc_path+"_tmp")
##            arcpy.management.CopyFeatures(source_fc_path, destination_fc_path)
##            arcpy.AddMessage("\t\tCopy Features:\n\t\t\t"+arcpy.GetMessages().replace("\n", "\n\t\t\t")+"\n")

##            new_field_order = {"ID"         : "ID",
##                               "SCIENAME"   : "Scientific Name",
##                               "COMNAME"    : "Common Name",
##                               "LISTENTITY" : "Listed Entity",
##                               "DPSESU"     : "Distinct Population Segment or Evolutionarily Significant Unit",
##                               "LISTSTATUS" : "Listed Status",
##                               "TAXON"      : "Taxon",
##                               "LEADOFFICE" : "Lead Office",
##                               "FEDREG"     : "Federal Register Rule",
##                               "PUBDATE"    : "Publication Date",
##                               "EFFECTDATE" : "Effective Date",
##                               "CREATEDATE" : "Create Date",
##                               "NOTES"      : "Notes",
##                               "INPORTURL"  : "InPort URL",
##                               "REFERENCE"  : "Reference",
##                               "NMFSPAGE"   : "Species Webpage",
##                               "PUBLIC"     : "Public Mapper",
##                               "LIFESTAGE"  : "Lifestage",
##                               "BEHAVIOR"   : "Behavior",
##                               "FEATNAME"   : "Feature Name",
##                              }

        arcpy.management.Delete(species_range_template)
        del species_range_template

        arcpy.management.Compact(project_gdb)

        del source_fcs

        del project_folder

        arcpy.AddMessage(f"\n{'--End' * 10}--")

        # Imports

        # Function parameters
        del project_gdb, source_gdb

    except KeyboardInterrupt:
        raise SystemExit
    except arcpy.ExecuteWarning:
        arcpy.AddWarning(arcpy.GetMessages())
    except arcpy.ExecuteError:
        traceback.print_exc()
        arcpy.AddError(arcpy.GetMessages())
    except Exception as e:
        arcpy.AddError(str(e))
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

def create_feature_class(project_gdb="", source_gdb=""):
    try:
        # Imports

        # Use all of the cores on the machine
        arcpy.env.parallelProcessingFactor = "100%"
        arcpy.env.overwriteOutput = True

        # Define variables
        project_folder = os.path.dirname(project_gdb)
        scratch_folder = rf"{project_folder}\Scratch"
        scratch_gdb    = rf"{scratch_folder}\scratch.gdb"

        create_project_gdb(project_gdb)
        create_scratch_gdb(scratch_gdb)

        # Set the workspace environment to local file geodatabase
        arcpy.env.workspace = project_gdb
        # Set the scratchWorkspace environment to local file geodatabase
        arcpy.env.scratchWorkspace = scratch_gdb

        # Clean-up variables
        del scratch_folder, scratch_gdb

        arcpy.AddMessage(f"\n{'--Start' * 10}--\n")

        # work

        arcpy.env.workspace = source_gdb

        source_fcs = arcpy.ListFeatureClasses()

        arcpy.env.workspace = project_gdb

        species_range_template = arcpy.management.CreateFeatureclass(project_gdb, "SpeciesRangeTemplate", geometry_type='POLYGON')

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

        arcpy.management.AddFields(species_range_template, field_description, None)

        del field_description

        arcpy.AddMessage(f"Crate new feature classes in Project GDB\n")
        for source_fc in sorted(source_fcs):
            arcpy.AddMessage(f"Source Feature Class: '{source_fc}'")
            arcpy.AddMessage(f"\tCopy Template Feature Class with source name to project GDB")
            arcpy.management.CopyFeatures(species_range_template, rf"{project_gdb}\{source_fc}")
            arcpy.AddMessage("\t\tCopy Features:\n\t\t\t"+arcpy.GetMessages().replace("\n", "\n\t\t\t")+"\n")

            del source_fc

##            source_fc_path      = rf"{source_gdb}\{source_fc}"
##            destination_fc      = source_fc
##            destination_fc_path = rf"{project_gdb}\{destination_fc}"
##            #if not arcpy.Exists(destination_fc_path):
##            # Copy Features
##            arcpy.AddMessage(f"\tCopy Features from '{source_fc}'")
##            #arcpy.management.CopyFeatures(source_fc_path, destination_fc_path+"_tmp")
##            arcpy.management.CopyFeatures(source_fc_path, destination_fc_path)
##            arcpy.AddMessage("\t\tCopy Features:\n\t\t\t"+arcpy.GetMessages().replace("\n", "\n\t\t\t")+"\n")

##            new_field_order = {"ID"         : "ID",
##                               "SCIENAME"   : "Scientific Name",
##                               "COMNAME"    : "Common Name",
##                               "LISTENTITY" : "Listed Entity",
##                               "DPSESU"     : "Distinct Population Segment or Evolutionarily Significant Unit",
##                               "LISTSTATUS" : "Listed Status",
##                               "TAXON"      : "Taxon",
##                               "LEADOFFICE" : "Lead Office",
##                               "FEDREG"     : "Federal Register Rule",
##                               "PUBDATE"    : "Publication Date",
##                               "EFFECTDATE" : "Effective Date",
##                               "CREATEDATE" : "Create Date",
##                               "NOTES"      : "Notes",
##                               "INPORTURL"  : "InPort URL",
##                               "REFERENCE"  : "Reference",
##                               "NMFSPAGE"   : "Species Webpage",
##                               "PUBLIC"     : "Public Mapper",
##                               "LIFESTAGE"  : "Lifestage",
##                               "BEHAVIOR"   : "Behavior",
##                               "FEATNAME"   : "Feature Name",
##                              }

        arcpy.management.Delete(species_range_template)
        del species_range_template

        arcpy.management.Compact(project_gdb)

        del source_fcs

        del project_folder

        arcpy.AddMessage(f"\n{'--End' * 10}--")

        # Imports

        # Function parameters
        del project_gdb, source_gdb
    except:
        traceback.print_exc()
    else:
        return True
    finally:
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: raise Warning(f"\nWARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk

def create_feature_class2(gdb=""):
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

        arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)

        arcpy.AddMessage("Create a template polygon")
        # Create a spatial reference from a wkid
        spatial_ref = arcpy.SpatialReference(4326)

        # A list of features and coordinate pairs
        feature_info = [[[-82, 11], [-82, 16], [-72, 16], [-72, 11]],
                        [[-80, 18], [-80, 24], [-75, 24], [-75, 18]]]

        # A list that will contain the Polygon objects
        features = []

        arcpy.AddMessage("Create a polygon object")
        # Create Polygon objects from an array of points
        for feature in feature_info:
            array = arcpy.Array([arcpy.Point(*coords) for coords in feature])

            # Add the first coordinate pair to the end to close polygon
            array.append(array[0])

            polygon = arcpy.Polygon(array, spatial_ref)
            features.append(polygon)

            del feature
        del spatial_ref, feature_info, array, polygon

        fc = "SpeciesRangeTemplate20241230"
        species_range_fc = rf"{gdb}\{fc}"
        del fc

        arcpy.AddMessage("Copy features to feature class")
        # Persist a copy of the Polygon objects using CopyFeatures
        arcpy.management.CopyFeatures(features, species_range_fc)
        del features

        field_description = [
                             #["FeatureClass", "TEXT", "Feature Class", 50, "#", "#"],
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

        arcpy.AddMessage("Add fields to template polygon")
        arcpy.management.AddFields(species_range_fc, field_description, None)

        del field_description

        # XML Files
        species_range_fc_metadata_xml         = rf"{project_folder}\{os.path.basename(species_range_fc)}.xml"
        species_range_fc_metadata_xml_updated = rf"{project_folder}\{os.path.basename(species_range_fc)} UPDATED.xml"
        species_range_metadata_template       = rf"{project_folder}\SpeciesRangeMetadataTemplate.xml"
        species_range_metadata_contact_template       = rf"{project_folder}\SpeciesRangeTemplateMetadataContact.xml"
        species_range_metadata_entity_template       = rf"{project_folder}\SpeciesRangeTemplateMetadataEntity.xml"

        arcpy.AddMessage("Create and Sync Metadata")

        dataset_md = md.Metadata(species_range_fc)
        dataset_md.synchronize('ALWAYS')
        dataset_md.save()

        arcpy.AddMessage("Save Metadata as an XML file")
        dataset_md.saveAsXML(species_range_fc_metadata_xml, "REMOVE_ALL_SENSITIVE_INFO")
        #dataset_md.saveAsXML(species_range_fc_metadata_xml, "EXACT_COPY")

        del dataset_md

        pretty_format_xml_file(species_range_fc_metadata_xml)

        dataset_md = md.Metadata(species_range_fc)
        #dataset_md = md.Metadata(species_range_fc_metadata_xml_updated)
        #dataset_md.importMetadata(species_range_metadata_template, "ARCGIS_METADATA")
        #arcpy.AddMessage("Import Metadata Contact Info")
        dataset_md.importMetadata(species_range_metadata_entity_template)
        dataset_md.synchronize('SELECTIVE')
        dataset_md.save()
        dataset_md.synchronize('ALWAYS')
        dataset_md.save()
        dataset_md.importMetadata(species_range_metadata_contact_template, "ARCGIS_METADATA")
        dataset_md.synchronize('SELECTIVE')
        dataset_md.save()
        dataset_md.synchronize('ALWAYS')
        dataset_md.save()
        #dataset_md.importMetadata(species_range_metadata_template)
        #new_md = md.Metadata(species_range_metadata_template)
        #dataset_md.copy(new_md)
        #del new_md
        #dataset_md.save()
        #dataset_md.synchronize('SELECTIVE')
        #dataset_md.save()
        #arcpy.AddMessage("Import Metadata Entity Info")
        #dataset_md.importMetadata(species_range_metadata_entity_template, "ARCGIS_METADATA")
        #dataset_md.importMetadata(species_range_metadata_contact_template)
        #dataset_md.save()
        #dataset_md.synchronize('SELECTIVE')
        #dataset_md.save()
        #dataset_md.synchronize('ALWAYS')
        #dataset_md.save()
        dataset_md.saveAsXML(species_range_fc_metadata_xml_updated, "REMOVE_ALL_SENSITIVE_INFO")

        del dataset_md

        del species_range_fc

        pretty_format_xml_file(species_range_fc_metadata_xml_updated)

        #print(species_range_fc_metadata_xml_updated.replace(".xml", " SELECTIVE.xml"))
        #metadata_xml_string = dataset_md.xml

        # Parse the XML file
        #tree = etree.parse(StringIO(metadata_xml_string))

        #print(etree.tostring(tree, pretty_print=True).decode())
        #print(etree.tostring(tree, pretty_print=True, method='html', encoding="utf-8").decode())

        #del tree
        #del metadata_xml_string

##        # Parse the XML file
##        eainfo_old_tree = etree.parse(StringIO(metadata_xml_string))
##        eainfo_new_tree = etree.parse(species_range_metadata_template)
##
##        del metadata_xml_string
##
##        # Get the root element
##        eainfo_old_root = eainfo_old_tree.getroot()
##        eainfo_new_root = eainfo_new_tree.getroot()
##
##        #print(eainfo_old_root.tag)
##        #print(eainfo_old_root.find("eainfo").tag)
##        #print(eainfo_new_root.tag)
##
##        # Find the elements
##        eainfo_old_child = eainfo_old_root.find("eainfo")
##        eainfo_new_child = eainfo_new_root.find("eainfo")
##
##        # Replace child1 with child2
##        eainfo_old_root.replace(eainfo_old_child, eainfo_new_child)
##
##        # Print the modified XML
##        #print(etree.tostring(eainfo_old_tree, pretty_print=True).decode())
##
##        #root = ET.fromstring(metadata_xml_string)
##        #del metadata_xml_string
##
##        # get modified XML
##        updated_xml_string = etree.tostring(eainfo_old_root, encoding="utf-8")
##        del eainfo_old_root
##
##        # import result back into metadata
##        arcpy.AddMessage("Saving updated metadata with the item...")
##        dataset_md.xml = updated_xml_string
##        dataset_md.save()
##        dataset_md.reload()
##        dataset_md.saveAsXML(species_range_fc_metadata_xml_updated, "REMOVE_ALL_SENSITIVE_INFO")
##        del dataset_md, updated_xml_string
##
##        del eainfo_old_tree, eainfo_new_tree, eainfo_new_root
##        del eainfo_old_child, eainfo_new_child
##
##        pretty_format_xml_file(species_range_fc_metadata_xml)
##        pretty_format_xml_file(species_range_fc_metadata_xml_updated)
##
##        pretty_format_xml_file(species_range_metadata_template)
##
##        arcpy.AddMessage("Compact GDB")
##        arcpy.management.Compact(gdb)

        del species_range_metadata_template
        del species_range_fc_metadata_xml, species_range_fc_metadata_xml_updated
        del species_range_metadata_contact_template, species_range_metadata_entity_template

        arcpy.AddMessage(f"\n{'--End' * 10}--")

        #
        del project_folder

        # Imports
        del md, etree, StringIO

        # Function parameters
        del gdb

    except arcpy.ExecuteError:
        arcpy.AddError(arcpy.GetMessages())
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

def process_list():
    try:
        pass

    except Warning as w:
        print(f"{w} captured in the '{inspect.stack()[0][3]}' function")
    except Exception as e:
        traceback.print_exc()
    except:
        traceback.print_exc()
    else:
        return True
    finally:
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: raise Warning(f"\nWARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk

def update_access_constraints():
    try:
        pass
    except Warning as w:
        print(f"{w} captured in the '{inspect.stack()[0][3]}' function")
    except Exception as e:
        traceback.print_exc()
    except:
        traceback.print_exc()
    else:
        return True
    finally:
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: raise Warning(f"\nWARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk

def main():
    try:
        from time import gmtime, localtime, strftime, time

        # Set a start time so that we can see how log things take
        start_time = time()

        print(f"{'-' * 90}")
        print(f"Python Script:  {os.path.basename(__file__)}")
        print(f"Location:       {os.path.dirname(__file__)}")
        print(f"Python Version: {sys.version} Environment: {os.path.basename(sys.exec_prefix)}")
        print(f"{'-' * 90}\n")

        folder = rf"{os.path.dirname(__file__)}\Export"

        # Create feature class
        CreateFeatureClass = True
        if CreateFeatureClass:
            create_feature_class(gdb=project_gdb)
        del CreateFeatureClass

        del folder

        # Elapsed time
        end_time = time()
        elapse_time =  end_time - start_time

        print(f"\n{'-' * 90}")
        print(f"Python script: {os.path.basename(__file__)} successfully completed {strftime('%a %b %d %I:%M %p', localtime())}")
        print(u"Elapsed Time {0} (H:M:S)".format(strftime("%H:%M:%S", gmtime(elapse_time))))
        print(f"{'-' * 90}")
        del elapse_time, end_time, start_time
        del gmtime, localtime, strftime, time

    except Warning as w:
        print(f"{w} captured in the '{inspect.stack()[0][3]}' function")
    except Exception as e:
        print(f"{e} captured in the '{inspect.stack()[0][3]}' function")
    except:
        traceback.print_exc()
    else:
        return True
    finally:
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: raise Warning(f"\nWARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk

if __name__ == '__main__':
    main()
