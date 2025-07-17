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

def create_maps(project_file="", project=""):
    try:
        # Import
        from arcpy import metadata as md

        import dismap
        importlib.reload(dismap)
        from dismap import dataset_title_dict, pretty_format_xml_file

        arcpy.env.overwriteOutput          = True
        arcpy.env.parallelProcessingFactor = "100%"
        arcpy.SetLogMetadata(True)
        arcpy.SetSeverityLevel(2)
        arcpy.SetMessageLevels(['NORMAL']) # NORMAL, COMMANDSYNTAX, DIAGNOSTICS, PROJECTIONTRANSFORMATION

        # Map Cleanup
        MapCleanup = False
        if MapCleanup:
            map_cleanup(project_file)
        del MapCleanup

        base_project_folder = rf"{os.path.dirname(project_file)}"
        project_file   = rf"{base_project_folder}\DisMAP.aprx"
        project_folder      = rf"{base_project_folder}\{project}"
        project_gdb         = rf"{project_folder}\{project}.gdb"
        metadata_folder     = rf"{project_folder}\Export Metadata"
        scratch_folder      = rf"{project_folder}\Scratch"

        arcpy.env.workspace        = project_gdb
        arcpy.env.scratchWorkspace = rf"{scratch_folder}\scratch.gdb"

        aprx = arcpy.mp.ArcGISProject(project_file)
        home_folder = aprx.homeFolder

        #arcpy.AddMessage(f"\n{'-' * 90}\n")

        metadata_dictionary = dataset_title_dict(project_gdb)

        datasets = list()

        walk = arcpy.da.Walk(project_gdb)

        for dirpath, dirnames, filenames in walk:
            for filename in filenames:
                datasets.append(os.path.join(dirpath, filename))
                del filename
            del dirpath, dirnames, filenames
        del walk

        for dataset_path in sorted(datasets):
            arcpy.AddMessage(dataset_path)
            dataset_name = os.path.basename(dataset_path)
            data_type = arcpy.Describe(dataset_path).dataType
            if data_type == "Table":
                #arcpy.AddMessage(f"Dataset Name: {dataset_name}")
                #arcpy.AddMessage(f"\tData Type: {data_type}")

                if "IDW" in dataset_name:
                    arcpy.AddMessage(f"Dataset Name: {dataset_name}")
                    if "Indicators" in dataset_name:
                        arcpy.AddMessage(f"\tRegion Indicators")

                    elif "LayerSpeciesYearImageName" in dataset_name:
                        arcpy.AddMessage(f"\tRegion Layer Species Year Image Name")

                    else:
                        arcpy.AddMessage(f"\tRegion Table")

                elif "GLMME" in dataset_name:
                    arcpy.AddMessage(f"Dataset Name: {dataset_name}")
                    if "Indicators" in dataset_name:
                        arcpy.AddMessage(f"\tGLMME Region Indicators")

                    elif "LayerSpeciesYearImageName" in dataset_name:
                        arcpy.AddMessage(f"\tGLMME Layer Species Year Image Name")

                    else:
                        arcpy.AddMessage(f"\tGLMME Region Table")

                else:
                    arcpy.AddMessage(f"Dataset Name: {dataset_name}")
                    if "Indicators" in dataset_name:
                        arcpy.AddMessage(f"\tMain Indicators Table")

                    elif "LayerSpeciesYearImageName" in dataset_name:
                        arcpy.AddMessage(f"\tLayer Species Year Image Name")

                    elif "Datasets" in dataset_name:
                        arcpy.AddMessage(f"\tDataset Table")

                    elif "Species_Filter" in dataset_name:
                        arcpy.AddMessage(f"\tSpecies Filter Table")

                    else:
                        arcpy.AddMessage(f"\tDataset Name: {dataset_name}")

            elif data_type == "FeatureClass":
                #arcpy.AddMessage(f"\tData Type: {data_type}")

                if "IDW" in dataset_name:
                    arcpy.AddMessage(f"Dataset Name: {dataset_name}")
                    if dataset_name.endswith("Boundary"):
                        arcpy.AddMessage(f"\tBoundary")

                    elif dataset_name.endswith("Extent_Points"):
                        arcpy.AddMessage(f"\tExtent_Points")

                    elif dataset_name.endswith("Fishnet"):
                        arcpy.AddMessage(f"\tFishnet")

                    elif dataset_name.endswith("Lat_Long"):
                        arcpy.AddMessage(f"\tLat_Long")

                    elif dataset_name.endswith("Region"):
                        arcpy.AddMessage(f"\tRegion")

                    elif dataset_name.endswith("Sample_Locations"):
                        arcpy.AddMessage(f"\tSample_Locations")

                    else:
                        pass

                elif "GLMME" in dataset_name:
                    arcpy.AddMessage(f"Dataset Name: {dataset_name}")
                    if dataset_name.endswith("Boundary"):
                        arcpy.AddMessage(f"\tBoundary")

                    elif dataset_name.endswith("Extent_Points"):
                        arcpy.AddMessage(f"\tExtent_Points")

                    elif dataset_name.endswith("Fishnet"):
                        arcpy.AddMessage(f"\tFishnet")

                    elif dataset_name.endswith("Lat_Long"):
                        arcpy.AddMessage(f"\tLat_Long")

                    elif dataset_name.endswith("Region"):
                        arcpy.AddMessage(f"\tRegion")

                    elif dataset_name.endswith("GRID_Points"):
                        arcpy.AddMessage(f"\tGRID_Points")

                    else:
                        pass

                elif "DisMAP_Regions" == dataset_name:
                    arcpy.AddMessage(f"Dataset Name: {dataset_name}")
                    if dataset_name.endswith("Regions"):
                        arcpy.AddMessage(f"\tDisMAP Regions")

                else:
                    arcpy.AddMessage(f"Else Dataset Name: {dataset_name}")

            elif data_type == "RasterDataset":

                if "IDW" in dataset_name:
                    arcpy.AddMessage(f"Dataset Name: {dataset_name}")
                    if dataset_name.endswith("Bathymetry"):
                        arcpy.AddMessage(f"\tBathymetry")

                    elif dataset_name.endswith("Latitude"):
                        arcpy.AddMessage(f"\tLatitude")

                    elif dataset_name.endswith("Longitude"):
                        arcpy.AddMessage(f"\tLongitude")

                    elif dataset_name.endswith("Raster_Mask"):
                        arcpy.AddMessage(f"\tRaster_Mask")

                elif "GLMME" in dataset_name:
                    arcpy.AddMessage(f"Dataset Name: {dataset_name}")
                    if dataset_name.endswith("Bathymetry"):
                        arcpy.AddMessage(f"\tBathymetry")

                    elif dataset_name.endswith("Latitude"):
                        arcpy.AddMessage(f"\tLatitude")

                    elif dataset_name.endswith("Longitude"):
                        arcpy.AddMessage(f"\tLongitude")

                    elif dataset_name.endswith("Raster_Mask"):
                        arcpy.AddMessage(f"\tRaster_Mask")

            elif data_type == "MosaicDataset":

                if "IDW" in dataset_name:
                    arcpy.AddMessage(f"Dataset Name: {dataset_name}")
                    if dataset_name.endswith("Mosaic"):
                        arcpy.AddMessage(f"\tMosaic")

                elif "GLMME" in dataset_name:
                    arcpy.AddMessage(f"Dataset Name: {dataset_name}")
                    if dataset_name.endswith("Mosaic"):
                        arcpy.AddMessage(f"\tMosaic")

                elif "CRF" in dataset_name:
                    arcpy.AddMessage(f"Dataset Name: {dataset_name}")
                    if dataset_name.endswith("CRF"):
                        arcpy.AddMessage(f"\tCRF")

                else:
                    pass
            else:
                pass

            del data_type

            del dataset_name, dataset_path
        del datasets

##        # DatasetCode, CSVFile, TransformUnit, TableName, GeographicArea, CellSize,
##        # PointFeatureType, FeatureClassName, Region, Season, DateCode, Status,
##        # DistributionProjectCode, DistributionProjectName, SummaryProduct,
##        # FilterRegion, FilterSubRegion, FeatureServiceName, FeatureServiceTitle,
##        # MosaicName, MosaicTitle, ImageServiceName, ImageServiceTitle
##
##        # Get values for table_name from Datasets table
##        #fields = ["FeatureClassName", "FeatureServiceName", "FeatureServiceTitle"]
##        fields = ["DatasetCode", "PointFeatureType", "FeatureClassName", "Region", "Season", "DateCode", "DistributionProjectCode"]
##        datasets = [row for row in arcpy.da.SearchCursor(rf"{project_gdb}\Datasets", fields, where_clause = f"FeatureClassName IS NOT NULL AND DistributionProjectCode NOT IN ('GLMME', 'GFDL')")]
##        #datasets = [row for row in arcpy.da.SearchCursor(rf"{project_gdb}\Datasets", fields, where_clause = f"FeatureClassName IS NOT NULL and TableName = 'AI_IDW'")]
##        del fields
##
##        for dataset in datasets:
##            dataset_code, point_feature_type, feature_class_name, region_latitude, season, date_code, distribution_project_code = dataset
##
##            feature_service_name  = f"{dataset_code}_{point_feature_type}_{date_code}".replace("None", "").replace(" ", "_").replace("__", "_")
##
##            if distribution_project_code == "IDW":
##                feature_service = f"{region_latitude} {season} {point_feature_type} {date_code}".replace("None", "").replace("  ", " ")
##            elif distribution_project_code in ["GLMME", "GFDL"]:
##                feature_service = f"{region_latitude} {distribution_project_code} {point_feature_type} {date_code}".replace("None", "").replace("  ", " ")
##            else:
##                feature_service = f"{feature_service_name}".replace("_", " ")
##
##            map_title = feature_service.replace("GRID Points", "").replace("Sample Locations", "").replace("  ", " ")
##
##            feature_class_path = f"{project_gdb}\{feature_class_name}"
##
##            arcpy.AddMessage(f"Dataset Code: {dataset_code}")
##            arcpy.AddMessage(f"\tFeature Service Name:   {feature_service_name}")
##            arcpy.AddMessage(f"\tFeature Service Title:  {feature_service}")
##            arcpy.AddMessage(f"\tMap Title:              {map_title}")
##            arcpy.AddMessage(f"\tFeature Class Name:     {feature_class_name}")
##            arcpy.AddMessage(f"\tFeature Class Path:     {feature_class_path}")
##
##            height = arcpy.Describe(feature_class_path).extent.YMax - arcpy.Describe(feature_class_path).extent.YMin
##            width  = arcpy.Describe(feature_class_path).extent.XMax - arcpy.Describe(feature_class_path).extent.XMin
##
##            # map_width, map_height
##            map_width, map_height = 2, 3
##            #map_width, map_height = 8.5, 11
##
##            if height > width:
##                page_height = map_height; page_width = map_width
##            elif height < width:
##                page_height = map_width; page_width = map_height
##            else:
##                page_width = map_width; page_height = map_height
##
##            del map_width, map_height
##            del height, width
##
##            if map_title not in [cm.name for cm in aprx.listMaps()]:
##                arcpy.AddMessage(f"Creating Map: {map_title}")
##                aprx.createMap(f"{map_title}", "Map")
##                aprx.save()
##
##            if map_title not in [cl.name for cl in aprx.listLayouts()]:
##                arcpy.AddMessage(f"Creating Layout: {map_title}")
##                aprx.createLayout(page_width, page_height, "INCH", f"{map_title}")
##                aprx.save()
##
##            del feature_service_name, feature_service
##            del dataset_code, point_feature_type, feature_class_name, region_latitude, season
##            del date_code, distribution_project_code
##
##            current_map = [cm for cm in aprx.listMaps() if cm.name == map_title][0]
##            arcpy.AddMessage(f"Current Map:  {current_map.name}")
##
##            feature_class_layer = arcpy.management.MakeFeatureLayer(feature_class_path, f"{map_title}")
##
##            feature_class_layer_file = arcpy.management.SaveToLayerFile(feature_class_layer, rf"{home_folder}\Layers\{feature_class_layer}.lyrx")
##            del feature_class_layer_file
##
##            feature_class_layer_file = arcpy.mp.LayerFile(rf"{home_folder}\Layers\{feature_class_layer}.lyrx")
##
##            arcpy.management.Delete(feature_class_layer)
##            del feature_class_layer
##
##            current_map.addLayer(feature_class_layer_file)
##            del feature_class_layer_file
##
##            #aprx_basemaps = aprx.listBasemaps()
##            #basemap = 'GEBCO Basemap/Contours (NOAA NCEI Visualization)'
##            basemap = "Terrain with Labels"
##
##            current_map.addBasemap(basemap)
##            del basemap
##
##            #current_map_view = current_map.defaultView
##            #current_map_view.exportToPNG(rf"{home_folder}\Layers\{map_title}.png", width=200, height=133, resolution = 96, color_mode="24-BIT_TRUE_COLOR", embed_color_profile=True)
##            #del current_map_view
##
##        # #            from arcpy import metadata as md
##        # #
##        # #            fc_md = md.Metadata(feature_class_path)
##        # #            fc_md.thumbnailUri = rf"{home_folder}\Layers\{map_title}.png"
##        # #            fc_md.save()
##        # #            del fc_md
##        # #            del md
##
##            aprx.save()
##
##            current_layout = [cl for cl in aprx.listLayouts() if cl.name == map_title][0]
##            arcpy.AddMessage(f"Current Layout: {current_layout.name}")
##
##            current_layout.openView()
##
##            arcpy.AddMessage(f"Create a new map frame using a point geometry")
##            #Create a new map frame using a point geometry
##            mf1 = current_layout.createMapFrame(arcpy.Point(0.01,0.01), current_map, 'New MF - Point')
##            #mf1.elementWidth = 10
##            #mf1.elementHeight = 7.5
##            mf1.elementWidth  = page_width  - 0.01
##            mf1.elementHeight = page_height - 0.01
##
##            lyr = current_map.listLayers(f"{map_title}")[0]
##
##            #Zoom to ALL selected features and export to PDF
##            arcpy.SelectLayerByAttribute_management(lyr, 'NEW_SELECTION')
##            mf1.zoomToAllLayers(True)
##            arcpy.SelectLayerByAttribute_management(lyr, 'CLEAR_SELECTION')
##
##            #Set the map frame extent to the extent of a layer and export to PDF
##            mf1.camera.setExtent(mf1.getLayerExtent(lyr, False, True))
##            mf1.camera.scale = mf1.camera.scale * 1.1 #add a slight buffer
##
##            del lyr
##
##            arcpy.AddMessage(f"Create a new bookmark set to the map frame's default extent")
##            #Create a new bookmark set to the map frame's default extent
##            bkmk = mf1.createBookmark('Default Extent', "The map's default extent")
##            bkmk.updateThumbnail()
##            del mf1
##            del bkmk
##
##            #Create point text element using a system style item
##            #txtStyleItem = aprx.listStyleItems('ArcGIS 2D', 'TEXT', 'Title (Serif)')[0]
##            #ptTxt = aprx.createTextElement(current_layout, arcpy.Point(5.5, 4.25), 'POINT', f'{map_title}', 10, style_item=txtStyleItem)
##            #del txtStyleItem
##
##            #Change the anchor position and reposition the text to center
##            #ptTxt.setAnchor('Center_Point')
##            #ptTxt.elementPositionX = page_width / 2.0
##            #ptTxt.elementPositionY = page_height - 0.25
##            #del ptTxt
##
##            #arcpy.AddMessage(f"Using CIM to update border")
##            #current_layout_cim = current_layout.getDefinition('V3')
##            #for elm in current_layout_cim.elements:
##            #    if type(elm).__name__ == 'CIMMapFrame':
##            #        if elm.graphicFrame.borderSymbol.symbol.symbolLayers:
##            #            sym = elm.graphicFrame.borderSymbol.symbol.symbolLayers[0]
##            #            sym.width = 5
##            #            sym.color.values = [255, 0, 0, 100]
##            #        else:
##            #            arcpy.AddWarning(elm.name + ' has NO symbol layers')
##            #current_layout.setDefinition(current_layout_cim)
##            #del current_layout_cim, elm, sym
##
##            ExportLayout = True
##            if ExportLayout:
##                #Export the resulting imported layout and changes to JPEG
##                arcpy.AddMessage(f"Exporting '{current_layout.name}'")
##                current_layout.exportToJPEG(rf"{home_folder}\Layouts\{current_layout.name}.jpg")
##            del ExportLayout
##
##
##            from arcpy import metadata as md
##
##            fc_md = md.Metadata(feature_class_path)
##            #fc_md.thumbnailUri = rf"{home_folder}\Layers\{map_title}.png"
##            fc_md.thumbnailUri = rf"{home_folder}\Layouts\{current_layout.name}.jpg"
##            fc_md.save()
##            del fc_md
##            del md
##
##            aprx.save()
##
##            aprx.deleteItem(current_map); del current_map
##            aprx.deleteItem(current_layout); del current_layout
##
##            del page_width, page_height
##            del map_title, feature_class_path
##            del dataset
##        del datasets
##
##        # TODO: Possibly create a dictionary that can be saved to JSON
##
##        aprx.save()
##
##        arcpy.AddMessage(f"\nCurrent Maps & Layouts")
##
##        current_maps    = aprx.listMaps()
##        current_layouts = aprx.listLayouts()
##
##        if current_maps:
##            arcpy.AddMessage(f"\nCurrent Maps\n")
##            for current_map in current_maps:
##                arcpy.AddMessage(f"\tProject Map: {current_map.name}")
##                del current_map
##        else:
##            arcpy.AddWarning("No maps in Project")
##
##        if current_layouts:
##            arcpy.AddMessage(f"\nCurrent Layouts\n")
##            for current_layout in current_layouts:
##                arcpy.AddMessage(f"\tProject Layout: {current_layout.name}")
##                del current_layout
##        else:
##            arcpy.AddWarning("No layouts in Project")
##
##        arcpy.AddMessage(f"\n{'-' * 90}\n")
##
##        del current_layouts, current_maps

        # Declared Variables set in function for aprx
        del home_folder
        # Save aprx one more time and then delete
        aprx.save()
        del aprx

        # Declared Variables set in function
        del project_gdb, base_project_folder, metadata_folder
        del project_folder, scratch_folder
        del metadata_dictionary

        # Imports
        del dismap, dataset_title_dict
        del md

        # Function Parameters
        del project_file, project

    except KeyboardInterrupt:
        raise SystemExit
    except arcpy.ExecuteWarning:
        arcpy.AddWarning(str(traceback.print_exc()) + arcpy.GetMessages())
        raise SystemExit
    except arcpy.ExecuteError:
        arcpy.AddError(str(traceback.print_exc()) + arcpy.GetMessages())
        raise SystemExit
    except SystemExit as se:
        arcpy.AddError(str(se))
        raise SystemExit
    except:
        arcpy.AddError(str(traceback.print_exc()))
        raise SystemExit
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
            sddraft.portalFolder = f"National ESA Species Ranges"

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

        CreateMaps = False
        if CreateMaps:
            result = create_maps(project_file, project)
            arcpy.AddMessage(result)
            del result
        del CreateMaps

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
        if rk: raise Warning(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        # Cleanup
        arcpy.management.ClearWorkspaceCache()

if __name__ == '__main__':
    try:
        # Append the location of this scrip to the System Path
        #sys.path.append(os.path.dirname(__file__))
        sys.path.append(os.path.dirname(os.path.dirname(__file__)))

        main(project_folder=rf"{os.path.dirname(os.path.dirname(__file__))}")
    except Warning as w:
        print(w, flush=True)