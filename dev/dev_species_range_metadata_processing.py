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

def create_thumbnails(base_project_file="", project_name=""):
    try:
        # Import
        from arcpy import metadata as md

        import dismap
        importlib.reload(dismap)
        from dismap import parse_xml_file_format_and_save

        arcpy.env.overwriteOutput          = True
        arcpy.env.parallelProcessingFactor = "100%"
        arcpy.SetLogMetadata(True)
        arcpy.SetSeverityLevel(2)
        arcpy.SetMessageLevels(['NORMAL']) # NORMAL, COMMANDSYNTAX, DIAGNOSTICS, PROJECTIONTRANSFORMATION

        base_project_folder = rf"{os.path.dirname(base_project_file)}"
        base_project_file   = rf"{base_project_folder}\DisMAP.aprx"
        project_folder      = rf"{base_project_folder}\{project_name}"
        project_gdb         = rf"{project_folder}\{project_name}.gdb"
        metadata_folder     = rf"{project_folder}\Export Metadata"
        crfs_folder         = rf"{project_folder}\CRFs"
        scratch_folder      = rf"{project_folder}\Scratch"

        arcpy.env.workspace        = project_gdb
        arcpy.env.scratchWorkspace = rf"{scratch_folder}\scratch.gdb"

        aprx = arcpy.mp.ArcGISProject(base_project_file)
        home_folder = aprx.homeFolder

        workspaces = [project_gdb, crfs_folder]

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

                print(f"Dataset Name: {dataset_name}")

                if "Datasets" == dataset_name:

                    print(f"\tDataset Table")

                    dataset_md = md.Metadata(dataset_path)

                    out_xml = rf"{metadata_folder}\Table\{dataset_name}.xml"
                    dataset_md.saveAsXML(out_xml)
                    parse_xml_file_format_and_save(out_xml)
                    del out_xml

                    del dataset_md

                elif "Species_Filter" == dataset_name:

                    print(f"\tSpecies Filter Table")

                    dataset_md = md.Metadata(dataset_path)

                    out_xml = rf"{metadata_folder}\Table\{dataset_name}.xml"
                    dataset_md.saveAsXML(out_xml)
                    parse_xml_file_format_and_save(out_xml)
                    del out_xml

                    del dataset_md

                elif "Indicators" in dataset_name:

                    print(f"\tIndicators")

                    dataset_md = md.Metadata(dataset_path)

                    out_xml = rf"{metadata_folder}\Table\{dataset_name}.xml"
                    dataset_md.saveAsXML(out_xml)
                    parse_xml_file_format_and_save(out_xml)
                    del out_xml

                    del dataset_md

                elif "LayerSpeciesYearImageName" in dataset_name:

                    print(f"\tLayer Species Year Image Name")

                    dataset_md = md.Metadata(dataset_path)

                    out_xml = rf"{metadata_folder}\Table\{dataset_name}.xml"
                    dataset_md.saveAsXML(out_xml)
                    parse_xml_file_format_and_save(out_xml)
                    del out_xml

                    del dataset_md

                elif dataset_name.endswith("Boundary"):

                    print(f"\tBoundary")

                    dataset_md = md.Metadata(dataset_path)

                    out_xml = rf"{metadata_folder}\Boundary\{dataset_name}.xml"
                    dataset_md.saveAsXML(out_xml)
                    parse_xml_file_format_and_save(out_xml)
                    del out_xml

                    del dataset_md

                elif dataset_name.endswith("Extent_Points"):

                    print(f"\tExtent_Points")

                    dataset_md = md.Metadata(dataset_path)

                    out_xml = rf"{metadata_folder}\Extent_Points\{dataset_name}.xml"
                    dataset_md.saveAsXML(out_xml)
                    parse_xml_file_format_and_save(out_xml)
                    del out_xml

                    del dataset_md

                elif dataset_name.endswith("Fishnet"):

                    print(f"\tFishnet")

                    dataset_md = md.Metadata(dataset_path)

                    out_xml = rf"{metadata_folder}\Fishnet\{dataset_name}.xml"
                    dataset_md.saveAsXML(out_xml)
                    parse_xml_file_format_and_save(out_xml)
                    del out_xml

                    del dataset_md

                elif dataset_name.endswith("Lat_Long"):

                    print(f"\tLat_Long")

                    dataset_md = md.Metadata(dataset_path)

                    out_xml = rf"{metadata_folder}\Lat_Long\{dataset_name}.xml"
                    dataset_md.saveAsXML(out_xml)
                    parse_xml_file_format_and_save(out_xml)
                    del out_xml

                    del dataset_md

                elif dataset_name.endswith("Region"):

                    print(f"\tRegion")

                    dataset_md = md.Metadata(dataset_path)

                    out_xml = rf"{metadata_folder}\Region\{dataset_name}.xml"
                    dataset_md.saveAsXML(out_xml)
                    parse_xml_file_format_and_save(out_xml)
                    del out_xml

                    del dataset_md

                elif dataset_name.endswith("Sample_Locations"):

                    print(f"\tSample_Locations")

                    dataset_md = md.Metadata(dataset_path)

                    out_xml = rf"{metadata_folder}\Sample_Locations\{dataset_name}.xml"
                    dataset_md.saveAsXML(out_xml)
                    parse_xml_file_format_and_save(out_xml)
                    del out_xml

                    del dataset_md

                elif dataset_name.endswith("GRID_Points"):

                    print(f"\tGRID_Points")

                    dataset_md = md.Metadata(dataset_path)

                    out_xml = rf"{metadata_folder}\GRID_Points\{dataset_name}.xml"
                    dataset_md.saveAsXML(out_xml)
                    parse_xml_file_format_and_save(out_xml)
                    del out_xml

                    del dataset_md

                elif "DisMAP_Regions" == dataset_name:

                    print(f"\tDisMAP_Regions")

                    dataset_md = md.Metadata(dataset_path)

                    out_xml = rf"{metadata_folder}\Region\{dataset_name}.xml"
                    dataset_md.saveAsXML(out_xml)
                    parse_xml_file_format_and_save(out_xml)
                    del out_xml

                    del dataset_md

                elif dataset_name.endswith("Bathymetry"):

                    print(f"\tBathymetry")

                    dataset_md = md.Metadata(dataset_path)

                    out_xml = rf"{metadata_folder}\Bathymetry\{dataset_name}.xml"
                    dataset_md.saveAsXML(out_xml)
                    parse_xml_file_format_and_save(out_xml)
                    del out_xml

                    del dataset_md

                elif dataset_name.endswith("Latitude"):

                    print(f"\tLatitude")

                    dataset_md = md.Metadata(dataset_path)

                    out_xml = rf"{metadata_folder}\Latitude\{dataset_name}.xml"
                    dataset_md.saveAsXML(out_xml)
                    parse_xml_file_format_and_save(out_xml)
                    del out_xml

                    del dataset_md

                elif dataset_name.endswith("Longitude"):

                    print(f"\tLongitude")

                    dataset_md = md.Metadata(dataset_path)

                    out_xml = rf"{metadata_folder}\Longitude\{dataset_name}.xml"
                    dataset_md.saveAsXML(out_xml)
                    parse_xml_file_format_and_save(out_xml)
                    del out_xml

                    del dataset_md

                elif dataset_name.endswith("Raster_Mask"):

                    print(f"\tRaster_Mask")

                    dataset_md = md.Metadata(dataset_path)

                    out_xml = rf"{metadata_folder}\Raster_Mask\{dataset_name}.xml"
                    dataset_md.saveAsXML(out_xml)
                    parse_xml_file_format_and_save(out_xml)
                    del out_xml

                    del dataset_md

                elif dataset_name.endswith("Mosaic"):

                    print(f"\tMosaic")

                    dataset_md = md.Metadata(dataset_path)

                    out_xml = rf"{metadata_folder}\Mosaic\{dataset_name}.xml"
                    dataset_md.saveAsXML(out_xml)
                    parse_xml_file_format_and_save(out_xml)
                    del out_xml

                    del dataset_md

                elif dataset_name.endswith(".crf"):

                    print(f"\tCRF")

                    dataset_md = md.Metadata(dataset_path)

                    out_xml = rf"{metadata_folder}\CRF\{dataset_name}.xml"
                    dataset_md.saveAsXML(out_xml)
                    parse_xml_file_format_and_save(out_xml)
                    del out_xml

                    del dataset_md

                else:
                    pass
                    print(f"\tRegion Table")

                    if dataset_name.endswith("IDW"):

                        dataset_md = md.Metadata(dataset_path)

                        out_xml = rf"{metadata_folder}\Table\{dataset_name}.xml"
                        dataset_md.saveAsXML(out_xml)
                        parse_xml_file_format_and_save(out_xml)
                        del out_xml

                        del dataset_md

                    elif dataset_name.endswith("GLMME"):

                        dataset_md = md.Metadata(dataset_path)

                        out_xml = rf"{metadata_folder}\Table\{dataset_name}.xml"
                        dataset_md.saveAsXML(out_xml)
                        parse_xml_file_format_and_save(out_xml)
                        del out_xml

                        del dataset_md

                    else:
                        pass

                del dataset_name, dataset_path

            del workspace, datasets

        del workspaces

        # Variables set in function for aprx
        del home_folder
        # Save aprx one more time and then delete
        aprx.save()
        del aprx

        # Variables set in function
        del project_gdb, base_project_folder, metadata_folder, crfs_folder
        del project_folder, scratch_folder

        # Imports
        del dismap, parse_xml_file_format_and_save
        del md

        # Function Parameters
        del base_project_file, project_name

    except Exception:
        pass
    except:
        traceback.print_exc()
    else:
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        pass

def export_to_inport_xml_files(base_project_file="", project_name=""):
    try:
        if not base_project_file or not project_name: raise SystemExit("parameters are missing")

        # Import
        from arcpy import metadata as md

        import dismap
        importlib.reload(dismap)
        from dismap import parse_xml_file_format_and_save

        arcpy.env.overwriteOutput          = True
        arcpy.env.parallelProcessingFactor = "100%"
        arcpy.SetLogMetadata(True)
        arcpy.SetSeverityLevel(2)
        arcpy.SetMessageLevels(['NORMAL']) # NORMAL, COMMANDSYNTAX, DIAGNOSTICS, PROJECTIONTRANSFORMATION

        base_project_folder = rf"{os.path.dirname(base_project_file)}"
        project_folder      = rf"{base_project_folder}\{project_name}"
        project_gdb         = rf"{project_folder}\{project_name}.gdb"
        metadata_folder     = rf"{project_folder}\InPort Metadata"
        crfs_folder         = rf"{project_folder}\CRFs"
        scratch_folder      = rf"{project_folder}\Scratch"

        arcpy.env.workspace        = project_gdb
        arcpy.env.scratchWorkspace = rf"{scratch_folder}\scratch.gdb"

        datasets = [rf"{project_gdb}\Species_Filter", rf"{project_gdb}\Indicators", rf"{project_gdb}\DisMAP_Regions", rf"{project_gdb}\GMEX_IDW_Sample_Locations", rf"{project_gdb}\GMEX_IDW_Mosaic", rf"{crfs_folder}\GMEX_IDW.crf"]

        for dataset_path in sorted(datasets):
            print(dataset_path)

            dataset_name = os.path.basename(dataset_path)

            print(f"Dataset Name: {dataset_name}")

            target_file_path = rf"{metadata_folder}\{dataset_name}.xml"
            custom_xslt_path = rf"{metadata_folder}\ArcGIS2InPort.xsl"

            dataset_md = md.Metadata(dataset_path)
            dataset_md.saveAsUsingCustomXSLT(target_file_path, custom_xslt_path)
            del dataset_md

            try:
                parse_xml_file_format_and_save(target_file_path)
            except Exception:
                raise Exception

            del target_file_path, custom_xslt_path

            del dataset_name, dataset_path

        del datasets

        # Variables set in function
        del project_gdb, base_project_folder, metadata_folder
        del project_folder, scratch_folder, crfs_folder

        # Imports
        del dismap, parse_xml_file_format_and_save
        del md

        # Function Parameters
        del base_project_file, project_name

    except Exception:
        pass
    except:
        traceback.print_exc()
    else:
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        pass

def create_maps(base_project_file="", project_name="", dataset=""):
    try:
        # Import
        from arcpy import metadata as md

        import dismap
        importlib.reload(dismap)
        from dismap import parse_xml_file_format_and_save

        arcpy.env.overwriteOutput          = True
        arcpy.env.parallelProcessingFactor = "100%"
        arcpy.SetLogMetadata(True)
        arcpy.SetSeverityLevel(2)
        arcpy.SetMessageLevels(['NORMAL']) # NORMAL, COMMANDSYNTAX, DIAGNOSTICS, PROJECTIONTRANSFORMATION

        base_project_folder = rf"{os.path.dirname(base_project_file)}"
        base_project_file   = rf"{base_project_folder}\DisMAP.aprx"
        project_folder      = rf"{base_project_folder}\{project_name}"
        project_gdb         = rf"{project_folder}\{project_name}.gdb"
        metadata_folder     = rf"{project_folder}\Export Metadata"
        crfs_folder         = rf"{project_folder}\CRFs"
        scratch_folder      = rf"{project_folder}\Scratch"

        arcpy.env.workspace        = project_gdb
        arcpy.env.scratchWorkspace = rf"{scratch_folder}\scratch.gdb"

        aprx = arcpy.mp.ArcGISProject(base_project_file)

        dataset_name = os.path.basename(dataset)

        print(f"Dataset Name: {dataset_name}")

        if dataset_name not in [cm.name for cm in aprx.listMaps()]:
            print(f"Creating Map: {dataset_name}")
            aprx.createMap(f"{dataset_name}", "Map")
            aprx.save()
        else:
            pass

        current_map = aprx.listMaps(f"{dataset_name}")[0]
        print(f"Current Map:  {current_map.name}")

        if dataset_name not in [lyr.name for lyr in current_map.listLayers(f"{dataset_name}")]:
            print(f"Adding {dataset_name} to Map")

            map_layer = arcpy.management.MakeFeatureLayer(dataset, f"{dataset_name}")

            #arcpy.management.Delete(rf"{project_folder}\Layers\{dataset_name}.lyrx")
            #os.remove(rf"{project_folder}\Layers\{dataset_name}.lyrx")

            map_layer_file = arcpy.management.SaveToLayerFile(map_layer, rf"{project_folder}\Layers\{dataset_name}.lyrx")
            del map_layer_file

            map_layer_file = arcpy.mp.LayerFile(rf"{project_folder}\Layers\{dataset_name}.lyrx")

            arcpy.management.Delete(map_layer)
            del map_layer

            current_map.addLayer(map_layer_file)
            del map_layer_file

            aprx.save()
        else:
            pass

        #aprx_basemaps = aprx.listBasemaps()
        #basemap = 'GEBCO Basemap/Contours (NOAA NCEI Visualization)'
        basemap = "Terrain with Labels"

        current_map.addBasemap(basemap)
        del basemap

        # Set Reference Scale
        current_map.referenceScale = 50000000

        # Clear Selection
        current_map.clearSelection()

        current_map_cim = current_map.getDefinition('V3')
        current_map_cim.enableWraparound = True
        current_map.setDefinition(current_map_cim)

        # Return the layer's CIM definition
        cim_lyr = lyr.getDefinition('V3')

        # Modify the color, width and dash template for the SolidStroke layer
        symLvl1 = cim_lyr.renderer.symbol.symbol.symbolLayers[0]
        symLvl1.color.values = [0, 0, 0, 100]
        symLvl1.width = 1

        # Push the changes back to the layer object
        lyr.setDefinition(cim_lyr)
        del symLvl1, cim_lyr

        aprx.save()

        height = arcpy.Describe(dataset).extent.YMax - arcpy.Describe(dataset).extent.YMin
        width  = arcpy.Describe(dataset).extent.XMax - arcpy.Describe(dataset).extent.XMin

        # map_width, map_height
        map_width, map_height = 8.5, 11

        if height > width:
            page_height = map_height; page_width = map_width
        elif height < width:
            page_height = map_width; page_width = map_height
        else:
            page_width = map_width; page_height = map_height

        del map_width, map_height
        del height, width

        if dataset_name not in [cl.name for cl in aprx.listLayouts()]:
            print(f"Creating Layout: {dataset_name}")
            aprx.createLayout(page_width, page_height, "INCH", f"{dataset_name}")
            aprx.save()
        else:
            print(f"Layout: {dataset_name} exists")

        #Set the default map camera to the extent of the park boundary before opening the new view
        #default camera only affects newly opened views
        lyr = current_map.listLayers(f"{dataset_name}")[-1]

        #
        arcpy.management.SelectLayerByAttribute(lyr, 'NEW_SELECTION', "DatasetCode in ('ENBS', 'HI', 'NEUS_SPR')")

        mv = current_map.openView()
        mv.panToExtent(mv.getLayerExtent(lyr, True, True))
        mv.zoomToAllLayers()
        del mv

        arcpy.management.SelectLayerByAttribute(lyr, 'CLEAR_SELECTION')

        av = aprx.activeView
        av.exportToPNG(rf"{project_folder}\Layers\{dataset_name}.png", width=288, height=192, resolution = 96, color_mode="24-BIT_TRUE_COLOR", embed_color_profile=True)
        av.exportToJPEG(rf"{project_folder}\Layers\{dataset_name}.jpg", width=288, height=192, resolution = 96, jpeg_color_mode="24-BIT_TRUE_COLOR", embed_color_profile=True)
        del av

        #print(current_map.referenceScale)

        #export the newly opened active view to PDF, then delete the new map
        #mv = aprx.activeView
        #mv.exportToPDF(r"C:\Temp\RangerStations.pdf", width=700, height=500, resolution=96)
        #aprx.deleteItem(current_map)

        #mv = aprx.activeView
        #mv = current_map.defaultView
        #mv.zoomToAllLayers()
        #print(mv.camera.getExtent())
        #arcpy.management.Delete(rf"{project_folder}\Layers\{dataset_name}.png")
        #arcpy.management.Delete(rf"{project_folder}\Layers\{dataset_name}.jpg")

        #os.remove(rf"{project_folder}\Layers\{dataset_name}.png")
        #os.remove(rf"{project_folder}\Layers\{dataset_name}.jpg")


        #mv.exportToPNG(rf"{project_folder}\Layers\{dataset_name}.png", width=288, height=192, resolution = 96, color_mode="24-BIT_TRUE_COLOR", embed_color_profile=True)
        #mv.exportToJPEG(rf"{project_folder}\Layers\{dataset_name}.jpg", width=288, height=192, resolution = 96, jpeg_color_mode="24-BIT_TRUE_COLOR", embed_color_profile=True)
        #del mv

        #Export the resulting imported layout and changes to JPEG
        #print(f"Exporting '{current_layout.name}'")
        #current_map.exportToJPEG(rf"{project_folder}\Layouts\{current_layout.name}.jpg", page_width, page_height)
        #current_map.exportToPNG(rf"{project_folder}\Layouts\{current_layout.name}.png", page_width, page_height)

        #fc_md = md.Metadata(dataset)
        #fc_md.thumbnailUri = rf"{project_folder}\Layouts\{dataset_name}.png"
        #fc_md.thumbnailUri = rf"{project_folder}\Layouts\{dataset_name}.jpg"
        #fc_md.save()
        #del fc_md

        aprx.save()


    # #            from arcpy import metadata as md
    # #
    # #            fc_md = md.Metadata(dataset)
    # #            fc_md.thumbnailUri = rf"{project_folder}\Layers\{dataset_name}.png"
    # #            fc_md.save()
    # #            del fc_md
    # #            del md

##        aprx.save()
##
##        current_layout = [cl for cl in aprx.listLayouts() if cl.name == dataset_name][0]
##        print(f"Current Layout: {current_layout.name}")
##
##        current_layout.openView()
##
##        # Remove all map frames
##        for mf in current_layout.listElements("MapFrame_Element"): current_layout.deleteElement(mf); del mf
##
##        # print(f'Layout Name: {current_layout.name}')
##        # print(f'    Width x height: {current_layout.pageWidth} x {current_layout.pageHeight} units are {current_layout.pageUnits}')
##        # print(f'    MapFrame count: {str(len(current_layout.listElements("MapFrame_Element")))}')
##        # for mf in current_layout.listElements("MapFrame_Element"):
##        #     if len(current_layout.listElements("MapFrame_Element")) > 0:
##        #         print(f'        MapFrame name: {mf.name}')
##        # print(f'    Total element count: {str(len(current_layout.listElements()))} \n')
##
##
##        print(f"Create a new map frame using a point geometry")
##        #Create a new map frame using a point geometry
##        #mf1 = current_layout.createMapFrame(arcpy.Point(0.01,0.01), current_map, 'New MF - Point')
##        mf1 = current_layout.createMapFrame(arcpy.Point(0.0,0.0), current_map, 'New MF - Point')
##        #mf1.elementWidth = 10
##        #mf1.elementHeight = 7.5
##        #mf1.elementWidth  = page_width  - 0.01
##        #mf1.elementHeight = page_height - 0.01
##        mf1.elementWidth  = page_width
##        mf1.elementHeight = page_height

##        lyr = current_map.listLayers(f"{dataset_name}")[0]
##
##        #Zoom to ALL selected features and export to PDF
##        #arcpy.SelectLayerByAttribute_management(lyr, 'NEW_SELECTION')
##        #mf1.zoomToAllLayers(True)
##        #arcpy.SelectLayerByAttribute_management(lyr, 'CLEAR_SELECTION')
##
##        #Set the map frame extent to the extent of a layer
##        #mf1.camera.setExtent(mf1.getLayerExtent(lyr, False, True))
##        #mf1.camera.scale = mf1.camera.scale * 1.1 #add a slight buffer
##
##        del lyr

##        print(f"Create a new bookmark set to the map frame's default extent")
##        #Create a new bookmark set to the map frame's default extent
##        bkmk = mf1.createBookmark('Default Extent', "The map's default extent")
##        bkmk.updateThumbnail()
##        del mf1
##        del bkmk

        # Create point text element using a system style item
        # txtStyleItem = aprx.listStyleItems('ArcGIS 2D', 'TEXT', 'Title (Serif)')[0]
        # ptTxt = aprx.createTextElement(current_layout, arcpy.Point(5.5, 4.25), 'POINT', f'{dataset_name}', 10, style_item=txtStyleItem)
        # del txtStyleItem

        # Change the anchor position and reposition the text to center
        # ptTxt.setAnchor('Center_Point')
        # ptTxt.elementPositionX = page_width / 2.0
        # ptTxt.elementPositionY = page_height - 0.25
        # del ptTxt

        # print(f"Using CIM to update border")
        # current_layout_cim = current_layout.getDefinition('V3')
        # for elm in current_layout_cim.elements:
        #     if type(elm).__name__ == 'CIMMapFrame':
        #         if elm.graphicFrame.borderSymbol.symbol.symbolLayers:
        #             sym = elm.graphicFrame.borderSymbol.symbol.symbolLayers[0]
        #             sym.width = 5
        #             sym.color.values = [255, 0, 0, 100]
        #         else:
        #             arcpy.AddWarning(elm.name + ' has NO symbol layers')
        # current_layout.setDefinition(current_layout_cim)
        # del current_layout_cim, elm, sym

##        ExportLayout = True
##        if ExportLayout:
##            #Export the resulting imported layout and changes to JPEG
##            print(f"Exporting '{current_layout.name}'")
##            current_layout.exportToJPEG(rf"{project_folder}\Layouts\{current_layout.name}.jpg")
##            current_layout.exportToPNG(rf"{project_folder}\Layouts\{current_layout.name}.png")
##        del ExportLayout

##        #Export the resulting imported layout and changes to JPEG
##        print(f"Exporting '{current_layout.name}'")
##        current_map.exportToJPEG(rf"{project_folder}\Layouts\{current_layout.name}.jpg", page_width, page_height)
##        current_map.exportToPNG(rf"{project_folder}\Layouts\{current_layout.name}.png", page_width, page_height)
##
##        fc_md = md.Metadata(dataset)
##        fc_md.thumbnailUri = rf"{project_folder}\Layouts\{current_layout.name}.png"
##        #fc_md.thumbnailUri = rf"{project_folder}\Layouts\{current_layout.name}.jpg"
##        fc_md.save()
##        del fc_md
##
##        aprx.save()

        # aprx.deleteItem(current_map)
        #aprx.deleteItem(current_layout)

        del current_map
        #, current_layout
        #del page_width, page_height
        del dataset_name, dataset

        aprx.save()

        print(f"\nCurrent Maps & Layouts")

        current_maps    = aprx.listMaps()
        #current_layouts = aprx.listLayouts()

        if current_maps:
            print(f"\nCurrent Maps\n")
            for current_map in current_maps:
                print(f"\tProject Map: {current_map.name}")
                del current_map
        else:
            arcpy.AddWarning("No maps in project_name")

##        if current_layouts:
##            print(f"\nCurrent Layouts\n")
##            for current_layout in current_layouts:
##                print(f"\tProject Layout: {current_layout.name}")
##                del current_layout
##        else:
##            arcpy.AddWarning("No layouts in Project")

        #del current_layouts
        del current_maps

        # Variables set in function for aprx

        # Save aprx one more time and then delete
        aprx.save()
        del aprx

        # Variables set in function
        del project_gdb, base_project_folder, metadata_folder, crfs_folder
        del project_folder, scratch_folder

        # Imports
        del dismap, parse_xml_file_format_and_save
        del md

        # Function Parameters
        del base_project_file, project_name

    except Exception:
        pass
    except:
        traceback.print_exc()
    else:
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        pass

def update_xml_elements(project_gdb="", contacts="", collective_title=""):
    try:
        # Imports
        from lxml import etree
        from io import StringIO
        import copy
        import arcpy
        from arcpy import metadata as md
        # Project modules
        #from src.project_tools import pretty_format_xml_file

        arcpy.env.overwriteOutput          = True
        arcpy.env.parallelProcessingFactor = "100%"
        arcpy.SetLogMetadata(True)
        arcpy.SetSeverityLevel(2)
        arcpy.SetMessageLevels(['NORMAL']) # NORMAL, COMMANDSYNTAX, DIAGNOSTICS, PROJECTIONTRANSFORMATION

        project_folder = os.path.dirname(project_gdb)
        crfs_folder    = rf"{project_folder}\CRFs"
        scratch_folder = rf"{project_folder}\Scratch"
        # Moved dictionaries to JSON

        workspaces = [project_gdb, crfs_folder]

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
            #for dataset_path in sorted([d for d in datasets if d.endswith("SeaTurtleKempsRidley_20210129")]):
            #for dataset_path in sorted([d for d in datasets if d.endswith("CoralElkhorn_20210712")]):
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

                print(f"Dataset Name: {dataset_name}")

                # presForm sub-section
                presForm  = idCitation.xpath(f"./presForm")[0]
                PresFormCd = presForm.xpath(f"./PresFormCd")
                if len(PresFormCd) == 0:
                    #print(f"Inserting fgdcGeoform at {position}")
                    _xml = '<presForm><PresFormCd Sync="TRUE" value="005"/></presForm>'
                    _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
                    presForm.insert(idCitation_dict['PresFormCd'], _root)
                    del _root, _xml
                elif len(PresFormCd) == 1:
                    #print(f"Updating fgdcGeoform if needed {position}")
                    PresFormCd[0].set('Sync', "TRUE")
                    PresFormCd[0].set('value', "005")

                presForm  = idCitation.xpath(f"./presForm")[0]
                fgdcGeoform = presForm.xpath(f"./fgdcGeoform")
                if len(fgdcGeoform) == 0:
                    _xml = '<fgdcGeoform>vector digital data</fgdcGeoform>'
                    _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
                    presForm.insert(idCitation_dict['fgdcGeoform'], _root)
                    del _root, _xml
                elif len(fgdcGeoform) == 1:
                    #print(f"Updating fgdcGeoform if needed {position}")
                    fgdcGeoform[0].text = 'vector digital data'

##                # ######################################################################
##                # Citation Responsiable Party
##                # ######################################################################
##
##                citRespParty  = idCitation.xpath(f"./citRespParty")
##                xml = '''<citRespParty>
##                            <editorSource>extermal</editorSource>
##                            <editorDigest>9cc0fe80de5687cc4d79f50f3a254f2c3ceb08ce</editorDigest>
##                            <rpIndName>Nikki Wildart</rpIndName>
##                            <rpOrgName>Office of Protected Resources, National Marine Fisheries Service</rpOrgName>
##                            <rpPosName>Biologist</rpPosName>
##                            <rpCntInfo>
##                                <cntAddress addressType="both">
##                                    <delPoint>1315 East West Highway</delPoint>
##                                    <city>Silver Spring</city>
##                                    <adminArea>MD</adminArea>
##                                    <postCode>20910-3282</postCode>
##                                    <eMailAdd>nikki.wildart@noaa.gov</eMailAdd>
##                                    <country>US</country>
##                                </cntAddress>
##                                <cntPhone>
##                                    <voiceNum tddtty="">(301) 427-8443</voiceNum>
##                                    <faxNum>(301) 427-8443</faxNum>
##                                </cntPhone>
##                                <cntHours>0700 - 1800 EST/EDT</cntHours>
##                                <cntOnlineRes>
##                                    <linkage>https://www.fisheries.noaa.gov/about/office-protected-resources</linkage>
##                                    <protocol>REST Service</protocol>
##                                    <orName>Fisheries OPR</orName>
##                                    <orDesc>NOAA Fisheries Office of Science and Technology</orDesc>
##                                    <orFunct>
##                                        <OnFunctCd value="002"></OnFunctCd>
##                                    </orFunct>
##                                </cntOnlineRes>
##                            </rpCntInfo>
##                            <editorSave>True</editorSave>
##                            <displayName>Nikki Wildart</displayName>
##                            <role>
##                                <RoleCd value="002"></RoleCd>
##                            </role>
##                        </citRespParty>'''
##
##                # Create an XML string
##                citRespParty_root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
##                citRespParty_email = citRespParty_root.xpath(f"./rpCntInfo/cntAddress/eMailAdd")[0].text
##
##                if len(citRespParty) == 0:
##                    position = idCitation_dict['citRespParty']
##                    #print("Inserting citRespParty at position: {position}")
##                    idCitation.insert(position, citRespParty_root)
##                    del position
##                elif len(citRespParty) == 1:
##                    position = idCitation_dict['citRespParty']
##                    #print(f"Updating citRespParty if needed at position: {position}")
##                    idCitation.insert(position, citRespParty[0])
##                    del position
##                    # Get email address from citRespParty[0]
##                    cit_resp_party_email = citRespParty[0].xpath(f"./rpCntInfo/cntAddress/eMailAdd")[0].text
##                    if cit_resp_party_email:
##                        #print(f"\tFound {cit_resp_party_email}")
##                        position = idCitation.index(citRespParty[0])
##                        if cit_resp_party_email != citRespParty_email:
##                            #print("\t\tInserting an additional citRespParty")
##                            idCitation.insert(position+1, citRespParty_root)
##                        else:
##                            pass
##                            #print("\t\tcitRespParty update complete")
##                        del position
##                    else:
##                        pass
##                    del cit_resp_party_email
##                elif len(citRespParty) > 1:
##                    #print(f"{len(citRespParty)} citRespParty")
##                    #print("does it have the same email and the new contact?")
##                    cit_resp_party_emails = list()
##                    for cit_resp_party in citRespParty:
##                        if len(idCitation.xpath(f"./citRespParty/rpCntInfo/cntAddress/eMailAdd")) > 0:
##                            cit_resp_party_email = idCitation.xpath(f"./citRespParty/rpCntInfo/cntAddress/eMailAdd")[0]
##                            #print(f"\tFound: {cit_resp_party_email.text}")
##                            if cit_resp_party_email not in cit_resp_party_emails:
##                                #print(f"\t{cit_resp_party_email.text} not in email list")
##                                cit_resp_party_emails.append(cit_resp_party_email)
##                            elif cit_resp_party_email in cit_resp_party_emails:
##                                # Remove the element
##                                if cit_resp_party is not None:
##                                    #print(f"\tRemoving {cit_resp_party_email.text}")
##                                    idCitation.remove(cit_resp_party)
##                                else:
##                                    pass
##                            else:
##                                pass
##                            del cit_resp_party_email
##                            #position = idCitation.index(cit_resp_party)
##                        else:
##                            pass
##                        del cit_resp_party
##                    del cit_resp_party_emails
##                else:
##                    pass
##                del citRespParty_root, citRespParty_email
##                del idCitation_dict
##
##                #print(etree.tostring(idCitationt, encoding='UTF-8',  method='xml', pretty_print=True).decode())
##                del xml, citRespParty
##                del idCitation

                # ######################################################################
                # envirDesc,
                # ######################################################################

                dataIdInfo = root.xpath(f"./dataIdInfo")[0]
                envirDesc = dataIdInfo.xpath(f"./envirDesc")
                if len(envirDesc) == 0:
                    _xml = '<envirDesc Sync="TRUE">Esri ArcGIS 13.1.0.41833</envirDesc>'
                    _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
                    dataIdInfo.insert(dataIdInfo_dict['envirDesc'], _root)
                    del _root, _xml
                elif len(envirDesc) == 1:
                    envirDesc[0].set("Sync", "TRUE")
                    dataIdInfo.insert(dataIdInfo_dict['envirDesc'], envirDesc[0])

                # ######################################################################
                # Topics
                # ######################################################################

                dataIdInfo = root.xpath(f"./dataIdInfo")[0]
                tpCat      = dataIdInfo.xpath(f"./tpCat")
                if len(tpCat) == 0:
                    position = dataIdInfo_dict['tpCat']
                    #print(f"Inserting tpCat at {position}")
                    for key in tpCat_dict:
                        _xml = tpCat_dict[key]
                        _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
                        dataIdInfo.insert(position, _root)
                        position+=1
                        del _root, _xml, key
                    del position

                elif len(tpCat) >= 1:
                    for i, key in enumerate(tpCat):
                        position = dataIdInfo_dict['tpCat']
                        if int(dataIdInfo.index(key)) not in range(position, position + len(tpCat_dict)):
                            #print(f"delete: {key.tag}")
                            dataIdInfo.remove(key)
                        del position
                        del i, key
                else:
                    pass

                mdFileID = root.xpath(f"./mdFileID")
                if len(mdFileID) == 0:
                    #print(f"Inserting 'mdFileID' at position: {root_dict['mdFileID']}")
                    _xml = '<mdFileID>gov.noaa.nmfs.inport:</mdFileID>'

                mdMaint = root.xpath(f"./mdMaint")
                if len(mdMaint) == 0:
                    _xml = '<mdMaint><maintFreq><MaintFreqCd value="009"></MaintFreqCd></maintFreq></mdMaint>'
                    MaintFreqCd.set('value', "009")



                    #ToDo3 stepDesc_text and stepDateTm_text

##                    if stepDesc_text and stepDateTm_text:
##                        _stepDesc_text = prcStep[0].xpath("./stepDesc/text()")
##                        _stepDateTm_text = prcStep[0].xpath("./stepDateTm/text()")
##                        #stepDesc_text[0].text =
##                        __stepDesc = prcStep[0].xpath("./stepDesc")
##                        __stepDesc[0].text = f"{_stepDesc_text}. Completed on {_stepDateTm_text}"
##
##                        stepProc = prcStep[0].xpath(".//stepProc")

                    #print(etree.tostring(dataLineage[0], encoding='UTF-8',  method='xml', pretty_print=True).decode())
                    #statement  = "" # _xml = "<statement></statement>"
                    #dataSource = "" # _xml = "<dataSource type=""><srcDesc></srcDesc><srcCitatn><resTitle></resTitle><date><pubDate></pubDate><createDate></createDate><reviseDate></reviseDate></date></srcCitatn></dataSource>"

                # #######################################################################
                #               ###--->>> distInfo section Start <<<---###
                # #######################################################################
# ######################################################################################
# Below is block so I can focus on step processes

                #ToDo1 distInfo

                _xml = '''<distInfo>
                            <distributor>
                                <distFormat>
                                    <formatName Sync="TRUE">File Geodatabase Feature Class</formatName>
                                    <formatVer>NMFS ESA Range Geodatabase 2024</formatVer>
                                    <fileDecmTech>ZIP</fileDecmTech>
                                    <formatInfo>NMFS ESA Range Geodatabase 2024</formatInfo>
                                </distFormat>
                                 <distorTran xmlns="">
                                    <unitsODist>MB</unitsODist>
                                    <transSize>8</transSize>
                                    <onLineSrc xmlns="">
                                       <linkage>https://www.fisheries.noaa.gov/science-and-data</linkage>
                                       <protocol>REST Service</protocol>
                                       <orName>NMFS ESA Range Geodatabase 2024</orName>
                                       <orDesc>File Geodatabase Download</orDesc>
                                       <orFunct>
                                          <OnFunctCd value="001"/>
                                       </orFunct>
                                    </onLineSrc>
                                 </distorTran>
                                <distorCont>
                                    <editorSource>extermal</editorSource>
                                    <editorDigest></editorDigest>
                                    <rpIndName></rpIndName>
                                    <rpOrgName></rpOrgName>
                                    <rpPosName></rpPosName>
                                    <rpCntInfo>
                                        <cntAddress addressType="both">
                                            <delPoint></delPoint>
                                            <city></city>
                                            <adminArea></adminArea>
                                            <postCode></postCode>
                                            <eMailAdd></eMailAdd>
                                            <country></country>
                                        </cntAddress>
                                        <cntPhone>
                                            <voiceNum tddtty=""></voiceNum>
                                            <faxNum></faxNum>
                                        </cntPhone>
                                        <cntHours></cntHours>
                                        <cntOnlineRes>
                                            <linkage></linkage>
                                            <protocol>REST Service</protocol>
                                            <orName></orName>
                                            <orDesc></orDesc>
                                            <orFunct>
                                                <OnFunctCd value="002"></OnFunctCd>
                                            </orFunct>
                                        </cntOnlineRes>
                                    </rpCntInfo>
                                    <editorSave>True</editorSave>
                                    <displayName></displayName>
                                    <role>
                                        <RoleCd value="005"></RoleCd>
                                    </role>
                                </distorCont>
                            </distributor>
                            <distributor>
                                <distFormat>
                                    <formatName Sync="TRUE">File Geodatabase Feature Class</formatName>
                                    <formatVer>NMFS ESA Range Geodatabase 2024</formatVer>
                                    <fileDecmTech>ZIP</fileDecmTech>
                                    <formatInfo>NMFS ESA Range Geodatabase 2024</formatInfo>
                                </distFormat>
                                 <distorTran xmlns="">
                                    <onLineSrc xmlns="">
                                       <linkage>https://services2.arcgis.com/C8EMgrsFcRFL6LrL/arcgis/rest/services/.../FeatureServer</linkage>
                                       <protocol>ArcGIS REST Services</protocol>
                                       <orName>Dataset </orName>
                                       <orDesc>Dataset Feature Service</orDesc>
                                       <orFunct>
                                          <OnFunctCd value="002"/>
                                       </orFunct>
                                    </onLineSrc>
                                 </distorTran>
                                <distorCont>
                                    <editorSource>extermal</editorSource>
                                    <editorDigest></editorDigest>
                                    <rpIndName></rpIndName>
                                    <rpOrgName></rpOrgName>
                                    <rpPosName></rpPosName>
                                    <rpCntInfo>
                                        <cntAddress addressType="both">
                                            <delPoint></delPoint>
                                            <city></city>
                                            <adminArea></adminArea>
                                            <postCode></postCode>
                                            <eMailAdd></eMailAdd>
                                            <country></country>
                                        </cntAddress>
                                        <cntPhone>
                                            <voiceNum tddtty=""></voiceNum>
                                            <faxNum></faxNum>
                                        </cntPhone>
                                        <cntHours></cntHours>
                                        <cntOnlineRes>
                                            <linkage></linkage>
                                            <protocol>REST Service</protocol>
                                            <orName></orName>
                                            <orDesc></orDesc>
                                            <orFunct>
                                                <OnFunctCd value="002"></OnFunctCd>
                                            </orFunct>
                                        </cntOnlineRes>
                                    </rpCntInfo>
                                    <editorSave>True</editorSave>
                                    <displayName></displayName>
                                    <role>
                                        <RoleCd value="005"></RoleCd>
                                    </role>
                                </distorCont>
                            </distributor>
                        </distInfo>'''


                #ToDo1 mdContact

##                mdContact = root.xpath(f"./mdContact")
##                from dev_get_new_contact_xml import get_new_contact
##                _contacts     = contacts["mdContact"][0]
##                mdContact_email_address = _contacts["eMailAdd"]
##                mdContact_user_name     = _contacts["rpIndName"]
##                del _contacts
##
##                contact_type = "mdContact"
##                _contact = [_contact for _contact in contacts[contact_type] if mdContact_user_name == _contact["rpIndName"] and mdContact_email_address == _contact["eMailAdd"]]
##                new_contact_xml_string = get_new_contact(contact=_contact[0], contact_type=contact_type)
##                parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
##                new_contact_xml_root = etree.fromstring(new_contact_xml_string, parser=parser) # To parse from a string, use the fromstring() function instead.
##                del parser
##                del new_contact_xml_string
##                del _contact, contact_type
##                del get_new_contact
##
##                if len(mdContact) == 0:
##                    root.insert(root_dict['mdContact'], new_contact_xml_root)
##                elif len(mdContact) >= 1:
##                    for _mdContact in mdContact:
##
##                        rpIndName = _mdContact.xpath("./rpIndName")
##                        if len(rpIndName) == 0: pass
##                        elif len(rpIndName) == 1: old_user_name = rpIndName[0].text
##                        elif len(rpIndName) > 1:
##                            for i in range(1, len(rpIndName)): mdContact[0].remove(rpIndName[i]); i+=1; del i
##                            old_user_name = rpIndName[0].text
##                        else: pass
##                        del rpIndName
##
##                        eMailAdd = _mdContact.xpath("./rpCntInfo/cntAddress/eMailAdd")
##                        if len(eMailAdd) == 0: pass
##                        elif len(eMailAdd) == 1: old_email_address = eMailAdd[0].text
##                        elif len(eMailAdd) > 1:
##                            for i in range(1, len(eMailAdd)): mdContact[0].remove(eMailAdd[i]); i+=1; del i
##                            old_email_address = eMailAdd[0].text
##                        else: pass
##                        del eMailAdd
##
##                        if old_user_name == mdContact_user_name and old_email_address == mdContact_email_address:
##                            root.replace(mdContact[0], new_contact_xml_root)
##
##                        elif old_user_name != mdContact_user_name and old_email_address != mdContact_email_address:
##                            print(f"\t\tCurrent Contact Name: {old_user_name}")
##                            print(f"\t\tCurrent Email:        {old_email_address}")
##                            print(f"\t\t\tReplacing Contact:  {old_user_name}")
##
##                            if len(root.xpath(f".//stepProc//eMailAdd[text()='{old_email_address}']/ancestor::*//stepProc/rpIndName[text()='{old_user_name}']/..")) >= 1:
##                                root.remove(_mdContact)

##                #del mdContact_email, mdContact_root, mdContact
##           #
##           #        elif len(citRespParty) == 1:
##           #            print(f"Updating citRespParty if needed at position: {idCitation.index(citRespParty[0])}")
##           #            position = 5
##           #            idCitation.insert(position, citRespParty[0])
##           #            # Get email address from citRespParty[0]
##           #            cit_resp_party_email = citRespParty[0].xpath(f"./rpCntInfo/cntAddress/eMailAdd")[0].text
##           #            if cit_resp_party_email:
##           #                print(f"\tFound {cit_resp_party_email}")
##           #                position = idCitation.index(citRespParty[0])
##           #                if cit_resp_party_email != new_cit_resp_party_email:
##           #                    print("\t\tInserting an additional citRespParty")
##           #                    idCitation.insert(position+1, new_cit_resp_party_root)
##           #                else:
##           #                    print("\t\tcitRespParty update complete")
##           #            else:
##           #                pass
##           #            del cit_resp_party_email
##           #            del position
##           #        elif len(citRespParty) > 1:
##           #            print(f"{len(citRespParty)} citRespParty")
##           #            print("does it have the same email and the new contact?")
##           #            cit_resp_party_emails = list()
##           #            for cit_resp_party in citRespParty:
##           #                if len(idCitation.xpath(f"./citRespParty/rpCntInfo/cntAddress/eMailAdd")) > 0:
##           #                    cit_resp_party_email = idCitation.xpath(f"./citRespParty/rpCntInfo/cntAddress/eMailAdd")[0]
##           #                    print(f"\tFound: {cit_resp_party_email.text}")
##           #                    if cit_resp_party_email not in cit_resp_party_emails:
##           #                        print(f"\t{cit_resp_party_email.text} not in email list")
##           #                        cit_resp_party_emails.append(cit_resp_party_email)
##           #                    elif cit_resp_party_email in cit_resp_party_emails:
##           #                        # Remove the element
##           #                        if cit_resp_party is not None:
##           #                            print(f"\tRemoving {cit_resp_party_email.text}")
##           #                            idCitation.remove(cit_resp_party)
##           #                        else:
##           #                            pass
##           #                    else:
##           #                        pass
##           #                    del cit_resp_party_email
##           #                    #position = idCitation.index(cit_resp_party)
##           #                else:
##           #                    pass
##           #                del cit_resp_party
##           #            del cit_resp_party_emails
##           #        else:
##           #            pass
##           #        del new_cit_resp_party_email, new_cit_resp_party_root
##           #        #print(etree.tostring(idCitationt, encoding='UTF-8',  method='xml', pretty_print=True).decode())
##           #        del xml, citRespParty

        #ToDo3 Binary

##                # ######################################################################
##                #               ###--->>> Binary section Start <<<---###
##                # ######################################################################
##                Binary      = root.xpath(f"./Binary")
##                if len(Binary) == 0:
##                    #print(f"Inserting 'Binary' at position: {root_dict['Binary']}")
##                    _xml = '<Binary Sync="TRUE"><Thumbnail><Data EsriPropertyType="PictureX"></Data></Thumbnail></Binary>'
##                    _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
##                    position = root_dict['Binary']
##                    root.insert(position, _root)
##                    del position, _root, _xml

        # Declared Variables
        del root_dict, contact_dict, dqInfo_dict
        del dataIdInfo_dict, tpCat_dict, esri_dict
        del idCitation_dict, RoleCd_dict
        del contacts_xml_root, contacts_xml_tree
        del project_folder, crfs_folder, scratch_folder, workspaces
        #del tree, root, dataset_name
        # Imports
        del etree, StringIO, copy, arcpy, md
        # Function Parameters
        del project_gdb, contacts, collective_title

    except:
        traceback.print_exc()
    else:
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
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
        crfs_folder    = rf"{project_folder}\CRFs"
        scratch_folder = rf"{project_folder}\Scratch"

        import json
        json_path = rf"{project_folder}\root_dict.json"
        with open(json_path, "r") as json_file:
            root_dict = json.load(json_file)
        del json_file
        del json_path
        del json

        import json
        json_path = rf"{project_folder}\contacts.json"
        with open(json_path, "r") as json_file:
            contacts = json.load(json_file)
        del json_file
        del json_path
        del json

        import json
        json_path = rf"{project_folder}\RoleCd_dict.json"
        # Write to File
        with open(json_path, "r") as json_file:
            RoleCd_dict = json.load(json_file)
        del json_file
        del json_path
        del json

        contact_type_dict = {"citRespParty":"002","idPoC":"007","distorCont":"005","mdContact":"011","stepProc":"009",}

        workspaces = [project_gdb, crfs_folder]

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

            #for dataset_path in sorted([d for d in datasets if d.endswith("SeaTurtleLeatherback_20210129")]):
            #for dataset_path in sorted([d for d in datasets if d.endswith("WhaleSperm_20211220")]):
            for dataset_path in sorted(datasets):
                dataset_name = os.path.basename(dataset_path)
                print(f"Dataset Name: {dataset_name}")
                #print(f"\tDataset Location: {os.path.basename(os.path.dirname(dataset_path))}")

                dataset_md = md.Metadata(dataset_path)
                dataset_md_xml = dataset_md.xml
                del dataset_md

                # Parse the XML
                parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
                tree = etree.parse(StringIO(dataset_md_xml), parser=parser)
                #root = tree.getroot()
                del parser, dataset_md_xml

                # print(etree.tostring(tree, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
                # etree.indent(tree, space='   ')
                # tree.write(xml_file, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True)

                contact_parents = tree.xpath(f".//rpIndName/text()/../..")

                if len(contact_parents) > 0:
                    print("\tSearch for Name and Email")
                    contact_count = len(contact_parents)
                    count = 0
                    for contact_parent in contact_parents:
                        count+=1
                        print(f"\t\tContact Parent: {contact_parent.tag:<12} {count} of {contact_count}")
                        #print(etree.tostring(contact_parent, encoding='UTF-8',  method='xml', pretty_print=True).decode())
                        contact_type = contact_parent.tag
                        #print(contact_type)
                        #print(contact_parent.getparent().tag)
                        rpIndName = contact_parent.xpath("./rpIndName/text()/..")
                        old_user_name = rpIndName[0].text
                        eMailAdd = contact_parent.xpath(".//eMailAdd/text()/..")
                        old_email_address = eMailAdd[0].text if len(eMailAdd) == 1 else ""

                        if old_user_name and old_email_address:
                            print(f"\t\t\tSearch for '{old_user_name}' and '{old_email_address}'")
                            new_contact_tree = contacts_xml_tree.xpath(f"//eMailAdd[text()='{old_email_address}']/ancestor::contact//rpIndName[text()='{old_user_name}']/ancestor::contact//editorSave[text()='True']/..")
                            for new_contact in new_contact_tree:
                                #print(etree.tostring(new_contact, encoding='UTF-8',  method='xml', pretty_print=True).decode())
                                role_code    = contact_type_dict[contact_type]
                                _new_contact = copy.deepcopy(new_contact_tree[0])
                                _new_contact.tag = f"{contact_type}"
                                _xml = etree.XML(f'<role><RoleCd value="{role_code}"/></role>')
                                # Append element
                                _new_contact.append(_xml)
                                del _xml, role_code
                                #_rpIndName = _new_contact.xpath("./rpIndName/text()/..")
                                #_user_name = _rpIndName[0].text
                                #_eMailAdd = _new_contact.xpath(".//eMailAdd/text()/..")
                                #_email_address = _eMailAdd[0].text
                                #del _eMailAdd, _rpIndName
                                #print(etree.tostring(contact_parent, encoding='UTF-8',  method='xml', pretty_print=True).decode())
                                #print(etree.tostring(_new_contact, encoding='UTF-8',  method='xml', pretty_print=True).decode())
                                contact_parent.getparent().replace(contact_parent, _new_contact)
                                #_contact_parent = tree.xpath(f"//eMailAdd[text()='{_email_address}']/ancestor::{contact_type}//rpIndName[text()='{_user_name}']/ancestor::{contact_type}//editorSave[text()='True']/..")
                                #print(etree.tostring(_contact_parent[0], encoding='UTF-8',  method='xml', pretty_print=True).decode())
                                #del _contact_parent
                                #del _email_address, _user_name
                                del _new_contact, new_contact
                            del new_contact_tree

                        elif old_user_name and not old_email_address:
                            print(f"\t\t\tSearch for '{old_user_name}'")
                            new_contact_tree = contacts_xml_tree.xpath(f"//rpIndName[text()='{old_user_name}']/ancestor::contact//editorSave[text()='True']/..")
                            for new_contact in new_contact_tree:
                                #print(etree.tostring(new_contact, encoding='UTF-8',  method='xml', pretty_print=True).decode())
                                role_code    = contact_type_dict[contact_type]
                                _new_contact = copy.deepcopy(new_contact_tree[0])
                                _new_contact.tag = f"{contact_type}"
                                _new_contact.set("xmlns", "")
                                _xml = etree.XML(f'<role><RoleCd value="{role_code}"/></role>')
                                # Append element
                                _new_contact.append(_xml)
                                del _xml, role_code
                                _rpIndName = _new_contact.xpath("./rpIndName/text()/..")
                                _user_name = _rpIndName[0].text
                                _eMailAdd = _new_contact.xpath(".//eMailAdd/text()/..")
                                _email_address = _eMailAdd[0].text
                                del _eMailAdd, _rpIndName
                                #print(etree.tostring(contact_parent, encoding='UTF-8',  method='xml', pretty_print=True).decode())
                                #print(etree.tostring(_new_contact, encoding='UTF-8',  method='xml', pretty_print=True).decode())
                                contact_parent.getparent().replace(contact_parent, _new_contact)
                                #_contact_parent = tree.xpath(f"//eMailAdd[text()='{_email_address}']/ancestor::{contact_type}//rpIndName[text()='{_user_name}']/ancestor::{contact_type}//editorSave[text()='True']/..")
                                #print(etree.tostring(_contact_parent[0], encoding='UTF-8',  method='xml', pretty_print=True).decode())
                                #del _contact_parent
                                del _email_address, _user_name
                                del _new_contact, new_contact
                            del new_contact_tree

                        del old_email_address, eMailAdd, old_user_name, rpIndName
                        del contact_type, contact_parent

                    # Declared variables
                    del contact_count, count
                    # Imports

                else:
                    pass
                    #raise Exception

                del dataset_name
                del contact_parents

                etree.indent(tree, space='    ')
                dataset_md_xml = etree.tostring(tree, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True)
                # This allows for sorting
                #doc = etree.XML(dataset_md_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
                #for parent in doc.xpath('.'): # Search for parent elements
                #  parent[:] = sorted(parent,key=lambda x: root_dict[x.tag])
                #  del parent
                #print(etree.tostring(doc, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
                #del doc
                del tree

                SaveBackXml = True
                if SaveBackXml:
                    dataset_md = md.Metadata(dataset_path)
                    dataset_md.xml = dataset_md_xml
                    dataset_md.save()
                    dataset_md.synchronize("ALWAYS")
                    dataset_md.save()
                    #dataset_md.reload()
                    del dataset_md
                else:
                    pass
                del SaveBackXml
                del dataset_md_xml
                del dataset_path

            del datasets
            del workspace

        # Variables set in function
        del contacts_xml_root, contacts_xml_tree
        del contacts
        del RoleCd_dict, root_dict, contact_type_dict
        del project_folder, crfs_folder, scratch_folder
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

def update_process_steps_contacts(project_gdb=""):
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
        crfs_folder    = rf"{project_folder}\CRFs"
        scratch_folder = rf"{project_folder}\Scratch"

        import json
        json_path = rf"{project_folder}\root_dict.json"
        with open(json_path, "r") as json_file:
            root_dict = json.load(json_file)
        del json_file
        del json_path
        del json

        import json
        json_path = rf"{project_folder}\contacts.json"
        with open(json_path, "r") as json_file:
            contacts = json.load(json_file)
        del json_file
        del json_path
        del json

        import json
        json_path = rf"{project_folder}\RoleCd_dict.json"
        # Write to File
        with open(json_path, "r") as json_file:
            RoleCd_dict = json.load(json_file)
        del json_file
        del json_path
        del json

        contact_type_dict = {"citRespParty":"002","idPoC":"007","distorCont":"005","mdContact":"011","stepProc":"009",}

        workspaces = [project_gdb, crfs_folder]

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

            #for dataset_path in sorted([d for d in datasets if d.endswith("CoralFimbriaphylliaParadivisa_20240712")]):
            #for dataset_path in sorted([d for d in datasets if d.endswith("CoralLobedStar_20210730")]):
            #for dataset_path in sorted([d for d in datasets if d.endswith("CoralMountainousStar_20210801")]):
            #for dataset_path in sorted([d for d in datasets if d.endswith("SealGuadalupeFur_20210228")]):
            #for dataset_path in sorted([d for d in datasets if d.endswith("SealHawaiianMonk_20211011")]):
            #for dataset_path in sorted([d for d in datasets if d.endswith("SealRinged_20210228")]):
            #for dataset_path in sorted([d for d in datasets if d.endswith("SealSpotted_20210228")]):
            #for dataset_path in sorted([d for d in datasets if d.endswith("SeaTurtleGreen_20210129")]):
            #for dataset_path in sorted([d for d in datasets if d.endswith("SeaTurtleLeatherback_20210129")]):
            #for dataset_path in sorted([d for d in datasets if d.endswith("SeaTurtleLoggerhead_20210129")]):

            # No Data Source
            #for dataset_path in sorted([d for d in datasets if d.endswith("WhaleSperm_20211220")]):

            for dataset_path in sorted(datasets):
                esri_xml_elements(dataset_path)
                #dq_info_xml_elements(dataset_path)

                del dataset_path

            del datasets
            del workspace

        # Variables set in function
        del contacts_xml_root, contacts_xml_tree
        del contacts
        del RoleCd_dict, root_dict, contact_type_dict
        del project_folder, crfs_folder, scratch_folder
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

def esri_xml_elements(dataset_path=str()):
    try:
        # Imports
        from lxml import etree
        from io import StringIO, BytesIO
        import copy
        import arcpy
        from arcpy import metadata as md

        arcpy.env.overwriteOutput          = True
        arcpy.env.parallelProcessingFactor = "100%"
        arcpy.SetLogMetadata(True)
        arcpy.SetSeverityLevel(2)
        arcpy.SetMessageLevels(['NORMAL']) # NORMAL, COMMANDSYNTAX, DIAGNOSTICS, PROJECTIONTRANSFORMATION

        project_gdb    = os.path.dirname(dataset_path)
        project_folder = os.path.dirname(project_gdb)
        scratch_gdb    = rf"{project_folder}\Scratch\scratch.gdb"

        arcpy.env.workspace        = project_gdb
        arcpy.env.scratchWorkspace = scratch_gdb

        import json
        json_path = rf"{project_folder}\root_dict.json"
        with open(json_path, "r") as json_file:
            root_dict = json.load(json_file)
        del json_file
        del json_path
        del json

        import json
        json_path = rf"{project_folder}\esri_dict.json"
        with open(json_path, "r") as json_file:
            esri_dict = json.load(json_file)
        del json_file
        del json_path
        del json

        dataset_name = os.path.basename(dataset_path)
        #print(f"Updating the Esri XML section for dataset: {dataset_name}")
        #print(f"\tDataset Location: {os.path.basename(os.path.dirname(dataset_path))}")

        dataset_md = md.Metadata(dataset_path)
        dataset_md.synchronize("ALWAYS")
        dataset_md.save()
        dataset_md_xml = dataset_md.xml
        del dataset_md

        # Parse the XML
        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
        tree = etree.parse(StringIO(dataset_md_xml), parser=parser)
        root = tree.getroot()
        #print(etree.tostring(root, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
        del parser, dataset_md_xml

        #print(f"{dataset_name}")

        # ToDo1 Don't worry about processing Esri
        Esri = root.xpath(f"//Esri")[0]

        #print(etree.tostring(Esri, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
        children = [e.tag for e in Esri.iterchildren()]
        if "ArcGISProfile" not in children:
            print(f"{dataset_name}")

##        for child in children:
##            if "ArcGISProfile" == child.tag:
##                print(f"{dataset_name}")
##                print(f"\t{child.tag}")
##            del child
        del children

        xml_file = BytesIO(b'''<?xml version='1.0' encoding='UTF-8'?>
                                <metadata xml:lang="en">
                                <Esri>
                                  <ArcGISstyle>ISO 19139 Metadata Implementation Specification GML3.2</ArcGISstyle>
                                  <scaleRange>
                                    <minScale>150000000</minScale>
                                    <maxScale>5000</maxScale>
                                  </scaleRange>
                                  <ArcGISProfile>ISO19139</ArcGISProfile>
                                </Esri></metadata>''')

        #print("##################################################################")

##        for event, element in etree.iterparse(xml_file):
##            #print(f"{event}, {element.tag:>4}, {element.text} {isinstance(element.text, type(None))}")
##
##            if isinstance(element.text, type(None)):
##                #print(f"{event}, {element.tag:>4}, {element.text} {isinstance(element.text, type(None))}")
##                ancestors = ""
##                root = element
##                while root.getparent() is not None:
##                    root = root.getparent()
##                    ancestors = f"/{root.tag}" + ancestors
##                element_path = f"{ancestors}/{element.tag}"
##                #print(f"element_path: {element_path}")
##
##                _element = Esri.xpath(f"{element_path}")
##                if len(_element) == 0:
##                    #print(f"append: {element.tag}")
##                    #print(ancestors)
##                    parent = Esri.xpath(f"{ancestors}")[0]
##                    parent.append(element)
##                    del parent
##                elif len(_element) == 1:
##                    print("udate?")
##                    print(_element[0].tag)
##                else: pass
##                #for __elem in __element:
##                #    print(__elem.tag)
##                del _element
##
##                del element_path
##                del ancestors
##            elif not isinstance(element.text, type(None)):
##                #print(f"{event}, {element.tag:>4}, {element.text} {isinstance(element.text, type(None))}")
##                ancestors = ""
##                _root = element
##                while _root.getparent() is not None:
##                    _root = _root.getparent()
##                ancestors = f"/{root.tag}" + ancestors
##                element_path = f"{ancestors}/{element.tag}"
##                #print(f"element_path: {element_path}")
##                del _root
##
##                _element = Esri.xpath(f"{element_path}")
##                if len(_element) == 0:
##                    #print(f"append: {element.tag}")
##                    #print(ancestors)
##                    parent = Esri.xpath(f"{ancestors}")[0]
##                    parent.append(element)
##                    del parent
##                elif len(_element) == 1 and not isinstance(_element[0].text, type(None)):
##                    pass
##                    #print(f"udate?\n\tTag: {_element[0].tag}, Text: {_element[0].text}")
##                else: pass
##                #for __elem in __element:
##                #    print(__elem.tag)
##                del _element
##
##                del element_path
##                del ancestors
##            else:
##                pass
##            del  event, element
##        del xml_file

        #print(etree.tostring(Esri, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())

##        # ######################################################################
##        #               ###--->>> Esri section Start <<<---###
##        # ######################################################################
##
##        # Check for ArcGISstyle
##        Esri = root.xpath(f"//Esri")[0]
##        #print(etree.tostring(Esri, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
##        ArcGISstyle = Esri.xpath(f"//ArcGISstyle")
##        if len(ArcGISstyle) == 0:
##            _xml = "<ArcGISstyle>ISO 19139 Metadata Implementation Specification GML3.2</ArcGISstyle>"
##            _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
##            Esri.insert(esri_dict["ArcGISstyle"], _root)
##            del _root, _xml
##        elif len(ArcGISstyle) == 1:
##            ArcGISstyle[0].text = "ISO 19139 Metadata Implementation Specification GML3.2"
##        elif len(ArcGISstyle) > 1:
##            for i in range(1, len(ArcGISstyle)): Esri.remove(ArcGISstyle[i]); i+=1; del i
##        else: pass
##        del Esri, ArcGISstyle
##
##        # ###--->>> Deletes an unwanted element
##        Esri = root.xpath(f"//Esri")[0]
##        itemSize = Esri.xpath(f"//itemSize")
##        if len(itemSize) == 0: pass
##        elif len(itemSize) == 1: pass #; Esri.remove(itemSize[0])
##        elif len(itemSize) > 1:
##            for i in range(1, len(itemSize)): Esri.remove(itemSize[i]); i+=1; del i
##        else: pass
##        del itemSize
##        del Esri
##        # ###--->>> Deletes an unwanted element
##
##        # ###--->>> Check for scaleRange
##        Esri = root.xpath(f"//Esri")[0]
##        scaleRange = Esri.xpath(f"//scaleRange")
##        if len(scaleRange) == 0:
##            _xml = "<scaleRange><minScale>150000000</minScale><maxScale>5000</maxScale></scaleRange>"
##            _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
##            Esri.insert(esri_dict["scaleRange"], _root)
##            del _root, _xml
##        elif len(scaleRange) == 1: pass
##        elif len(scaleRange) > 1:
##            for i in range(1, len(scaleRange)): Esri.remove(scaleRange[i]); i+=1; del i
##        else: pass
##        del scaleRange, Esri
##        # ###--->>>
##
##        # ###--->>> Check for ArcGISProfile
##        Esri = root.xpath(f"//Esri")[0]
##        ArcGISProfile = Esri.xpath(f"//ArcGISProfile")
##        if len(ArcGISProfile) == 0:
##            _xml = "<ArcGISProfile>ISO19139</ArcGISProfile>"
##            _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
##            Esri.insert(esri_dict["ArcGISProfile"], _root)
##            del _root, _xml
##        elif len(ArcGISProfile) == 1: ArcGISProfile[0].text = 'ISO19139'
##        elif len(ArcGISProfile) > 1:
##            for i in range(1, len(ArcGISProfile)): Esri.remove(ArcGISProfile[i]); i+=1; del i
##        else: pass
##        del ArcGISProfile
##        del Esri
##        # ###--->>>

        # ######################################################################
        #               ###--->>> Esri section End <<<---###
        # ######################################################################

        # ###--->>>
        mdFileID = root.xpath(f"//mdFileID")
        if len(mdFileID) == 0:
            _xml = '<mdFileID>gov.noaa.nmfs.inport:</mdFileID>'
            _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
            root.insert(root_dict['mdFileID'], _root)
            del _root, _xml
        elif len(mdFileID) == 1:
            if "gov.noaa.nmfs.inport:" not in mdFileID[0].text:
                mdFileID[0].text = "gov.noaa.nmfs.inport:" + " " + mdFileID[0].text
            else:
                pass
        elif len(mdFileID) > 1:
            for i in range(1, len(mdFileID)): root.remove(mdFileID[i]); i+=1; del i
        else: pass
        del mdFileID
        # ###--->>>

        # ###--->>>
        mdMaint = root.xpath(f"//mdMaint")
        if len(mdMaint) == 0:
            _xml = '<mdMaint><maintFreq><MaintFreqCd value="009"></MaintFreqCd></maintFreq></mdMaint>'
            _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
            root.insert(root_dict['mdMaint'], _root)
            del _root, _xml
        elif len(mdMaint) == 1:
            MaintFreqCd = mdMaint[0].xpath(".//MaintFreqCd")[0]
            #MaintFreqCd.set('value', "009")
            del MaintFreqCd
        elif len(mdMaint) > 1:
            for i in range(1, len(mdMaint)): root.remove(mdMaint[i]); i+=1; del i
        else: pass
        del mdMaint
        # ###--->>>

        # #######################################################################
        #               ###--->>> metadata detail section End <<<---###
        # #######################################################################

        Esri = root.xpath(f"//Esri")[0]
        for child in Esri.xpath("."):
            child[:] = sorted(child, key=lambda x: esri_dict[x.tag])
            del child
        #print(etree.tostring(Esri, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
        del Esri

        SaveBackXml = True
        if SaveBackXml:
            etree.indent(root, space='    ')
            dataset_md_xml = etree.tostring(tree, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True)
            dataset_md = md.Metadata(dataset_path)
            dataset_md.xml = dataset_md_xml
            dataset_md.save()
            dataset_md.synchronize("ALWAYS")
            dataset_md.save()
            del dataset_md
            del dataset_md_xml
        else:
            pass
        del SaveBackXml

        del xml_file
        del dataset_name, tree, root

        # Declared Variables
        del esri_dict, root_dict
        del project_gdb, project_folder, scratch_gdb
        #del contacts, collective_title
        # Imports
        del etree, StringIO, BytesIO, copy, arcpy, md
        # Function Parameters
        del dataset_path

    except:
        traceback.print_exc()
    else:
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        pass

def add_update_contacts(dataset_name="", parent="", resTitle="", resAltTitle="", collTitle=""):
    try:
        # Imports
        from lxml import etree
        import copy

        root = parent
        while root.getparent() is not None:
            root = root.getparent()
        #print(root.tag)

        ancestors = ""
        for ancestor in parent.iterancestors():
            ancestors = f"/{ancestor.tag}" + ancestors
            del ancestor

        # <SyncDate> <SyncTime>
        CreaDate = root.xpath(f"//Esri/CreaDate")[0].text
        CreaTime = root.xpath(f"//Esri/CreaTime")[0].text
        #print(CreaDate, CreaTime)
        CreaDateTime = f"{CreaDate[:4]}-{CreaDate[4:6]}-{CreaDate[6:]}T{CreaTime[:2]}:{CreaTime[2:4]}:{CreaTime[4:6]}"
        #print(f"\tCreaDateTime: {CreaDateTime}")
        #del CreaDateTime
        del CreaDate, CreaTime
        ModDate = root.xpath(f"//Esri/ModDate")[0].text
        ModTime = root.xpath(f"//Esri/ModTime")[0].text
        #print(ModDate, ModTime)
        ModDateTime = f"{ModDate[:4]}-{ModDate[4:6]}-{ModDate[6:]}T{ModTime[:2]}:{ModTime[2:4]}:{ModTime[4:6]}"
        #print(f"\tModDateTime: {ModDateTime}")
        #del ModDateTime
        del ModDate, ModTime

        contact_type_dict = {"citRespParty":"002","idPoC":"007","distorCont":"005","mdContact":"011","stepProc":"009",}

        contacts_xml = rf"{os.environ['USERPROFILE']}\Documents\ArcGIS\Descriptions\contacts.xml"
        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
        contacts_xml_tree = etree.parse(contacts_xml, parser=parser) # To parse from a string, use the fromstring() function instead.
        del parser
        del contacts_xml
        contacts_xml_root = contacts_xml_tree.getroot()
        #etree.indent(contacts_xml_root, space="  ")
        #print(etree.tostring(contacts_xml_root, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())

        contact_parents = root.xpath(f"/{ancestors}//rpIndName/text()/../..")

        if len(contact_parents) > 0:
            #print("\tSearch for Name and Email")
            contact_count = len(contact_parents)
            count = 0
            for contact_parent in contact_parents:
                count+=1
                #print(f"\t\tContact Parent: {contact_parent.tag:<12} {count} of {contact_count}")
                #print(etree.tostring(contact_parent, encoding='UTF-8',  method='xml', pretty_print=True).decode())
                contact_type = contact_parent.tag
                #print(contact_type)
                #print(contact_parent.getparent().tag)
                rpIndName = contact_parent.xpath(f"/{ancestors}//rpIndName/text()/..")
                old_user_name = rpIndName[0].text
                eMailAdd = contact_parent.xpath(f"/{ancestors}//eMailAdd/text()/..")
                old_email_address = eMailAdd[0].text if len(eMailAdd) == 1 else ""

                if old_user_name and old_email_address:
                    #print(f"\t\t\tSearch for '{old_user_name}' and '{old_email_address}'")
                    new_contact_tree = contacts_xml_tree.xpath(f"//eMailAdd[text()='{old_email_address}']/ancestor::contact//rpIndName[text()='{old_user_name}']/ancestor::contact//editorSave[text()='True']/..")
                    for new_contact in new_contact_tree:
                        #print(etree.tostring(new_contact, encoding='UTF-8',  method='xml', pretty_print=True).decode())
                        role_code    = contact_type_dict[contact_type]
                        _new_contact = copy.deepcopy(new_contact_tree[0])
                        _new_contact.tag = f"{contact_type}"
                        _xml = etree.XML(f'<role><RoleCd value="{role_code}"/></role>')
                        # Append element
                        _new_contact.append(_xml)
                        del _xml, role_code
                        _rpIndName = _new_contact.xpath("//rpIndName/text()/..")
                        _user_name = _rpIndName[0].text
                        _eMailAdd = _new_contact.xpath("//eMailAdd/text()/..")
                        _email_address = _eMailAdd[0].text
                        del _eMailAdd, _rpIndName
                        #print(etree.tostring(contact_parent, encoding='UTF-8',  method='xml', pretty_print=True).decode())
                        #print(etree.tostring(_new_contact, encoding='UTF-8',  method='xml', pretty_print=True).decode())
                        contact_parent.getparent().replace(contact_parent, _new_contact)
                        #_contact_parent = root.xpath(f"//eMailAdd[text()='{_email_address}']/ancestor::{contact_type}//rpIndName[text()='{_user_name}']/ancestor::{contact_type}//editorSave[text()='True']/..")
                        #print(etree.tostring(_contact_parent[0], encoding='UTF-8',  method='xml', pretty_print=True).decode())
                        #del _contact_parent
                        del _email_address, _user_name
                        del _new_contact, new_contact
                    del new_contact_tree

                elif old_user_name and not old_email_address:
                    #print(f"\t\t\tSearch for '{old_user_name}'")
                    new_contact_tree = contacts_xml_tree.xpath(f"//rpIndName[text()='{old_user_name}']/ancestor::contact//editorSave[text()='True']/..")
                    for new_contact in new_contact_tree:
                        #print(etree.tostring(new_contact, encoding='UTF-8',  method='xml', pretty_print=True).decode())
                        role_code    = contact_type_dict[contact_type]
                        _new_contact = copy.deepcopy(new_contact_tree[0])
                        _new_contact.tag = f"{contact_type}"
                        _new_contact.set("xmlns", "")
                        _xml = etree.XML(f'<role><RoleCd value="{role_code}"/></role>')
                        # Append element
                        _new_contact.append(_xml)
                        del _xml, role_code
                        _rpIndName = _new_contact.xpath("//rpIndName/text()/..")
                        _user_name = _rpIndName[0].text
                        _eMailAdd = _new_contact.xpath("//eMailAdd/text()/..")
                        _email_address = _eMailAdd[0].text
                        del _eMailAdd, _rpIndName
                        #print(etree.tostring(contact_parent, encoding='UTF-8',  method='xml', pretty_print=True).decode())
                        #print(etree.tostring(_new_contact, encoding='UTF-8',  method='xml', pretty_print=True).decode())
                        contact_parent.getparent().replace(contact_parent, _new_contact)
                        #_contact_parent = root.xpath(f"//eMailAdd[text()='{_email_address}']/ancestor::{contact_type}//rpIndName[text()='{_user_name}']/ancestor::{contact_type}//editorSave[text()='True']/..")
                        #print(etree.tostring(_contact_parent[0], encoding='UTF-8',  method='xml', pretty_print=True).decode())
                        #del _contact_parent
                        del _email_address, _user_name
                        del _new_contact, new_contact
                    del new_contact_tree

                del old_email_address, eMailAdd, old_user_name, rpIndName
                del contact_type, contact_parent

            # Declared variables
            del contact_count, count
            # Imports

        else:
            pass

        del contact_type_dict, contacts_xml_tree, contacts_xml_root
        del contact_parents

        # Declared Variables
        del CreaDateTime, ModDateTime
        del root, ancestors
        # Imports
        del etree, copy
        # Function Parameters
        del dataset_name, parent, resTitle, resAltTitle, collTitle

    except:
        traceback.print_exc()
    else:
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        pass

def add_update_dates(dataset_name="", parent="", resTitle="", resAltTitle="", collTitle=""):
    try:
        # Imports
        from lxml import etree

        root = parent
        while root.getparent() is not None:
            root = root.getparent()
        #print(root.tag)

        ancestors = ""
        for ancestor in parent.iterancestors():
            ancestors = f"/{ancestor.tag}" + ancestors
            del ancestor

        # <SyncDate> <SyncTime>
        CreaDate = root.xpath(f"//Esri/CreaDate")[0].text
        CreaTime = root.xpath(f"//Esri/CreaTime")[0].text
        #print(CreaDate, CreaTime)
        CreaDateTime = f"{CreaDate[:4]}-{CreaDate[4:6]}-{CreaDate[6:]}T{CreaTime[:2]}:{CreaTime[2:4]}:{CreaTime[4:6]}"
        #print(f"\tCreaDateTime: {CreaDateTime}")
        #del CreaDateTime
        del CreaDate, CreaTime
        ModDate = root.xpath(f"//Esri/ModDate")[0].text
        ModTime = root.xpath(f"//Esri/ModTime")[0].text
        #print(ModDate, ModTime)
        ModDateTime = f"{ModDate[:4]}-{ModDate[4:6]}-{ModDate[6:]}T{ModTime[:2]}:{ModTime[2:4]}:{ModTime[4:6]}"
        #print(f"\tModDateTime: {ModDateTime}")
        #del ModDateTime
        del ModDate, ModTime

        dates = parent.xpath(f"{ancestors}//date")

##        if len(dates) == 0:
##            #print("insert date")
##            _xml = '<date></date>'
##            _root = etree.XML(_xml)
##            parent.insert(0, _root)
##            del _root, _xml
##            _dates = parent.xpath(f"{ancestors}//date")
##            _xml = f'<createDate>{CreaDateTime}</createDate>'
##            _root = etree.XML(_xml)
##            _dates[0].insert(0, _root)
##            del _root, _xml
##            _xml = f'<pubDate>{CreaDateTime}</pubDate>'
##            _root = etree.XML(_xml)
##            _dates[0].insert(0, _root)
##            del _root, _xml
##            _xml = f'<reviseDate>{ModDateTime}</reviseDate>'
##            _root = etree.XML(_xml)
##            _dates[0].insert(0, _root)
##            del _root, _xml
##            del _dates
##        el
        if len(dates) == 1:
            #print("Modify date")
            createDate = dates[0].xpath(f"{ancestors}//createDate")
            if len(createDate) == 0:
                _xml = f'<createDate>{CreaDateTime}</createDate>'
                _root = etree.XML(_xml)
                dates[0].insert(1, _root)
                del _root, _xml
            elif len(createDate) == 1:
                if createDate[0].text:
                    pass
                elif not createDate[0].text:
                    createDate[0].text = CreaDateTime
                else:
                    pass
                #print(f"\tcreateDate: {createDate[0].text}")
            elif len(createDate) > 1:
                for i in range(1, len(createDate)): dates[0].remove(createDate[i]); i+=1; del i
            del createDate

            pubDate = dates[0].xpath(f"{ancestors}//pubDate")
            if len(pubDate) == 0:
                _xml = f'<pubDate>{CreaDateTime}</pubDate>'
                _root = etree.XML(_xml)
                dates[0].insert(2, _root)
                del _root, _xml
            elif len(pubDate) == 1:
                if pubDate[0].text:
                    pass
                elif not pubDate[0].text:
                    pubDate[0].text = CreaDateTime
                else:
                    pass
                #print(f"\tpubDate: {pubDate[0].text}")
            elif len(pubDate) > 1:
                for i in range(1, len(pubDate)): dates[0].remove(pubDate[i]); i+=1; del i
            del pubDate

            reviseDate = dates[0].xpath(f"{ancestors}//reviseDate")
            if len(reviseDate) == 0:
                _xml = f'<reviseDate>{ModDateTime}</reviseDate>'
                _root = etree.XML(_xml)
                dates[0].insert(3, _root)
                del _root, _xml
            elif len(reviseDate) == 1:
                if reviseDate[0].text:
                    pass
                elif not reviseDate[0].text:
                    reviseDate[0].text = ModDateTime
                else:
                    pass
            elif len(reviseDate) > 1:
                for i in range(1, len(reviseDate)): dates[0].remove(reviseDate[i]); i+=1; del i
            del reviseDate
            #print(etree.tostring(dates[0], encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())

        elif len(dates) > 1:
            pass #print("Delete date")
            for i in range(1, len(dates)): dates[i].getparent().remove(dates[i]); i+=1; del i
        else:
            pass

        del dates

        # Declared Variables
        del CreaDateTime, ModDateTime
        del root, ancestors
        # Imports
        del etree
        # Function Parameters
        del dataset_name, parent, resTitle, resAltTitle, collTitle

    except:
        traceback.print_exc()
    else:
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        pass

def add_update_titles(dataset_name="", parent="", resTitle="", resAltTitle="", collTitle=""):
    try:
        # Imports
        from lxml import etree

        root = parent
        while root.getparent() is not None:
            root = root.getparent()

        ancestors = ""
        for ancestor in parent.iterancestors():
            ancestors = f"/{ancestor.tag}" + ancestors
            del ancestor

        position = 0

        _resTitle = parent.xpath(f"{ancestors}//resTitle")

##        if len(_resTitle) == 0:
##            if resTitle:
##                _xml = f"<resTitle>{_resTitle}</resTitle>"
##            elif not resTitle:
##                _xml = f"<resTitle>{dataset_name.replace('_', ' ')}</resTitle>"
##            else: pass
##            _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
##            parent.insert(position, _root)
##            del _root, _xml
##        el
        if len(_resTitle) == 1:
            if _resTitle[0].text:
                if dataset_name.replace('_', ' ') not in _resTitle[0].text:
                    new_resTitle = _resTitle[0].text + ". " + dataset_name.replace('_', ' ')
                    _resTitle[0].text = new_resTitle
                    del new_resTitle
                else: pass
            elif not _resTitle[0].text:
                _resTitle[0].text = dataset_name.replace('_', ' ')
            else: pass

        elif len(_resTitle) > 1:
            for i in range(1, len(_resTitle)): _resTitle[i].getparent().remove(_resTitle[i]); i+=1; del i
        else: pass
        del _resTitle

        _resAltTitle = parent.xpath(f"/{ancestors}//resAltTitle")

##        if len(_resAltTitle) == 0:
##            if resAltTitle:
##                _xml = f"<resAltTitle>{resAltTitle}</resAltTitle>"
##            elif not resAltTitle:
##                _xml = f"<resAltTitle>{dataset_name.replace('_', ' ')}</resAltTitle>"
##            else: pass
##            _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
##            parent.insert(position+1, _root)
##            del _root, _xml
##        el
        if len(_resAltTitle) == 1:
            #print(f"Updating resTitle if needed at index: {idCitation.index(idCitation.xpath(f'./resTitle')[0])}")
            if _resAltTitle[0].text:
                if dataset_name.replace('_', ' ') not in _resAltTitle[0].text:
                    new_resAltTitle = _resAltTitle[0].text + ". " + dataset_name.replace('_', ' ')
                    _resAltTitle[0].text = new_resAltTitle
                    del new_resAltTitle
                else: pass
            elif not _resAltTitle[0].text:
                _resAltTitle[0].text = dataset_name.replace('_', ' ')
            else: pass
        elif len(_resAltTitle) > 1:
            for i in range(1, len(_resAltTitle)): _resAltTitle[i].getparent().remove(_resAltTitle[i]); i+=1; del i
        else:
            pass
        del _resAltTitle
        #print(etree.tostring(parent, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())

        _collTitle = parent.xpath(f"/{ancestors}//collTitle")

##        if len(_collTitle) == 0:
##            if collTitle:
##                _xml = f"<collTitle>{collTitle}</collTitle>"
##            elif not collTitle:
##                _xml = f"<collTitle>{dataset_name.replace('_', ' ')}</collTitle>"
##            else: pass
##            _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
##            parent.insert(position+2, _root)
##            del _root, _xml
##        el
        if len(_collTitle) == 1:
            #print(f"Updating resTitle if needed at index: {idCitation.index(idCitation.xpath(f'./resTitle')[0])}")
            if _collTitle[0].text:
                if dataset_name.replace('_', ' ') not in _collTitle[0].text:
                    new_collTitle = _collTitle[0].text + ". " + dataset_name.replace('_', ' ')
                    _collTitle[0].text = new_collTitle
                    del new_collTitle
                else: pass
            elif not _collTitle[0].text:
                _collTitle[0].text = dataset_name.replace('_', ' ')
            else: pass
        elif len(_collTitle) > 1:
            for i in range(1, len(_collTitle)): _collTitle[i].getparent().remove(_collTitle[i]); i+=1; del i
        else:
            pass
        del _collTitle

        #print(etree.tostring(parent, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())

        # Variables
        del ancestors, position, root
        # Imports
        del etree
        # Function parameters
        del dataset_name, parent, resTitle, resAltTitle, collTitle

    except:
        traceback.print_exc()
    else:
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        pass

def dq_info_xml_elements(dataset_path=str()):
    try:
        # Imports
        from lxml import etree
        from io import StringIO, BytesIO
        import copy
        import arcpy
        from arcpy import metadata as md

        arcpy.env.overwriteOutput          = True
        arcpy.env.parallelProcessingFactor = "100%"
        arcpy.SetLogMetadata(True)
        arcpy.SetSeverityLevel(2)
        arcpy.SetMessageLevels(['NORMAL']) # NORMAL, COMMANDSYNTAX, DIAGNOSTICS, PROJECTIONTRANSFORMATION

        project_gdb    = os.path.dirname(dataset_path)
        project_folder = os.path.dirname(project_gdb)
        scratch_gdb    = rf"{project_folder}\Scratch\scratch.gdb"

        arcpy.env.workspace        = project_gdb
        arcpy.env.scratchWorkspace = scratch_gdb

        import json
        json_path = rf"{project_folder}\root_dict.json"
        with open(json_path, "r") as json_file:
            root_dict = json.load(json_file)
        del json_file
        del json_path
        del json

        import json
        json_path = rf"{project_folder}\dqInfo_dict.json"
        with open(json_path, "r") as json_file:
            dqInfo_dict = json.load(json_file)
        del json_file
        del json_path
        del json

        dataset_name = os.path.basename(dataset_path)
        print(f"Dataset Name: {dataset_name}")
        #print(f"\tDataset Location: {os.path.basename(os.path.dirname(dataset_path))}")

        dataset_md = md.Metadata(dataset_path)
        dataset_md.synchronize("ALWAYS")
        dataset_md.save()
        dataset_md_xml = dataset_md.xml
        del dataset_md

        # Parse the XML
        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
        target_tree = etree.parse(StringIO(dataset_md_xml), parser=parser)
        target_root = target_tree.getroot()
        del parser, dataset_md_xml

        # ######################################################################
        #               ###--->>> Start <<<---###
        # ######################################################################

        #dqInfo = target_root.xpath(f"//dqInfo")[0]

        #for child in dqInfo.xpath("*"):
        #    child[:] = sorted(child, key=lambda x: dqInfo_dict[x.tag])
        #    del child

        #print(etree.tostring(dqInfo, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())

        xml_file = b'''<?xml version='1.0' encoding='UTF-8'?>
                       <metadata xml:lang="en">
                           <dqInfo>
                            <dqScope xmlns="">
                                <scpLvl>
                                    <ScopeCd value="005"></ScopeCd>
                                </scpLvl>
                                <scpLvlDesc xmlns="">
                                    <datasetSet Sync="TRUE">Feature Class</datasetSet>
                                </scpLvlDesc>
                            </dqScope>
                            <report type="DQConcConsis" dimension="horizontal">
                                <measDesc>Based on a review from species' experts, we determined that all necessary features were included in the species' range file.</measDesc>
                                 <measResult>
                                    <ConResult>
                                       <conSpec>
                                          <resTitle>Specification Title.</resTitle>
                                          <resAltTitle></resAltTitle>
                                          <collTitle></collTitle>
                                          <date>
                                            <createDate></createDate>
                                            <pubDate></pubDate>
                                            <reviseDate></reviseDate>
                                          </date>
                                       </conSpec>
                                       <conExpl>Based on a review from species' experts, we determined that all necessary features were included in the species' range file.</conExpl>
                                       <conPass>1</conPass>
                                    </ConResult>
                                 </measResult>
                            </report>
                            <report type="DQCompOm" dimension="horizontal">
                                <measDesc>Based on a review from species' experts, we determined that all necessary features were included in the species' range file.</measDesc>
                                 <measResult>
                                    <ConResult>
                                       <conSpec>
                                          <resTitle>Specification Title.</resTitle>
                                          <resAltTitle></resAltTitle>
                                          <collTitle></collTitle>
                                          <date>
                                            <createDate></createDate>
                                            <pubDate></pubDate>
                                            <reviseDate></reviseDate>
                                          </date>
                                       </conSpec>
                                       <conExpl>Based on a review from species' experts, we determined that all necessary features were included in the species' range file.</conExpl>
                                       <conPass>1</conPass>
                                    </ConResult>
                                 </measResult>
                            </report>
                            <dataLineage>
                                <statement></statement>
                                <dataSource type="">
                                    <srcDesc></srcDesc>
                                    <srcCitatn>
                                        <resTitle></resTitle>
                                        <resAltTitle></resAltTitle>
                                        <collTitle></collTitle>
                                        <citOnlineRes>
                                            <linkage></linkage>
                                            <protocol></protocol>
                                            <orName></orName>
                                            <orDesc></orDesc>
                                            <orFunct>
                                                <OnFunctCd></OnFunctCd>
                                            </orFunct>
                                        </citOnlineRes>
                                        <date>
                                            <createDate></createDate>
                                            <pubDate></pubDate>
                                            <reviseDate></reviseDate>
                                        </date>
                                        <otherCitDet></otherCitDet>
                                        <presForm>
                                            <fgdcGeoform>document</fgdcGeoform>
                                            <PresFormCd value="001"></PresFormCd>
                                        </presForm>
                                        <citRespParty>
                                            <editorSource>extermal</editorSource>
                                            <editorDigest></editorDigest>
                                            <rpIndName></rpIndName>
                                            <rpOrgName></rpOrgName>
                                            <rpPosName></rpPosName>
                                            <rpCntInfo>
                                                <cntAddress addressType="both">
                                                    <delPoint></delPoint>
                                                    <city></city>
                                                    <adminArea></adminArea>
                                                    <postCode></postCode>
                                                    <eMailAdd></eMailAdd>
                                                    <country></country>
                                                </cntAddress>
                                                <cntPhone>
                                                    <voiceNum tddtty=""></voiceNum>
                                                    <faxNum></faxNum>
                                                </cntPhone>
                                                <cntHours></cntHours>
                                                <cntOnlineRes>
                                                    <linkage></linkage>
                                                    <protocol>REST Service</protocol>
                                                    <orName></orName>
                                                    <orDesc></orDesc>
                                                    <orFunct>
                                                        <OnFunctCd value="002"></OnFunctCd>
                                                    </orFunct>
                                                </cntOnlineRes>
                                            </rpCntInfo>
                                            <editorSave>True</editorSave>
                                            <displayName></displayName>
                                            <role>
                                                <RoleCd value="005"></RoleCd>
                                            </role>
                                        </citRespParty>
                                    </srcCitatn>
                                    <srcMedName>
                                        <MedNameCd value="015"/>
                                    </srcMedName>
                                </dataSource>
                                <prcStep>
                                    <stepDesc>Metadata Update</stepDesc>
                                    <stepProc>
                                        <editorSource>extermal</editorSource>
                                        <editorDigest></editorDigest>
                                        <rpIndName></rpIndName>
                                        <rpOrgName></rpOrgName>
                                        <rpPosName></rpPosName>
                                        <rpCntInfo>
                                            <cntAddress addressType="both">
                                                <delPoint></delPoint>
                                                <city></city>
                                                <adminArea></adminArea>
                                                <postCode></postCode>
                                                <eMailAdd></eMailAdd>
                                                <country>US</country>
                                            </cntAddress>
                                            <cntPhone>
                                                <voiceNum tddtty=""></voiceNum>
                                                <faxNum></faxNum>
                                            </cntPhone>
                                            <cntHours>0700 - 1800 EST/EDT</cntHours>
                                            <cntOnlineRes>
                                                <linkage></linkage>
                                                <protocol>REST Service</protocol>
                                                <orName>Fisheries</orName>
                                                <orDesc></orDesc>
                                                <orFunct>
                                                    <OnFunctCd value="002"></OnFunctCd>
                                                </orFunct>
                                            </cntOnlineRes>
                                        </rpCntInfo>
                                        <editorSave>True</editorSave>
                                        <displayName></displayName>
                                        <role>
                                            <RoleCd value="009"></RoleCd>
                                        </role>
                                    </stepProc>
                                    <stepDateTm></stepDateTm>
                                </prcStep>
                            </dataLineage>
                        </dqInfo>
                    </metadata>
                     '''
        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
        source_tree = etree.parse(BytesIO(xml_file), parser=parser)
        source_root = source_tree.getroot()
        del parser

        element_paths = list()

        for element in source_root.iter():
            element_path = source_tree.getpath(element)
            if element_path not in element_paths:
                element_paths.append(element_path)
            del element_path
            #element.clear()
            del element

        for element_path in element_paths:
            #print(element_path)
            if len(source_tree.xpath(f"/{element_path}")) > 0:
                element = source_tree.xpath(f"/{element_path}")[0]
                _element_path = source_tree.getpath(element)
                #print(element.xpath(_element_path)[0])
                #print(_element_path)
                if isinstance(element.getparent(), type(None)):
                    pass # Nothing to do, at the root of the tree
                elif not isinstance(element.getparent(), type(None)):
                    # Get the parent of the source element, this should be in target
                    parent = element.getparent()
                    # Get the ancestors of the current element
                    ancestors = source_tree.getpath(parent)
                    #print()
                    #print("Element Path")
                    #print(_element_path)
                    #print(ancestors)

                    # Get the elements from the target using the source path
                    target_elements = target_tree.xpath(f"/{source_tree.getpath(element)}")
                    #print(len(target_elements))
                    if len(target_elements) == 0:
                        #print(element.getroottree().getpath(element))
                        #print(target_tree.xpath(element.getroottree().getpath(element.getparent())))
                        target_parent_elements = target_tree.xpath(element.getroottree().getpath(element.getparent()))
                        for target_parent_element in target_parent_elements:
                            #print(target_tree.getpath(target_parent_element))
                            target_parent_element.insert(-1, element)
                            add_update_titles(dataset_name=dataset_name, parent=target_parent_element, resTitle="", resAltTitle="", collTitle="")
                            add_update_dates(dataset_name=dataset_name, parent=target_parent_element, resTitle="", resAltTitle="", collTitle="")
                            for child in target_parent_element.xpath("*"):
                                child[:] = sorted(child, key=lambda x: dqInfo_dict[x.tag])
                                del child
                            #print(etree.tostring(target_parent_element, encoding='UTF-8', method='xml', pretty_print=True).decode())
                            del target_parent_element
                        del target_parent_elements

                    for target_element in target_elements:
                        pass
                        #print(target_tree.getpath(target_element))

##                    if len(target_elements) == 0:
##                        _ancestor_target_elements = target_root.xpath(f"/{ancestors}")
##                        #print(len(_ancestor_target_elements))
##                        if len(_ancestor_target_elements) == 0:
##                            pass #print(f"ancestor not found: {ancestors}")
##                        elif len(_ancestor_target_elements) > 0:
##                            for _ancestor_target_element in _ancestor_target_elements:
##                                #print(_element_path)
##                                #print(ancestors)
##                                print(element.getroottree().getpath(element))
##                                print(element.getroottree().getpath(element.getparent()))
##                                print(target_tree.getpath(_ancestor_target_element))
##                                print()
##                                #print(f"ancestor found: {_ancestor_target_element.tag} {ancestors}")
##                                _ancestor_target_element.append(element)
##                                del _ancestor_target_element
##                        #print(f"Need to use ancestors: {ancestors}")
##                        #print(_element_path)
##                        del _ancestor_target_elements
##                    elif len(target_elements) == 1:
##                        pass
##                        #print(f"found one")
##                        #print(f"\t{target_elements[0].tag}")
##                        #print(_element_path)
##                    elif len(target_elements) > 1:
##                        pass
##                        #print(f"found more than one")
##                        #for target_element in target_elements:
##                        #    print(f"\t{target_element.tag}")

                        del target_element
                    del ancestors, parent
                    del target_elements

                del _element_path, element
            del element_path
        #print(etree.tostring(target_tree, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
        del element_paths
        del source_tree, source_root

            #print(element.tag)
            #if len(element) > 0:
            #    for _element in print(target_root.xpath(f"/{element_path}"))
##            if len(target_root.xpath(f"/{element_path}")) == 0:
##                if len(target_root.xpath(f"/{ancestors}")) == 0:
##                    pass
##                elif len(target_root.xpath(f"/{ancestors}")) == 1:
##                    #print(f"\tSource Path Found: {ancestors}")
##                    target_parent = target_root.xpath(f"/{ancestors}")[0]
##                    #print(target_parent.tag)
##                    target_parent.append(source_element)
##                    del target_parent

##            del _element_path
##            del element
##            del element_path


##        element_paths = list()
##        for event, element in etree.iterparse(BytesIO(xml_file)):
##            #print(f"{event}, {element.tag:>4}, {element.text.strip() if not isinstance(element.text, type(None)) else ''} {isinstance(element.text, type(None))}")
##            ancestors = ""
##            #print(element.getpath())
##            #print(BytesIO(xml_file).getroot())
##
##            _root = element
##            while _root.getparent() is not None:
##                _root = _root.getparent()
##                ancestors = f"/{_root.tag}" + ancestors
##            del _root
##            element_path = f"{ancestors}/{element.tag}"
##            del ancestors
##            #print(f"\telement_path: {element_path}")
##            if element_path not in element_paths:
##                element_paths.append(element_path)
##            del element_path
##            element.clear()
##            del event, element

##        for element_path in sorted(element_paths):
##            #print(f"Element Path: {element_path}")
##            parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
##            source_tree = etree.parse(BytesIO(xml_file), parser=parser)
##            del parser
##            source_root = source_tree.getroot()
##            del source_tree
##
##            source_elements = source_root.xpath(element_path)
##
##            if len(source_elements) == 0:
##                print("found nothing")
##            elif len(source_elements) == 1:
##                _source_element = source_elements[0]
##                print(f"one found: {_source_element.tag} {element_path}")
##                del _source_element
##            elif len(source_elements) > 1:
##                print("many found")
##                element_count = len(source_elements)
##                count = 0
##                #print(f"\t\tContact Parent: {contact_parent.tag:<12} {count} of {contact_count}")
##                for _source_element in source_elements:
##                    #print(f"Found: {_source_element.tag} {count} of {element_count} {element_path}")
##                    print(f"Found: {source_elements[count].tag} {count} of {element_count} {element_path}")
##                    count+=1
##                    del _source_element
##                del count, element_count
##
##            del source_elements

##            ancestors = ""
##            _root = source_element
##            while _root.getparent() is not None:
##                _root = _root.getparent()
##                ancestors = f"/{_root.tag}" + ancestors
##            del _root
##            #print(f"Ancestors: {ancestors}")
##
##            if len(target_root.xpath(f"/{element_path}")) == 0:
##                if len(target_root.xpath(f"/{ancestors}")) == 0:
##                    pass
##                elif len(target_root.xpath(f"/{ancestors}")) == 1:
##                    #print(f"\tSource Path Found: {ancestors}")
##                    target_parent = target_root.xpath(f"/{ancestors}")[0]
##                    #print(target_parent.tag)
##                    target_parent.append(source_element)
##                    del target_parent
##                elif len(target_root.xpath(f"/{ancestors}")) > 1:
##                    pass
##                else:
##                    pass
##
##            elif len(target_root.xpath(f"/{element_path}")) == 1:
##                #print(f"\tPath found: {element_path}")
##                _found_element = target_root.xpath(f"/{element_path}")[0]
##                #print(_found_element.tag)
##                #print(f"\tTarget Path Found: {element_path}")
##                del _found_element
##
##            elif len(target_root.xpath(f"/{element_path}")) > 1:
##                pass
##                #print(f"\tPath found: {element_path} {len(target_root.xpath(f'/{element_path}'))}")
##                #for _found_element in target_root.xpath(f"/{element_path}"):
##                #    print(etree.tostring(_found_element, encoding='UTF-8', method='xml', pretty_print=True).decode())
##                    #_found_element = target_root.xpath(f"/{ancestors}")[0]
##                    #print(f"\tSource Path Found: {ancestors}")
##                    #print(len(ancestors))
##                    #print(root.xpath(f"{ancestors}")[0].tag)
##                #    del _found_element

        del xml_file

        #print(etree.tostring(target_tree, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())

        srcCitatn = target_tree.xpath(f"//srcCitatn")[0]
        add_update_titles(dataset_name=dataset_name, parent=srcCitatn, resTitle="", resAltTitle="", collTitle="")
        add_update_dates(dataset_name=dataset_name, parent=srcCitatn, resTitle="", resAltTitle="", collTitle="")
        for child in srcCitatn.xpath("*"):
            child[:] = sorted(child, key=lambda x: dqInfo_dict[x.tag])
            del child
        #print(etree.tostring(srcCitatn, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
        del srcCitatn

        dqInfo = target_tree.xpath(f"//dqInfo")[0]
        add_update_titles(dataset_name=dataset_name, parent=dqInfo, resTitle="", resAltTitle="", collTitle="")
        add_update_dates(dataset_name=dataset_name, parent=dqInfo, resTitle="", resAltTitle="", collTitle="")
        for child in dqInfo.xpath("*"):
            child[:] = sorted(child, key=lambda x: dqInfo_dict[x.tag])
            del child
        #print(etree.tostring(dqInfo, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
        del dqInfo

        dataSources = target_root.xpath(f"//dataSource")
        for dataSource in dataSources:
            add_update_titles(dataset_name=dataset_name, parent=dataSource, resTitle="", resAltTitle="", collTitle="")
            add_update_dates(dataset_name=dataset_name, parent=dataSource, resTitle="", resAltTitle="", collTitle="")
            for child in dataSource.xpath("*"):
                child[:] = sorted(child, key=lambda x: dqInfo_dict[x.tag])
                del child
            #print(etree.tostring(dataSource, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
            del dataSource
        del dataSources

        #ToDo3 Save for later f'<statement>Data processing and metadata creation for "{_resTitle}"</statement>'

##        statement = root.xpath(f"//dqInfo//dataLineage//statement")
##        if len(statement) == 0:
##            _resTitle = root.xpath("//dataIdInfo//idCitation//resTitle")[0].text
##            dataLineage = root.xpath(f"//dqInfo//dataLineage")[0]
##            _xml = f'<statement>Data processing and metadata creation for "{_resTitle}"</statement>'
##            _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
##            dataLineage.insert(dqInfo_dict['statement'], _root)
##            del _root, _xml
##            del dataLineage, _resTitle

        #ToDo3 Save for later
        # _xml = f'<srcDesc>Data processing and metadata creation for "{_resTitle}"</srcDesc>'

##        srcDesc = root.xpath(f"//dqInfo/dataLineage//dataSource//srcDesc")
##            _resTitle = root.xpath("//dataIdInfo//idCitation//resTitle")[0].text
##            dataSource = root.xpath(f"//dqInfo//dataLineage//dataSource")[0]
##            _xml = f'<srcDesc>Data processing and metadata creation for "{_resTitle}"</srcDesc>'
##            _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
##            dataSource.insert(dqInfo_dict['srcDesc'], _root)
##            del _root, _xml
##            del dataSource, _resTitle

            #ToDo1 Address updating these lements
            # add_update_titles
            # add_update_dates
            # add_update_contacts

##        element = root.xpath("//dqInfo//dataLineage//dataSource//srcCitatn")[0]
##        #element = root.xpath("//dqInfo")[0]
##        #ancestors = tree.getpath(element)
##        #print(ancestors); del ancestors
##        add_update_titles(dataset_name=dataset_name, parent=element, resTitle="", resAltTitle="", collTitle="")
##        add_update_dates(dataset_name=dataset_name, parent=element, resTitle="", resAltTitle="", collTitle="")
##        add_update_contacts(dataset_name=dataset_name, parent=element, resTitle="", resAltTitle="", collTitle="")
##        del element

        #ToDo3 Save for later
        # _xml = f'<stepDesc>{_resTitle}</stepDesc>'
        #stepDesc = root.xpath(f"//dqInfo//dataLineage//prcStep//stepDesc")
        #if len(stepDesc) == 0:
        #    _resTitle = root.xpath("//dataIdInfo//idCitation//resTitle")[0].text
        #    prcStep = root.xpath(f"//dqInfo//dataLineage//prcStep")[0]
        #    _xml = f'<stepDesc>{_resTitle}</stepDesc>'

        #ToDo3 Save for later
        # _stepDateTm.text = CreaDateTime
        #stepDateTm = root.xpath(f"//dqInfo//dataLineage//prcStep//stepDateTm")
        #    for _stepDateTm in root.xpath(f"//dqInfo//dataLineage//prcStep//stepDateTm"):
        #        if not _stepDateTm.text:
        #            _stepDateTm.text = CreaDateTime

        # ######################################################################
        #               ###--->>> End <<<---###
        # ######################################################################

        dqInfo = target_root.xpath(f"//dqInfo")[0]
        add_update_titles(dataset_name=dataset_name, parent=dqInfo, resTitle="", resAltTitle="", collTitle="")
        add_update_dates(dataset_name=dataset_name, parent=dqInfo, resTitle="", resAltTitle="", collTitle="")
        add_update_contacts(dataset_name=dataset_name, parent=dqInfo, resTitle="", resAltTitle="", collTitle="")
        del dqInfo

        dqInfo = target_root.xpath(f"//dqInfo")[0]
        for child in dqInfo.xpath("*"):
            child[:] = sorted(child, key=lambda x: dqInfo_dict[x.tag])
            del child
        del dqInfo

        SaveBackXml = False
        if SaveBackXml:
            #print(etree.tostring(target_tree, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
            etree.indent(target_tree, space='    ')
            dataset_md_xml = etree.tostring(target_tree, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode()
            dataset_md = md.Metadata(dataset_path)
            dataset_md.xml = dataset_md_xml
            dataset_md.save()
            dataset_md.synchronize("ALWAYS")
            dataset_md.save()

            del dataset_md
            del dataset_md_xml
        else:
            pass
        del SaveBackXml

        del dataset_name, target_tree, target_root

        # Declared Variables
        del dqInfo_dict, root_dict
        del project_gdb, project_folder, scratch_gdb
        #del contacts, collective_title
        # Imports
        del etree, StringIO, BytesIO, copy, arcpy, md
        # Function Parameters
        del dataset_path

    except:
        traceback.print_exc()
    else:
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        pass

def main(project_gdb="", contacts="", collective_title=""):
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

        arcpy.env.overwriteOutput = True
        arcpy.env.parallelProcessingFactor = "100%"

        project_folder      = rf"{os.path.dirname(project_gdb)}"
        #base_project_folder = rf"{os.path.dirname(project_folder)}"
        #base_project_file   = rf"{base_project_folder}\DisMAP.aprx"

        del project_folder

        # Test if passed workspace exists, if not raise SystemExit
        #if not arcpy.Exists(base_project_file):
        #    print(f"{os.path.basename(base_project_file)} is missing!!")

        # Test if passed workspace exists, if not raise SystemExit
        if not arcpy.Exists(project_gdb):
            print(f"{os.path.basename(project_gdb)} is missing!!")
            print(project_gdb)

        Backup = False
        if Backup:
            dismap.backup_gdb(project_gdb)
        del Backup

        try:
            UpdateExistingContacts = False
            if UpdateExistingContacts:
                update_existing_contacts(project_gdb=project_gdb)
            else:
                pass
            del UpdateExistingContacts

            UpdateProcessStepsContacts = True
            if UpdateProcessStepsContacts:
                update_process_steps_contacts(project_gdb=project_gdb)
            else:
                pass
            del UpdateProcessStepsContacts

            UpdateXmlElements = False
            if UpdateXmlElements:
                update_xml_elements(project_gdb=project_gdb, contacts=contacts, collective_title=collective_title)
            else:
                pass
            del UpdateXmlElements

            CreateThumbnails = False
            if CreateThumbnails:
               create_thumbnails(project_gdb=project_gdb)
            else:
                pass
            del CreateThumbnails

            CreateMaps = False
            if CreateMaps:
                create_maps(project_gdb=project_gdb, dataset=rf"{project_gdb}\DisMAP_Regions")
            else:
                pass
            del CreateMaps

            ExportToInportXmlFiles = False
            if ExportToInportXmlFiles:
                export_to_inport_xml_files(project_gdb=project_gdb)
            else:
                pass
            del ExportToInportXmlFiles

        except Exception as e:
            print(str(e))
            traceback.print_exc()


        print(f"Compact GDB")
        arcpy.management.Compact(project_gdb)
        print("\t"+arcpy.GetMessages().replace("\n", "\n\t")+"\n")

        # Declared Varaiables

        # Imports

        # Function Parameters
        del project_gdb, contacts, collective_title

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
        pass
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

        base_project_folder = rf"{os.path.dirname(os.path.dirname(__file__))}"
        # ###################### DisMAP ########################################
        contacts = {"citRespParty"     : {"rpIndName" : "Timothy J Haverland",                   "eMailAdd" : "tim.haverland@noaa.gov"},
                        "idPoC"        : {"rpIndName" : "Melissa Karp",                          "eMailAdd" : "melissa.karp@noaa.gov"},
                        "distorCont"   : {"rpIndName" : "NMFS Office of Science and Technology", "eMailAdd" : "tim.haverland@noaa.gov"},
                        "mdContact"    : {"rpIndName" : "John F Kennedy",                        "eMailAdd" : "john.f.kennedy@noaa.gov"},
                        "stepProc"     : [{"rpIndName" : "John F Kennedy",                        "eMailAdd" : "john.f.kennedy@noaa.gov"},
                                          {"rpIndName" : "Melissa Karp",                          "eMailAdd" : "melissa.karp@noaa.gov"},
                                         ],
                        }

        collective_title = "NMFS DisMAP 2024"
        #project_name = "April 1 2023"
        #project_name = "July 1 2024"
        #project_name   = "December 1 2024"
        #project_folder = rf"{base_project_folder}\{project_name}"
        # ###################### DisMAP ########################################
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

        contacts = {"citRespParty"     : [{"role"  : "Custodian",        "rpIndName" : "Nikki Wildart",       "eMailAdd" : "nikki.wildart@noaa.gov"},],
                        "idPoC"        : [{"role"  : "Point of Contact", "rpIndName" : "Nikki Wildart",       "eMailAdd" : "nikki.wildart@noaa.gov"},],
                        "distorCont"   : [{"role"  : "Distributor",      "rpIndName" : "Nikki Wildart",       "eMailAdd" : "nikki.wildart@noaa.gov"},],
                        "mdContact"    : [{"role"  : "Author",           "rpIndName" : "Nikki Wildart",       "eMailAdd" : "nikki.wildart@noaa.gov"},],
                        "stepProc"     : [{"role" : "Processor",        "rpIndName" : "Nikki Wildart",       "eMailAdd" : "nikki.wildart@noaa.gov"},
                                          {"role" : "Processor",        "rpIndName" : "Dan Lawson",          "eMailAdd" : "dan.lawson@noaa.gov"},
                                          {"role" : "Processor",        "rpIndName" : "Jeffrey A. Seminoff", "eMailAdd" : "jeffrey.seminoff@noaa.gov"},
                                          {"role" : "Processor",        "rpIndName" : "Jennifer Schultz",    "eMailAdd" : "jennifer.schultz@noaa.gov"},
                                          {"role" : "Processor",        "rpIndName" : "Jonathan Molineaux",  "eMailAdd" : "jonathan.molineaux@noaa.gov"},
                                          {"role" : "Processor",        "rpIndName" : "Marc Romano",         "eMailAdd" : "marc.romano@noaa.gov"},
                                          {"role" : "Processor",        "rpIndName" : "Susan Wang",          "eMailAdd" : "susan.wang@noaa.gov"},
                                         ],
                        }

        collective_title = "NMFS ESA Range Geodatabase 2024"
        project_name     = "National Mapper"
        #project_name    = "NMFS_ESA_Range"
        project_folder   = rf"{base_project_folder}"
        project_gdb      = rf"{project_folder}\{project_name}.gdb"

        main(project_gdb=project_gdb, contacts=contacts, collective_title=collective_title)

        # Variables
        del contacts, collective_title
        del project_gdb, project_name, project_folder, base_project_folder

        # Imports

    except:
        traceback.print_exc()
    else:
        pass
    finally:
        pass
