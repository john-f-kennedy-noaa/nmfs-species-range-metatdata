#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john.f.kennedy
#
# Created:     09/02/2025
# Copyright:   (c) john.f.kennedy 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os, sys  # built-ins first
import traceback
import importlib
import inspect

from lxml import etree
from io import StringIO

import arcpy  # third-parties second

def parse_xml_file_format_and_save(xml_file=""):
    try:
        root_dict = {"Esri"       :  0, "dataIdInfo" :  1, "mdChar"      :  2,
                     "mdContact"  :  3, "mdDateSt"   :  4, "mdFileID"    :  5,
                     "mdLang"     :  6, "mdMaint"    :  7, "mdHrLv"      :  8,
                     "mdHrLvName" :  9, "refSysInfo" : 10, "spatRepInfo" : 11,
                     "spdoinfo"   : 12, "dqInfo"     : 13, "distInfo"    : 14,
                     "eainfo"     : 15, "contInfo"   : 16, "spref"       : 17,
                     "spatRepInfo" : 18, "dataSetFn" : 19, "Binary"      : 100,}

        from lxml import etree
        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
        tree = etree.parse(xml_file, parser=parser) # To parse from a string, use the fromstring() function instead.
        del parser
        root = tree.getroot()
        for child in root.xpath("."):
            child[:] = sorted(child, key=lambda x: root_dict[x.tag])
            del child
        del root
        etree.indent(tree, space='   ')
        tree.write(xml_file, encoding="utf-8",  method='xml', xml_declaration=True, pretty_print=True)
        del tree
        del xml_file, etree
        del root_dict
    except:
        traceback.print_exc()
    else:
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        pass

def print_xml_file(xml_file=""):
    try:
        root_dict = {"Esri"       :  0, "dataIdInfo" :  1, "mdChar"      :  2,
                     "mdContact"  :  3, "mdDateSt"   :  4, "mdFileID"    :  5,
                     "mdLang"     :  6, "mdMaint"    :  7, "mdHrLv"      :  8,
                     "mdHrLvName" :  9, "refSysInfo" : 10, "spatRepInfo" : 11,
                     "spdoinfo"   : 12, "dqInfo"     : 13, "distInfo"    : 14,
                     "eainfo"     : 15, "contInfo"   : 16, "spref"       : 17,
                     "spatRepInfo" : 18, "dataSetFn" : 19, "Binary"      : 100,}

        from lxml import etree
        parser = etree.XMLParser(encoding='utf-8', remove_blank_text=True)
        tree = etree.parse(xml_file, parser=parser) # To parse from a string, use the fromstring() function instead.
        del parser
        root = tree.getroot()
        for child in root.xpath("."):
            child[:] = sorted(child, key=lambda x: root_dict[x.tag])
            del child
        del root
        etree.indent(tree, space='   ')
        print(etree.tostring(tree, encoding="utf-8",  method='xml', xml_declaration=True, pretty_print=True).decode())
        del tree
        del xml_file, etree
        del root_dict
    except:
        traceback.print_exc()
    else:
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        pass

def main():
    try:

        from lxml import etree

        xml = '''<metadata><mdContact>
            <editorSource>extermal</editorSource>
            <editorDigest>9cc0fe80de5687cc4d79f50f3a254f2c3ceb08ce</editorDigest>
            <rpIndName>Nikki Wildart</rpIndName>
            <rpOrgName>Office of Protected Resources, National Marine Fisheries Service</rpOrgName>
            <rpPosName>Biologist</rpPosName>
            <rpCntInfo>
                <cntAddress addressType="both">
                    <delPoint>1315 East West Highway</delPoint>
                    <city>Silver Spring</city>
                    <adminArea>MD</adminArea>
                    <postCode>20910-3282</postCode>
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
                    <protocol>REST Service</protocol>
                    <orName>Fisheries OPR</orName>
                    <orDesc>NOAA Fisheries Office of Science and Technology</orDesc>
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
        </mdContact></metadata>'''

        from arcpy import metadata as md

        from src.project_tools import pretty_format_xml_file

        project_folder   = rf"{os.path.dirname(os.path.dirname(__file__))}"
        project_name     = "Metadata"
        project_gdb      = rf"{project_folder}\{project_name}.gdb"
        species_range_fc = rf"{project_gdb}\SpeciesRangeTemplate"

        # Create a new Metadata object and add some content to it
        new_md = md.Metadata()
        new_md.title             = 'My Title'
        new_md.tags              = 'Tag1, Tag2'
        new_md.summary           = 'My Summary'
        new_md.description       = 'My Description'
        new_md.credits           = 'My Credits'
        new_md.accessConstraints = 'My Access Constraints'

        out_xml = rf"{project_folder}\Export\temp.xml"
        new_md.saveAsXML(out_xml)

        parse_xml_file_format_and_save(xml_file=out_xml)
        #print_xml_file(xml_file=out_xml)
        #del out_xml

        dataset_md = md.Metadata(species_range_fc)
        # Synchronize the item's metadata now
        dataset_md.synchronize('ALWAYS')
        if not dataset_md.isReadOnly:
            dataset_md.copy(new_md)
            dataset_md.save()
        dataset_md.synchronize("SELECTIVE")
        dataset_md.save()
        del new_md

        species_range_fc_metadata_xml = rf"{project_folder}\Export\{os.path.basename(species_range_fc)}.xml"
        dataset_md.saveAsXML(species_range_fc_metadata_xml)
        parse_xml_file_format_and_save(xml_file=species_range_fc_metadata_xml)
        #print_xml_file(xml_file=species_range_fc_metadata_xml)
        del dataset_md
        del species_range_fc_metadata_xml

        # Import an xml file
        dataset_md = md.Metadata(species_range_fc)
        if not dataset_md.isReadOnly:
            dataset_md.importMetadata(out_xml, "ARCGIS_METADATA")
            dataset_md.save()
        dataset_md.synchronize("ALWAYS")
        dataset_md.save()
        #dataset_md.reload()

        species_range_fc_metadata_xml = rf"{project_folder}\Export\{os.path.basename(species_range_fc)}.xml"
        dataset_md.saveAsXML(species_range_fc_metadata_xml)
        parse_xml_file_format_and_save(xml_file=species_range_fc_metadata_xml)
        #print_xml_file(xml_file=species_range_fc_metadata_xml)
        del dataset_md
        del species_range_fc_metadata_xml

        del out_xml

        # Parse the XML
        eainfo_xml_file = rf"{project_folder}\eainfo.xml"
        parse_xml_file_format_and_save(xml_file=eainfo_xml_file)
        #print_xml_file(xml_file=eainfo_xml_file)

        # Import an xml file
        dataset_md = md.Metadata(species_range_fc)
        if not dataset_md.isReadOnly:
            dataset_md.importMetadata(eainfo_xml_file, "ARCGIS_METADATA")
            dataset_md.save()
            dataset_md.synchronize("OVERWRITE")
            dataset_md.save()
            dataset_md.reload()

        species_range_fc_metadata_xml = rf"{project_folder}\Export\{os.path.basename(species_range_fc)}.xml"
        dataset_md.saveAsXML(species_range_fc_metadata_xml)
        parse_xml_file_format_and_save(xml_file=species_range_fc_metadata_xml)
        #print_xml_file(xml_file=species_range_fc_metadata_xml)
        del dataset_md
        del species_range_fc_metadata_xml

        #dataset_md = md.Metadata(species_range_fc)
        # Not working
        # Import the standard-format metadata content to the target item
        #if not dataset_md.isReadOnly:
        #    dataset_md.importMetadata(etree.tostring(etree.fromstring(xml)))
        #    dataset_md.save()
        #    dataset_md.synchronize("CREATED")
        #    dataset_md.save()
        #    dataset_md.reload()

        #species_range_fc_metadata_xml = rf"{project_folder}\Export\{os.path.basename(species_range_fc)}.xml"
        #dataset_md.saveAsXML(species_range_fc_metadata_xml)
        #parse_xml_file_format_and_save(xml_file=species_range_fc_metadata_xml)
        #print_xml_file(xml_file=species_range_fc_metadata_xml)
        #del dataset_md

        _xml = r"{os.environ['USERPROFILE']}\Documents\ArcGIS\Projects\DisMap\ArcGIS-Analysis-Python\April 1 2023\Template Metadata\sample_locations_template.xml"
        #pretty_format_xml_file(_xml)
        del _xml

        _xml = r"{os.environ['USERPROFILE']}\Documents\ArcGIS\Projects\DisMap\ArcGIS-Analysis-Python\July 1 2024\conf_metadata.xml"
        #parse_xml_file_format_and_save(_xml)
        #print_xml_file(xml_file=_xml)

        #parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)  # lxml.etree only!
        root = etree.fromstring(xml)
        #print("After Copy")
        etree.indent(root, space="  ")
        #print(etree.tostring(root, encoding="utf-8",  method='xml', xml_declaration=True, pretty_print=True).decode())
        del root

        _xml = rf"{os.environ['USERPROFILE']}\Documents\ArcGIS\Descriptions\contacts.xml"
        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
        tree = etree.parse(_xml, parser=parser) # To parse from a string, use the fromstring() function instead.
        del parser
        root = tree.getroot()
        etree.indent(root, space="  ")
        #print(etree.tostring(root, encoding="utf-8",  method='xml', xml_declaration=True, pretty_print=True).decode())
        del root, _xml

##        root_dict = {"Esri"       :  0, "dataIdInfo" :  1, "mdChar"      :  2,
##                     "mdContact"  :  3, "mdDateSt"   :  4, "mdFileID"    :  5,
##                     "mdLang"     :  6, "mdMaint"    :  7, "mdHrLv"      :  8,
##                     "mdHrLvName" :  9, "refSysInfo" : 10, "spatRepInfo" : 11,
##                     "spdoinfo"   : 12, "dqInfo"     : 13, "distInfo"    : 14,
##                     "eainfo"     : 15, "Binary"     : 16,}
##
##        root = etree.fromstring(dataset_md.xml)
##        etree.indent(root, space="  ")
##        # Sort the XML
##        for child in root.xpath("."):
##            child[:] = sorted(child, key=lambda x: root_dict[x.tag])
##            del child
##        dataset_md.xml = etree.tostring(root, encoding='UTF-8').decode()
##        dataset_md.save()
##        dataset_md.reload()
##        del root
##
##        if not dataset_md.isReadOnly:
##            root = etree.fromstring(dataset_md.xml)
##            etree.indent(root, space="  ")
##            print(etree.tostring(root, pretty_print=True).decode())
##            del root

##        dataset_md.importMetadata(etree.XML(xml), "ARCGIS_METADATA")
##        dataset_md.save()
##        root = etree.fromstring(dataset_md.xml)
##        print("Species Range Template after Import Metadata")
##        etree.indent(root, space="  ")
##        print(etree.tostring(root, pretty_print=True).decode())
##        del root
##
##        dataset_md.synchronize("NOT_CREATED")
##        dataset_md.save()
##        dataset_md.reload()
##        root = etree.fromstring(dataset_md.xml)
##        print("Species Range Template after synchronize CREATED")
##        etree.indent(root, space="  ")
##        print(etree.tostring(root, pretty_print=True, method='html', encoding="utf-8").decode())
##        del root

    ##        # Parse the XML
    ##        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
    ##        target_name = os.path.basename(fc_metadata_xml_file).replace(".xml", "")
    ##        target_tree = etree.parse(fc_metadata_xml_file, parser=parser)
    ##        target_root = target_tree.getroot()
    ##        del parser

    ##        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
    ##        eainfo_tree = etree.parse(eainfo_xml_file, parser=parser)
    ##        eainfo_root = eainfo_tree.getroot()
    ##
    ##        #print(etree.tostring(eainfo_root, pretty_print=True).decode())

        # Pretty print
        #target_xml_string = etree.tostring(target_tree, pretty_print=True, method='html', encoding="utf-8").decode()

##        dataset_md.save()
##        root = etree.fromstring(dataset_md.xml)
##        print("After Save")
##        print(etree.tostring(root, pretty_print=True).decode())
##        del root



##        dataset_md.synchronize("NOT_CREATED")
##        root = etree.fromstring(dataset_md.xml)
##        print('Synchronize "NOT_CREATED"')
##        print(etree.tostring(root, pretty_print=True).decode())
##        del root

##        #root = tree.getroot()
##        #print(etree.tostring(root, pretty_print=True).decode())
##
##        xml = '''<metadata xml:lang="en">
##                    <eainfo>
##                        <detailed xmlns="" Name="AbaloneBlack_20210712">
##                            <enttyp>
##                                <enttypl>Attribute Table Fields</enttypl>
##                                <enttypt>Feature Class</enttypt>
##                                <enttypc>1</enttypc>
##                                <enttypd>A collection of geographic features with the same geometry type.</enttypd>
##                                <enttypds>Esri</enttypds>
##                            </enttyp>
##                            <attr xmlns="">
##                                <attrlabl>ID</attrlabl>
##                                <attalias>ID</attalias>
##                                <attrtype>String</attrtype>
##                                <attwidth>10</attwidth>
##                                <atprecis>0</atprecis>
##                                <attscale>0</attscale>
##                                <attrdef>9 digit unique identifier for each feature in the geodatabase. Used to relate or join supplemental attribute tables.</attrdef>
##                                <attrdefs>National Marine Fisheries Service</attrdefs>
##                                <attrdomv>
##                                    <udom>9 digit unique identifier for each feature in the geodatabase. Used to relate or join supplemental attribute tables.</udom>
##                                </attrdomv>
##                            </attr>
##                        </detailed>
##                    </eainfo>
##                 </metadata>'''
##        eainfo_xml = r"{os.environ['USERPROFILE']}\Documents\ArcGIS\Projects\ArcPy Studies\XML\nmfs-species-range-metatdata\eainfo.xml"
##        try:
##            dataset_md.importMetadata(eainfo_xml, "ARCGIS_METADATA")
##            dataset_md.save()
##            dataset_md.synchronize('CREATED')
##            dataset_md.save()
##            dataset_md.reload()
##
##            print("fuck yeah")
##        # Return geoprocessing specific errors
##        except arcpy.ExecuteError:
##            arcpy.AddError(arcpy.GetMessages(2))
##        # Return any other type of error
##        except:
##            # By default any other errors will be caught here
##            e = sys.exc_info()[1]
##            print(e.args[0])

##        dataset_md.save()
##        dataset_md.reload()
##        dataset_md.synchronize('SELECTIVE')
##        dataset_md.save()
##        dataset_md.synchronize("ALWAYS")
##        dataset_md.save()
##        dataset_md.reload()

##        dataset_md.save()
##
##        root = etree.fromstring(dataset_md.xml)
##        print(etree.tostring(root, pretty_print=True).decode())
##
##
##        del dataset_md

        #new_md_xml = new_md.xml
        #root = etree.fromstring(new_md_xml)
        #print(etree.tostring(root, pretty_print=True).decode())

        # Parse the XML
        #parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
        #tree = etree.parse(new_md_xml, parser=parser)
        #root = tree.getroot()
        #del parser

        #tree = etree.parse(new_md_xml)
        #root = tree.getroot()
        #print(etree.tostring(root, pretty_print=True).decode())



    ##        # Parse the XML
    ##        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
    ##        target_name = os.path.basename(fc_metadata_xml_file).replace(".xml", "")
    ##        target_tree = etree.parse(fc_metadata_xml_file, parser=parser)
    ##        target_root = target_tree.getroot()
    ##        del parser

    ##        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
    ##        eainfo_tree = etree.parse(eainfo_xml_file, parser=parser)
    ##        eainfo_root = eainfo_tree.getroot()
    ##
    ##        #print(etree.tostring(eainfo_root, pretty_print=True).decode())

        from io import BytesIO, StringIO

        xml_file = b'''<metadata><mdContact>
            <editorSource>extermal</editorSource>
            <editorDigest>9cc0fe80de5687cc4d79f50f3a254f2c3ceb08ce</editorDigest>
            <rpIndName>Nikki Wildart</rpIndName>
            <rpOrgName>Office of Protected Resources, National Marine Fisheries Service</rpOrgName>
            <rpPosName>Biologist</rpPosName>
            <rpCntInfo>
                <cntAddress addressType="both">
                    <delPoint>1315 East West Highway</delPoint>
                    <city>Silver Spring</city>
                    <adminArea>MD</adminArea>
                    <postCode>20910-3282</postCode>
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
                    <protocol>REST Service</protocol>
                    <orName>Fisheries OPR</orName>
                    <orDesc>NOAA Fisheries Office of Science and Technology</orDesc>
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
        </mdContact></metadata>'''
        #import xml.etree.cElementTree as etree

        #print(StringIO(xml))
        #print(BytesIO(xml))

        import io
        #print(io.StringIO(xml))

        #parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)  # lxml.etree only!
        #root = etree.fromstring(xml)
        #print(f"{root.getroot()}")
        #etree.indent(root, space="  ")
        #print(etree.tostring(root, encoding="utf-8",  method='xml', xml_declaration=True, pretty_print=True).decode())
        #del root

        _xml = rf"{os.environ['USERPROFILE']}\Documents\ArcGIS\Descriptions\contacts.xml"
        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
        tree = etree.parse(_xml, parser=parser) # To parse from a string, use the fromstring() function instead.
        del parser
        root = tree.getroot()
        etree.indent(root, space="  ")
        #print(etree.tostring(root, encoding="utf-8",  method='xml', xml_declaration=True, pretty_print=True).decode())
        #del root, _xml

        #for event, elem in etree.iterparse(_xml, events=('start', 'end')):
        for event, elem in etree.iterwalk(root, events=('start', 'end')):
            if event == 'start':
               print(f"Tag: {elem.tag}") # use only tag name and attributes here
               print(f"Parent: {elem.getparent()}")
            elif event == 'end':
               # elem children elements, elem.text, elem.tail are available
               if elem.text is not None and elem.tail is not None:
                  print(repr(elem.tail))


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
        # Append the location of this scrip to the System Path
    #sys.path.append(os.path.dirname(__file__))
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    main()
