"""
This module contains . . .

Requires : Python 3.11
           ArcGIS Pro 3.x

Copyright 2025 NMFS
Licensed under the Apache License, Version 2.0 (the 'License');
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an 'AS IS' BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
# Python Built-in's modules are loaded first
import os, sys
import traceback, inspect

def metadata_element_report(target_xml=""):
    try:
        # Imports
        from lxml import etree

        # Project modules
        from src.project_tools import pretty_format_xml_file

        target_xml_name = os.path.basename(target_xml)
        print(f"Target Metadata: {target_xml_name}", flush=True)
        #del target_xml_name

        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
        # Parse the XML
        target_tree = etree.parse(target_xml, parser=parser)
        target_root = target_tree.getroot()
        del parser
        #etree.indent(tree, space="    ")
        # Pretty print
        #target_xml_string = etree.tostring(target_tree, pretty_print=True, method='html', encoding='UTF-8').decode()
        #print(target_xml_string,flush=True); del target_xml_string

        print(f"\tProcessing: {target_xml_name}")

        children_tags = list()
        children = target_root.iterchildren()
        for child in children:
            #print(f"\t\t{child.tag}, {child.text}")
            if child.tag not in children_tags:
                children_tags.append(child.tag)
            del child
        del children

        #print(f"\t\t{list(set(children_tags))}")

        #del children_tags

##        etree.indent(target_root, space='    ')
##        xml_string = etree.tostring(target_tree, pretty_print=True, method='html', encoding='UTF-8').decode()
##        try:
##            with open(target_xml, "w") as f:
##                f.write(xml_string)
##            del f
##        except:
##            print(f"The metadata file: {os.path.basename(xml)} can not be overwritten!!")
##        del xml_string
##
##        pretty_format_xml_file(target_xml)

        # Declared Variabkes
        del target_xml_name
        del target_tree, target_root
        # Imports
        del etree, pretty_format_xml_file
        # Function parameters
        del target_xml

    except:
        traceback.print_exc()
    else:
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__') and key not in ["children_tags"]]
        if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        #return True
        return children_tags
    finally:
        del children_tags

def main(metadata_workspace=""):
    try:
        # Imports
        from time import gmtime, localtime, strftime, time
        # Set a start time so that we can see how log things take
        start_time = time()
        print(f"{'-' * 80}")
        print(f"Python Script:  {os.path.basename(__file__)}")
        print(f"Location:       {os.path.dirname(__file__)}")
        print(f"Python Version: {sys.version} Environment: {os.path.basename(sys.exec_prefix)}")
        print(f"{'-' * 80}\n")

        # if metadata_workspace is a folder, use os.listdir
        target_xmls = [rf"{metadata_workspace}\{f}" for f in os.listdir(rf"{metadata_workspace}") if f.endswith(".xml")]
        # else, use arcpy.List*

        GetUniqueListOfRootTags = False
        if GetUniqueListOfRootTags:
            children_tags = list()
            # For loop of target xml records
            for target_xml in target_xmls:
                tags = metadata_element_report(target_xml=target_xml)
                for tag in tags:
                    if tag not in children_tags:
                        children_tags.append(tag)
                    del tag
                del tags
                del target_xml
            print(f"\t\t{sorted(list(set(children_tags)))}")
            del children_tags
        # ['Binary', 'Esri', 'dataIdInfo', 'distInfo', 'dqInfo', 'eainfo', 'mdChar',
        #  'mdContact', 'mdDateSt', 'mdHrLv', 'mdHrLvName', 'mdLang', 'mdMaint',
        #  'mdStanName', 'mdStanVer', 'refSysInfo', 'spatRepInfo', 'spdoinfo']
        del GetUniqueListOfRootTags

        # Declared Variables
        del target_xmls

        # Function parameters
        del metadata_workspace

        # Elapsed time
        end_time = time()
        elapse_time =  end_time - start_time
        print(f"\n{'-' * 80}")
        print(f"Python script: {os.path.basename(__file__)} successfully completed {strftime('%a %b %d %I:%M %p', localtime())}")
        print(u"Elapsed Time {0} (H:M:S)".format(strftime("%H:%M:%S", gmtime(elapse_time))))
        print(f"{'-' * 80}")
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
        pass

if __name__ == '__main__':
    try:
        # Imports
        from datetime import date

        # Append the location of this scrip to the System Path
        #sys.path.append(os.path.dirname(__file__))
        sys.path.append(os.path.dirname(os.path.dirname(__file__)))

        today = date.today()
        date_string = today.strftime("%Y-%m-%d")

        project_folder  = rf"{os.path.dirname(os.path.dirname(__file__))}"
        #metadata_workspace = f"Export"
        #metadata_workspace = f"Export {date_string}"
        metadata_workspace = rf"{project_folder}\Export 2025-01-27"

        main(metadata_workspace=metadata_workspace)

        # Declared Variables
        del project_folder, metadata_workspace
        del today, date_string
        # Imports
        del date

    except:
        traceback.print_exc()
    else:
        pass
    finally:
        pass