#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john.f.kennedy
#
# Created:     15/01/2025
# Copyright:   (c) john.f.kennedy 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Python Built-in's modules are loaded first
import os, sys
import traceback, inspect

# Third-party modules are loaded second
import arcpy

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

def getSortValue(elem):
    from lxml import etree
    if isinstance(elem, etree._Comment):
        # sort comment by its content
        return elem.text
    else:
        # sort entities by tag and then by name
        #return elem.tag + elem.attrib.get('name','')
        return elem.tag

def export_metadata(project_gdb=""):
    try:
        # Imports
        from arcpy import metadata as md
        from lxml import etree
        from src.project_tools import pretty_format_xml_file

        # Use all of the cores on the machine
        arcpy.env.parallelProcessingFactor = "100%"
        arcpy.env.overwriteOutput = True

        # Define variables
        project_folder = os.path.dirname(project_gdb)
        scratch_folder = rf"{project_folder}\Scratch"
        scratch_gdb    = rf"{scratch_folder}\scratch.gdb"
        export_folder  = rf"{project_folder}\Export"

        # Set the workspace environment to local file geodatabase
        arcpy.env.workspace = project_gdb
        # Set the scratchWorkspace environment to local file geodatabase
        arcpy.env.scratchWorkspace = scratch_gdb

        # Clean-up variables
        del scratch_folder, scratch_gdb

        print(f"{'--Start' * 10}--\n")

        fcs = arcpy.ListFeatureClasses()

        print(f"Synchronize and export feature classes metadata from Project GDB\n",flush=True)
        for fc in sorted(fcs):
            print(f"Exporting the metadata record for: '{fc}'",flush=True)

            fc_path = rf"{project_gdb}\{fc}"

            export_xml_metadata_path = rf"{export_folder}\{fc}.xml"

            dataset_md = md.Metadata(fc_path)
            dataset_md.synchronize("ALWAYS")
            dataset_md.save()
            dataset_md.reload()
            dataset_md.saveAsXML(export_xml_metadata_path, "REMOVE_ALL_SENSITIVE_INFO")
            #if dataset_md.thumbnailUri:
            #    arcpy.management.Copy(dataset_md.thumbnailUri, rf"{export_folder}\{fc} Thumbnail.jpg")
            #    arcpy.management.Copy(dataset_md.thumbnailUri, rf"{export_folder}\{fc} Browse Graphic.jpg")
            del dataset_md
            #if arcpy.Exists(export_xml_metadata_path): pretty_format_xml_file(export_xml_metadata_path) #else: #    pass

            # https://stackoverflow.com/questions/78713666/find-the-index-of-a-child-in-lxml
            # Parse the XML
            parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
            # Parse the XML
            tree = etree.parse(export_xml_metadata_path,  parser=parser)
            del parser
            #tree = etree.parse(export_xml_metadata_path)
            root = tree.getroot()
            for parent in tree.xpath('//*[./*]'): # Search for parent elements
                parent[:] = sorted(parent, key=lambda x: getSortValue(x))
                del parent
            # https://lxml.de/apidoc/lxml.etree.html#lxml.etree.indent
            # import lxml.etree as ET
            # ET.indent(tree, space='    ')  # clean all indentations - use 4 spaces
            # ET.indent(tree, space='....')  # clean all indentations - use 4 dots - looks like TOC (Table Of Contents) in book :)
            # ET.indent(tree)   # clean all indentations - use (default) 2 spaces
            #etree.indent(tree, space='    ')
            #print(etree.tostring(tree, pretty_print=True, method='html', encoding='UTF-8').decode())
            #etree.indent(root, space='    ')
            #etree.dump(root)
            etree.indent(root, space='    ')
            xml_string = etree.tostring(tree, pretty_print=True, method='html', encoding='UTF-8').decode()
            try:
                with open(export_xml_metadata_path, "w") as f:
                    f.write(xml_string)
                del f
            except:
                arcpy.AddError(f"The metadata file: {os.path.basename(xml)} can not be overwritten!!")

            pretty_format_xml_file(export_xml_metadata_path)

            # Variables
            del xml_string
            del tree, root
            del export_xml_metadata_path
            del fc, fc_path

        del fcs
        del project_folder, export_folder

        print(f"\n{'--End' * 10}--",flush=True)

        # Imports
        del md, etree, pretty_format_xml_file
        # Function parameters
        del project_gdb

    #except Exception as e:
    #    raise Exception(e)
    #except arcpy.ExecuteWarning:
    #    arcpy.AddWarning(arcpy.GetMessages())
    #except arcpy.ExecuteError:
    #    arcpy.AddError(arcpy.GetMessages())
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

def main(project_folder=""):
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

        ExportMetadata = True
        if ExportMetadata:
            try:
                export_metadata(project_gdb=project_gdb)
            except Exception as e:
                print(e)
        del ExportMetadata

        # Variables
        del project_gdb

        # Imports

        # Function parameters
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
    finally:
        pass
        # Cleanup
        # arcpy.management.ClearWorkspaceCache()

if __name__ == '__main__':
    try:
        main(project_folder=rf"{os.path.dirname(os.path.dirname(__file__))}")
    except Warning as w:
        print(w)
