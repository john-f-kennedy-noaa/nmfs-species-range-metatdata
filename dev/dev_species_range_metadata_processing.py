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
        scratch_folder      = rf"{project_folder}\Scratch"
        arcpy.env.workspace        = project_gdb
        arcpy.env.scratchWorkspace = rf"{scratch_folder}\scratch.gdb"
        aprx = arcpy.mp.ArcGISProject(base_project_file)
        home_folder = aprx.homeFolder
        workspaces = [project_gdb]
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

        # Declared Variables set in function for aprx
        del home_folder
        # Save aprx one more time and then delete
        aprx.save()
        del aprx

        # Declared Variables set in function
        del project_gdb, base_project_folder, metadata_folder
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

        # Declared Variables set in function
        del project_gdb, base_project_folder, metadata_folder
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

        # Declared Variables set in function for aprx

        # Save aprx one more time and then delete
        aprx.save()
        del aprx

        # Declared Variables set in function
        del project_gdb, base_project_folder, metadata_folder
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

def remove_duplicate_elements(root):
    seen = {}
    for element in root.iter():
        key = (element.tag, element.text, tuple(element.attrib.items()))
        if key in seen:
            element.getparent().remove(element)
        else:
            seen[key] = True
        del key, element
    del seen, root

"""
This is an attempt to merge to XML trees.  It works but it probably doesn't do what you want because XML elements are not only identified
by their tag.  Take a POM for example, it will have many <dependency> nodes that are only distinguished by the text on their daughter
node 'GroupId'.  This code does not take that into account.
"""
def xml_tree_merge(source, target):
    import copy
    """Merge two xml trees A and B, so that each recursively found leaf element of B is added to A.  If the element
    already exists in A, it is replaced with B's version.  Tree structure is created in A as required to reflect the
    position of the leaf element in B.
    Given <top><first><a/><b/></first></top> and  <top><first><c/></first></top>, a merge results in
    <top><first><a/><b/><c/></first></top> (order not guaranteed)
    """
    def inner(aparent, bparent):
        for bchild in bparent:
            achild = aparent.xpath('./' + bchild.tag)
            if not achild:
                aparent.append(bchild)
            elif bchild.getchildren():
                inner(achild[0], bchild)

    source_copy = copy.deepcopy(source)
    inner(source_copy, target)
    return source_copy

def insert_missing_elements(dataset_path):
    try:
        from lxml import etree
        from arcpy import metadata as md
        from io import BytesIO, StringIO
        import copy

        project_gdb    = os.path.dirname(dataset_path)
        project_folder = os.path.dirname(project_gdb)
        export_folder  = rf"{project_folder}\Export"
        scratch_folder = rf"{project_folder}\Scratch"

        import json
        json_path = rf"{project_folder}\root_dict.json"
        with open(json_path, "r") as json_file:
            root_dict = json.load(json_file)
        json_path = rf"{project_folder}\esri_dict.json"
        with open(json_path, "r") as json_file:
            esri_dict = json.load(json_file)
        json_path = rf"{project_folder}\dataIdInfo_dict.json"
        with open(json_path, "r") as json_file:
            dataIdInfo_dict = json.load(json_file)
        json_path = rf"{project_folder}\contact_dict.json"
        with open(json_path, "r") as json_file:
            contact_dict = json.load(json_file)
        json_path = rf"{project_folder}\dqInfo_dict.json"
        with open(json_path, "r") as json_file:
            dqInfo_dict = json.load(json_file)
        json_path = rf"{project_folder}\RoleCd_dict.json"
        with open(json_path, "r") as json_file:
            RoleCd_dict = json.load(json_file)
        json_path = rf"{project_folder}\tpCat_dict.json"
        with open(json_path, "r") as json_file:
            tpCat_dict = json.load(json_file)
        del json_file
        del json_path
        del json

        arcpy.env.workspace        = project_gdb
        arcpy.env.scratchWorkspace = rf"{scratch_folder}\scratch.gdb"
        del scratch_folder
        del project_folder
        del project_gdb

        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # Get contact information
        contacts_xml = rf"{os.environ['USERPROFILE']}\Documents\ArcGIS\Descriptions\contacts.xml"
        contacts_xml_tree = etree.parse(contacts_xml, parser=etree.XMLParser(encoding='UTF-8', remove_blank_text=True)) # To parse from a string, use the fromstring() function instead.
        del contacts_xml

        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # Get Prefered contact information
        mdContact_rpIndName = contact_dict["mdContact"][0]["rpIndName"]
        mdContact_eMailAdd  = contact_dict["mdContact"][0]["eMailAdd"]
        mdContact_role      = contact_dict["mdContact"][0]["role"]

        citRespParty_rpIndName = contact_dict["citRespParty"][0]["rpIndName"]
        citRespParty_eMailAdd  = contact_dict["citRespParty"][0]["eMailAdd"]
        citRespParty_role      = contact_dict["citRespParty"][0]["role"]

        idPoC_rpIndName = contact_dict["idPoC"][0]["rpIndName"]
        idPoC_eMailAdd  = contact_dict["idPoC"][0]["eMailAdd"]
        idPoC_role      = contact_dict["idPoC"][0]["role"]

        distorCont_rpIndName = contact_dict["distorCont"][0]["rpIndName"]
        distorCont_eMailAdd  = contact_dict["distorCont"][0]["eMailAdd"]
        distorCont_role      = contact_dict["distorCont"][0]["role"]

        srcCitatn_rpIndName = contact_dict["srcCitatn"][0]["rpIndName"]
        srcCitatn_eMailAdd  = contact_dict["srcCitatn"][0]["eMailAdd"]
        srcCitatn_role      = contact_dict["srcCitatn"][0]["role"]

        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        #print(etree.tostring(target_root, encoding='UTF-8', method='xml', pretty_print=True).decode())

        dataset_md = md.Metadata(dataset_path)
        dataset_md.synchronize("ALWAYS")
        dataset_md.save()
        dataset_md.reload()
        dataset_md_xml = dataset_md.xml
        del dataset_md

        # Parse the XML
        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
        target_tree = etree.parse(StringIO(dataset_md_xml), parser=parser)
        target_root = target_tree.getroot()
        del parser, dataset_md_xml

        CreaDate = target_root.xpath(f"//Esri/CreaDate")[0].text
        CreaTime = target_root.xpath(f"//Esri/CreaTime")[0].text
        #print(CreaDate, CreaTime)
        CreaDateTime = f"{CreaDate[:4]}-{CreaDate[4:6]}-{CreaDate[6:]}T{CreaTime[:2]}:{CreaTime[2:4]}:{CreaTime[4:6]}"
        #print(f"\tCreaDateTime: {CreaDateTime}")
        #del CreaDateTime
        del CreaDate, CreaTime
        ModDate = target_root.xpath(f"//Esri/ModDate")[0].text
        ModTime = target_root.xpath(f"//Esri/ModTime")[0].text
        #print(ModDate, ModTime)
        ModDateTime = f"{ModDate[:4]}-{ModDate[4:6]}-{ModDate[6:]}T{ModTime[:2]}:{ModTime[2:4]}:{ModTime[4:6]}"
        #print(f"\tModDateTime: {ModDateTime}")
        #del ModDateTime
        del ModDate, ModTime

        dataset_name = os.path.basename(dataset_path)
        print(f"Processing/Updating elements for dataset: '{dataset_name}'")

        xml_file = b'''<?xml version='1.0' encoding='UTF-8'?>
                        <metadata xml:lang="en">
                            <Esri>
                                <ArcGISstyle>ISO 19139 Metadata Implementation Specification GML3.2</ArcGISstyle>
                                <ArcGISProfile>ISO19139</ArcGISProfile>
                            </Esri>
                            <dataIdInfo>
                                <envirDesc Sync="TRUE">Esri ArcGIS 13.1.0.41833</envirDesc>
                                <idCitation>
                                    <resTitle>feature class name</resTitle>
                                    <resAltTitle>feature class name</resAltTitle>
                                    <collTitle>NMFS ESA Range Geodatabase 2024</collTitle>
                                    <presForm>
                                        <PresFormCd value="005" Sync="TRUE"></PresFormCd>
                                        <fgdcGeoform>vector digital data</fgdcGeoform>
                                    </presForm>
                                    <date>
                                        <createDate/>
                                        <pubDate/>
                                        <reviseDate/>
                                    </date>
                                    <citRespParty>
                                        <editorSource>external</editorSource>
                                        <editorDigest>9cc0fe80de5687cc4d79f50f3a254f2c3ceb08ce</editorDigest>
                                        <rpIndName>Nikki Wildart</rpIndName>
                                        <rpOrgName>Office of Protected Resources, National Marine Fisheries Service</rpOrgName>
                                        <rpPosName>Biologist</rpPosName>
                                        <rpCntInfo>
                                            <cntAddress addressType="both">
                                                <delPoint>1315 East West Highway</delPoint>
                                                <city>Silver Spring</city>
                                                <adminArea>MD</adminArea>
                                                <postCode>20910</postCode>
                                                <eMailAdd>nikki.wildart@noaa.gov</eMailAdd>
                                                <country>US</country>
                                            </cntAddress>
                                            <cntPhone>
                                                <voiceNum tddtty="">(301) 427-8443</voiceNum>
                                                <faxNum>(301) 427-8443</faxNum>
                                            </cntPhone>
                                            <cntHours>0700 - 1800 EST/EDT</cntHours>
                                            <cntOnlineRes>
                                                <linkage>https://www.fisheries.noaa.gov/about/office-protected-resources</linkage>
                                                <orName>NMFS Office of Protected Resources</orName>
                                                <orDesc>NOAA Fisheries Office of Protected Resources</orDesc>
                                                <orFunct>
                                                    <OnFunctCd value="002"></OnFunctCd>
                                                </orFunct>
                                            </cntOnlineRes>
                                        </rpCntInfo>
                                        <editorSave>True</editorSave>
                                        <displayName>Nikki Wildart</displayName>
                                        <role>
                                            <RoleCd value="002"></RoleCd>
                                        </role>
                                    </citRespParty>
                                </idCitation>
                                <searchKeys>
                                    <keyword>ESA</keyword>
                                </searchKeys>
                                <idAbs>This range includes [all; marine; freshwater; adult; immature/juvenile; larval] life stages of the species [add any caveats, e.g., why something is not included]. The range was based on the following [tracking, tagging, bycatch, and sighting] data: [Provide data and citations used to create range, including name/version/date of shoreline data.] Disclaimer: The spatial data provided here display an approximate distribution of the listed entity based on the best available information at the time of creation; they should not be conflated with the definitive range of the listed entity under the ESA. As such, the distribution of the listed entity may not be exclusively limited to the range identified herein, and we have not verified the listed entity's occurrence in every area comprising the range. Please notify us if you have recent information that is not reflected in our data (see Citation contacts). Use of these data do not replace the ESA section 7 consultation process; however, these data may be a first step in determining whether a proposed federal action overlaps with listed specie's ranges or critical habitat.</idAbs>
                                <discKeys>
                                    <keyword>species name</keyword>
                                    <thesaName>
                                        <resTitle>Integrated Taxonomic Information System (ITIS)</resTitle>
                                        <date>
                                            <createDate/>
                                            <pubDate/>
                                            <reviseDate/>
                                        </date>
                                        <citOnlineRes>
                                            <linkage>https://www.itits.org</linkage>
                                            <protocol>REST Service</protocol>
                                            <orName>ITIS</orName>
                                            <orDesc>Integrated Taxonomic Information System (ITIS)</orDesc>
                                            <orFunct>
                                                <OnFunctCd value="002"/>
                                            </orFunct>
                                        </citOnlineRes>
                                    </thesaName>
                                </discKeys>
                                <themeKeys xmlns="">
                                     <keyword>ESA</keyword>
                                     <thesaName>
                                        <resTitle>Global Change Master Directory (GCMD) Science Keywords</resTitle>
                                        <date>
                                            <createDate/>
                                            <pubDate/>
                                            <reviseDate/>
                                        </date>
                                        <citOnlineRes>
                                            <linkage>https://www.fisheries.noaa.gov/inport/help/components/keywords</linkage>
                                            <protocol>REST Service</protocol>
                                            <orName>GCMD</orName>
                                            <orDesc>Global Change Master Directory (GCMD) Science Keywords</orDesc>
                                            <orFunct>
                                                <OnFunctCd value="002"/>
                                            </orFunct>
                                        </citOnlineRes>
                                     </thesaName>
                                     <thesaLang>
                                        <languageCode value="eng"/>
                                        <countryCode value="US"/>
                                     </thesaLang>
                                </themeKeys>
                                <placeKeys xmlns="">
                                     <keyword></keyword>
                                     <thesaName>
                                        <resTitle>Global Change Master Directory (GCMD) Location Keywords</resTitle>
                                        <date>
                                            <createDate></createDate>
                                            <pubDate></pubDate>
                                            <reviseDate></reviseDate>
                                        </date>
                                        <citOnlineRes>
                                            <linkage>https://www.fisheries.noaa.gov/inport/help/components/keywords</linkage>
                                            <protocol>REST Service</protocol>
                                            <orName></orName>
                                            <orDesc></orDesc>
                                            <orFunct>
                                                <OnFunctCd value="002"/>
                                            </orFunct>
                                        </citOnlineRes>
                                     </thesaName>
                                     <thesaLang>
                                        <languageCode value="eng"/>
                                        <countryCode value="US"/>
                                     </thesaLang>
                                </placeKeys>
                                <tempKeys xmlns="">
                                    <keyword>Multi-Year</keyword>
                                     <thesaName>
                                        <resTitle>Global Change Master Directory (GCMD) Temporal Data Resolution Keywords</resTitle>
                                        <date>
                                            <createDate></createDate>
                                            <pubDate></pubDate>
                                            <reviseDate/>
                                        </date>
                                        <citOnlineRes>
                                            <linkage>https://www.fisheries.noaa.gov/inport/help/components/keywords</linkage>
                                            <protocol>REST Service</protocol>
                                            <orName></orName>
                                            <orDesc></orDesc>
                                            <orFunct>
                                                <OnFunctCd value="002"/>
                                            </orFunct>
                                        </citOnlineRes>
                                     </thesaName>
                                     <thesaLang>
                                        <languageCode value="eng"/>
                                        <countryCode value="US"/>
                                     </thesaLang>
                                  </tempKeys>
                                <idPurp>This feature class depicts the entire range of the ENTER SPECIES NAME. All boundaries should be considered approximate and, as such, caution is warranted when using it for any other purpose (e.g., analyses).</idPurp>
                                <idCredit>NOAA Fisheries. 2024. Endangered Species Act Species Range Geodatabase. Silver Spring, MD: National Oceanic and Atmospheric Administration (NOAA), National Marine Fisheries Service (NMFS), Office of Protected Resources (OPR).</idCredit>
                                <idStatus>
                                    <ProgCd value="004"/>
                                </idStatus>
                                <idPoC>
                                    <editorSource>external</editorSource>
                                    <editorDigest>9cc0fe80de5687cc4d79f50f3a254f2c3ceb08ce</editorDigest>
                                    <rpIndName>Nikki Wildart</rpIndName>
                                    <rpOrgName>Office of Protected Resources, National Marine Fisheries Service</rpOrgName>
                                    <rpPosName>Biologist</rpPosName>
                                    <rpCntInfo>
                                        <cntAddress addressType="both">
                                            <delPoint>1315 East West Highway</delPoint>
                                            <city>Silver Spring</city>
                                            <adminArea>MD</adminArea>
                                            <postCode>20910</postCode>
                                            <eMailAdd>nikki.wildart@noaa.gov</eMailAdd>
                                            <country>US</country>
                                        </cntAddress>
                                        <cntPhone>
                                            <voiceNum tddtty="">(301) 427-8443</voiceNum>
                                            <faxNum>(301) 427-8443</faxNum>
                                        </cntPhone>
                                        <cntHours>0700 - 1800 EST/EDT</cntHours>
                                        <cntOnlineRes>
                                            <linkage>https://www.fisheries.noaa.gov/about/office-protected-resources</linkage>
                                            <orName>NMFS Office of Protected Resources</orName>
                                            <orDesc>NOAA Fisheries Office of Protected Resources</orDesc>
                                            <orFunct>
                                                <OnFunctCd value="002"></OnFunctCd>
                                            </orFunct>
                                        </cntOnlineRes>
                                    </rpCntInfo>
                                    <editorSave>True</editorSave>
                                    <displayName>Nikki Wildart</displayName>
                                    <role>
                                        <RoleCd value="007"></RoleCd>
                                    </role>
                                </idPoC>
                                <resConst>
                                    <Consts>
                                        <useLimit>*** Attribution *** Whenever NMFS material is reproduced and re-disseminated, we request that users attribute the material appropriately. Pursuant to 17 U.S. C. 403, parties who produce copyrighted works consisting predominantly of material created by the Federal Government are encouraged to provide notice with such work(s) identifying the U.S. Government material incorporated and stating that such material is not subject to copyright protection. Please cite the species range datasets as indicated in the metadata for each species, or if not indicated, as follows with the appropriate information substituted for all text in {CURLY BRACKETS}: NOAA Fisheries Service. Endangered Species Act Species Range Geodatabase. Silver Spring, MD: National Oceanic and Atmospheric Administration (NOAA), National Marine Fisheries Service (NMFS), Office of Protected Resources (OPR) [producer] {GEODATABASE PUBLICATION DATE}. {ADD URL}
                                        ***No Warranty*** The user assumes the entire risk related to its use of these data. NMFS is providing these data "as is," and NMFS disclaims any and all warranties, whether express or implied, including (without limitation) any implied warranties of merchantability or fitness for a particular purpose. No warranty expressed or implied is made regarding the accuracy or utility of the data on any other system or for general or scientific purposes, nor shall the act of distribution constitute any such warranty. It is strongly recommended that careful attention be paid to the contents of the metadata file associated with these data to evaluate dataset limitations, restrictions or intended use. In no event will NMFS be liable to you or to any third party for any direct, indirect, incidental, consequential, special or exemplary damages or lost profit resulting from any use or misuse of this data.
                                        *** Proper Usage *** The information on government servers are in the public domain, unless specifically annotated otherwise, and may be used freely by the public. Before using information obtained from this server, special attention should be given to the date and time of the data and products being displayed. This information shall not be modified in content and then presented as official government material. This dataset was created to generally represent our best professional judgment of the ranges of listed species based on the best available information at the time of publication, including: geographic factors, time of year, and the biology of each species. The dataset should not be used to infer information regarding the existence or details of other marine features or resources, including, but not limited to, navigable waters, coastlines, bathymetry, submerged features, or man-made structures. Users assume responsibility for determining the appropriate use of this dataset.
                                        *** Temporal Considerations *** Species' ranges are subject to change or modification. Generally, we become aware of these changes during the 5-year review of the species status, as required under the ESA. If changes to the range are deemed necessary, we will make such changes in the database, which will be archived and replaced by an updated version as soon as feasible. It is the user's responsibility to ensure the most recent species' range data are being used.
                                        *** Shorelines/Base Layers *** The accuracy of this dataset is dependent upon the accuracy and resolution of the datasets (e.g. shoreline, hydrography, bathymetry, shared administrative boundaries) used in the creation process. Source datasets used are specified in the metadata. These data sources were selected for their suitability to a broad audience, and may not be suitable for specific uses requiring higher-resolution information. Coastlines and water body boundaries change. Unless otherwise noted, where the National Hydrography Dataset or NOAA Medium Resolution Shoreline is used, assume the boundary reaches the most current river, estuary, or coastal shoreline delineation available.
                                        *** Data Limitations *** Our data may lack the spatial resolution to capture the entire range of a species, especially outside of a major waterway (e.g., in a very small tributary, or shallow area near a marsh). For section 7 consultations, we recommend that Federal action agencies request technical assistance to verify presence/absence of listed species within their action area.</useLimit>
                                    </Consts>
                                    <LegConsts>
                                        <accessConsts>
                                            <RestrictCd value="008"/>
                                        </accessConsts>
                                            <othConsts>Other Constraints</othConsts>
                                    </LegConsts>
                                    <SecConsts xmlns="">
                                        <class>
                                            <ClasscationCd value="001"/>
                                        </class>
                                        <classSys>FISMA Low</classSys>
                                    </SecConsts>
                                </resConst>
                                <resMaint>
                                    <maintFreq>
                                        <MaintFreqCd value="009"></MaintFreqCd>
                                    </maintFreq>
                                </resMaint>
                                <envirDesc Sync="TRUE"></envirDesc>
                                <dataLang>
                                    <languageCode value="eng" Sync="TRUE"></languageCode>
                                    <countryCode value="USA" Sync="TRUE"></countryCode>
                                </dataLang>
                                <dataChar>
                                    <CharSetCd value="004"></CharSetCd>
                                </dataChar>
                                <dataExt>
                                    <exDesc>[Location extent description]. The data represents an approximate distribution of the listed entity based on the best available information from [date of first source] to [date of final species expert review].</exDesc>
                                    <geoEle>
                                        <GeoBndBox esriExtentType="search">
                                            <exTypeCode Sync="TRUE">1</exTypeCode>
                                            <westBL Sync="TRUE">-179.999989</westBL>
                                            <eastBL Sync="TRUE">179.999989</eastBL>
                                            <northBL Sync="TRUE">78.378549</northBL>
                                            <southBL Sync="TRUE">-87.997582</southBL>
                                        </GeoBndBox>
                                    </geoEle>
                                    <tempEle>
                                        <TempExtent>
                                            <exTemp>
                                                <TM_Period Sync="TRUE">
                                                    <tmBegin></tmBegin>
                                                    <tmEnd></tmEnd>
                                                </TM_Period>
                                                <TM_Instant Sync="TRUE">
                                                    <tmPosition></tmPosition>
                                                </TM_Instant>
                                            </exTemp>
                                        </TempExtent>
                                    </tempEle>
                                </dataExt>
                                <spatRpType>
                                    <SpatRepTypCd value="001" Sync="TRUE"></SpatRepTypCd>
                                </spatRpType>
                                <tpCat Sync="TRUE"><TopicCatCd value="002"></TopicCatCd></tpCat>
                                <tpCat Sync="TRUE"><TopicCatCd value="007"></TopicCatCd></tpCat>
                                <tpCat Sync="TRUE"><TopicCatCd value="014"></TopicCatCd></tpCat>
                             </dataIdInfo>
                        <dqInfo>
                            <dqScope xmlns="">
                                <scpLvl>
                                    <ScopeCd value="005"></ScopeCd>
                                </scpLvl>
                                <scpLvlDesc xmlns="">
                                    <datasetSet>dataset</datasetSet>
                                </scpLvlDesc>
                            </dqScope>
                            <report type="DQConcConsis" dimension="horizontal">
                                <measDesc>Based on a review from species' experts, we determined that all necessary features were included in the species' range file.</measDesc>
                                 <measResult>
                                    <ConResult>
                                       <conSpec>
                                          <resTitle>NMFS ESA Range Geodatabase 2024</resTitle>
                                          <resAltTitle>NMFS ESA Range Geodatabase 2024</resAltTitle>
                                          <collTitle>NMFS ESA Range Geodatabase 2024</collTitle>
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
                                          <resTitle>NMFS ESA Range Geodatabase 2024</resTitle>
                                          <resAltTitle>NMFS ESA Range Geodatabase 2024</resAltTitle>
                                          <collTitle>NMFS ESA Range Geodatabase 2024</collTitle>
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
                                <statement>Update dataLineage statement</statement>
                                <dataSource type="">
                                    <srcDesc>Data Source Description</srcDesc>
                                    <srcMedName>
                                        <MedNameCd value="015"/>
                                    </srcMedName>
                                    <srcCitatn>
                                        <resTitle>NMFS ESA Range Geodatabase 2024</resTitle>
                                        <resAltTitle>NMFS ESA Range Geodatabase 2024</resAltTitle>
                                        <collTitle>NMFS ESA Range Geodatabase 2024</collTitle>
                                        <citOnlineRes>
                                            <linkage>https://www.fisheries.noaa.gov/about/office-protected-resources</linkage>
                                            <protocol>REST Service</protocol>
                                            <orName>NMFS Office of Protected Resources</orName>
                                            <orDesc>NOAA Fisheries Office of Protected Resources</orDesc>
                                            <orFunct>
                                                <OnFunctCd value="002" />
                                            </orFunct>
                                        </citOnlineRes>
                                        <date>
                                            <createDate></createDate>
                                            <pubDate></pubDate>
                                            <reviseDate></reviseDate>
                                        </date>
                                        <presForm>
                                            <fgdcGeoform>document</fgdcGeoform>
                                            <PresFormCd value="001"></PresFormCd>
                                        </presForm>
                                        <citRespParty>
                                            <editorSource>external</editorSource>
                                            <editorDigest>9cc0fe80de5687cc4d79f50f3a254f2c3ceb08ce</editorDigest>
                                            <rpIndName>Nikki Wildart</rpIndName>
                                            <rpOrgName>Office of Protected Resources, National Marine Fisheries Service</rpOrgName>
                                            <rpPosName>Biologist</rpPosName>
                                            <rpCntInfo>
                                                <cntAddress addressType="both">
                                                    <delPoint>1315 East West Highway</delPoint>
                                                    <city>Silver Spring</city>
                                                    <adminArea>MD</adminArea>
                                                    <postCode>20910</postCode>
                                                    <eMailAdd>nikki.wildart@noaa.gov</eMailAdd>
                                                    <country>US</country>
                                                </cntAddress>
                                                <cntPhone>
                                                    <voiceNum tddtty="">(301) 427-8443</voiceNum>
                                                    <faxNum>(301) 427-8443</faxNum>
                                                </cntPhone>
                                                <cntHours>0700 - 1800 EST/EDT</cntHours>
                                                <cntOnlineRes>
                                                    <linkage>https://www.fisheries.noaa.gov/about/office-protected-resources</linkage>
                                                    <orName>NMFS Office of Protected Resources</orName>
                                                    <orDesc>NOAA Fisheries Office of Protected Resources</orDesc>
                                                    <orFunct>
                                                        <OnFunctCd value="002"></OnFunctCd>
                                                    </orFunct>
                                                </cntOnlineRes>
                                            </rpCntInfo>
                                            <editorSave>True</editorSave>
                                            <displayName>Nikki Wildart</displayName>
                                            <role>
                                                <RoleCd value="002"></RoleCd>
                                            </role>
                                        </citRespParty>
                                    </srcCitatn>
                                </dataSource>
                                <prcStep>
                                    <stepDesc>Create feature class from template polygon range</stepDesc>
                                    <stepDateTm></stepDateTm>
                                    <stepProc>
                                        <editorSource>external</editorSource>
                                        <editorDigest>9cc0fe80de5687cc4d79f50f3a254f2c3ceb08ce</editorDigest>
                                        <rpIndName>Nikki Wildart</rpIndName>
                                        <rpOrgName>Office of Protected Resources, National Marine Fisheries Service</rpOrgName>
                                        <rpPosName>Biologist</rpPosName>
                                        <rpCntInfo>
                                            <cntAddress addressType="both">
                                                <delPoint>1315 East West Highway</delPoint>
                                                <city>Silver Spring</city>
                                                <adminArea>MD</adminArea>
                                                <postCode>20910</postCode>
                                                <eMailAdd>nikki.wildart@noaa.gov</eMailAdd>
                                                <country>US</country>
                                            </cntAddress>
                                            <cntPhone>
                                                <voiceNum tddtty="">(301) 427-8443</voiceNum>
                                                <faxNum>(301) 427-8443</faxNum>
                                            </cntPhone>
                                            <cntHours>0700 - 1800 EST/EDT</cntHours>
                                            <cntOnlineRes>
                                                <linkage>https://www.fisheries.noaa.gov/about/office-protected-resources</linkage>
                                                <orName>NMFS Office of Protected Resources</orName>
                                                <orDesc>NOAA Fisheries Office of Protected Resources</orDesc>
                                                <orFunct>
                                                    <OnFunctCd value="002"></OnFunctCd>
                                                </orFunct>
                                            </cntOnlineRes>
                                        </rpCntInfo>
                                        <editorSave>True</editorSave>
                                        <displayName>Nikki Wildart</displayName>
                                        <role>
                                            <RoleCd value="009"></RoleCd>
                                        </role>
                                    </stepProc>
                                    <stepSrc type="used">
                                        <srcDesc>NMFS ESA Range Geodatabase 2024</srcDesc>
                                        <srcMedName><MedNameCd value="015"/></srcMedName>
                                        <srcCitatn></srcCitatn>
                                    </stepSrc>
                                </prcStep>
                                <prcStep>
                                    <stepDesc>Update Metadata 2025</stepDesc>
                                    <stepDateTm></stepDateTm>
                                    <stepProc>
                                        <editorSource>external</editorSource>
                                        <editorDigest>9cc0fe80de5687cc4d79f50f3a254f2c3ceb08ce</editorDigest>
                                        <rpIndName>Nikki Wildart</rpIndName>
                                        <rpOrgName>Office of Protected Resources, National Marine Fisheries Service</rpOrgName>
                                        <rpPosName>Biologist</rpPosName>
                                        <rpCntInfo>
                                            <cntAddress addressType="both">
                                                <delPoint>1315 East West Highway</delPoint>
                                                <city>Silver Spring</city>
                                                <adminArea>MD</adminArea>
                                                <postCode>20910</postCode>
                                                <eMailAdd>nikki.wildart@noaa.gov</eMailAdd>
                                                <country>US</country>
                                            </cntAddress>
                                            <cntPhone>
                                                <voiceNum tddtty="">(301) 427-8443</voiceNum>
                                                <faxNum>(301) 427-8443</faxNum>
                                            </cntPhone>
                                            <cntHours>0700 - 1800 EST/EDT</cntHours>
                                            <cntOnlineRes>
                                                <linkage>https://www.fisheries.noaa.gov/about/office-protected-resources</linkage>
                                                <orName>NMFS Office of Protected Resources</orName>
                                                <orDesc>NOAA Fisheries Office of Protected Resources</orDesc>
                                                <orFunct>
                                                    <OnFunctCd value="002"></OnFunctCd>
                                                </orFunct>
                                            </cntOnlineRes>
                                        </rpCntInfo>
                                        <editorSave>True</editorSave>
                                        <displayName>Nikki Wildart</displayName>
                                        <role>
                                            <RoleCd value="009"></RoleCd>
                                        </role>
                                    </stepProc>
                                    <stepSrc type="used">
                                        <srcDesc>NMFS ESA Range Geodatabase 2024</srcDesc>
                                        <srcMedName><MedNameCd value="015"/></srcMedName>
                                        <srcCitatn>
                                        </srcCitatn>
                                    </stepSrc>
                                </prcStep>
                            </dataLineage>
                        </dqInfo>
                            <distInfo>
                                <distFormat>
                                    <formatName Sync="TRUE">ESRI File Geodatabase</formatName>
                                    <formatVer>po r </formatVer>
                                    <fileDecmTech>Compressed</fileDecmTech>
                                    <formatInfo>NMFS ESA Range Geodatabase 2024</formatInfo>
                                </distFormat>
                                <distributor>
                                    <distorCont>
                                        <editorSource>external</editorSource>
                                        <editorDigest>d6865ab3a834719aef999600529568de978609bf</editorDigest>
                                        <rpIndName>NMFS Office of Protected Resources</rpIndName>
                                        <rpOrgName>Office of Protected Resources, National Marine Fisheries Service</rpOrgName>
                                        <rpPosName>Biologist</rpPosName>
                                        <rpCntInfo>
                                            <cntAddress addressType="both">
                                                <delPoint>1315 East West Highway</delPoint>
                                                <city>Silver Spring</city>
                                                <adminArea>MD</adminArea>
                                                <postCode>20910</postCode>
                                                <eMailAdd>nikki.wildart@noaa.gov</eMailAdd>
                                                <country>US</country>
                                            </cntAddress>
                                            <cntPhone>
                                                <voiceNum tddtty="">(301) 427-8443</voiceNum>
                                                <faxNum>(301) 427-8443</faxNum>
                                            </cntPhone>
                                            <cntHours>0700 - 1800 EST/EDT</cntHours>
                                            <cntOnlineRes>
                                                <linkage>https://www.fisheries.noaa.gov/about/office-protected-resources</linkage>
                                                <orName>NMFS Office of Protected Resources</orName>
                                                <orDesc>NOAA Fisheries Office of Protected Resources</orDesc>
                                                <orFunct>
                                                    <OnFunctCd value="002"></OnFunctCd>
                                                </orFunct>
                                            </cntOnlineRes>
                                        </rpCntInfo>
                                        <editorSave>True</editorSave>
                                        <displayName>NMFS Office of Protected Resources</displayName>
                                        <role>
                                            <RoleCd value="005"></RoleCd>
                                        </role>
                                    </distorCont>
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
                                    <distorTran xmlns="">
                                        <onLineSrc xmlns="">
                                            <linkage>https://services2.arcgis.com/C8EMgrsFcRFL6LrL/arcgis/rest/services/.../FeatureServer</linkage>
                                            <protocol>ESRI REST Service</protocol>
                                            <orName>Dataset</orName>
                                            <orDesc>Dataset Feature Service</orDesc>
                                            <orFunct>
                                               <OnFunctCd value="002"/>
                                            </orFunct>
                                        </onLineSrc>
                                    </distorTran>
                                </distributor>
                            </distInfo>
                    </metadata>
                     '''

        source_tree = etree.parse(BytesIO(xml_file), etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
        source_root = source_tree.getroot()

        # Merge Target wtih Source
        target_source_merge = xml_tree_merge(target_root, source_root)
        #print(etree.tostring(target_source_merge, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
        # Merge Source wtih Target
        source_target_merge = xml_tree_merge(target_source_merge, target_root)

        del target_source_merge
        del source_tree, source_root, xml_file

        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        #
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        dataset_md_xml = etree.tostring(source_target_merge, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=False)

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
        del source_target_merge

        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        #
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

        dataset_md = md.Metadata(dataset_path)
        dataset_md.synchronize("ALWAYS")
        dataset_md.save()
        dataset_md.reload()
        dataset_md_xml = dataset_md.xml
        del dataset_md

        # Parse the XML
        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
        target_tree = etree.parse(StringIO(dataset_md_xml), parser=parser)
        target_root = target_tree.getroot()
        del parser, dataset_md_xml

        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # discKeys, themeKeys, placeKeys, tempKeys
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # discKeys
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        keywords = target_root.xpath("//dataIdInfo/discKeys/keyword")
        if keywords is not None and len(keywords) and len(keywords[0]) == 0:
            new_item_name = target_root.find("./Esri/DataProperties/itemProps/itemName").text
            keyword = target_root.xpath("//dataIdInfo/discKeys/keyword")[0]
            keyword.text = f"Enter scientific keywords for {new_item_name}, separated by a semicolon"
            del keyword, new_item_name
        elif keywords is not None and len(keywords) and len(keywords[0]) >= 1:
            pass
        del keywords
        createDate = target_root.xpath("//dataIdInfo/discKeys/thesaName/date/createDate")
        if createDate is not None and len(createDate) and len(createDate[0]) == 0:
            target_root.xpath("//dataIdInfo/discKeys/thesaName/date/createDate")[0].text = CreaDateTime
        elif createDate is not None and len(createDate) and len(createDate[0]) == 1:
            pass
        else:
            pass
        del createDate
        pubDate    = target_root.xpath("//dataIdInfo/discKeys/thesaName/date/pubDate")
        if pubDate is not None and len(pubDate) and len(pubDate[0]) == 0:
            target_root.xpath("//dataIdInfo/discKeys/thesaName/date/pubDate")[0].text = CreaDateTime
        elif pubDate is not None and len(pubDate) and len(pubDate[0]) == 1:
            pass
        else:
            pass
        del pubDate
        reviseDate = target_root.xpath("//dataIdInfo/discKeys/thesaName/date/reviseDate")
        if reviseDate is not None and len(reviseDate) and len(reviseDate[0]) == 0:
            target_root.xpath("//dataIdInfo/discKeys/thesaName/date/reviseDate")[0].text = ModDateTime
        elif reviseDate is not None and len(reviseDate) and len(reviseDate[0]) == 1:
            pass
        else:
            pass
        del reviseDate
        resTitle = target_root.xpath("//dataIdInfo/discKeys/thesaName/resTitle")
        if resTitle is not None and len(resTitle) and len(resTitle[0]) == 0:
            target_root.xpath("//dataIdInfo/discKeys/thesaName/resTitle")[0].text = "Integrated Taxonomic Information System (ITIS)"
        elif resTitle is not None and len(resTitle) and len(resTitle[0]) == 1:
            pass
        else:
            pass
        del resTitle
        discKeys = target_root.xpath("//dataIdInfo/discKeys")
        for i in range(0, len(discKeys)):
            #print(etree.tostring(discKeys[i], encoding='UTF-8', method='xml', pretty_print=True).decode())
            del i
        del discKeys
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # themeKeys
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        keywords = target_root.xpath("//dataIdInfo/themeKeys/keyword")
        if keywords is not None and len(keywords) and len(keywords[0]) == 0:
            new_item_name = target_root.find("./Esri/DataProperties/itemProps/itemName").text
            keyword = target_root.xpath("//dataIdInfo/themeKeys/keyword")[0]
            keyword.text = f"Enter theme keywords, that do not fit elsewhere, for {new_item_name}, separated by a semicolon"
            del keyword, new_item_name
        elif keywords is not None and len(keywords) and len(keywords[0]) >= 1:
            pass
        del keywords
        createDate = target_root.xpath("//dataIdInfo/themeKeys/thesaName/date/createDate")
        if createDate is not None and len(createDate) and len(createDate[0]) == 0:
            target_root.xpath("//dataIdInfo/themeKeys/thesaName/date/createDate")[0].text = CreaDateTime
        elif createDate is not None and len(createDate) and len(createDate[0]) == 1:
            pass
        else:
            pass
        del createDate
        pubDate    = target_root.xpath("//dataIdInfo/themeKeys/thesaName/date/pubDate")
        if pubDate is not None and len(pubDate) and len(pubDate[0]) == 0:
            target_root.xpath("//dataIdInfo/themeKeys/thesaName/date/pubDate")[0].text = CreaDateTime
        elif pubDate is not None and len(pubDate) and len(pubDate[0]) == 1:
            pass
        else:
            pass
        del pubDate
        reviseDate = target_root.xpath("//dataIdInfo/themeKeys/thesaName/date/reviseDate")
        if reviseDate is not None and len(reviseDate) and len(reviseDate[0]) == 0:
            target_root.xpath("//dataIdInfo/themeKeys/thesaName/date/reviseDate")[0].text = ModDateTime
        elif reviseDate is not None and len(reviseDate) and len(reviseDate[0]) == 1:
            pass
        else:
            pass
        del reviseDate
        resTitle = target_root.xpath("//dataIdInfo/themeKeys/thesaName/resTitle")
        if resTitle is not None and len(resTitle) and len(resTitle[0]) == 0:
            target_root.xpath("//dataIdInfo/themeKeys/thesaName/resTitle")[0].text = "Global Change Master Directory (GCMD) Science Keyword"
        elif resTitle is not None and len(resTitle) and len(resTitle[0]) == 1:
            pass
        else:
            pass
        del resTitle
        themeKeys = target_root.xpath("//dataIdInfo/themeKeys")
        for i in range(0, len(themeKeys)):
            #print(etree.tostring(themeKeys[i], encoding='UTF-8', method='xml', pretty_print=True).decode())
            del i
        del themeKeys
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # placeKeys
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        keywords = target_root.xpath("//dataIdInfo/placeKeys/keyword")
        if keywords is not None and len(keywords) and len(keywords[0]) == 0:
            new_item_name = target_root.find("./Esri/DataProperties/itemProps/itemName").text
            keyword = target_root.xpath("//dataIdInfo/placeKeys/keyword")[0]
            keyword.text = f"Enter place/geography keywords for {new_item_name}, separated by a semicolon"
            del keyword, new_item_name
        elif keywords is not None and len(keywords) and len(keywords[0]) >= 1:
            pass
        del keywords
        createDate = target_root.xpath("//dataIdInfo/placeKeys/thesaName/date/createDate")
        if createDate is not None and len(createDate) and len(createDate[0]) == 0:
            target_root.xpath("//dataIdInfo/placeKeys/thesaName/date/createDate")[0].text = CreaDateTime
        elif createDate is not None and len(createDate) and len(createDate[0]) == 1:
            pass
        else:
            pass
        del createDate
        pubDate = target_root.xpath("//dataIdInfo/placeKeys/thesaName/date/pubDate")
        if pubDate is not None and len(pubDate) and len(pubDate[0]) == 0:
            target_root.xpath("//dataIdInfo/placeKeys/thesaName/date/pubDate")[0].text = CreaDateTime
        elif pubDate is not None and len(pubDate) and len(pubDate[0]) == 1:
            pass
        else:
            pass
        del pubDate
        reviseDate = target_root.xpath("//dataIdInfo/placeKeys/thesaName/date/reviseDate")
        if reviseDate is not None and len(reviseDate) and len(reviseDate[0]) == 0:
            target_root.xpath("//dataIdInfo/placeKeys/thesaName/date/reviseDate")[0].text = ModDateTime
        elif reviseDate is not None and len(reviseDate) and len(reviseDate[0]) == 1:
            pass
        else:
            pass
        del reviseDate
        resTitle = target_root.xpath("//dataIdInfo/placeKeys/thesaName/resTitle")
        if resTitle is not None and len(resTitle) and len(resTitle[0]) == 0:
            target_root.xpath("//dataIdInfo/placeKeys/thesaName/resTitle")[0].text = "Global Change Master Directory (GCMD) Location Keywords"
        elif resTitle is not None and len(resTitle) and len(resTitle[0]) == 1:
            pass
        else:
            pass
        del resTitle
        placeKeys = target_root.xpath("//dataIdInfo/placeKeys")
        for i in range(0, len(placeKeys)):
            #print(etree.tostring(placeKeys[i], encoding='UTF-8', method='xml', pretty_print=True).decode())
            del i
        del placeKeys
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # tempKeys
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        keywords = target_root.xpath("//dataIdInfo/tempKeys/keyword")
        if keywords is not None and len(keywords) and len(keywords[0]) == 0:
            new_item_name = target_root.find("./Esri/DataProperties/itemProps/itemName").text
            keyword = target_root.xpath("//dataIdInfo/tempKeys/keyword")[0]
            keyword.text = f"Enter temporal keywords (e.g. year, year range, season, etc.) for {new_item_name}, separated by a semicolon"
            del keyword, new_item_name
        elif keywords is not None and len(keywords) and len(keywords[0]) >= 1:
            pass
        del keywords
        createDate = target_root.xpath("//dataIdInfo/tempKeys/thesaName/date/createDate")
        if createDate is not None and len(createDate) and len(createDate[0]) == 0:
            target_root.xpath("//dataIdInfo/tempKeys/thesaName/date/createDate")[0].text = CreaDateTime
        elif createDate is not None and len(createDate) and len(createDate[0]) == 1:
            pass
        else:
            pass
        del createDate
        pubDate = target_root.xpath("//dataIdInfo/tempKeys/thesaName/date/pubDate")
        if pubDate is not None and len(pubDate) and len(pubDate[0]) == 0:
            target_root.xpath("//dataIdInfo/tempKeys/thesaName/date/pubDate")[0].text = CreaDateTime
        elif pubDate is not None and len(pubDate) and len(pubDate[0]) == 1:
            pass
        else:
            pass
        del pubDate
        reviseDate = target_root.xpath("//dataIdInfo/tempKeys/thesaName/date/reviseDate")
        if reviseDate is not None and len(reviseDate) and len(reviseDate[0]) == 0:
            target_root.xpath("//dataIdInfo/tempKeys/thesaName/date/reviseDate")[0].text = ModDateTime
        elif reviseDate is not None and len(reviseDate) and len(reviseDate[0]) == 1:
            pass
        else:
            pass
        del reviseDate
        resTitle = target_root.xpath("//dataIdInfo/tempKeys/thesaName/resTitle")
        if resTitle is not None and len(resTitle) and len(resTitle[0]) == 0:
            target_root.xpath("//dataIdInfo/tempKeys/thesaName/resTitle")[0].text = "Global Change Master Directory (GCMD) Temporal Data Resolution Keywords"
        elif resTitle is not None and len(resTitle) and len(resTitle[0]) == 1:
            pass
        else:
            pass
        del resTitle
        tempKeys = target_root.xpath("//dataIdInfo/tempKeys")
        for i in range(0, len(tempKeys)):
            #print(etree.tostring(tempKeys[i], encoding='UTF-8', method='xml', pretty_print=True).decode())
            del i
        del tempKeys
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # Data Extent
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        dataExt = target_root.xpath("//dataIdInfo/dataExt")[0]
        exDesc = dataExt.xpath("//exDesc")
        if len(exDesc) == 0:
            _xml = "<exDesc>The geographic and temporal extent of the dataset are listed below.</exDesc>"
            _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
            dataExt.insert(0, _root)
            del _root, _xml
        del exDesc
        tempEle = dataExt.xpath("//tempEle")
        if len(tempEle) == 0:
            _xml = f'<tempEle><TempExtent><exTemp><TM_Period Sync="TRUE"> \
                     <tmBegin>{CreaDateTime}</tmBegin><tmEnd>{ModDateTime}</tmEnd></TM_Period><TM_Instant Sync="TRUE"> \
                     <tmPosition>{ModDateTime}</tmPosition></TM_Instant></exTemp></TempExtent></tempEle>'
            _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
            dataExt.insert(2, _root)
            del _root, _xml
        elif len(tempEle) == 1:
            _xml = f'<tempEle><TempExtent><exTemp><TM_Period Sync="TRUE"> \
                     <tmBegin>{CreaDateTime}</tmBegin><tmEnd>{ModDateTime}</tmEnd></TM_Period><TM_Instant Sync="TRUE"> \
                     <tmPosition>{ModDateTime}</tmPosition></TM_Instant></exTemp></TempExtent></tempEle>'
            _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
            tempEle[0].getparent().replace(tempEle[0], _root)
            del _root, _xml
        del tempEle
        del dataExt
        dataExt = target_root.xpath("//dataIdInfo/dataExt")
        for i in range(1, len(dataExt)):
            #print(etree.tostring(dataExt[i], encoding='UTF-8', method='xml', pretty_print=True).decode())
            del i
        del dataExt
        dataExt = target_root.xpath("//dataIdInfo/dataExt")
        for i in range(1, len(dataExt)):
            dataExt[i].getparent().remove(dataExt[i])
            del i
        del dataExt
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        PresFormCd   = target_root.xpath("/metadata/dataIdInfo/idCitation/presForm/PresFormCd")[0]
        fgdcGeoform  = target_root.xpath("/metadata/dataIdInfo/idCitation/presForm/fgdcGeoform")[0]
        SpatRepTypCd = target_root.xpath("/metadata/dataIdInfo/spatRpType/SpatRepTypCd")[0]
        datasetSet   = target_root.xpath("/metadata/dqInfo/dqScope/scpLvlDesc/datasetSet")[0]
        target_root.xpath("/metadata/dqInfo/dqScope/scpLvl/ScopeCd")[0].set('value', "005")
        if PresFormCd.get("value") == "005" and SpatRepTypCd.get("value") == "001":
            fgdcGeoform.text = "Vector Digital Data"
            datasetSet.text  = "Vector Digital Data"
        elif PresFormCd.get("value") == "011" and SpatRepTypCd.get("value") == "002":
            fgdcGeoform.text = "Raster Digital Data"
            datasetSet.text  = "Raster Digital Data"
        elif PresFormCd.get("value") == "011" and SpatRepTypCd.get("value") == "003":
            fgdcGeoform.text = "Tabular Digital Data"
            datasetSet.text  = "Tabular Digital Data"
        else:
            pass
        del datasetSet, SpatRepTypCd, fgdcGeoform, PresFormCd
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        mdFileID = target_root.xpath(f"//mdFileID")
        if mdFileID is not None and len(mdFileID) == 0:
            _xml = '<mdFileID>gov.noaa.nmfs.inport:</mdFileID>'
            _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
            target_root.insert(root_dict['mdFileID'], _root)
            del _root, _xml
        elif mdFileID is not None and len(mdFileID) and len(mdFileID[0]) == 0:
            mdFileID[0].text = "gov.noaa.nmfs.inport:"
        elif mdFileID is not None and len(mdFileID) and len(mdFileID[0]) == 1:
            pass
        #print(mdFileID[0].text)
        del mdFileID
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        mdMaint = target_root.xpath(f"//mdMaint")
        if mdMaint is not None and len(mdMaint) == 0:
            _xml = '<mdMaint><maintFreq><MaintFreqCd value="009"></MaintFreqCd></maintFreq></mdMaint>'
            _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
            target_root.insert(root_dict['mdMaint'], _root)
            del _root, _xml
        elif mdMaint is not None and len(mdMaint) and len(mdMaint[0]) == 0:
            target_root.xpath("/metadata/mdMaint/maintFreq/MaintFreqCd")[0].attrib["value"] = "009"
        elif mdMaint is not None and len(mdMaint) and len(mdMaint[0]) == 1:
            pass #print(etree.tostring(mdMaint[0], encoding='UTF-8', method='xml', pretty_print=True).decode())
        del mdMaint
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        distInfo = target_root.xpath("./distInfo")[0]
        #print(etree.tostring(distInfo, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
        _xml = b'''<distInfo>
                    <distFormat>
                        <formatName Sync="TRUE">ESRI File Geodatabase</formatName>
                        <formatVer>po r </formatVer>
                        <fileDecmTech>Compressed</fileDecmTech>
                        <formatInfo>NMFS ESA Range Geodatabase 2024</formatInfo>
                    </distFormat>
                    <distributor>
                        <distorCont>
                            <editorSource>external</editorSource>
                            <editorDigest>d6865ab3a834719aef999600529568de978609bf</editorDigest>
                            <rpIndName>NMFS Office of Protected Resources</rpIndName>
                            <rpOrgName>NMFS Office of Protected Resources</rpOrgName>
                            <rpPosName>Biologist</rpPosName>
                            <rpCntInfo>
                                <cntAddress addressType="both">
                                    <delPoint>1315 East West Highway</delPoint>
                                    <city>Silver Spring</city>
                                    <adminArea>MD</adminArea>
                                    <postCode>20910</postCode>
                                    <eMailAdd>nikki.wildart@noaa.gov</eMailAdd>
                                    <country>US</country>
                                </cntAddress>
                                <cntPhone>
                                    <voiceNum tddtty="">(301) 427-8443</voiceNum>
                                    <faxNum>(301) 427-8443</faxNum>
                                </cntPhone>
                                <cntHours>0700 - 1800 EST/EDT</cntHours>
                                <cntOnlineRes>
                                    <linkage>https://www.fisheries.noaa.gov/about/office-protected-resources</linkage>
                                    <orName>NMFS Office of Protected Resources</orName>
                                    <orDesc>NOAA Fisheries Office of Protected Resources</orDesc>
                                    <orFunct>
                                        <OnFunctCd value="002"></OnFunctCd>
                                    </orFunct>
                                </cntOnlineRes>
                            </rpCntInfo>
                            <editorSave>True</editorSave>
                            <displayName>NMFS Office of Protected Resources</displayName>
                            <role>
                                <RoleCd value="005"></RoleCd>
                            </role>
                        </distorCont>
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
                        <distorTran xmlns="">
                            <onLineSrc xmlns="">
                                <linkage>https://services2.arcgis.com/C8EMgrsFcRFL6LrL/arcgis/rest/services/.../FeatureServer</linkage>
                                <protocol>ESRI REST Service</protocol>
                                <orName>Dataset</orName>
                                <orDesc>Dataset Feature Service</orDesc>
                                <orFunct>
                                   <OnFunctCd value="002"/>
                                </orFunct>
                            </onLineSrc>
                        </distorTran>
                    </distributor>
                </distInfo>'''
        _tree = etree.parse(BytesIO(_xml), etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
        distInfo.getparent().replace(distInfo, _tree.getroot())
        distInfo = target_root.xpath("./distInfo")[0]
        #print(etree.tostring(distInfo, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
        del distInfo

        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # Main distFormat
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        formatName = target_root.xpath("./distInfo/distFormat/formatName")[0]
        formatVer = target_root.xpath("./distInfo/distFormat/formatVer")[0].text
        envirDesc = target_root.xpath("./dataIdInfo/envirDesc")[0]
        envirDesc.set('Sync', "TRUE")
                                                                # 001 = Grid
        '''<spatRpType>                                         # 002 = Grid
         <SpatRepTypCd value="003" Sync="TRUE"></SpatRepTypCd>  # 003 = Text Table
        </spatRpType>'''

        format_name_text = ""
        try:
            GeoObjTypCd = target_root.xpath("./spatRepInfo/VectSpatRep/geometObjs/geoObjTyp/GeoObjTypCd")[0].get("value")
            if GeoObjTypCd == "002":
               format_name_text = "ESRI File Geodatabase"
        except:
            format_name_text = "ESRI Geodatabase Table"
        del GeoObjTypCd
        formatName.text = format_name_text
        del format_name_text
        formatVer_text = str.rstrip(str.lstrip(envirDesc.text))
        formatVer = target_root.xpath("./distInfo/distFormat/formatVer")[0]
        formatVer.text = str.rstrip(str.lstrip(formatVer_text))
        del formatVer_text
        del envirDesc
        del formatVer
        del formatName
##        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
##        formatName = target_root.xpath("./distInfo/distributor/distFormat/formatName")[1]
##        formatVer = target_root.xpath("./distInfo/distributor/distFormat/formatVer")[1].text
##        envirDesc = target_root.xpath("./dataIdInfo/envirDesc")[0]
##        envirDesc.set('Sync', "TRUE")
##        GeoObjTypCd = target_root.xpath("./spatRepInfo/VectSpatRep/geometObjs/geoObjTyp/GeoObjTypCd")[0].get("value")
##        if GeoObjTypCd == "002":
##            formatName.text = "ESRI File Geodatabase"
##        del GeoObjTypCd
##        formatVer_text = str.rstrip(str.lstrip(envirDesc.text))
##        formatVer = target_root.xpath("./distInfo/distributor/distFormat/formatVer")[1]
##        formatVer.text = str.rstrip(str.lstrip(formatVer_text))
##        del formatVer_text
##        del envirDesc
##        del formatVer
##        del formatName
##        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
##        distFormat_0 = target_root.xpath("./distInfo[.//formatName/text()]")
##        for distFormat in distFormat_0:
##            #print(etree.tostring(distFormat, encoding='UTF-8', method='xml', pretty_print=True).decode())
##            del distFormat
##        del distFormat_0
##        distFormat_0 = target_root.xpath("./distInfo/distributor/distFormat")
##        for distFormat in distFormat_0:
##            #print(etree.tostring(distFormat, encoding='UTF-8', method='xml', pretty_print=True).decode())
##            del distFormat
##        del distFormat_0
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

        mdStanName = target_root.xpath("./mdStanName")
        for _mdStanName in mdStanName:
            _mdStanName.getparent().remove(_mdStanName)
            del _mdStanName
        del mdStanName

        mdStanVer = target_root.xpath("./mdStanVer")
        for _mdStanVer in mdStanVer:
            _mdStanVer.getparent().remove(_mdStanVer)
            del _mdStanVer
        del mdStanVer

        new_item_name = target_root.find("./Esri/DataProperties/itemProps/itemName").text
        onLineSrcs = target_root.findall("./distInfo/distributor/distorTran/onLineSrc")
        for onLineSrc in onLineSrcs:
            if onLineSrc.find('./protocol').text == "ESRI REST Service":
                old_linkage_element = onLineSrc.find('./linkage')
                old_linkage = old_linkage_element.text
                #print(old_linkage, flush=True)
                old_item_name = old_linkage[old_linkage.find("/services/")+len("/services/"):old_linkage.find("/FeatureServer")]
                new_linkage = old_linkage.replace(old_item_name, new_item_name)
                #print(new_linkage, flush=True)
                old_linkage_element.text = new_linkage
                #print(old_linkage_element.text, flush=True)
                del old_linkage_element
                del old_item_name, old_linkage, new_linkage
            del onLineSrc
        del onLineSrcs, new_item_name

##        statement = target_root.xpath("./dqInfo/dataLineage/statement")
##        if statement is not None and len(statement) == 0:
##            pass # Need to insert statement
##        elif statement is not None and len(statement) and len(statement[0]) == 0:
##            target_root.xpath("./dqInfo/dataLineage/statement")[0].text = "Need to update datalienage"
##        elif statement is not None and len(statement) and len(statement[0]) == 1:
##            pass
##        elif statement is not None and len(statement) and len(statement[0]) >= 1:
##            pass
##        else:
##            pass
##        #print(etree.tostring(target_root.xpath("./dqInfo/dataLineage/statement")[0], encoding='UTF-8', method='xml', pretty_print=True).decode())
##        del statement
##        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
##        # srcDesc
##        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
##        srcDesc = target_root.xpath("./dqInfo/dataLineage/dataSource/srcDesc")
##        if srcDesc is not None and len(srcDesc) == 0:
##            pass # Need to insert srcDesc
##        elif srcDesc is not None and len(srcDesc) and len(srcDesc[0]) == 0:
##            target_root.xpath("./dqInfo/dataLineage/dataSource/srcDesc")[0].text = "Need to update srcDesc"
##        elif srcDesc is not None and len(srcDesc) and len(srcDesc[0]) == 1:
##            pass
##        elif srcDesc is not None and len(srcDesc) and len(srcDesc[0]) >= 1:
##            pass
##        else:
##            pass
##        #print(etree.tostring(target_root.xpath("./dqInfo/dataLineage/dataSource")[0], encoding='UTF-8', method='xml', pretty_print=True).decode())
##        del srcDesc
##        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
##        # prcStep
##        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
##        prcStep = target_root.xpath("./dqInfo/dataLineage/prcStep")
##        if prcStep is not None and len(prcStep) == 0:
##            pass
##        elif prcStep is not None and len(prcStep) and len(prcStep[0]) == 0:
##            pass
##            #target_root.xpath("./dqInfo/dataLineage/prcStep")[0].text = "Need to update srcDesc"
##        elif prcStep is not None and len(prcStep) and len(prcStep[0]) == 1:
##            stepDesc = prcStep.xpath("./stepDesc")[0]
##            prcStep.insert(0, stepDesc)
##            del stepDesc
##            stepDateTm = prcStep.xpath("./stepDateTm")[0]
##            prcStep.insert(1, stepDateTm)
##            del stepDateTm
##        elif prcStep is not None and len(prcStep) and len(prcStep[0]) >= 1:
##            pass
##        else:
##            pass
##        #print(etree.tostring(target_root.xpath("./dqInfo/dataLineage/prcStep")[0], encoding='UTF-8', method='xml', pretty_print=True).decode())
##        del prcStep
##        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
##        # prcStep
##        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
##        stepProcs = target_root.xpath("./dqInfo/dataLineage/prcStep/stepProc")
##        if stepProcs is not None and len(stepProcs) == 0:
##            pass
##        elif stepProcs is not None and len(stepProcs) and len(stepProcs[0]) == 0:
##            pass
##        elif stepProcs is not None and len(stepProcs) and len(stepProcs[0]) == 1:
##            pass
##        elif stepProcs is not None and len(stepProcs) and len(stepProcs[0]) >= 1:
##            for stepProc in stepProcs:
##                if stepProc is not None and len(stepProc) == 0:
##                    target_root.xpath("./dqInfo/dataLineage/prcStep")[0].remove(stepProc)
##                elif stepProc is not None and len(stepProc) and len(stepProcs[0]) == 0:
##                    pass
##                elif stepProc is not None and len(stepProc) and len(stepProcs[0]) == 1:
##                    pass
##                elif stepProc is not None and len(stepProc) and len(stepProcs[0]) > 1:
##                    pass
##                else:
##                    pass
##            del stepProc
##        else:
##            pass
##        #print(etree.tostring(stepProcs[0].getparent(), encoding='UTF-8', method='xml', pretty_print=True).decode())
##        del stepProcs
##        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
##        # report
##        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
##        reports = target_root.xpath("./dqInfo/report")
##        if reports is not None and len(reports) == 0:
##            print(reports)
##        elif reports is not None and len(reports) and len(reports[0]) == 0:
##            print(reports)
##        elif reports is not None and len(reports) and len(reports[0]) == 1:
##            print(reports)
##        elif reports is not None and len(reports) and len(reports[0]) >= 1:
##            for i in range(0, len(reports)):
##                if reports[i] is not None and len(reports[i]) == 0:
##                    pass # target_root.xpath("./dqInfo/dataLineage/prcStep")[0].remove(stepProc)
##                elif reports[i] is not None and len(reports[i]) and len(reports[i]) == 0:
##                    pass # print(etree.tostring(reports[i], encoding='UTF-8', method='xml', pretty_print=True).decode())
##                elif reports[i] is not None and len(reports[i]) and len(reports[0]) == 1:
##                    pass # print(etree.tostring(reports[i], encoding='UTF-8', method='xml', pretty_print=True).decode())
##                elif reports[i] is not None and len(reports[i]) and len(reports[0]) > 1:
##                    createDate = target_root.xpath("./dqInfo/report/measResult/ConResult/conSpec/date/createDate")
##                    if createDate is not None and len(createDate) and len(createDate[0]) == 0:
##                        target_root.xpath("./dqInfo/report/measResult/ConResult/conSpec/date/createDate")[i].text = CreaDateTime
##                    elif createDate is not None and len(createDate) and len(createDate[0]) == 1:
##                        pass
##                    else:
##                        pass
##                    del createDate
##                    pubDate = target_root.xpath("./dqInfo/report/measResult/ConResult/conSpec/date/pubDate")
##                    if pubDate is not None and len(pubDate) and len(pubDate[0]) == 0:
##                        target_root.xpath("./dqInfo/report/measResult/ConResult/conSpec/date/pubDate")[i].text = CreaDateTime
##                    elif pubDate is not None and len(pubDate) and len(pubDate[0]) == 1:
##                        pass
##                    else:
##                        pass
##                    del pubDate
##                    reviseDate = target_root.xpath("./dqInfo/report/measResult/ConResult/conSpec/date/reviseDate")
##                    if reviseDate is not None and len(reviseDate) and len(reviseDate[0]) == 0:
##                        target_root.xpath("./dqInfo/report/measResult/ConResult/conSpec/date/reviseDate")[i].text = ModDateTime
##                    elif reviseDate is not None and len(reviseDate) and len(reviseDate[0]) == 1:
##                        pass
##                    else:
##                        pass
##                    del reviseDate
##                else:
##                    pass
##                del i
##        else:
##            pass
##        # print(etree.tostring(reports[0].getparent(), encoding='UTF-8', method='xml', pretty_print=True).decode())
##        del reports
##
##        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
##        # report
##        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
##        dataSources = target_root.xpath("./dqInfo/dataLineage/dataSource")
##        if dataSources is not None and len(dataSources) == 0:
##            print(dataSources)
##        elif dataSources is not None and len(dataSources) and len(dataSources[0]) == 0:
##            print(dataSources)
##        elif dataSources is not None and len(dataSources) and len(dataSources[0]) == 1:
##            print(dataSources)
##        elif dataSources is not None and len(dataSources) and len(dataSources[0]) >= 1:
##            for i in range(0, len(dataSources)):
##                if dataSources[i] is not None and len(dataSources[i]) == 0:
##                    pass # target_root.xpath("./dqInfo/dataLineage/prcStep")[0].remove(stepProc)
##                elif dataSources[i] is not None and len(dataSources[i]) and len(dataSources[i]) == 0:
##                    pass # print(etree.tostring(reports[i], encoding='UTF-8', method='xml', pretty_print=True).decode())
##                elif dataSources[i] is not None and len(dataSources[i]) and len(dataSources[i]) == 1:
##                    pass
##                    #print(etree.tostring(dataSources[i], encoding='UTF-8', method='xml', pretty_print=True).decode())
##                elif dataSources[i] is not None and len(dataSources[i]) and len(dataSources[i]) > 1:
##                    citRespParty = target_root.xpath("./dqInfo/dataLineage/dataSource/srcCitatn/citRespParty")
##                    if citRespParty is not None and len(citRespParty) == 0:
##                        pass
##                    elif citRespParty is not None and len(citRespParty) and len(citRespParty) == 0:
##                        pass # print(etree.tostring(reports[i], encoding='UTF-8', method='xml', pretty_print=True).decode())
##                    elif citRespParty is not None and len(citRespParty) and len(citRespParty) == 1:
##                        new_contact_tree = contacts_xml_tree.xpath(f"//contact[./rpIndName[text()='{citRespParty_rpIndName}'] and ./rpCntInfo/cntAddress/eMailAdd[text()='{citRespParty_eMailAdd}'] and ./editorSave[text()='True']]")
##                        new_contact = copy.deepcopy(new_contact_tree[0])
##                        new_contact.tag = "citRespParty"
##                        _xml = f'<role><RoleCd value="002"></RoleCd></role>'
##                        _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
##                        new_contact.insert(100, _root)
##                        del _root, _xml
##                        citRespParty[0].getparent().replace(citRespParty[0], new_contact)
##                        del new_contact, new_contact_tree
##                    elif citRespParty is not None and len(citRespParty) and len(citRespParty) > 1:
##                        pass
##                    del citRespParty
##                else:
##                    pass
##                del i
##        else:
##            pass
##        # print(etree.tostring(reports[0].getparent(), encoding='UTF-8', method='xml', pretty_print=True).decode())
##        del dataSources

        for child in target_root.xpath("/metadata/Esri"):
            child[:] = sorted(child, key=lambda x: esri_dict[x.tag])
            del child

        for child in target_root.xpath("/metadata/dataIdInfo"):
            child[:] = sorted(child, key=lambda x: dataIdInfo_dict[x.tag])
            del child

        #for child in target_root.xpath("/metadata/dataIdInfo/idCitation_dict"):
        #    child[:] = sorted(child, key=lambda x: idCitation_dict[x.tag])
        #    del child

        for child in target_root.xpath("/metadata/dqInfo"):
            child[:] = sorted(child, key=lambda x: dqInfo_dict[x.tag])
            del child

        for child in target_root.xpath("."):
            child[:] = sorted(child, key=lambda x: root_dict[x.tag])
            del child

        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        #print(etree.tostring(target_tree, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
        etree.indent(target_tree, space='    ')
        dataset_md_xml = etree.tostring(target_tree, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True)

        SaveBackXml = True
        if SaveBackXml:
            dataset_md = md.Metadata(dataset_path)
            dataset_md.xml = dataset_md_xml
            dataset_md.save()
            dataset_md.synchronize("ALWAYS")
            dataset_md.save()
            _tree = etree.parse(StringIO(dataset_md.xml), parser=etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
            _tree.write(rf"{export_folder}\{dataset_name}.xml", pretty_print=True)
            del _tree
            #dataset_md.saveAsXML(, "REMOVE_ALL_SENSITIVE_INFO")
            del dataset_md
        else:
            pass
        del SaveBackXml
        del dataset_md_xml

        del dataset_name
        del CreaDateTime, ModDateTime
        del contact_dict, RoleCd_dict, tpCat_dict, dataIdInfo_dict, dqInfo_dict, esri_dict, root_dict
        # Imports
        del etree, md, BytesIO, StringIO, copy
        # Declared variables
        del target_root, target_tree
        # Function Parameters
        del dataset_path
    except:
        traceback.print_exc()
    else:
        # While in development, leave here. For test, move to finally
        #rk = [key for key in locals().keys() if not key.startswith('__')]
        #if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        pass

def update_existing_contacts(dataset_path=""):
    try:
        # Imports
        from lxml import etree
        from io import StringIO, BytesIO
        import copy
        from arcpy import metadata as md

        arcpy.env.overwriteOutput          = True
        arcpy.env.parallelProcessingFactor = "100%"

        dataset_md = md.Metadata(dataset_path)
        dataset_md.synchronize("ALWAYS")
        dataset_md.save()
        dataset_md.reload()
        dataset_md_xml = dataset_md.xml
        del dataset_md

        # Parse the XML
        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
        target_tree = etree.parse(StringIO(dataset_md_xml), parser=parser)
        target_root = target_tree.getroot()
        del parser, dataset_md_xml

        contacts_xml = rf"{os.environ['USERPROFILE']}\Documents\ArcGIS\Descriptions\contacts.xml"
        contacts_xml_tree = etree.parse(contacts_xml, parser=etree.XMLParser(encoding='UTF-8', remove_blank_text=True)) # To parse from a string, use the fromstring() function instead.
        del contacts_xml
        contacts_xml_root = contacts_xml_tree.getroot()
        #etree.indent(contacts_xml_root, space="  ")
        #print(etree.tostring(contacts_xml_root, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())

        dataset_name = os.path.basename(dataset_path)
        print(f"Processing Add/Update Existing Contacts for dataset: '{dataset_name}'")

        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # Search for rpIndName or eMailAdd first
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

        #print(f"\tSearch for rpIndName or eMailAdd first")
        contacts = target_tree.xpath("//*[./rpIndName/text() or ./rpCntInfo/cntAddress/eMailAdd/text()]")
        contacts_count = len(contacts)
        count=0
        for contact in contacts:
            count+=1
            #print(f"\tContact Path: {target_tree.getpath(contact)} {count} of {contacts_count}")
            #print(etree.tostring(contact, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
            contact_name = contact.find("rpIndName").text if contact.find("rpIndName") is not None else None
            contact_email = contact.find("rpCntInfo/cntAddress/eMailAdd").text if contact.find("rpCntInfo/cntAddress/eMailAdd") is not None else ""
            #print(contact_name, contact_email)

            if contact_name is not None and contact_email is not None:
                #print(f"\t\tName and email: {contact_name}, {contact_email}")
                #print(f"\t\t\t{target_tree.getpath(contact)}\n")
                new_contact_tree = contacts_xml_tree.xpath(f"//contact[./rpIndName[text()='{contact_name}'] or ./rpCntInfo/cntAddress/eMailAdd[text()='{contact_email}'] and ./editorSave[text()='True']]")
                if len(new_contact_tree) == 0:
                    #print(f"\tContact: {contact_name}, {contact_email} not in contacts.xml\n")
                    #raise Exception(f"\n!!!! Contact: {contact_name}, {contact_email} not in contacts.xml!!!\n")
                    try:
                        new_contact_tree = contacts_xml_tree.xpath(f"//contact[./rpCntInfo/cntAddress/eMailAdd[text()='{contact_email}'] and ./editorSave[text()='False']]")
                        new_contact = copy.deepcopy(new_contact_tree[0])
                        new_contact.tag = contact.tag
                        new_contact.insert(100, copy.deepcopy(contact.find(f"role")))
                        _contact = target_tree.xpath(f"/{target_tree.getpath(contact)}")[0]
                        _contact.getparent().replace(_contact, new_contact)
                        del _contact, new_contact, new_contact_tree
                    except:
                        pass
                elif len(new_contact_tree) == 1:
                    new_contact = copy.deepcopy(new_contact_tree[0])
                    new_contact.tag = contact.tag
                    new_contact.insert(100, copy.deepcopy(contact.find(f"role")))
                    _contact = target_tree.xpath(f"/{target_tree.getpath(contact)}")[0]
                    _contact.getparent().replace(_contact, new_contact)
                    del _contact, new_contact
                else:
                    pass
                del new_contact_tree
            elif not contact_name and contact_email:
                #print(f"\t\tEmail: {contact_email}")
                #print(f"\t\t\t{target_tree.getpath(contact)}")
                new_contact_tree = contacts_xml_tree.xpath(f"//contact[./rpCntInfo/cntAddress/eMailAdd[text()='{contact_email}'] and ./editorSave[text()='True']]")
                if len(new_contact_tree) == 0:
                    #print(f"\tContact: {contact_name}, {contact_email} not in contacts.xml\n")
                    #raise Exception(f"\n!!!! Contact: {contact_name}, {contact_email} not in contacts.xml!!!\n")
                    new_contact_tree = contacts_xml_tree.xpath(f"//contact[./rpCntInfo/cntAddress/eMailAdd[text()='{contact_email}'] and ./editorSave[text()='False']]")
                    new_contact = copy.deepcopy(new_contact_tree[0])
                    new_contact.tag = contact.tag
                    new_contact.insert(100, copy.deepcopy(contact.find(f"role")))
                    _contact = target_tree.xpath(f"/{target_tree.getpath(contact)}")[0]
                    _contact.getparent().replace(_contact, new_contact)
                    del _contact, new_contact, new_contact_tree
                elif len(new_contact_tree) > 0:
                    new_contact = copy.deepcopy(new_contact_tree[0])
                    new_contact.tag = contact.tag
                    new_contact.insert(100, copy.deepcopy(contact.find(f"role")))
                    _contact = target_tree.xpath(f"/{target_tree.getpath(contact)}")[0]
                    _contact.getparent().replace(_contact, new_contact)
                    del _contact, new_contact
                else:
                    pass
                del new_contact_tree
            elif contact_name and not contact_email:
                #print(f"\t\tName: {contact_name}")
                #print(f"\t\t\t{target_tree.getpath(contact)}")
                new_contact_tree = contacts_xml_tree.xpath(f"//contact[./rpIndName[text()='{contact_name}'] and ./editorSave[text()='True']]")
                if len(new_contact_tree) == 0:
                    #print(f"\tContact: {contact_name}, {contact_email} not in contacts.xml\n")
                    #raise Exception(f"\n!!!! Contact: {contact_name}, {contact_email} not in contacts.xml!!!\n")
                    new_contact_tree = contacts_xml_tree.xpath(f"//contact[./rpCntInfo/cntAddress/eMailAdd[text()='{contact_email}'] and ./editorSave[text()='False']]")
                    new_contact = copy.deepcopy(new_contact_tree[0])
                    new_contact.tag = contact.tag
                    new_contact.insert(100, copy.deepcopy(contact.find(f"role")))
                    _contact = target_tree.xpath(f"/{target_tree.getpath(contact)}")[0]
                    _contact.getparent().replace(_contact, new_contact)
                    del _contact, new_contact, new_contact_tree
                elif len(new_contact_tree) > 0:
                    new_contact = copy.deepcopy(new_contact_tree[0])
                    new_contact.tag = contact.tag
                    new_contact.insert(100, copy.deepcopy(contact.find(f"role")))
                    _contact = target_tree.xpath(f"/{target_tree.getpath(contact)}")[0]
                    _contact.getparent().replace(_contact, new_contact)
                    del _contact, new_contact
                else:
                    pass
                del new_contact_tree
            del contact_name, contact_email, contact
        del contacts, contacts_count, count

        contacts = target_tree.xpath("//*[./rpIndName/text() or ./rpCntInfo/cntAddress/eMailAdd/text()]")
        for contact in contacts:
            #print(etree.tostring(contact, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
            del contact
        del contacts

        etree.indent(target_tree, space='    ')
        dataset_md_xml = etree.tostring(target_tree, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True)

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

        # Declared variables
        del dataset_name
        del contacts_xml_tree, contacts_xml_root
        del target_tree, target_root
        # Imports
        del md, etree, copy, StringIO, BytesIO
        # Function Parameters
        del dataset_path

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

def update_process_steps(dataset_path=""):
    try:
        # Imports
        from lxml import etree
        from io import StringIO, BytesIO
        import copy
        from arcpy import metadata as md

        dataset_md = md.Metadata(dataset_path)
        dataset_md.synchronize("ALWAYS")
        dataset_md.save()
        dataset_md.reload()
        dataset_md_xml = dataset_md.xml
        del dataset_md

        # Parse the XML
        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
        target_tree = etree.parse(StringIO(dataset_md_xml), parser=parser)
        target_root = target_tree.getroot()
        del parser, dataset_md_xml

        dataset_name = os.path.basename(dataset_path)
        print(f"Processing Process Steps for dataset: '{dataset_name}'")
        #print(f"\tDataset Location: {os.path.basename(os.path.dirname(dataset_path))}")

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

        target_prcSteps = target_tree.xpath("/metadata/dqInfo/dataLineage/prcStep")
        dataLineage     = target_tree.xpath("/metadata/dqInfo/dataLineage")[0]
        if isinstance(target_prcSteps, type(None)):
            pass # Nothing to do, at the root of the tree
        elif not isinstance(target_prcSteps, type(None)) and len(target_prcSteps) == 0:
            source_prcSteps = source_tree.xpath("/metadata/dqInfo/dataLineage/prcStep")
            if not isinstance(source_prcSteps, type(None)) and len(source_prcSteps) > 0:
                for source_prcStep in source_prcSteps:
                    CreaDate = target_root.xpath(f"//Esri/CreaDate")[0].text
                    CreaTime = target_root.xpath(f"//Esri/CreaTime")[0].text
                    CreaDateTime = f"{CreaDate[:4]}-{CreaDate[4:6]}-{CreaDate[6:]}T{CreaTime[:2]}:{CreaTime[2:4]}:{CreaTime[4:6]}"
                    del CreaDate, CreaTime
                    source_prcStep.find("./stepDesc").text = "Metadata Update 2025"
                    source_prcStep.find("./stepDateTm").text = CreaDateTime

                    source_stepProcs = source_prcStep.xpath("./stepProc")
                    if not isinstance(source_stepProcs, type(None)) and len(source_stepProcs) > 0:
                        citRespPartys = target_tree.xpath("/metadata/dataIdInfo/idCitation/citRespParty")
                        if not isinstance(citRespPartys, type(None)) and len(citRespPartys) > 0:
                            citRespPartys_count = len(citRespPartys)
                            citRespParty_count  = 0
                            for citRespParty in citRespPartys:
                                citRespParty_count+=1
                                print(f"\tContacts Path: {target_tree.getpath(citRespParty)} {citRespParty_count} of {citRespPartys_count}")
                                #print(etree.tostring(citRespParty, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
                                contact_name  = citRespParty.find("./rpIndName").text if citRespParty.find("./rpIndName") is not None else None
                                contact_email = citRespParty.find("./rpCntInfo/cntAddress/eMailAdd").text if citRespParty.find("./rpCntInfo/cntAddress/eMailAdd") is not None else ""
                                print(f"\t\tProcesser: {contact_name}, {contact_email}")
                                for source_stepProc in source_stepProcs:
                                    step_processer = source_stepProc.xpath(f"//{source_stepProc.tag}[./rpIndName[text()='{contact_name}'] and ./rpCntInfo/cntAddress/eMailAdd[text()='{contact_email}'] and ./editorSave[text()='True']]")
                                    if not isinstance(step_processer, type(None)) and len(step_processer) == 0:
                                        print("\t\t\tNothing Found")
                                        _citRespParty = copy.deepcopy(citRespParty)
                                        _citRespParty.tag = source_stepProc.tag
                                        source_stepProc.append(_citRespParty)
                                        #_mdContact = copy.deepcopy(mdContact)
                                        #_mdContact.tag = source_stepProc.tag
                                        #step_processer.getparent().replace(step_processer, _mdContact)
                                        del _citRespParty
                                    elif not isinstance(step_processer, type(None)) and len(step_processer) > 0:
                                        print("\t\t\tFound contacts")
                                        #print(etree.tostring(source_stepProc, encoding='UTF-8', method='xml', pretty_print=True).decode())
                                    else:
                                        pass
                                    del step_processer
                                    del source_stepProc
                                del contact_name, contact_email
                                #print(etree.tostring(citRespParty, encoding='UTF-8', method='xml', pretty_print=True).decode())
                                del citRespParty
                            del citRespParty_count
                            del citRespPartys_count
                        else:
                            pass
                        del citRespPartys
                        idPoCs = target_tree.xpath("/metadata/dataIdInfo/idPoC")
                        if not isinstance(idPoCs, type(None)) and len(idPoCs) > 0:
                            idPoCs_count = len(idPoCs)
                            idPoC_count  = 0
                            for idPoC in idPoCs:
                                idPoC_count+=1
                                print(f"\tContacts Path: {target_tree.getpath(idPoC)} {idPoC_count} of {idPoCs_count}")
                                #print(etree.tostring(idPoC, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
                                contact_name  = idPoC.find("./rpIndName").text if idPoC.find("./rpIndName") is not None else None
                                contact_email = idPoC.find("./rpCntInfo/cntAddress/eMailAdd").text if idPoC.find("./rpCntInfo/cntAddress/eMailAdd") is not None else ""
                                print(f"\t\tProcesser: {contact_name}, {contact_email}")
                                for source_stepProc in source_stepProcs:
                                    step_processer = source_stepProc.xpath(f"//{source_stepProc.tag}[./rpIndName[text()='{contact_name}'] and ./rpCntInfo/cntAddress/eMailAdd[text()='{contact_email}'] and ./editorSave[text()='True']]")
                                    if not isinstance(step_processer, type(None)) and len(step_processer) == 0:
                                        print("\t\t\tNothing Found")
                                        _idPoC = copy.deepcopy(idPoC)
                                        _idPoC.tag = source_stepProc.tag
                                        source_stepProc.append(_idPoC)
                                        #_mdContact = copy.deepcopy(mdContact)
                                        #_mdContact.tag = source_stepProc.tag
                                        #step_processer.getparent().replace(step_processer, _mdContact)
                                        del _idPoC
                                    elif not isinstance(step_processer, type(None)) and len(step_processer) > 0:
                                        print("\t\t\tFound contacts")
                                        #print(etree.tostring(source_stepProc, encoding='UTF-8', method='xml', pretty_print=True).decode())
                                    else:
                                        pass
                                    del step_processer
                                    del source_stepProc
                                del contact_name, contact_email
                                #print(etree.tostring(idPoC, encoding='UTF-8', method='xml', pretty_print=True).decode())
                                del idPoC
                            del idPoC_count
                            del idPoCs_count
                        else:
                            pass
                        del idPoCs
                        mdContacts = target_tree.xpath("/metadata/mdContact")
                        if not isinstance(mdContacts, type(None)) and len(mdContacts) > 0:
                            mdContacts_count = len(mdContacts)
                            mdContact_count  = 0
                            for mdContact in mdContacts:
                                mdContact_count+=1
                                print(f"\tContacts Path: {target_tree.getpath(mdContact)} {mdContact_count} of {mdContacts_count}")
                                #print(etree.tostring(mdContact, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
                                contact_name  = mdContact.find("./rpIndName").text
                                contact_email = mdContact.find("./rpCntInfo/cntAddress/eMailAdd").text
                                print(f"\t\tProcesser: {contact_name}, {contact_email}")
                                for source_stepProc in source_stepProcs:
                                    step_processer = source_stepProc.xpath(f"//{source_stepProc.tag}[./rpIndName[text()='{contact_name}'] and ./rpCntInfo/cntAddress/eMailAdd[text()='{contact_email}'] and ./editorSave[text()='True']]")
                                    if not isinstance(step_processer, type(None)) and len(step_processer) == 0:
                                        print("\t\t\tNothing Found")
                                        _mdContact = copy.deepcopy(mdContact)
                                        _mdContact.tag = source_stepProc.tag
                                        source_stepProc.append(_mdContact)
                                        #_mdContact = copy.deepcopy(mdContact)
                                        #_mdContact.tag = source_stepProc.tag
                                        #step_processer.getparent().replace(step_processer, _mdContact)
                                        del _mdContact
                                    elif not isinstance(step_processer, type(None)) and len(step_processer) > 0:
                                        print("\t\t\tFound contacts")
                                        #print(etree.tostring(source_stepProc, encoding='UTF-8', method='xml', pretty_print=True).decode())
                                    else:
                                        pass
                                    del step_processer
                                    del source_stepProc
                                del contact_name, contact_email
                                #print(etree.tostring(mdContact, encoding='UTF-8', method='xml', pretty_print=True).decode())
                                del mdContact
                            del mdContact_count
                            del mdContacts_count
                        else:
                            pass
                        del mdContacts
                        #for source_stepProc in source_stepProcs:
                        #    #print(etree.tostring(source_stepProc, encoding='UTF-8', method='xml', pretty_print=True).decode())
                        #    del source_stepProc
                    del source_stepProcs
                    #print(target_contact_elements)
                    dataLineage.append(source_prcStep)
                    del CreaDateTime
                    del source_prcStep
            else:
                pass
            del source_prcSteps
            #print(etree.tostring(dataLineage, encoding='UTF-8', method='xml', pretty_print=True).decode())

        elif not isinstance(target_prcSteps, type(None)) and len(target_prcSteps) >= 1:
            target_prcSteps_count = len(target_prcSteps)
            target_prcStep_count  = 0
            for target_prcStep in target_prcSteps:
                target_prcStep_count+=1
                #print(etree.tostring(target_prcStep, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())

                CreaDate = target_root.xpath(f"//Esri/CreaDate")[0].text
                CreaTime = target_root.xpath(f"//Esri/CreaTime")[0].text
                CreaDateTime = f"{CreaDate[:4]}-{CreaDate[4:6]}-{CreaDate[6:]}T{CreaTime[:2]}:{CreaTime[2:4]}:{CreaTime[4:6]}"
                del CreaDate, CreaTime
                if not target_prcStep.find("./stepDesc").text:
                    target_prcStep.find("./stepDesc").text = "Metadata Update 2025"
                if not target_prcStep.find("./stepDateTm").text:
                    target_prcStep.find("./stepDateTm").text = CreaDateTime
                del CreaDateTime

                print(f"\tProcess Steps Path: {target_tree.getpath(target_prcStep)} {target_prcStep_count} of {target_prcSteps_count}")
                print(f"\t\tStep Description: {target_prcStep.find('stepDesc').text}")
                print(f"\t\tStep Date/Time:   {target_prcStep.find('stepDateTm').text}")

                citRespPartys = target_tree.xpath("/dataIdInfo/idCitation/citRespParty")
                if not isinstance(citRespPartys, type(None)) and len(citRespPartys) > 0:
                    citRespPartys_count = len(citRespPartys)
                    citRespParty_count  = 0
                    for citRespParty in citRespPartys:
                        citRespParty_count+=1
                        print(f"\tContacts Path: {target_tree.getpath(citRespParty)} {citRespParty_count} of {citRespPartys_count}")
                        #print(etree.tostring(citRespParty, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
                        contact_name  = citRespParty.find("./rpIndName").text
                        contact_email = citRespParty.find("./rpCntInfo/cntAddress/eMailAdd").text
                        print(f"\t\tProcesser: {contact_name}, {contact_email}")
                        target_stepProcs       = target_prcStep.xpath("./stepProc")
                        target_stepProcs_count = len(target_stepProcs)
                        target_stepProc_count  = 0
                        for target_stepProc in target_stepProcs:
                            target_stepProc_count+=1
                            print(f"\t\tStep Processor Path: {target_tree.getpath(target_stepProc)} {target_stepProc_count} of {target_stepProcs_count}")
                            step_processer = target_stepProc.xpath(f"//{target_stepProc.tag}[./rpIndName[text()='{contact_name}'] and ./rpCntInfo/cntAddress/eMailAdd[text()='{contact_email}'] and ./editorSave[text()='True']]")
                            if not isinstance(step_processer, type(None)) and len(step_processer) == 0:
                                print("\t\t\tNothing Found")
                                _citRespParty = copy.deepcopy(citRespParty)
                                _citRespParty.tag = target_stepProc.tag
                                target_stepProc.append(_citRespParty)
                                del _citRespParty
                            elif not isinstance(step_processer, type(None)) and len(step_processer) > 0:
                                print("\t\t\tFound contacts")
                                #print(etree.tostring(target_stepProc, encoding='UTF-8', method='xml', pretty_print=True).decode())
                            else:
                                pass
                            del step_processer
                            del target_stepProc
                        del contact_name, contact_email
                        del target_stepProc_count
                        del target_stepProcs_count
                        del target_stepProcs
                        #print(etree.tostring(citRespParty, encoding='UTF-8', method='xml', pretty_print=True).decode())
                        del citRespParty
                    del citRespParty_count
                    del citRespPartys_count
                else:
                    pass
                del citRespPartys

                idPoCs = target_tree.xpath("./dataIdInfo/idPoC")
                if not isinstance(idPoCs, type(None)) and len(idPoCs) > 0:
                    idPoCs_count = len(idPoCs)
                    idPoC_count  = 0
                    for idPoC in idPoCs:
                        idPoC_count+=1
                        print(f"\tContacts Path: {target_tree.getpath(idPoC)} {idPoC_count} of {idPoCs_count}")
                        #print(etree.tostring(idPoC, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
                        contact_name  = idPoC.find("./rpIndName").text
                        contact_email = idPoC.find("./rpCntInfo/cntAddress/eMailAdd").text
                        print(f"\t\tProcesser: {contact_name}, {contact_email}")
                        target_stepProcs       = target_prcStep.xpath("./stepProc")
                        target_stepProcs_count = len(target_stepProcs)
                        target_stepProc_count  = 0
                        for target_stepProc in target_stepProcs:
                            target_stepProc_count+=1
                            print(f"\t\tStep Processor Path: {target_tree.getpath(target_stepProc)} {target_stepProc_count} of {target_stepProcs_count}")
                            step_processer = target_stepProc.xpath(f"//{target_stepProc.tag}[./rpIndName[text()='{contact_name}'] and ./rpCntInfo/cntAddress/eMailAdd[text()='{contact_email}'] and ./editorSave[text()='True']]")
                            if not isinstance(step_processer, type(None)) and len(step_processer) == 0:
                                print("\t\t\tNothing Found")
                                _idPoC = copy.deepcopy(idPoC)
                                _idPoC.tag = target_stepProc.tag
                                target_stepProc.append(_idPoC)
                                del _idPoC
                            elif not isinstance(step_processer, type(None)) and len(step_processer) > 0:
                                print("\t\t\tFound contacts")
                                #print(etree.tostring(target_stepProc, encoding='UTF-8', method='xml', pretty_print=True).decode())
                            else:
                                pass
                            del step_processer
                            del target_stepProc
                        del contact_name, contact_email
                        del target_stepProc_count
                        del target_stepProcs_count
                        del target_stepProcs
                        #print(etree.tostring(idPoC, encoding='UTF-8', method='xml', pretty_print=True).decode())
                        del idPoC
                    del idPoC_count
                    del idPoCs_count
                else:
                    pass
                del idPoCs

                mdContacts = target_tree.xpath("/metadata/mdContact")
                if not isinstance(mdContacts, type(None)) and len(mdContacts) > 0:
                    mdContacts_count = len(mdContacts)
                    mdContact_count  = 0
                    for mdContact in mdContacts:
                        mdContact_count+=1
                        print(f"\tContacts Path: {target_tree.getpath(mdContact)} {mdContact_count} of {mdContacts_count}")
                        #print(etree.tostring(mdContact, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
                        contact_name  = mdContact.find("./rpIndName").text
                        contact_email = mdContact.find("./rpCntInfo/cntAddress/eMailAdd").text
                        print(f"\t\tProcesser: {contact_name}, {contact_email}")
                        target_stepProcs       = target_prcStep.xpath("./stepProc")
                        target_stepProcs_count = len(target_stepProcs)
                        target_stepProc_count  = 0
                        for target_stepProc in target_stepProcs:
                            target_stepProc_count+=1
                            print(f"\t\tStep Processor Path: {target_tree.getpath(target_stepProc)} {target_stepProc_count} of {target_stepProcs_count}")
                            step_processer = target_stepProc.xpath(f"//{target_stepProc.tag}[./rpIndName[text()='{contact_name}'] and ./rpCntInfo/cntAddress/eMailAdd[text()='{contact_email}'] and ./editorSave[text()='True']]")
                            if not isinstance(step_processer, type(None)) and len(step_processer) == 0:
                                print("\t\t\tNothing Found")
                                _mdContact = copy.deepcopy(mdContact)
                                _mdContact.tag = target_stepProc.tag
                                target_stepProc.append(_mdContact)
                                del _mdContact
                            elif not isinstance(step_processer, type(None)) and len(step_processer) > 0:
                                print("\t\t\tFound contacts")
                                #print(etree.tostring(target_stepProc, encoding='UTF-8', method='xml', pretty_print=True).decode())
                            else:
                                pass
                            del step_processer
                            del target_stepProc
                        del contact_name, contact_email
                        del target_stepProc_count
                        del target_stepProcs_count
                        del target_stepProcs
                        #print(etree.tostring(mdContact, encoding='UTF-8', method='xml', pretty_print=True).decode())
                        del mdContact
                    del mdContact_count
                    del mdContacts_count
                else:
                    pass
                del mdContacts

                del target_prcStep
            del target_prcStep_count
            del target_prcSteps_count
            del dataset_name, target_prcSteps
        else:
            pass
        #print(etree.tostring(dataLineage, encoding='UTF-8', method='xml', pretty_print=True).decode())
        del dataLineage

        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

        # No changes needed below
        #print(etree.tostring(target_tree.xpath("//dataIdInfo")[0], encoding='UTF-8', method='xml', pretty_print=True).decode())
        #print(etree.tostring(target_tree, encoding='UTF-8', method='xml', pretty_print=True).decode())
        etree.indent(target_tree, space='    ')
        dataset_md_xml = etree.tostring(target_tree, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True)

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

        # Declared Variables
        del source_tree, source_root
        del target_tree, target_root
        # Imports
        del StringIO, BytesIO, etree, md, copy
        # Functiona Parameters
        del dataset_path

    except Exception:
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

def add_update_contacts(dataset_path=""):
    try:
        # Imports
        from lxml import etree
        from io import StringIO, BytesIO
        import copy
        from arcpy import metadata as md

        arcpy.env.overwriteOutput          = True
        arcpy.env.parallelProcessingFactor = "100%"

        project_gdb    = os.path.dirname(dataset_path)
        project_folder = os.path.dirname(project_gdb)
        scratch_folder = rf"{project_folder}\Scratch"

        arcpy.env.workspace        = project_gdb
        arcpy.env.scratchWorkspace = rf"{scratch_folder}\scratch.gdb"

        import json
        json_path = rf"{project_folder}\root_dict.json"
        with open(json_path, "r") as json_file:
            root_dict = json.load(json_file)
        json_path = rf"{project_folder}\esri_dict.json"
        with open(json_path, "r") as json_file:
            esri_dict = json.load(json_file)
        json_path = rf"{project_folder}\dataIdInfo_dict.json"
        with open(json_path, "r") as json_file:
            dataIdInfo_dict = json.load(json_file)
        json_path = rf"{project_folder}\contact_dict.json"
        with open(json_path, "r") as json_file:
            contact_dict = json.load(json_file)
        json_path = rf"{project_folder}\dqInfo_dict.json"
        with open(json_path, "r") as json_file:
            dqInfo_dict = json.load(json_file)
        json_path = rf"{project_folder}\distInfo_dict.json"
        with open(json_path, "r") as json_file:
            distInfo_dict = json.load(json_file)
        json_path = rf"{project_folder}\RoleCd_dict.json"
        with open(json_path, "r") as json_file:
            RoleCd_dict = json.load(json_file)
        json_path = rf"{project_folder}\tpCat_dict.json"
        with open(json_path, "r") as json_file:
            tpCat_dict = json.load(json_file)
        del json_file

        del json_path
        del json

        contacts_xml = rf"{os.environ['USERPROFILE']}\Documents\ArcGIS\Descriptions\contacts.xml"
        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
        contacts_xml_tree = etree.parse(contacts_xml, parser=parser) # To parse from a string, use the fromstring() function instead.
        del parser
        del contacts_xml
        contacts_xml_root = contacts_xml_tree.getroot()
        #etree.indent(contacts_xml_root, space="  ")
        #print(etree.tostring(contacts_xml_root, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())

        dataset_name = os.path.basename(dataset_path)
        print(f"Processing Add/Update Contacts for dataset: '{dataset_name}'")
        #print(f"\tDataset Location: {os.path.basename(os.path.dirname(dataset_path))}")

##        dataset_md = md.Metadata(dataset_path)
##        dataset_md.synchronize("ALWAYS")
##        dataset_md.save()
##        dataset_md.reload()
##        dataset_md_xml = dataset_md.xml
##        del dataset_md
##
##        # Parse the XML
##        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
##        target_tree = etree.parse(StringIO(dataset_md_xml), parser=parser)
##        target_root = target_tree.getroot()
##        del parser, dataset_md_xml
##        old_root_dict = {dataset_name : list()}
##        kids = target_root.iterchildren(tag=[child.tag for child in target_root])
##        for kid in kids:
##            kid.clear()
##            if kid.tag not in old_root_dict[dataset_name] and kid.tag != "Binary":
##                old_root_dict[dataset_name].append(kid.tag)
##            del kid
##        del kids
##        for key in old_root_dict:
##            if "mdContact" not in old_root_dict[key]:
##                #print(f"{key:<39}: {', '.join(sorted(old_root_dict[key]))}")
##                print(f"{key}: {', '.join(sorted(old_root_dict[key]))}")
##            else:
##                print(f"{key}: {', '.join(sorted(old_root_dict[key]))}")
##            del key
##        del old_root_dict
##        del target_root, target_tree

        dataset_md = md.Metadata(dataset_path)
        dataset_md.synchronize("ALWAYS")
        dataset_md.save()
        dataset_md.reload()
        dataset_md_xml = dataset_md.xml
        del dataset_md

        # Parse the XML
        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
        target_tree = etree.parse(StringIO(dataset_md_xml), parser=parser)
        target_root = target_tree.getroot()
        del parser, dataset_md_xml

        #print(etree.tostring(target_root, encoding='UTF-8', method='xml', pretty_print=True).decode())

        CreaDate = target_root.xpath(f"//Esri/CreaDate")[0].text
        CreaTime = target_root.xpath(f"//Esri/CreaTime")[0].text
        #print(CreaDate, CreaTime)
        CreaDateTime = f"{CreaDate[:4]}-{CreaDate[4:6]}-{CreaDate[6:]}T{CreaTime[:2]}:{CreaTime[2:4]}:{CreaTime[4:6]}"
        #print(f"\tCreaDateTime: {CreaDateTime}")
        #del CreaDateTime
        del CreaDate, CreaTime
        ModDate = target_root.xpath(f"//Esri/ModDate")[0].text
        ModTime = target_root.xpath(f"//Esri/ModTime")[0].text
        #print(ModDate, ModTime)
        ModDateTime = f"{ModDate[:4]}-{ModDate[4:6]}-{ModDate[6:]}T{ModTime[:2]}:{ModTime[2:4]}:{ModTime[4:6]}"
        #print(f"\tModDateTime: {ModDateTime}")
        #del ModDateTime
        del ModDate, ModTime

        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # Get Prefered contact information
        mdContact_rpIndName = contact_dict["mdContact"][0]["rpIndName"]
        mdContact_eMailAdd  = contact_dict["mdContact"][0]["eMailAdd"]
        mdContact_role      = contact_dict["mdContact"][0]["role"]

        citRespParty_rpIndName = contact_dict["citRespParty"][0]["rpIndName"]
        citRespParty_eMailAdd  = contact_dict["citRespParty"][0]["eMailAdd"]
        citRespParty_role      = contact_dict["citRespParty"][0]["role"]

        idPoC_rpIndName = contact_dict["idPoC"][0]["rpIndName"]
        idPoC_eMailAdd  = contact_dict["idPoC"][0]["eMailAdd"]
        idPoC_role      = contact_dict["idPoC"][0]["role"]

        distorCont_rpIndName = contact_dict["distorCont"][0]["rpIndName"]
        distorCont_eMailAdd  = contact_dict["distorCont"][0]["eMailAdd"]
        distorCont_role      = contact_dict["distorCont"][0]["role"]

        srcCitatn_rpIndName = contact_dict["srcCitatn"][0]["rpIndName"]
        srcCitatn_eMailAdd  = contact_dict["srcCitatn"][0]["eMailAdd"]
        srcCitatn_role      = contact_dict["srcCitatn"][0]["role"]

        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        #print(etree.tostring(target_root, encoding='UTF-8', method='xml', pretty_print=True).decode())

        # Remove duplicates
        mdContacts = target_root.xpath(f"./mdContact")
        #remove_duplicate_elements(mdContacts[0].getparent())
        del mdContacts

        #print(etree.tostring(target_root.find("./dqInfo"), encoding='UTF-8', method='xml', pretty_print=True).decode())

        '''mdContact exists?
                if no, then insert new prefered contact element
                if yes, does it have content? yes or no
                    if yes, then two questions
                        check if is in step processors
                            if no, copy over
                            if yes, ignore
                        check if prefered contact element
                            if yes, ignore
                            if no, remove mdcontact
        '''
       #print(f"\tmdContact Section")
        # Get list of mdContact elements
        mdContacts = target_root.xpath(f"./mdContact")
        if len(mdContacts) == 0:
           #print("\tMissing Element. Inserting prefered contact element")
            new_contact_tree = contacts_xml_tree.xpath(f"//contact[./rpIndName[text()='{mdContact_rpIndName}'] and ./rpCntInfo/cntAddress/eMailAdd[text()='{mdContact_eMailAdd}'] and ./editorSave[text()='True']]")
            new_contact = copy.deepcopy(new_contact_tree[0])
            new_contact.tag = "mdContact"
            _xml = f'<role><RoleCd value="011"></RoleCd></role>'
            _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
            new_contact.insert(100, _root)
            del _root, _xml
            target_root.insert(root_dict["mdContact"], new_contact)
            del new_contact, new_contact_tree
        del mdContacts

        mdContacts = target_root.xpath(f"./mdContact")
        #print(len(mdContacts))
        if len(mdContacts) >= 1:
            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #####
            prefered_mdContact = target_root.xpath(f"./mdContact[./rpIndName[text()='{mdContact_rpIndName}'] and ./rpCntInfo/cntAddress/eMailAdd[text()='{mdContact_eMailAdd}']]")
            #print(len(prefered_mdContact))
            if len(prefered_mdContact) == 0:
                new_contact_tree = contacts_xml_tree.xpath(f"//contact[./rpIndName[text()='{mdContact_rpIndName}'] and ./rpCntInfo/cntAddress/eMailAdd[text()='{mdContact_eMailAdd}'] and ./editorSave[text()='True']]")
                new_contact = copy.deepcopy(new_contact_tree[0])
                new_contact.tag = "mdContact"
                _xml = f'<role><RoleCd value="011"></RoleCd></role>'
                _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
                new_contact.insert(100, _root)
                del _root, _xml
                target_root.insert(root_dict["mdContact"], new_contact)
                del new_contact, new_contact_tree
            elif len(prefered_mdContact) == 1:
                #print(len(prefered_mdContact))
                pass
            elif len(prefered_mdContact) > 1:
               #print(len(prefered_mdContact))
                pass
            else:
                pass
            del prefered_mdContact
            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #####

            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #####
            empty_mdContacts = [mdC for mdC in target_root.xpath(f"./mdContact") if len(mdC) == 0]
            for empty_mdContact in empty_mdContacts:
                new_contact_tree = contacts_xml_tree.xpath(f"//contact[./rpIndName[text()='{mdContact_rpIndName}'] and ./rpCntInfo/cntAddress/eMailAdd[text()='{mdContact_eMailAdd}'] and ./editorSave[text()='True']]")
                new_contact = copy.deepcopy(new_contact_tree[0])
                new_contact.tag = "mdContact"
                _xml = f'<role><RoleCd value="011"></RoleCd></role>'
                _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
                new_contact.insert(100, _root)
                del _root, _xml
                element.getparent().replace(element, new_contact)
                del new_contact, new_contact_tree
                del empty_mdContact
            del empty_mdContacts
            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #####

            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #####
            non_empty_mdContacts = [mdC for mdC in target_root.xpath(f"./mdContact") if len(mdC) != 0]
            for non_empty_mdContact in non_empty_mdContacts:
                #print(etree.tostring(non_empty_mdContact, encoding='UTF-8', method='xml', pretty_print=True).decode())
                contact_name = non_empty_mdContact.find("./rpIndName").text if non_empty_mdContact.find("rpIndName") is not None else None
                contact_email = non_empty_mdContact.find("./rpCntInfo/cntAddress/eMailAdd").text if non_empty_mdContact.find("rpCntInfo/cntAddress/eMailAdd") is not None else None
               #print(f"\t\tName and email: {contact_name}, {contact_email}")

                step_processers = target_root.xpath(f"./dqInfo/dataLineage/prcStep/stepProc[./rpIndName[text()='{contact_name}'] or ./rpCntInfo/cntAddress/eMailAdd[text()='{contact_email}']]")
                if len(step_processers) == 0:
                   #print(f"\t\t\tContact '{contact_name}' is not in step processors")
                    _non_empty_mdContact = copy.deepcopy(non_empty_mdContact)
                    _non_empty_mdContact.tag = "stepProc"
                    _non_empty_mdContact.find(f"./role/RoleCd").set('value', "009")

                    empty_step_procs = target_root.xpath(f"./dqInfo/dataLineage/prcStep/stepProc[./rpIndName[not(text())] and ./rpCntInfo/cntAddress/eMailAdd[not(text())]]")
                    if len(empty_step_procs) == 0:
                        prcStep = target_root.xpath(f"./dqInfo/dataLineage/prcStep")[0]
                        prcStep.insert(-1, _non_empty_mdContact)
                        del prcStep
                        if contact_name != mdContact_rpIndName and contact_email != mdContact_eMailAdd:
                            non_empty_mdContact.getparent().remove(non_empty_mdContact)
                        else:
                            pass
                    elif len(empty_step_procs) == 1:
                        empty_step_procs[0].getparent().replace(empty_step_procs[0], _non_empty_mdContact)
                    else:
                        pass
                    del _non_empty_mdContact
                    del empty_step_procs
                elif len(step_processers) == 1:
                   #print(f"\t\t\tContact '{contact_name}' is in step processors. Removing from mdContact")
                    if contact_name != mdContact_rpIndName and contact_email != mdContact_eMailAdd:
                        non_empty_mdContact.getparent().remove(non_empty_mdContact)
                    else:
                        pass
                del step_processers
                del contact_name, contact_email
                del non_empty_mdContact
            del non_empty_mdContacts
            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #####
        else:
            pass
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #####
        prefered_mdContact = target_root.xpath(f"./mdContact[./rpIndName[text()='{mdContact_rpIndName}'] and ./rpCntInfo/cntAddress/eMailAdd[text()='{mdContact_eMailAdd}']]")
        #print(len(prefered_mdContact))
        if len(prefered_mdContact) == 0:
            #print(len(prefered_mdContact))
            pass
        elif len(prefered_mdContact) == 1:
            #print(len(prefered_mdContact))
            pass
        elif len(prefered_mdContact) > 1:
            #print(len(prefered_mdContact))
            pass
        else:
            pass
        del prefered_mdContact
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #####
        del mdContacts

        for mdContact in target_root.xpath(f"./mdContact"):
            #print(etree.tostring(mdContact, encoding='UTF-8', method='xml', pretty_print=True).decode())
            del mdContact

        for prcStep in target_root.xpath(f"./dqInfo/dataLineage/prcStep"): # /stepProc
            #print(etree.tostring(prcStep, encoding='UTF-8', method='xml', pretty_print=True).decode())
            del prcStep

       #print(f"\tidPoCs Section")
        # Get list of idPoCs elements
        idPoCs = target_tree.xpath("./dataIdInfo/idPoC")
        #print(f"idPoCs: {len(idPoCs)}")
        if len(idPoCs) == 0:
           #print("\tMissing Element. Inserting prefered contact element")
            new_contact_tree = contacts_xml_tree.xpath(f"//contact[./rpIndName[text()='{idPoC_rpIndName}'] and ./rpCntInfo/cntAddress/eMailAdd[text()='{idPoC_eMailAdd}'] and ./editorSave[text()='True']]")
            new_contact = copy.deepcopy(new_contact_tree[0])
            new_contact.tag = "idPoC"
            _xml = f'<role><RoleCd value="007"></RoleCd></role>'
            _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
            new_contact.insert(100, _root)
            del _root, _xml
            target_root.find("./dataIdInfo").insert(dataIdInfo_dict["idPoC"], new_contact)
            del new_contact, new_contact_tree
        del idPoCs

        idPoCs = target_root.xpath(f"./dataIdInfo/idPoC")
        if len(idPoCs) >= 1:
            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #####
            prefered_idPoC = target_root.xpath(f"./dataIdInfo/idPoC[./rpIndName[text()='{idPoC_rpIndName}'] and ./rpCntInfo/cntAddress/eMailAdd[text()='{idPoC_eMailAdd}']]")
            #print(f"prefered_idPoC: {len(prefered_idPoC)}")
            if len(prefered_idPoC) == 0:
                new_contact_tree = contacts_xml_tree.xpath(f"//contact[./rpIndName[text()='{idPoC_rpIndName}'] and ./rpCntInfo/cntAddress/eMailAdd[text()='{idPoC_eMailAdd}'] and ./editorSave[text()='True']]")
                new_contact = copy.deepcopy(new_contact_tree[0])
                new_contact.tag = "idPoC"
                _xml = f'<role><RoleCd value="007"></RoleCd></role>'
                _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
                new_contact.insert(100, _root)
                del _root, _xml
                target_root.find("./dataIdInfo").insert(dataIdInfo_dict["idPoC"], new_contact)
                del new_contact, new_contact_tree
            elif len(prefered_idPoC) == 1:
                #print(len(prefered_idPoC))
                pass
            elif len(prefered_idPoC) > 1:
                #print(len(prefered_idPoC))
                pass
            else:
                pass
            del prefered_idPoC
            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #####

            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #####
            empty_idPoCs = [mdC for mdC in target_root.xpath(f"./dataIdInfo/idPoC") if len(mdC) == 0]
            #print(len(empty_idPoCs))
            for empty_idPoC in empty_idPoCs:
                new_contact_tree = contacts_xml_tree.xpath(f"//contact[./rpIndName[text()='{idPoC_rpIndName}'] and ./rpCntInfo/cntAddress/eMailAdd[text()='{idPoC_eMailAdd}'] and ./editorSave[text()='True']]")
                new_contact = copy.deepcopy(new_contact_tree[0])
                new_contact.tag = "idPoC"
                _xml = f'<role><RoleCd value="007"></RoleCd></role>'
                _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
                new_contact.insert(100, _root)
                del _root, _xml
                target_root.find("./dataIdInfo").replace(empty_idPoC, new_contact)
                del new_contact, new_contact_tree
                del empty_idPoC
            del empty_idPoCs
            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #####

            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #####
            non_empty_idPoCs = [mdC for mdC in target_root.xpath(f"./dataIdInfo/idPoC") if len(mdC) != 0]
            #print(f"non_empty_idPoCs: {len(non_empty_idPoCs)}")
            for non_empty_idPoC in non_empty_idPoCs:
                #print(etree.tostring(non_empty_idPoC, encoding='UTF-8', method='xml', pretty_print=True).decode())
                contact_name = non_empty_idPoC.find("./rpIndName").text if non_empty_idPoC.find("rpIndName") is not None else None
                contact_email = non_empty_idPoC.find("./rpCntInfo/cntAddress/eMailAdd").text if non_empty_idPoC.find("rpCntInfo/cntAddress/eMailAdd") is not None else None
               #print(f"\t\tName and email: {contact_name}, {contact_email}")

                step_processers = target_root.xpath(f"./dqInfo/dataLineage/prcStep/stepProc[./rpIndName[text()='{contact_name}'] or ./rpCntInfo/cntAddress/eMailAdd[text()='{contact_email}']]")
                if len(step_processers) == 0:
                   #print(f"\t\t\tContact '{contact_name}' is not in step processors")
                    _non_empty_idPoC = copy.deepcopy(non_empty_idPoC)
                    _non_empty_idPoC.tag = "stepProc"
                    _non_empty_idPoC.find(f"./role/RoleCd").set('value', "009")

                    empty_step_procs = target_root.xpath(f"./dqInfo/dataLineage/prcStep/stepProc[./rpIndName[not(text())] and ./rpCntInfo/cntAddress/eMailAdd[not(text())]]")
                    if len(empty_step_procs) == 0:
                        prcStep = target_root.xpath(f"./dqInfo/dataLineage/prcStep")[0]
                        prcStep.insert(-1, _non_empty_idPoC)
                        del prcStep
                        if contact_name != idPoC_rpIndName and contact_email != idPoC_eMailAdd:
                            pass
                            non_empty_idPoC.getparent().remove(non_empty_idPoC)
                        else:
                            pass
                    elif len(empty_step_procs) == 1:
                        empty_step_procs[0].getparent().replace(empty_step_procs[0], _non_empty_idPoC)
                    else:
                        pass
                    del _non_empty_idPoC
                    del empty_step_procs
                elif len(step_processers) == 1:
                   #print(f"\t\t\tContact '{contact_name}' is in step processors. Removing from idPoCs")
                    if contact_name != idPoC_rpIndName and contact_email != idPoC_eMailAdd:
                        pass
                        #non_empty_idPoC.getparent().remove(non_empty_idPoC)
                    else:
                        pass
                del step_processers
                del contact_name, contact_email
                del non_empty_idPoC
            del non_empty_idPoCs
            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #####
        del idPoCs

       #print(f"\tcitRespPartys Section")
        citRespPartys = target_tree.xpath("./dataIdInfo/idCitation/citRespParty")
       #print(f"\t\tcitRespPartys: {len(citRespPartys)}")
        if len(citRespPartys) == 0:
           #print("\tMissing the citRespParty element. Inserting prefered contact element")
            new_contact_tree = contacts_xml_tree.xpath(f"//contact[./rpIndName[text()='{citRespParty_rpIndName}'] and ./rpCntInfo/cntAddress/eMailAdd[text()='{citRespParty_eMailAdd}'] and ./editorSave[text()='True']]")
            new_contact = copy.deepcopy(new_contact_tree[0])
            new_contact.tag = "citRespParty"
            _xml = f'<role><RoleCd value="007"></RoleCd></role>'
            _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
            new_contact.insert(100, _root)
            del _root, _xml
            #target_root.find("./dataIdInfo/idCitation").insert(dataIdInfo_dict["citRespParty"], new_contact)
            del new_contact, new_contact_tree
        del citRespPartys

        citRespPartys = target_root.xpath(f"./dataIdInfo/idCitation/citRespParty")
        if len(citRespPartys) >= 1:
            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #####
            prefered_citRespParty = target_root.xpath(f"./dataIdInfo/idCitation/citRespParty[./rpIndName[text()='{citRespParty_rpIndName}'] and ./rpCntInfo/cntAddress/eMailAdd[text()='{citRespParty_eMailAdd}']]")
           #print(f"\t\tprefered_citRespParty: {len(prefered_citRespParty)}")
            if len(prefered_citRespParty) == 0:
                new_contact_tree = contacts_xml_tree.xpath(f"//contact[./rpIndName[text()='{citRespParty_rpIndName}'] and ./rpCntInfo/cntAddress/eMailAdd[text()='{citRespParty_eMailAdd}'] and ./editorSave[text()='True']]")
                new_contact = copy.deepcopy(new_contact_tree[0])
                new_contact.tag = "citRespParty"
                _xml = f'<role><RoleCd value="007"></RoleCd></role>'
                _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
                new_contact.insert(100, _root)
                del _root, _xml
                target_root.find("./dataIdInfo/idCitation").insert(dataIdInfo_dict["citRespParty"], new_contact)
                del new_contact, new_contact_tree
            elif len(prefered_citRespParty) == 1:
                #print(len(prefered_citRespParty))
                pass
            elif len(prefered_citRespParty) > 1:
                #print(f"\t\tprefered_citRespParty: {len(prefered_citRespParty)}")
                pass
            else:
                pass
            del prefered_citRespParty
            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #####

            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #####
            empty_citRespPartys = [mdC for mdC in target_root.xpath(f"./dataIdInfo/idCitation/citRespParty") if len(mdC) == 0]
           #print(f"\t\tempty_citRespPartys: {len(empty_citRespPartys)}")
            for empty_citRespParty in empty_citRespPartys:
                new_contact_tree = contacts_xml_tree.xpath(f"//contact[./rpIndName[text()='{citRespParty_rpIndName}'] and ./rpCntInfo/cntAddress/eMailAdd[text()='{citRespParty_eMailAdd}'] and ./editorSave[text()='True']]")
                new_contact = copy.deepcopy(new_contact_tree[0])
                new_contact.tag = "citRespParty"
                _xml = f'<role><RoleCd value="002"></RoleCd></role>'
                _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
                new_contact.insert(100, _root)
                del _root, _xml
                target_root.find("./dataIdInfo/idCitation").replace(empty_citRespParty, new_contact)
                del new_contact, new_contact_tree
                del empty_citRespParty
            del empty_citRespPartys
            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #####

            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #####
            non_empty_citRespPartys = [mdC for mdC in target_root.xpath(f"./dataIdInfo/idCitation/citRespParty") if len(mdC) != 0]
           #print(f"\t\tnon_empty_citRespPartys: {len(non_empty_citRespPartys)}")
            for non_empty_citRespParty in non_empty_citRespPartys:
                #print(etree.tostring(non_empty_citRespParty, encoding='UTF-8', method='xml', pretty_print=True).decode())
                contact_name = non_empty_citRespParty.find("./rpIndName").text if non_empty_citRespParty.find("rpIndName") is not None else None
                contact_email = non_empty_citRespParty.find("./rpCntInfo/cntAddress/eMailAdd").text if non_empty_citRespParty.find("rpCntInfo/cntAddress/eMailAdd") is not None else None
               #print(f"\t\tName and email: {contact_name}, {contact_email}")

                step_processers = target_root.xpath(f"./dqInfo/dataLineage/prcStep/stepProc[./rpIndName[text()='{contact_name}'] or ./rpCntInfo/cntAddress/eMailAdd[text()='{contact_email}']]")
                if len(step_processers) == 0:
                   #print(f"\t\t\tContact '{contact_name}' is not in step processors")
                    _non_empty_citRespParty = copy.deepcopy(non_empty_citRespParty)
                    _non_empty_citRespParty.tag = "stepProc"
                    _non_empty_citRespParty.find(f"./role/RoleCd").set('value', "009")

                    empty_step_procs = target_root.xpath(f"./dqInfo/dataLineage/prcStep/stepProc[./rpIndName[not(text())] and ./rpCntInfo/cntAddress/eMailAdd[not(text())]]")
                    if len(empty_step_procs) == 0:
                        prcStep = target_root.xpath(f"./dqInfo/dataLineage/prcStep")[0]
                        prcStep.insert(-1, _non_empty_citRespParty)
                        del prcStep
                        if contact_name != citRespParty_rpIndName and contact_email != citRespParty_eMailAdd:
                            non_empty_citRespParty.getparent().remove(non_empty_citRespParty)
                        else:
                            pass
                    elif len(empty_step_procs) == 1:
                        empty_step_procs[0].getparent().replace(empty_step_procs[0], _non_empty_citRespParty)
                    else:
                        pass
                    del _non_empty_citRespParty
                    del empty_step_procs
                elif len(step_processers) == 1:
                   #print(f"\t\t\tContact '{contact_name}' is in step processors. Removing from citRespParty")
                    if contact_name != citRespParty_rpIndName and contact_email != citRespParty_eMailAdd:
                        pass
                        # non_empty_citRespParty.getparent().remove(non_empty_citRespParty)
                    else:
                        pass
                del step_processers
                del contact_name, contact_email
                del non_empty_citRespParty
            del non_empty_citRespPartys
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #####
        prefered_citRespParty = target_root.xpath(f"./dataIdInfo/idCitation/citRespParty[./rpIndName[text()='{mdContact_rpIndName}'] and ./rpCntInfo/cntAddress/eMailAdd[text()='{mdContact_eMailAdd}']]")
        #print(len(prefered_citRespParty))
        if len(prefered_citRespParty) == 0:
            #print(len(prefered_citRespParty))
            pass
        elif len(prefered_citRespParty) == 1:
            #print(len(prefered_citRespParty))
            pass
        elif len(prefered_citRespParty) > 1:
            #print(len(prefered_citRespParty))
            for i in range(1, len(prefered_citRespParty)):
                prefered_citRespParty[i].getparent().remove(prefered_citRespParty[i])
                del i
            pass
        else:
            pass
        del prefered_citRespParty
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #####
        del citRespPartys

       #print(f"\tdistorCont Section")
        distorConts = target_tree.xpath("./distInfo/distributor/distorCont")
       #print(f"\t\tdistorConts: {len(distorConts)}")
        if len(distorConts) == 0:
           #print("\tMissing the citRespParty element. Inserting prefered contact element")
            new_contact_tree = contacts_xml_tree.xpath(f"//contact[./rpIndName[text()='{distorCont_rpIndName}'] and ./rpCntInfo/cntAddress/eMailAdd[text()='{distorCont_eMailAdd}'] and ./editorSave[text()='True']]")
            new_contact = copy.deepcopy(new_contact_tree[0])
            new_contact.tag = "distorCont"
            _xml = f'<role><RoleCd value="005"></RoleCd></role>'
            _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
            new_contact.insert(100, _root)
            del _root, _xml
            #target_root.find("./dataIdInfo/idCitation").insert(dataIdInfo_dict["citRespParty"], new_contact)
            del new_contact, new_contact_tree
        del distorConts

        distorConts = target_root.xpath(f"./distInfo/distributor/distorCont")
        if len(distorConts) >= 1:
            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #####
            prefered_distorCont = target_root.xpath(f"./distInfo/distributor/distorCont[./rpIndName[text()='{distorCont_rpIndName}'] and ./rpCntInfo/cntAddress/eMailAdd[text()='{distorCont_eMailAdd}']]")
           #print(f"\t\tprefered_citRespParty: {len(prefered_distorCont)}")
            if len(prefered_distorCont) == 0:
                new_contact_tree = contacts_xml_tree.xpath(f"//contact[./rpIndName[text()='{distorCont_rpIndName}'] and ./rpCntInfo/cntAddress/eMailAdd[text()='{citRespParty_eMailAdd}'] and ./editorSave[text()='True']]")
                new_contact = copy.deepcopy(new_contact_tree[0])
                new_contact.tag = "distorCont"
                _xml = f'<role><RoleCd value="005"></RoleCd></role>'
                _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
                new_contact.insert(100, _root)
                del _root, _xml
                target_root.find("./distInfo/distributor").insert(distInfo_dict["distorCont"], new_contact)
                del new_contact, new_contact_tree
            elif len(prefered_distorCont) == 1:
                #print(len(prefered_distorCont))
                pass
            elif len(prefered_distorCont) > 1:
                #print(f"\t\tprefered_citRespParty: {len(prefered_distorCont)}")
                pass
            else:
                pass
            del prefered_distorCont
            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #####

            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #####
            empty_distorConts = [mdC for mdC in target_root.xpath(f"./distInfo/distributor/distorCont") if len(mdC) == 0]
           #print(f"\t\tempty_distorConts: {len(empty_distorConts)}")
            for empty_distorCont in empty_distorConts:
                new_contact_tree = contacts_xml_tree.xpath(f"//contact[./rpIndName[text()='{distorCont_rpIndName}'] and ./rpCntInfo/cntAddress/eMailAdd[text()='{distorCont_eMailAdd}'] and ./editorSave[text()='True']]")
                new_contact = copy.deepcopy(new_contact_tree[0])
                new_contact.tag = "distorCont"
                _xml = f'<role><RoleCd value="005"></RoleCd></role>'
                _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
                new_contact.insert(100, _root)
                del _root, _xml
                target_root.find("./distInfo/distributor").replace(empty_distorCont, new_contact)
                del new_contact, new_contact_tree
                del empty_distorCont
            del empty_distorConts
            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #####

            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #####
            non_empty_distorConts = [mdC for mdC in target_root.xpath(f"./distInfo/distributor/distorCont") if len(mdC) != 0]
           #print(f"\t\tnon_empty_citRespPartys: {len(non_empty_distorConts)}")
            for non_empty_distorCont in non_empty_distorConts:
                #print(etree.tostring(non_empty_distorCont, encoding='UTF-8', method='xml', pretty_print=True).decode())
                contact_name = non_empty_distorCont.find("./rpIndName").text if non_empty_distorCont.find("rpIndName") is not None else None
                contact_email = non_empty_distorCont.find("./rpCntInfo/cntAddress/eMailAdd").text if non_empty_distorCont.find("rpCntInfo/cntAddress/eMailAdd") is not None else None
               #print(f"\t\tName and email: {contact_name}, {contact_email}")

                step_processers = target_root.xpath(f"./dqInfo/dataLineage/prcStep/stepProc[./rpIndName[text()='{contact_name}'] or ./rpCntInfo/cntAddress/eMailAdd[text()='{contact_email}']]")
                if len(step_processers) == 0:
                   #print(f"\t\t\tContact '{contact_name}' is not in step processors")
                    _non_empty_distorCont = copy.deepcopy(non_empty_distorCont)
                    _non_empty_distorCont.tag = "stepProc"
                    _non_empty_distorCont.find(f"./role/RoleCd").set('value', "009")

                    empty_step_procs = target_root.xpath(f"./dqInfo/dataLineage/prcStep/stepProc[./rpIndName[not(text())] and ./rpCntInfo/cntAddress/eMailAdd[not(text())]]")
                    if len(empty_step_procs) == 0:
                        prcStep = target_root.xpath(f"./dqInfo/dataLineage/prcStep")[0]
                        prcStep.insert(-1, _non_empty_distorCont)
                        del prcStep
                        if contact_name != distorCont_rpIndName and contact_email != distorCont_eMailAdd:
                            non_empty_distorCont.getparent().remove(non_empty_distorCont)
                        else:
                            pass
                    elif len(empty_step_procs) == 1:
                        empty_step_procs[0].getparent().replace(empty_step_procs[0], _non_empty_distorCont)
                    else:
                        pass
                    del _non_empty_distorCont
                    del empty_step_procs
                elif len(step_processers) == 1:
                   #print(f"\t\t\tContact '{contact_name}' is in step processors. Removing from distorCont")
                    if contact_name != distorCont_rpIndName and contact_email != distorCont_eMailAdd:
                        pass
                        # non_empty_distorCont.getparent().remove(non_empty_distorCont)
                    else:
                        pass
                del step_processers
                del contact_name, contact_email
                del non_empty_distorCont
            del non_empty_distorConts
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #####
        prefered_distorCont = target_root.xpath(f"./distInfo/distributor/distorCont[./rpIndName[text()='{mdContact_rpIndName}'] and ./rpCntInfo/cntAddress/eMailAdd[text()='{mdContact_eMailAdd}']]")
        #print(len(prefered_distorCont))
        if len(prefered_distorCont) == 0:
            #print(len(prefered_distorCont))
            pass
        elif len(prefered_distorCont) == 1:
            #print(len(prefered_distorCont))
            pass
        elif len(prefered_distorCont) > 1:
            #print(len(prefered_distorCont))
            for i in range(1, len(prefered_distorCont)):
                prefered_distorCont[i].getparent().remove(prefered_distorCont[i])
                del i
            pass
        else:
            pass
        del prefered_distorCont
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #####
        del distorConts

        for distorCont in target_root.xpath(f"./distInfo/distributor/distorCont"):
            #print(etree.tostring(distorCont, encoding='UTF-8', method='xml', pretty_print=True).decode())
            del distorCont

        for idCitation in target_root.xpath(f"./dataIdInfo/idCitation"):
            #print(etree.tostring(idCitation, encoding='UTF-8', method='xml', pretty_print=True).decode())
            del idCitation

        for idPoC in target_root.xpath(f"./dataIdInfo/idPoC"):
            #print(etree.tostring(idPoC, encoding='UTF-8', method='xml', pretty_print=True).decode())
            del idPoC

        for prcStep in target_root.xpath(f"./dqInfo/dataLineage/prcStep"): # /stepProc
            #print(etree.tostring(prcStep, encoding='UTF-8', method='xml', pretty_print=True).decode())
            del prcStep

        for mdContact in target_root.xpath(f"./mdContact"):
            #print(etree.tostring(mdContact, encoding='UTF-8', method='xml', pretty_print=True).decode())
            del mdContact

##       #print(f"\tsrcCitatns")
##        srcCitatns = target_root.xpath(f"./dqInfo/dataLineage/dataSource/srcCitatn[./rpIndName[text()!='{srcCitatn_rpIndName}'] and ./rpCntInfo/cntAddress/eMailAdd[text()!='{srcCitatn_eMailAdd}'] and ./editorSave[text()='True']]")
##        if srcCitatns is not None and len(srcCitatns) >= 1 and len(srcCitatns[0]) > 0:
##            for srcCitatn in srcCitatns:
##                #print(etree.tostring(srcCitatns, encoding='UTF-8', method='xml', pretty_print=True).decode())
##                contact_name  = srcCitatn.find("rpIndName").text if srcCitatn.find("rpIndName") is not None else None
##                contact_email = srcCitatn.find("rpCntInfo/cntAddress/eMailAdd").text if srcCitatn.find("rpCntInfo/cntAddress/eMailAdd") is not None else None
##                #print(contact_name, contact_email)
##                if contact_name is not None and contact_email is not None :
##                    pass
##                    print(f"\t\tName and email: {contact_name}, {contact_email}")
##                    print(f"\t\t\t{target_root.getpath(srcCitatn)}\n")
##                    step_processers = target_root.xpath(f"//prcStep/stepProc[./rpIndName[text()='{contact_name}'] and ./rpCntInfo/cntAddress/eMailAdd[text()='{contact_email}'] and ./editorSave[text()='True']]")
##                    if step_processers is not None and len(step_processers) == 1:
##                        pass
##                        print(f"\t\t{srcCitatn.tag} Contact in Step Processors")
##                    if step_processers is not None and len(step_processers) == 0:
##                        print(f"\t\t{srcCitatn.tag} Contact is not in Step Processors. Need to copy over")
##                        _step_processers = target_root.xpath(f"//prcStep/stepProc")
##                        #print(_step_processers)
##                        #print(_step_processers.getparent())
##                        _srcCitatn = copy.deepcopy(srcCitatn)
##                        _srcCitatn.tag = "stepProc"
##                        _step_processers.getparent().insert(10, _srcCitatn)
##                        del _srcCitatn
##                        del _step_processers
##                        new_contact_tree = contacts_xml_tree.xpath(f"//contact[./rpIndName[text()='{srcCitatn_rpIndName}'] and ./rpCntInfo/cntAddress/eMailAdd[text()='{srcCitatn_eMailAdd}'] and ./editorSave[text()='True']]")
##                        new_contact = copy.deepcopy(new_contact_tree[0])
##                        new_contact.tag = "srcCitatn"
##                        _xml = f'<role><RoleCd value="008"></RoleCd></role>'
##                        _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
##                        new_contact.insert(100, _root)
##                        del _root, _xml
##                        srcCitatn.getparent().replace(srcCitatn, new_contact)
##                        del new_contact, new_contact_tree
##                    elif step_processers is not None and len(step_processers) > 1:
##                        print(f"\t\tToo many {srcCitatn.tag} Contact in Step Processors.")
##                        _srcCitatn = copy.deepcopy(srcCitatn)
##                        _srcCitatn.tag = "stepProc"
##                        step_processers.getparent().insert(10, _srcCitatn)
##                    del step_processers
##                elif contact_name is None and contact_email is None :
##                    print(f"\t\tContact is empty in {srcCitatn.tag}. Name and email: {contact_name}, {contact_email}")
##                    new_contact_tree = contacts_xml_tree.xpath(f"//contact[./rpIndName[text()='{srcCitatn_rpIndName}'] and ./rpCntInfo/cntAddress/eMailAdd[text()='{srcCitatn_eMailAdd}'] and ./editorSave[text()='True']]")
##                    new_contact = copy.deepcopy(new_contact_tree[0])
##                    new_contact.tag = "srcCitatn"
##                    _xml = f'<role><RoleCd value="008"></RoleCd></role>'
##                    _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
##                    new_contact.insert(100, _root)
##                    del _root, _xml
##                    srcCitatn.getparent().replace(srcCitatn, new_contact)
##                    del new_contact, new_contact_tree
##                del contact_name, contact_email
##                del srcCitatn
##        del srcCitatns
##        for srcCitatn in target_root.xpath(f"./dqInfo/dataLineage/dataSource/srcCitatn"):
##            #print(etree.tostring(srcCitatn, encoding='UTF-8', method='xml', pretty_print=True).decode())
##            del srcCitatn

##        <dataLineage>
##            <statement>[Enter a thorough lineage statement detailing how range was created. This should provide a description of all sources and data layer inputs including documentation of how they were used. Further this should document any process steps used to create the range]</statement>
##            <dataSource type="">
##                <srcDesc>[Provide a description of the data sources used]</srcDesc>
##                <srcMedName>
##                    <MedNameCd value="015"/>
##                </srcMedName>
##                <srcCitatn>




##                RoleCd_dict = {"001" : "Resource Provider", "002" : "Custodian",
##                               "003" : "Owner",             "004" : "User",
##                               "005" : "Distributor",       "006" : "Originator",
##                               "007" : "Point of Contact",  "008" : "Principal Investigator",
##                               "009" : "Processor",         "010" : "Publisher",
##                               "011" : "Author",            "012" : "Collaborator",
##                               "013" : "Editor",            "014" : "Mediator",
##                               "015" : "Rights Holder",}


##                contact_dict = {"citRespParty" : [{"role"  : "Custodian",         "rpIndName" : "Nikki Wildart",       "eMailAdd" : "nikki.wildart@noaa.gov"},],
##                                 "idPoC"        : [{"role"  : "Point of Contact", "rpIndName" : "Nikki Wildart",       "eMailAdd" : "nikki.wildart@noaa.gov"},],
##                                 "distorCont"   : [{"role"  : "Distributor",      "rpIndName" : "Nikki Wildart",       "eMailAdd" : "nikki.wildart@noaa.gov"},],
##                                 "mdContact"    : [{"role"  : "Author",           "rpIndName" : "Nikki Wildart",       "eMailAdd" : "nikki.wildart@noaa.gov"},],
##                                 "srcCitatn"    : [{"role"  : "Author",           "rpIndName" : "Nikki Wildart",       "eMailAdd" : "nikki.wildart@noaa.gov"},],
##                                 "stepProc"     : [{"role" : "Processor",         "rpIndName" : "Nikki Wildart",       "eMailAdd" : "nikki.wildart@noaa.gov"},
##                                                   {"role" : "Processor",         "rpIndName" : "Dan Lawson",          "eMailAdd" : "dan.lawson@noaa.gov"},
##                                                   {"role" : "Processor",         "rpIndName" : "Jeffrey A. Seminoff", "eMailAdd" : "jeffrey.seminoff@noaa.gov"},
##                                                   {"role" : "Processor",         "rpIndName" : "Jennifer Schultz",    "eMailAdd" : "jennifer.schultz@noaa.gov"},
##                                                   {"role" : "Processor",         "rpIndName" : "Jonathan Molineaux",  "eMailAdd" : "jonathan.molineaux@noaa.gov"},
##                                                   {"role" : "Processor",         "rpIndName" : "Marc Romano",         "eMailAdd" : "marc.romano@noaa.gov"},
##                                                   {"role" : "Processor",         "rpIndName" : "Susan Wang",          "eMailAdd" : "susan.wang@noaa.gov"},
##                                                 ],}

##        for child in target_root.xpath("/metadata"):
##            child[:] = sorted(child, key=lambda x: root_dict[x.tag])
##            del child
##
##        for child in target_root.xpath("/metadata/Esri"):
##            child[:] = sorted(child, key=lambda x: esri_dict[x.tag])
##            del child
##
##        for child in target_root.xpath("/metadata/dataIdInfo"):
##            child[:] = sorted(child, key=lambda x: dataIdInfo_dict[x.tag])
##            del child
##
##        for child in target_root.xpath("/metadata/dqInfo"):
##            child[:] = sorted(child, key=lambda x: dqInfo_dict[x.tag])
##            del child

        # No changes needed below
        #print(etree.tostring(target_tree, encoding='UTF-8', method='xml', pretty_print=True).decode())
        etree.indent(target_tree, space='    ')
        dataset_md_xml = etree.tostring(target_tree, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True)

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

        # Declared Variables
        del CreaDateTime, ModDateTime
        #del xml_file
        del dataset_name
        del contacts_xml_tree, contacts_xml_root
        del mdContact_role, mdContact_eMailAdd, mdContact_rpIndName
        del citRespParty_rpIndName, citRespParty_eMailAdd, citRespParty_role
        del idPoC_rpIndName, idPoC_eMailAdd, idPoC_role
        del srcCitatn_rpIndName, srcCitatn_eMailAdd, srcCitatn_role
        del distorCont_rpIndName, distorCont_eMailAdd, distorCont_role
        del dqInfo_dict, dataIdInfo_dict, esri_dict, root_dict, tpCat_dict
        del distInfo_dict
        del contact_dict, RoleCd_dict
        del project_folder, scratch_folder
        del project_gdb

        # Declared Variables
        del target_tree, target_root
        # Imports
        del StringIO, BytesIO, etree, md, copy
        # Functiona Parameters
        del dataset_path

    except Exception:
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

def update_eainfo_xml_elements(dataset_path=""):
    try:
        # Imports
        from lxml import etree
        from io import StringIO, BytesIO
        import copy
        from arcpy import metadata as md

        arcpy.env.overwriteOutput          = True
        arcpy.env.parallelProcessingFactor = "100%"

        project_gdb    = os.path.dirname(dataset_path)
        project_folder = os.path.dirname(project_gdb)
        scratch_folder = rf"{project_folder}\Scratch"

        arcpy.env.workspace        = project_gdb
        arcpy.env.scratchWorkspace = rf"{scratch_folder}\scratch.gdb"

        import json
        json_path = rf"{project_folder}\root_dict.json"
        with open(json_path, "r") as json_file:
            root_dict = json.load(json_file)
        json_path = rf"{project_folder}\esri_dict.json"
        with open(json_path, "r") as json_file:
            esri_dict = json.load(json_file)
        json_path = rf"{project_folder}\dataIdInfo_dict.json"
        with open(json_path, "r") as json_file:
            dataIdInfo_dict = json.load(json_file)
        json_path = rf"{project_folder}\contact_dict.json"
        with open(json_path, "r") as json_file:
            contact_dict = json.load(json_file)
        json_path = rf"{project_folder}\dqInfo_dict.json"
        with open(json_path, "r") as json_file:
            dqInfo_dict = json.load(json_file)
        json_path = rf"{project_folder}\RoleCd_dict.json"
        with open(json_path, "r") as json_file:
            RoleCd_dict = json.load(json_file)
        json_path = rf"{project_folder}\tpCat_dict.json"
        with open(json_path, "r") as json_file:
            tpCat_dict = json.load(json_file)
        del json_file
        del json_path
        del json

        contacts_xml = rf"{os.environ['USERPROFILE']}\Documents\ArcGIS\Descriptions\contacts.xml"
        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
        contacts_xml_tree = etree.parse(contacts_xml, parser=parser) # To parse from a string, use the fromstring() function instead.
        del parser
        del contacts_xml
        contacts_xml_root = contacts_xml_tree.getroot()
        #etree.indent(contacts_xml_root, space="  ")
        #print(etree.tostring(contacts_xml_root, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())

        xml_file = rf"{project_folder}\eainfo.xml"
        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
        source_tree = etree.parse(xml_file, parser=parser)
        source_root = source_tree.getroot()
        del parser
        del xml_file

        dataset_md = md.Metadata(dataset_path)
        dataset_md.synchronize("ALWAYS")
        dataset_md.save()
        dataset_md.reload()
        dataset_md_xml = dataset_md.xml
        del dataset_md

        # Parse the XML
        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
        target_tree = etree.parse(StringIO(dataset_md_xml), parser=parser)
        target_root = target_tree.getroot()
        del parser, dataset_md_xml

        dataset_name = os.path.basename(dataset_path)
        print(f"Processing Entity Attributes for dataset: '{dataset_name}'")

        # Source XML
        source_eainfo = source_root.xpath("./eainfo")[0]
        #print(etree.tostring(source_eainfo, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
        # Target XML
        target_eainfo = target_root.xpath("./eainfo")[0]
        #print(etree.tostring(target_eainfo, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())

        # Step 1 update the detailed Name attribute element
        source_eainfo_detailed = source_root.xpath("./eainfo/detailed")[0]
        target_eainfo_detailed = target_root.xpath("./eainfo/detailed")[0]
        source_eainfo_detailed.attrib["Name"] = target_eainfo_detailed.get("Name")
        #print(etree.tostring(source_eainfo_detailed, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
        #print(etree.tostring(target_eainfo_detailed, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
        del target_eainfo_detailed, source_eainfo_detailed

        # Step 2 update the enttyp element
        source_eainfo_detailed_enttyp = source_root.xpath("./eainfo/detailed/enttyp")[0]
        #print(etree.tostring(source_eainfo_detailed_enttyp, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
        target_eainfo_detailed_enttyp = target_root.xpath("./eainfo/detailed/enttyp")[0]
        #print(etree.tostring(target_eainfo_detailed_enttyp, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
        source_eainfo_detailed_enttyp.getparent().replace(source_eainfo_detailed_enttyp, target_eainfo_detailed_enttyp)
        source_eainfo_detailed_enttyp = source_root.xpath("./eainfo/detailed/enttyp")[0]
        #print(etree.tostring(source_eainfo_detailed_enttyp.getparent().getparent(), encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
        del target_eainfo_detailed_enttyp, source_eainfo_detailed_enttyp

        # Step 3
        #print(etree.tostring(source_eainfo, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
        #print(etree.tostring(source_eainfo, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
        target_eainfo.getparent().replace(target_eainfo, source_eainfo)
        del target_eainfo

        target_eainfo = target_root.xpath("./eainfo")[0]
        #print(etree.tostring(target_eainfo, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())

        del target_eainfo, source_eainfo

        for child in target_root.xpath("/metadata"):
            child[:] = sorted(child, key=lambda x: root_dict[x.tag])
            del child

        for child in target_root.xpath("/metadata/Esri"):
            child[:] = sorted(child, key=lambda x: esri_dict[x.tag])
            del child

        for child in target_root.xpath("/metadata/dataIdInfo"):
            child[:] = sorted(child, key=lambda x: dataIdInfo_dict[x.tag])
            del child

        for child in target_root.xpath("/metadata/dqInfo"):
            child[:] = sorted(child, key=lambda x: dqInfo_dict[x.tag])
            del child

        # No changes needed below
        #print(etree.tostring(target_tree, encoding='UTF-8', method='xml', pretty_print=True).decode())
        etree.indent(target_tree, space='    ')
        dataset_md_xml = etree.tostring(target_tree, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True)

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

        # Declared Variables
        del dataset_name
        del contacts_xml_tree, contacts_xml_root
        del dqInfo_dict, dataIdInfo_dict, esri_dict, root_dict, tpCat_dict
        del contact_dict, RoleCd_dict
        del project_folder, scratch_folder
        del project_gdb

        # Declared Variables
        del source_tree, source_root
        del target_tree, target_root
        # Imports
        del StringIO, BytesIO, etree, md, copy
        # Functiona Parameters
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

def add_update_dates(dataset_path=""):
    try:
        # Imports
        from lxml import etree
        from io import StringIO, BytesIO
        import copy
        from arcpy import metadata as md

        arcpy.env.overwriteOutput          = True
        arcpy.env.parallelProcessingFactor = "100%"

        #print(dataset_path)
        dataset_name = os.path.basename(dataset_path)
        print(f"Processing Add/Update Dates for dataset: '{dataset_name}'")
        #print(f"\tDataset Location: {os.path.basename(os.path.dirname(dataset_path))}")

        dataset_md = md.Metadata(dataset_path)
        dataset_md.synchronize("ALWAYS")
        dataset_md.save()
        dataset_md.reload()
        dataset_md_xml = dataset_md.xml
        del dataset_md

        # Parse the XML
        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
        target_tree = etree.parse(StringIO(dataset_md_xml), parser=parser)
        target_root = target_tree.getroot()
        del parser, dataset_md_xml

        CreaDate = target_root.xpath(f"//Esri/CreaDate")[0].text
        CreaTime = target_root.xpath(f"//Esri/CreaTime")[0].text
        #print(CreaDate, CreaTime)
        CreaDateTime = f"{CreaDate[:4]}-{CreaDate[4:6]}-{CreaDate[6:]}T{CreaTime[:2]}:{CreaTime[2:4]}:{CreaTime[4:6]}"
        #print(f"\tCreaDateTime: {CreaDateTime}")
        #del CreaDateTime
        del CreaDate, CreaTime
        ModDate = target_root.xpath(f"//Esri/ModDate")[0].text
        ModTime = target_root.xpath(f"//Esri/ModTime")[0].text
        #print(ModDate, ModTime)
        ModDateTime = f"{ModDate[:4]}-{ModDate[4:6]}-{ModDate[6:]}T{ModTime[:2]}:{ModTime[2:4]}:{ModTime[4:6]}"
        #print(f"\tModDateTime: {ModDateTime}")
        #del ModDateTime
        del ModDate, ModTime

        dates = target_tree.xpath(f"//date")
        count=0
        count_dates = len(dates)
        for date in dates:
            #_date = copy.deepcopy(date)
            count+=1

            createDate = date.xpath(f"./createDate")
            #print(f"Element list:  '{createDate}'")
            #print(f"Element count: '{len(createDate)}'")
            #print(len(createDate[0].text))
            #print(type(createDate[0].text))
            if not len(createDate):
                _xml = f"<createDate>{CreaDateTime}</createDate>"
                _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
                date.insert(0, _root)
                del _root, _xml
            elif len(createDate) and createDate[0].text is not None:
                pass
                #print(f"createDate exists and has content '{createDate[0].text}'")
                #print(etree.tostring(createDate[0], encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
            elif len(createDate) and createDate[0].text is None:
                #print(f"createDate exists and but does not have content.")
                createDate[0].text = CreaDateTime
                date.insert(0, createDate[0])
            del createDate

            pubDate = date.xpath(f"./pubDate")
            if not len(pubDate):
                _xml = f"<pubDate>{CreaDateTime}</pubDate>"
                _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
                date.insert(0, _root)
                del _root, _xml
            if len(pubDate) and pubDate[0].text is not None:
                pass
                #print(f"pubDate exists and has content '{pubDate[0].text}'")
                #print(etree.tostring(pubDate[0], encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
            elif len(pubDate) and pubDate[0].text is None:
                #print(f"pubDate exists and but does not have content.")
                pubDate[0].text = CreaDateTime
                date.insert(1, pubDate[0])
            del pubDate

            reviseDate = date.xpath(f"./reviseDate")
            if not len(reviseDate):
                _xml = f"<reviseDate>{ModDateTime}</reviseDate>"
                _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
                date.insert(0, _root)
                del _root, _xml
            if len(reviseDate) and reviseDate[0].text is not None:
                pass
                #print(f"reviseDate exists and has content '{reviseDate[0].text}'")
                #print(etree.tostring(reviseDate[0], encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
            elif len(reviseDate) and reviseDate[0].text is None:
                #print(f"reviseDate exists and but does not have content.")
                reviseDate[0].text = ModDateTime
                date.insert(2, reviseDate[0])
            del reviseDate

##            if len(createDate) == 0:
##                _xml = f"<createDate>{CreaDateTime}</createDate>"
##                _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
##                date.insert(0, _root)
##                del _root, _xml
##            elif len(createDate) == 1:
##                if createDate[0].text:
##                    createDate[0].text = createDate[0].text
##                elif not createDate[0].text:
##                    createDate[0].text = CreaDateTime
##                else:
##                    pass
##            else:
##                pass
            #print(etree.tostring(createDate[0], encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
##            pubDate = date.xpath(f"./date/pubDate")
##            if len(pubDate) == 0:
##                _xml = f"<pubDate>{CreaDateTime}</pubDate>"
##                _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
##                date.insert(0, _root)
##                del _root, _xml
##            elif len(pubDate) == 1:
##                if pubDate[0].text:
##                    pubDate[0].text = pubDate[0].text
##                elif not pubDate[0].text:
##                    pubDate[0].text = CreaDateTime
##                else:
##                    pass
##            else:
##                pass
##            del pubDate
##
##            try:
##                revisedDate = date.xpath(f"./date/revisedDate")[0]
##                revisedDate.tag = "reviseDate"
##                del revisedDate
##            except:
##                pass
##
##            reviseDate = date.xpath(f"./date/reviseDate")
##            if len(reviseDate) == 0:
##                _xml = f"<reviseDate>{CreaDateTime}</reviseDate>"
##                _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
##                date.insert(0, _root)
##                del _root, _xml
##            elif len(reviseDate) == 1:
##                if reviseDate[0].text:
##                    reviseDate[0].text = reviseDate[0].text
##                elif not reviseDate[0].text:
##                    reviseDate[0].text = ModDateTime
##                else:
##                    pass
##            else:
##                pass
##            del reviseDate

##            date.getparent().replace(date, _date)

            #print(etree.tostring(date, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())

            del date
        del count, count_dates
        del dates

        dates = target_root.xpath(f"//date")
        count=0
        count_dates = len(dates)
        for date in dates:
            count+=1
            #print(f"\tDate: {count} of {count_dates}")
            #print(f"\t\tCreaDateTime: {CreaDateTime}")
            #print(f"\t\tModDateTime:  {ModDateTime}")
            #print(date.getroottree().getpath(date))
            #print(etree.tostring(date, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
            del date
        del count, count_dates
        del dates

        # No changes needed below
        #print(etree.tostring(target_tree, encoding='UTF-8', method='xml', pretty_print=True).decode())
        etree.indent(target_root, space='    ')
        dataset_md_xml = etree.tostring(target_tree, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True)

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

        del dataset_name, target_tree, target_root

        # Declared Variables
        del CreaDateTime, ModDateTime
        # Imports
        del etree, StringIO, BytesIO, copy, md
        # Function Parameters
        del dataset_path

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

def add_update_titles(dataset_path=""):
    try:
        # Imports
        from lxml import etree
        from io import StringIO, BytesIO
        import copy
        from arcpy import metadata as md
        # Project modules
        #from src.project_tools import pretty_format_xml_file

        arcpy.env.overwriteOutput          = True
        arcpy.env.parallelProcessingFactor = "100%"

        #print(dataset_path)
        dataset_name = os.path.basename(dataset_path)
        print(f"Processing Add/Update Titles for dataset: '{dataset_name}'")
        #print(f"\tDataset Location: {os.path.basename(os.path.dirname(dataset_path))}")

        dataset_md = md.Metadata(dataset_path)
        dataset_md_xml = dataset_md.xml
        del dataset_md

        # Parse the XML
        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
        target_tree = etree.parse(StringIO(dataset_md_xml), parser=parser)
        target_root = target_tree.getroot()
        del parser, dataset_md_xml

        elements_with_titles = target_tree.xpath(f"//*[./resTitle or ./resAltTitle or ./collTitle]")

        for element_with_a_title in elements_with_titles:

            element_path = element_with_a_title.getroottree().getpath(element_with_a_title)

            # resTitle
            #print(element_path)
            element = target_tree.xpath(f"{element_path}")[0]
            if len(element.xpath("./resTitle")) == 0:
                _xml = f"<resTitle>Update resTitle</resTitle>"
                _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
                element.insert(0, _root)
                del _root, _xml
            elif len(element.xpath("./resTitle")) == 1:
                resTitle = element.xpath(f"./resTitle")
                if resTitle[0].text:
                    resTitle[0].text = resTitle[0].text
                elif not resTitle[0].text:
                    element.xpath("./resTitle")[0].text = "Update resTitle"
                else:
                    pass
                del resTitle
            elif len(element.xpath("./resTitle")) > 1:
                raise Exception("too many resTitles")

            # resAltTitle
            if len(element.xpath("./resAltTitle")) == 0:
                _xml = f"<resAltTitle>Update resAltTitle</resAltTitle>"
                _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
                element.insert(1, _root)
                del _root, _xml
            elif len(element.xpath("./resAltTitle")) == 1:
                resAltTitle = element.xpath(f"./resAltTitle")
                if resAltTitle[0].text:
                    resAltTitle[0].text = resAltTitle[0].text
                elif not resAltTitle[0].text:
                    element.xpath("./resAltTitle")[0].text = "Update resAltTitle"
                else:
                    pass
                del resAltTitle
            elif len(element.xpath("./resAltTitle")) > 1:
                raise Exception("too many resAltTitle")

            # collTitle
            if len(element.xpath("./collTitle")) == 0:
                _xml = f"<collTitle>Update collTitle</collTitle>"
                _root = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))
                element.insert(3, _root)
                del _root, _xml
            elif len(element.xpath("./collTitle")) == 1:
                collTitle = element.xpath(f"./collTitle")
                if collTitle[0].text:
                    if "resAltTitle" in collTitle[0].text:
                        collTitle[0].text.replace("resAltTitle", "collTitle")
                    collTitle[0].text = collTitle[0].text
                elif not collTitle[0].text:
                    element.xpath("./collTitle")[0].text = "Update collTitle"
                else:
                    pass
                del collTitle
            elif len(element.xpath("./collTitle")) > 1:
                raise Exception("too many collTitle")
            else:
                pass
            #print(etree.tostring(element, encoding='UTF-8', method='xml', pretty_print=True).decode())
            del element
            del element_path

            resTitle = element_with_a_title.xpath("./resTitle")[0]
            resTitle.getparent().insert(0, resTitle)
            del resTitle
            resAltTitle = element_with_a_title.xpath("./resAltTitle")[0]
            resAltTitle.getparent().insert(1, resAltTitle)
            del resAltTitle
            collTitle = element_with_a_title.xpath("./collTitle")[0]
            collTitle.getparent().insert(2, collTitle)
            del collTitle
            date = element_with_a_title.xpath("./date")[0]
            date.getparent().insert(3, date)
            del date
            #citOnlineRes = element_with_a_title.xpath("./citOnlineRes")[0]
            #citOnlineRes.getparent().insert(4, citOnlineRes)
            #del citOnlineRes
            #print(etree.tostring(element_with_a_title, encoding='UTF-8', method='xml', pretty_print=True).decode())

            #print(etree.tostring(element_with_a_title, encoding='UTF-8', method='xml', pretty_print=True).decode())

            del element_with_a_title
        del elements_with_titles

        # No changes needed below
        #print(etree.tostring(target_tree, encoding='UTF-8', method='xml', pretty_print=True).decode())
        etree.indent(target_root, space='    ')
        dataset_md_xml = etree.tostring(target_tree, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True)

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

        # Declared Variables
        del target_tree, target_root
        del dataset_name
        # Imports
        del etree, StringIO, BytesIO, copy, md
        # Function Parameters
        del dataset_path

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

        # Points
        #for dataset_path in sorted([ds for ds in datasets if ds.endswith("AI_Sample_Locations") or ds.endswith("AI_IDW_Sample_Locations")]):
        #for dataset_path in sorted([ds for ds in datasets if ds.endswith("EBS_Sample_Locations") or ds.endswith("EBS_IDW_Sample_Locations")]):
        # Polylines
        #for dataset_path in sorted([ds for ds in datasets if ds.endswith("AI_Boundary") or ds.endswith("AI_IDW_Boundary")]):
        # Polygons
        #for dataset_path in sorted([ds for ds in datasets if ds.endswith("AI_Region") or ds.endswith("AI_IDW_Region")]):
        # Table
        # for dataset_path in sorted([ds for ds in datasets if ds.endswith("AI_Indicators") or ds.endswith("AI_IDW_Indicators")]):
        # Raster
        #for dataset_path in sorted([ds for ds in datasets if ds.endswith("AI_Bathymetry") or ds.endswith("AI_IDW_Bathymetry")]):
        #for dataset_path in sorted([ds for ds in datasets if ds.endswith("AI_Raster_Mask") or ds.endswith("AI_IDW_Raster_Mask")]):
        #for dataset_path in sorted([ds for ds in datasets if ds.endswith("AI_Raster_Mosaic") or ds.endswith("AI_IDW_Mosaic")]):
        #for dataset_path in sorted([ds for ds in datasets if any (ds.endswith(d) for d in ["Datasets", "AI_IDW_Extent_Points", "AI_IDW_Latitude", "AI_IDW_Raster_Mask"])]):
        #for dataset_path in sorted([ds for ds in datasets if any (ds.endswith(d) for d in ["Species_Filer", "EBS_IDW_Extent_Points", "EBS_IDW_Latitude", "EBS_IDW_Raster_Mask"])]):

        #for dataset_path in sorted([d for d in datasets if d.endswith("CoralFimbriaphylliaParadivisa_20240712")]):
        #for dataset_path in sorted([d for d in datasets if d.endswith("CoralLobedStar_20210730")]):
        #for dataset_path in sorted([d for d in datasets if d.endswith("CoralMountainousStar_20210801")]):
        #for dataset_path in sorted([d for d in datasets if d.endswith("SealGuadalupeFur_20210228")]):
        #for dataset_path in sorted([d for d in datasets if d.endswith("SealHawaiianMonk_20211011")]):
        #for dataset_path in sorted([d for d in datasets if d.endswith("SealRinged_20210228")]):
        # Has mcContact, but it is empty
        #for dataset_path in sorted([d for d in datasets if d.endswith("SealSpotted_20210228")]):
        # Missing: mdContact
        #for dataset_path in sorted([d for d in datasets if d.endswith("SeaTurtleGreen_20210129")]):
        # Missing: mdContact
        #for dataset_path in sorted([d for d in datasets if d.endswith("SeaTurtleLoggerhead_20210129")]):
        # Missing: mdContact
        #for dataset_path in sorted([d for d in datasets if d.endswith("SeaTurtleOliveRidley_20210129")]):
        # Missing: mdContact
        #for dataset_path in sorted([d for d in datasets if d.endswith("WhaleBlue_20201014")]):
        #for dataset_path in sorted([d for d in datasets if d.endswith("CoralElkhorn_20210712")]):
        #for dataset_path in sorted([d for d in datasets if d.endswith("SeaTurtleLeatherback_20210129")]):
        #for dataset_path in sorted([d for d in datasets if d.endswith("WhaleSperm_20211220")]):
        for dataset_path in sorted([d for d in datasets if d.endswith("AbaloneBlack_20210712")]):
        # has all three in stepProc
        #for dataset_path in sorted([d for d in datasets if d.endswith("AbaloneWhite_20210728")]):
        # Missing: mdContact
        #for dataset_path in sorted([d for d in datasets if d.endswith("WhaleFinback_20201215")]):
        # Missing: mdContact
        #for dataset_path in sorted([d for d in datasets if d.endswith("WhaleNorthPacificRight_20201015")]):
        #for dataset_path in sorted([d for d in datasets if d.endswith("SpeciesRangeTable20241212")]):
        # ALL
        #for dataset_path in sorted(datasets):
        #for dataset_path in sorted([d for d in datasets if not d.endswith("SpeciesRangeTable20241212")]):

            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
            InsertMissingElements = True
            if InsertMissingElements:
                insert_missing_elements(dataset_path)
            else:
                pass
            del InsertMissingElements

            # A keeper. Adds entity attribute details
            UpdateEaInfoXmlElements = False
            if UpdateEaInfoXmlElements:
                update_eainfo_xml_elements(dataset_path)
            else:
                pass
            del UpdateEaInfoXmlElements

            UpdateExistingContacts = False
            if UpdateExistingContacts:
                update_existing_contacts(dataset_path)
            else:
                pass
            del UpdateExistingContacts

            AddUpdateContacts = False
            if AddUpdateContacts:
                add_update_contacts(dataset_path=dataset_path)
            else:
                pass
            del AddUpdateContacts

            AddUpdateDates = False
            if AddUpdateDates:
                add_update_dates(dataset_path)
            else:
                pass
            del AddUpdateDates
            AddUpdateTitles = False
            if AddUpdateTitles:
                add_update_titles(dataset_path)
            else:
                pass
            del AddUpdateTitles
            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

            UpdateProcessSteps = False
            if UpdateProcessSteps:
                update_process_steps(dataset_path)
            else:
                pass
            del UpdateProcessSteps

            PrintTargetTree = False
            if PrintTargetTree:
                dataset_md = md.Metadata(dataset_path)
                dataset_md.synchronize("ALWAYS")
                dataset_md.save()
                dataset_md.reload()
                dataset_md_xml = dataset_md.xml
                del dataset_md
                # Parse the XML
                parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
                target_tree = etree.parse(StringIO(dataset_md_xml), parser=parser)
                target_root = target_tree.getroot()
                del parser, dataset_md_xml
                print(etree.tostring(target_tree, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
                del target_tree, target_root
            else:
                pass
            del PrintTargetTree

        CompactGDB = False
        if CompactGDB:
            print(f"Compact GDB")
            arcpy.management.Compact(project_gdb)
            print("\t"+arcpy.GetMessages().replace("\n", "\n\t")+"\n")
        else:
            pass
        del CompactGDB

        # Declared Varaiables
        del datasets, dataset_path
        # Imports
        del etree, StringIO, BytesIO, md
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
        #sys.path.append(os.path.dirname(__file__))
        sys.path.append(os.path.dirname(os.path.dirname(__file__)))

        # Imports

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

        # Declared Variables
        del contacts, collective_title
        del project_gdb, project_name, project_folder, base_project_folder

        # Imports

    except:
        traceback.print_exc()
    else:
        pass
    finally:
        pass
