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

def create_folder(folder):
    try:
        # Test if the folder exists. If not, then create the folder
        if not arcpy.Exists(folder):
            arcpy.AddMessage(f"Creating Folder: {os.path.basename(folder)}")
            # Execute CreateFolder
            arcpy.management.CreateFolder(os.path.dirname(folder), os.path.basename(folder))
            msg = "\tCreate Folder:\n\t\t"+arcpy.GetMessages().replace("\n", "\n\t\t")+"\n"
            arcpy.AddMessage(f"{msg}"); del msg
        else:
            arcpy.AddMessage(f"The folder '{os.path.basename(folder)}' exists")

    except:
        traceback.print_exc()
        raise Exception

def create_gdb(gdb):
    try:
        # Test of the Project GDB exists. If not, then create the Project GDB
        if not arcpy.Exists(gdb):
            arcpy.AddMessage(f"Creating the Project GDB: {os.path.basename(gdb)}")
            arcpy.management.CreateFileGDB(os.path.dirname(gdb), os.path.basename(gdb))
            msg = "\tCreate the GDB:\n\t\t"+arcpy.GetMessages().replace("\n", "\n\t\t")+"\n"
            arcpy.AddMessage(f"{msg}"); del msg
        else:
            arcpy.AddMessage(f"The GDB '{os.path.basename(gdb)}' exists")
    except:
        traceback.print_exc()
        raise Exception

def pretty_format_xml_file(xml=""):
    try:
        # Imports
        from lxml import etree

        #arcpy.AddMessage(f"###--->>> Converting metadata file: {os.path.basename(xml)} to pretty format")
        if os.path.isfile(xml):

            parser = etree.XMLParser(remove_blank_text=True)
            # Parse the XML
            tree = etree.parse(xml, parser=parser)

            etree.indent(tree, space="    ")

            # Pretty print
            xml_string = etree.tostring(tree, pretty_print=True, method='html', encoding="utf-8").decode()

            xml_string = xml_string.replace(' code="0">\n', ' code="0">')
            xml_string = xml_string.replace(' code="4">\n', ' code="4">')
            xml_string = xml_string.replace(' code="4326">\n', ' code="4326">')

            xml_string = xml_string.replace(' country="US">\n', ' country="US">')

            xml_string = xml_string.replace(' Sync="TRUE">\n', ' Sync="TRUE">')
            xml_string = xml_string.replace(' Sync="FALSE">\n', ' Sync="FALSE">')
            xml_string = xml_string.replace(' Sync="TRUE">            <enttyp>', ' Sync="TRUE">\n            <enttyp>')

            xml_string = xml_string.replace(' value="001">\n', ' value="001">')
            xml_string = xml_string.replace(' value="002">\n', ' value="002">')
            xml_string = xml_string.replace(' value="003">\n', ' value="003">')
            xml_string = xml_string.replace(' value="004">\n', ' value="004">')
            xml_string = xml_string.replace(' value="005">\n', ' value="005">')
            xml_string = xml_string.replace(' value="006">\n', ' value="006">')
            xml_string = xml_string.replace(' value="007">\n', ' value="007">')
            xml_string = xml_string.replace(' value="008">\n', ' value="008">')
            xml_string = xml_string.replace(' value="009">\n', ' value="009">')
            xml_string = xml_string.replace(' value="010">\n', ' value="010">')
            xml_string = xml_string.replace(' value="011">\n', ' value="011">')
            xml_string = xml_string.replace(' value="012">\n', ' value="012">')
            xml_string = xml_string.replace(' value="013">\n', ' value="013">')
            xml_string = xml_string.replace(' value="014">\n', ' value="014">')
            xml_string = xml_string.replace(' value="015">\n', ' value="015">')
            xml_string = xml_string.replace(' value="031">\n', ' value="031">')

            xml_string = xml_string.replace(' value="eng">\n', ' value="eng">')
            xml_string = xml_string.replace(' value="USA">\n', ' value="USA">')

            #xml_string = xml_string.replace("<attrdef>", '<attrdef Sync="TRUE">')
            #xml_string = xml_string.replace("<attrdefs>", '<attrdefs Sync="TRUE">')
            #xml_string = xml_string.replace("<udom>", '<udom Sync="TRUE">')
            xml_string = xml_string.replace('<UOM type="length">\n', '<UOM type="length">')

            try:
                with open(xml, "w") as f:
                    f.write(xml_string)
                del f
            except:
                arcpy.AddError(f"The metadata file: {os.path.basename(xml)} can not be overwritten!!")

            del xml_string
            del parser, tree

        # Imports
        del etree
        # Function parameters
        del xml

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
            traceback.print_exc()
            raise Exception
    finally:
        pass

def create_metadata_xml():
    try:
        import xml.etree.ElementTree as ET
        import xml.dom.minidom as minidom

        root = ET.Element('metadata')
        root.set("{http://www.w3.org/XML/1998/namespace}lang", "en")

        esri = ET.SubElement(root, 'Esri')

        ET.SubElement(esri, 'CreaDate').text = '20210712'
        ET.SubElement(esri, 'CreaTime').text = '10033400'
        ET.SubElement(esri, 'ArcGISFormat').text = '1.0'
        ET.SubElement(esri, 'ArcGISstyle').text = 'ISO 19139 Metadata Implementation Specification'
        ET.SubElement(esri, 'ArcGISProfile').text = 'ISO19139'
        ET.SubElement(esri, 'SyncOnce').text = 'FALSE'

        data_properties = ET.SubElement(esri, 'DataProperties')

        item_props = ET.SubElement(data_properties, 'itemProps')
        ET.SubElement(item_props, 'itemName', attrib={'Sync' : 'TRUE'}).text = 'AbaloneBlack_20210712'
        ET.SubElement(item_props, 'imsContentType', attrib={'Sync' : 'TRUE', 'export' : 'False'}).text = '002'

        native_ext_box = ET.SubElement(item_props, 'nativeExtBox')
        ET.SubElement(native_ext_box, 'westBL', attrib={'Sync' : 'TRUE'}).text = '-125.138309'
        ET.SubElement(native_ext_box, 'eastBL', attrib={'Sync' : 'TRUE'}).text = '-109.670789'
        ET.SubElement(native_ext_box, 'southBL', attrib={'Sync' : 'TRUE'}).text = '22.342045'
        ET.SubElement(native_ext_box, 'northBL', attrib={'Sync' : 'TRUE'}).text = '42.001571'
        ET.SubElement(native_ext_box, 'exTypeCode', attrib={'Sync' : 'TRUE'}).text = '1'

        coord_ref = ET.SubElement(data_properties, 'coordRef')
        ET.SubElement(coord_ref, 'type', attrib={'Sync' : 'TRUE'}).text = 'Geographic'
        ET.SubElement(coord_ref, 'geogcsn', attrib={'Sync' : 'TRUE'}).text = 'GCS_WGS_1984'
        ET.SubElement(coord_ref, 'csUnits', attrib={'Sync' : 'TRUE'}).text = 'Angular Unit: Degree (0.017453)'
        ET.SubElement(coord_ref, 'peXml', attrib={'Sync' : 'TRUE'}).text = "&lt;GeographicCoordinateSystem xsi:type='typens:GeographicCoordinateSystem' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xmlns:xs='http://www.w3.org/2001/XMLSchema' xmlns:typens='http://www.esri.com/schemas/ArcGIS/3.4.0'&gt;&lt;WKT&gt;GEOGCS[&amp;quot;GCS_WGS_1984&amp;quot;,DATUM[&amp;quot;D_WGS_1984&amp;quot;,SPHEROID[&amp;quot;WGS_1984&amp;quot;,6378137.0,298.257223563]],PRIMEM[&amp;quot;Greenwich&amp;quot;,0.0],UNIT[&amp;quot;Degree&amp;quot;,0.0174532925199433],AUTHORITY[&amp;quot;EPSG&amp;quot;,4326]]&lt;/WKT&gt;&lt;XOrigin&gt;-400&lt;/XOrigin&gt;&lt;YOrigin&gt;-400&lt;/YOrigin&gt;&lt;XYScale&gt;999999999.99999988&lt;/XYScale&gt;&lt;ZOrigin&gt;-100000&lt;/ZOrigin&gt;&lt;ZScale&gt;10000&lt;/ZScale&gt;&lt;MOrigin&gt;-100000&lt;/MOrigin&gt;&lt;MScale&gt;10000&lt;/MScale&gt;&lt;XYTolerance&gt;8.983152841195215e-09&lt;/XYTolerance&gt;&lt;ZTolerance&gt;0.001&lt;/ZTolerance&gt;&lt;MTolerance&gt;0.001&lt;/MTolerance&gt;&lt;HighPrecision&gt;true&lt;/HighPrecision&gt;&lt;LeftLongitude&gt;-180&lt;/LeftLongitude&gt;&lt;WKID&gt;4326&lt;/WKID&gt;&lt;LatestWKID&gt;4326&lt;/LatestWKID&gt;&lt;/GeographicCoordinateSystem&gt;"

        scale_range = ET.SubElement(esri, 'scaleRange')
        ET.SubElement(scale_range, 'minScale').text = '150000000'
        ET.SubElement(scale_range, 'maxScale').text = '5000'

        ET.SubElement(esri, 'SyncDate').text = '20241124'
        ET.SubElement(esri, 'SyncTime').text = '12383200'
        ET.SubElement(esri, 'ModDate').text = '20241124'
        ET.SubElement(esri, 'ModTime').text = '12383200'

        dataIdInfo = ET.SubElement(root, 'dataIdInfo')
        ET.SubElement(dataIdInfo, 'envirDesc', attrib={'Sync' : 'TRUE'}).text = 'Esri ArcGIS 13.4.0.55405'

        dataLang = ET.SubElement(dataIdInfo, 'dataLang')
        ET.SubElement(dataLang, 'languageCode', attrib={'value' : 'eng', 'Sync' : 'TRUE'})
        ET.SubElement(dataLang, 'countryCode', attrib={'value' : 'USA', 'Sync' : 'TRUE'})
        del dataLang

        idCitation = ET.SubElement(dataIdInfo, 'idCitation')
        ET.SubElement(idCitation, 'resTitle', attrib={'Sync' : 'TRUE'}).text = '[insert file name here]'

        presForm = ET.SubElement(idCitation, 'presForm')
        ET.SubElement(presForm, 'PresFormCd', attrib={'value' : '005', 'Sync' : 'TRUE'})

        ET.SubElement(presForm, 'fgdcGeoform').text = 'vector digital data'
        del presForm

        citRespParty = ET.SubElement(idCitation, 'citRespParty')
        ET.SubElement(citRespParty, 'rpIndName').text = 'Jonathan Molineaux'
        ET.SubElement(citRespParty, 'rpOrgName').text = 'NMFS Office Of Protected Resources'
        ET.SubElement(citRespParty, 'rpPosName').text = 'Fisheries Biologist'

        role = ET.SubElement(citRespParty, 'role')
        ET.SubElement(role, 'RoleCd', attrib={'value' : '001'})
        del role

        rpCntInfo = ET.SubElement(citRespParty, 'rpCntInfo')
        cntAddress = ET.SubElement(rpCntInfo, 'cntAddress', attrib={'addressType' : 'BOTH'})
        ET.SubElement(cntAddress, 'eMailAdd').text = 'jonathan.molineaux@noaa.gov'
        del rpCntInfo, cntAddress

        ET.SubElement(citRespParty, 'displayName').text = 'Jonathan Molineaux'

        date = ET.SubElement(idCitation, 'date')
        ET.SubElement(date, 'pubDate').text = '2024-11-22T00:00:00'
        del idCitation

        ##ET.SubElement('spatRpType').text = ''
        ##ET.SubElement('SpatRepTypCd').set('value', '001', 'Sync', 'TRUE')
        ##
        ##
        ##ET.SubElement('idPurp').text = 'This is new text for an existing Purpose metadata element.'
        ##
        ##ET.SubElement('dataChar').text = ''
        ##ET.SubElement('CharSetCd').set('value', '004')
        ##
        ##
        ##ET.SubElement('resMaint').text = ''
        ##ET.SubElement('maintFreq').text = ''
        ##ET.SubElement('MaintFreqCd').set('value', '009')
        ##
        ##
        ##
        ##ET.SubElement('idPoC').text = ''
        ##ET.SubElement('rpIndName').text = 'Jonathan Molineaux'
        ##ET.SubElement('rpOrgName').text = 'NOAA Fisheries Office of Protected Resources'
        ##ET.SubElement('rpPosName').text = 'Fisheries Biologist'
        ##ET.SubElement('role').text = ''
        ##ET.SubElement('RoleCd').set('value', '001')
        ##ET.SubElement('rpCntInfo').text = ''
        ##ET.SubElement('cntAddress').set('addressType', '').text = ''
        ##ET.SubElement('eMailAdd').text = 'jonathan.molineaux@noaa.gov'
        ##ET.SubElement('idPoC').text = ''
        ##ET.SubElement('rpIndName').text = 'Jennifer Schultz'
        ##
        ##ET.SubElement('rpOrgName').text = 'NOAA Fisheries Office of Protected Resources'
        ##
        ##ET.SubElement('rpPosName').text = 'Fisheries Biologist'
        ##
        ##ET.SubElement('role').text = ''
        ##ET.SubElement('RoleCd').set('value', '001')
        ##
        ##
        ##ET.SubElement('rpCntInfo').text = ''
        ##ET.SubElement('cntAddress').set('addressType', '').text = ''
        ##ET.SubElement('eMailAdd').text = 'jennifer.schultz@noaa.gov'
        ##
        ##
        ##
        ##
        ##ET.SubElement('idAbs').text = '<DIV STYLE="text-align:Left;"><DIV><DIV><P><SPAN>This range includes [all; marine; freshwater; adult; immature/juvenile; larval] life stages of the species [add any caveats, e.g., why something is not included]. The range was based on the following [tracking, tagging, bycatch, and sighting] data: [Provide data and citations used to create range, including name/version/date of shoreline data.] Disclaimer: the spatial data provided here display an approximate distribution; they should not be conflated with the definitive range of the listed entity under the ESA. The spatial data provided here display an approximate distribution of the listed entity based on the best available information at the time of creation; they do not constitute should not be conflated with the definitive range of the listed entity under the ESA. As such, the distribution of the listed entity may not be exclusively limited to the range identified herein, and we have not verified the listed entity’s occurrence in every area comprising the range. Please notify us if you have recent information that is not reflected in our data (see Citation contacts). Use of these data do not replace the ESA section 7 consultation process; however, these data may be a first step in determining whether a proposed federal action overlaps with listed species’ ranges or critical habitat.</SPAN></P><P><SPAN /></P></DIV></DIV></DIV>'
        ##
        ##ET.SubElement('idCredit').text = 'This is new text for an existing Purpose metadata element.'
        ##
        ##ET.SubElement('searchKeys').text = ''
        ##ET.SubElement('keyword').text = '[inert ESA-listed entity name here]; ESA; range; NMFS'
        ##
        ##
        ##ET.SubElement('themeKeys').text = ''
        ##ET.SubElement('thesaName').text = ''
        ##ET.SubElement('resTitle').text = 'N/A'
        ##
        ##ET.SubElement('date').text = ''
        ##ET.SubElement('pubDate').text = '2024-11-22T00:00:00'
        ##
        ##
        ##
        ##ET.SubElement('keyword').text = 'ESA, NMFS, Species' Range'
        ##
        ##
        ##ET.SubElement('placeKeys').text = ''
        ##ET.SubElement('keyword').text = 'Global, National'
        ##
        ##
        ##ET.SubElement('idStatus').text = ''
        ##ET.SubElement('ProgCd').set('value', '004')
        ##
        ##
        ##ET.SubElement('resConst').text = ''
        ##ET.SubElement('Consts').text = ''
        ##ET.SubElement('useLimit').text = '<DIV STYLE="text-align:Left;"><DIV><DIV><DIV STYLE="font-size:12pt"><P><SPAN>*** Attribution *** Whenever NMFS material is reproduced and re-disseminated, we request that users attribute the material appropriately. Pursuant to 17 U.S. C. 403, parties who produce copyrighted works consisting predominantly of material created by the Federal Government are encouraged to provide notice with such work(s) identifying the U.S. Government material incorporated and stating that such material is not subject to copyright protection. Please cite the species range datasets as indicated in the metadata for each species, or if not indicated, as follows with the appropriate information substituted for all text in {CURLY BRACKETS}: </SPAN></P><P><SPAN>NOAA Fisheries Service. Endangered Species Act Species Range Geodatabase. Silver Spring, MD: National Oceanic and Atmospheric Administration (NOAA), National Marine Fisheries Service (NMFS), Office of Protected Resources (OPR) [producer] {GEODATABASE PUBLICATION DATE}. {ADD URL}</SPAN></P><P><SPAN>***No Warranty*** The user assumes the entire risk related to its use of these data. NMFS is providing these data "as is," and NMFS disclaims any and all warranties, whether express or implied, including (without limitation) any implied warranties of merchantability or fitness for a particular purpose. No warranty expressed or implied is made regarding the accuracy or utility of the data on any other system or for general or scientific purposes, nor shall the act of distribution constitute any such warranty. It is strongly recommended that careful attention be paid to the contents of the metadata file associated with these data to evaluate dataset limitations, restrictions or intended use. In no event will NMFS be liable to you or to any third party for any direct, indirect, incidental, consequential, special or exemplary damages or lost profit resulting from any use or misuse of this data. </SPAN></P><P><SPAN>*** Proper Usage *** The information on government servers are in the public domain, unless specifically annotated otherwise, and may be used freely by the public. Before using information obtained from this server, special attention should be given to the date and time of the data and products being displayed. This information shall not be modified in content and then presented as official government material. This dataset was created to generally represent our best professional judgment of the ranges of listed species based on the best available information at the time of publication, including: geographic factors, time of year, and the biology of each species. The dataset should not be used to infer information regarding the existence or details of other marine features or resources, including, but not limited to, navigable waters, coastlines, bathymetry, submerged features, or man-made structures. Users assume responsibility for determining the appropriate use of this dataset. </SPAN></P><P><SPAN>*** Temporal Considerations *** Species’ ranges are subject to change or modification. Generally, we become aware of these changes during the 5-year review of the species’ status, as required under the ESA. If changes to the range are deemed necessary, we will make such changes in the database, which will be archived and replaced by an updated version as soon as feasible. It is the user’s responsibility to ensure the most recent species’ range data are being used. </SPAN></P><P><SPAN>*** Shorelines/Base Layers *** The accuracy of this dataset is dependent upon the accuracy and resolution of the datasets (e.g. shoreline, hydrography, bathymetry, shared administrative boundaries) used in the creation process. Source datasets used are specified in the metadata. These data sources were selected for their suitability to a broad audience, and may not be suitable for specific uses requiring higher-resolution information. Coastlines and water body boundaries change. Unless otherwise noted, where the National Hydrography Dataset or NOAA Medium Resolution Shoreline is used, assume the boundary reaches the most current river, estuary, or coastal shoreline delineation available.</SPAN></P><P><SPAN>*** Data Limitations ***</SPAN></P><P><SPAN>Our data may lack the spatial resolution to capture the entire range of a species, especially outside of a major waterway (e.g., in a very small tributary, or shallow area near a marsh). For section 7 consultations, we recommend that Federal action agencies request technical assistance to verify presence/absence of listed species within their action area.</SPAN></P></DIV></DIV></DIV></DIV>'
        ##
        ##
        ##
        ##ET.SubElement('dataExt').text = ''
        ##ET.SubElement('geoEle').text = ''
        ##ET.SubElement('GeoBndBox').set('esriExtentType', 'search').text = ''
        ##ET.SubElement('exTypeCode', attrib={'Sync' : 'TRUE'}).text = '1'
        ##
        ##ET.SubElement('westBL', attrib={'Sync' : 'TRUE'}).text = '-125.138309'
        ##
        ##ET.SubElement('eastBL', attrib={'Sync' : 'TRUE'}).text = '-109.670789'
        ##
        ##ET.SubElement('northBL', attrib={'Sync' : 'TRUE'}).text = '42.001571'
        ##
        ##ET.SubElement('southBL', attrib={'Sync' : 'TRUE'}).text = '22.342045'
        ##
        ##
        ##
        ##
        ##ET.SubElement('tpCat').text = ''
        ##ET.SubElement('TopicCatCd').set('value', '002')
        ##
        ##
        ##ET.SubElement('tpCat').text = ''
        ##ET.SubElement('TopicCatCd').set('value', '007')
        ##
        ##
        ##ET.SubElement('tpCat').text = ''
        ##ET.SubElement('TopicCatCd').set('value', '014')
        ##
        ##
        ##ET.SubElement('idCredit').text = 'This is new text for an existing Purpose metadata element.'
        ##

        #ET.SubElement(item_props, 'imsContentType', attrib={'Sync' : 'TRUE', 'export' : 'False'})

        del dataIdInfo

        mdLang = ET.SubElement(root, 'mdLang')
        ET.SubElement(mdLang, 'languageCode', attrib={'value' : 'eng', 'Sync' : 'TRUE'})
        ET.SubElement(mdLang, 'countryCode', attrib={'value' : 'USA', 'Sync' : 'TRUE'})
        del mdLang

        mdChar = ET.SubElement(root, 'mdChar')
        ET.SubElement(mdChar, 'CharSetCd', attrib={'value' : '004', 'Sync' : 'TRUE'})
        del mdChar

        distInfo = ET.SubElement(root, 'distInfo')
        distFormat = ET.SubElement(distInfo, 'distFormat')
        ET.SubElement(distFormat, 'formatName', attrib={'Sync' : 'TRUE'}).text = 'File Geodatabase Feature Class'
        ET.SubElement(distFormat, 'formatVer').text = 'NMFS ESA Range Geodatabase 2021'
        del distFormat

        ET.SubElement(distInfo, 'distributor')
        ##ET.SubElement('distorCont').text = ''
        ##ET.SubElement('rpOrgName').text = 'NMFS Office Of Protected Resources'
        ##
        ##ET.SubElement('displayName').text = 'Department of Commerce (DOC), National Oceanic and Atmospheric Administration (NOAA), National Marine Fisheries Service (NMFS)'
        ##
        ##ET.SubElement('role').text = ''
        ##ET.SubElement('RoleCd').set('value', '005')
        ##
        ##
        ##ET.SubElement('rpCntInfo').text = ''
        ##ET.SubElement('cntAddress').set('addressType', '').text = ''
        ##ET.SubElement('eMailAdd').text = 'jonathan.molineaux@noaa.gov'
        ##
        ##
        ##
        ##
        ##ET.SubElement('distorFormat').text = ''
        ##ET.SubElement('formatName').text = 'File Geodatabase Feature Class'
        ##
        ##ET.SubElement('formatVer').text = 'NMFS ESA Range Geodatabase 2021'
        ##
        ##
        ##ET.SubElement('distorTran').text = ''
        ##ET.SubElement('onLineSrc').text = ''
        ##ET.SubElement('linkage').text = 'https://www.fisheries.noaa.gov/science-and-data'

        del distInfo

        mdHrLv = ET.SubElement(root, 'mdHrLv')
        ET.SubElement(mdHrLv, 'ScopeCd', attrib={'value' : '005', 'Sync' : 'TRUE'})
        del mdHrLv

        ET.SubElement(root, 'mdHrLvName', attrib={'Sync' : 'TRUE'}).text = 'dataset'

        ##ET.SubElement('refSysInfo').text = ''
        ##ET.SubElement('RefSystem').set('dimension', '').text = ''
        ##ET.SubElement('refSysID').text = ''
        ##ET.SubElement('identCode').set('code', '4326', 'Sync', 'TRUE')
        ##
        ##ET.SubElement('idCodeSpace', attrib={'Sync' : 'TRUE'}).text = 'EPSG'
        ##
        ##ET.SubElement('idVersion', attrib={'Sync' : 'TRUE'}).text = '6.2(3.0.1)'
        ##
        ##
        ##
        ##
        ##ET.SubElement('spatRepInfo').text = ''
        ##ET.SubElement('VectSpatRep').text = ''
        ##ET.SubElement('geometObjs').set('Name', 'AbaloneBlack_20210712').text = ''
        ##ET.SubElement('geoObjTyp').text = ''
        ##ET.SubElement('GeoObjTypCd').set('value', '002', 'Sync', 'TRUE')
        ##
        ##
        ##ET.SubElement('geoObjCnt', attrib={'Sync' : 'TRUE'}).text = '2'
        ##
        ##
        ##ET.SubElement('topLvl').text = ''
        ##ET.SubElement('TopoLevCd').set('value', '001', 'Sync', 'TRUE')
        ##
        ##
        ##
        ##
        ##ET.SubElement('spdoinfo').text = ''
        ##ET.SubElement('ptvctinf').text = ''
        ##ET.SubElement('esriterm').set('Name', 'AbaloneBlack_20210712').text = ''
        ##ET.SubElement('efeatyp', attrib={'Sync' : 'TRUE'}).text = 'Simple'
        ##
        ##ET.SubElement('efeageom').set('code', '4', 'Sync', 'TRUE')
        ##
        ##ET.SubElement('esritopo', attrib={'Sync' : 'TRUE'}).text = 'FALSE'
        ##
        ##ET.SubElement('efeacnt', attrib={'Sync' : 'TRUE'}).text = '2'
        ##
        ##ET.SubElement('spindex', attrib={'Sync' : 'TRUE'}).text = 'TRUE'
        ##
        ##ET.SubElement('linrefer', attrib={'Sync' : 'TRUE'}).text = 'FALSE'
        ##
        ##
        ##
        ##
        ##ET.SubElement('eainfo').text = ''
        ##ET.SubElement('detailed').set('Name', 'AbaloneBlack_20210712').text = ''
        ##ET.SubElement('enttyp').text = ''
        ##ET.SubElement('enttypl', attrib={'Sync' : 'TRUE'}).text = 'AbaloneBlack_20210712'
        ##
        ##ET.SubElement('enttypt', attrib={'Sync' : 'TRUE'}).text = 'Feature Class'
        ##
        ##ET.SubElement('enttypc', attrib={'Sync' : 'TRUE'}).text = '2'
        ##
        ##ET.SubElement('enttypd').text = 'A collection of geographic features with the same geometry type.'
        ##
        ##ET.SubElement('enttypds').text = 'Esri'
        ##
        ##
        ##ET.SubElement('attr').text = ''
        ##ET.SubElement('attrlabl', attrib={'Sync' : 'TRUE'}).text = 'OBJECTID'
        ##
        ##ET.SubElement('attalias', attrib={'Sync' : 'TRUE'}).text = 'OBJECTID'
        ##
        ##ET.SubElement('attrtype', attrib={'Sync' : 'TRUE'}).text = 'OID'
        ##
        ##ET.SubElement('attwidth', attrib={'Sync' : 'TRUE'}).text = '4'
        ##
        ##ET.SubElement('atprecis', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attscale', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attrdef', attrib={'Sync' : 'TRUE'}).text = 'Internal feature number.'
        ##
        ##ET.SubElement('attrdefs', attrib={'Sync' : 'TRUE'}).text = 'Esri'
        ##
        ##ET.SubElement('attrdomv').text = ''
        ##ET.SubElement('udom', attrib={'Sync' : 'TRUE'}).text = 'Sequential unique whole numbers that are automatically generated.'
        ##
        ##
        ##
        ##ET.SubElement('attr').text = ''
        ##ET.SubElement('attrlabl', attrib={'Sync' : 'TRUE'}).text = 'SHAPE'
        ##
        ##ET.SubElement('attalias', attrib={'Sync' : 'TRUE'}).text = 'Shape'
        ##
        ##ET.SubElement('attrtype', attrib={'Sync' : 'TRUE'}).text = 'Geometry'
        ##
        ##ET.SubElement('attwidth', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('atprecis', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attscale', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attrdef', attrib={'Sync' : 'TRUE'}).text = 'Feature geometry.'
        ##
        ##ET.SubElement('attrdefs', attrib={'Sync' : 'TRUE'}).text = 'Esri'
        ##
        ##ET.SubElement('attrdomv').text = ''
        ##ET.SubElement('udom', attrib={'Sync' : 'TRUE'}).text = 'Coordinates defining the features.'
        ##
        ##
        ##
        ##ET.SubElement('attr').text = ''
        ##ET.SubElement('attrlabl', attrib={'Sync' : 'TRUE'}).text = 'ID'
        ##
        ##ET.SubElement('attalias', attrib={'Sync' : 'TRUE'}).text = 'ID'
        ##
        ##ET.SubElement('attrtype', attrib={'Sync' : 'TRUE'}).text = 'Double'
        ##
        ##ET.SubElement('attwidth', attrib={'Sync' : 'TRUE'}).text = '8'
        ##
        ##ET.SubElement('atprecis', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attscale', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attrdef', attrib={'Sync' : 'TRUE'}).text = '9 digit unique identifier for each feature in the geodatabase.
        ##Used to relate or join supplemental attribute tables.'
        ##
        ##ET.SubElement('attrdefs', attrib={'Sync' : 'TRUE'}).text = 'National Marine Fisheries Service'
        ##
        ##
        ##ET.SubElement('attr').text = ''
        ##ET.SubElement('attrlabl', attrib={'Sync' : 'TRUE'}).text = 'SCIENAME'
        ##
        ##ET.SubElement('attalias', attrib={'Sync' : 'TRUE'}).text = 'Scientific Name'
        ##
        ##ET.SubElement('attrtype', attrib={'Sync' : 'TRUE'}).text = 'String'
        ##
        ##ET.SubElement('attwidth', attrib={'Sync' : 'TRUE'}).text = '100'
        ##
        ##ET.SubElement('atprecis', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attscale', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attrdef', attrib={'Sync' : 'TRUE'}).text = 'Binomial or trinomial scientific name. Value formatted as written in the Code of Federal Regulations.'
        ##
        ##ET.SubElement('attrdefs', attrib={'Sync' : 'TRUE'}).text = 'National Marine Fisheries Service'
        ##
        ##
        ##ET.SubElement('attr').text = ''
        ##ET.SubElement('attrlabl', attrib={'Sync' : 'TRUE'}).text = 'COMNAME'
        ##
        ##ET.SubElement('attalias', attrib={'Sync' : 'TRUE'}).text = 'Common Name'
        ##
        ##ET.SubElement('attrtype', attrib={'Sync' : 'TRUE'}).text = 'String'
        ##
        ##ET.SubElement('attwidth', attrib={'Sync' : 'TRUE'}).text = '100'
        ##
        ##ET.SubElement('atprecis', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attscale', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attrdef', attrib={'Sync' : 'TRUE'}).text = 'Legal common name of species. Value formatted as written in the Code of Federal Regulations.'
        ##
        ##ET.SubElement('attrdefs', attrib={'Sync' : 'TRUE'}).text = 'National Marine Fisheries Service'
        ##
        ##
        ##ET.SubElement('attr').text = ''
        ##ET.SubElement('attrlabl', attrib={'Sync' : 'TRUE'}).text = 'LISTENTITY'
        ##
        ##ET.SubElement('attalias', attrib={'Sync' : 'TRUE'}).text = 'Listed Entity'
        ##
        ##ET.SubElement('attrtype', attrib={'Sync' : 'TRUE'}).text = 'String'
        ##
        ##ET.SubElement('attwidth', attrib={'Sync' : 'TRUE'}).text = '100'
        ##
        ##ET.SubElement('atprecis', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attscale', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attrdef', attrib={'Sync' : 'TRUE'}).text = 'Full text of the ESA listed entity: Species, Subspecies, Distinct Population Segment (DPS), or Evolutionarily Significant Unit (ESU). Value formatted as written in the Code of Federal Regulations. *Note: for entire species listings, this value will be the same as COMNAME value.'
        ##
        ##ET.SubElement('attrdefs', attrib={'Sync' : 'TRUE'}).text = 'National Marine Fisheries Service'
        ##
        ##
        ##ET.SubElement('attr').text = ''
        ##ET.SubElement('attrlabl', attrib={'Sync' : 'TRUE'}).text = 'LISTSTATUS'
        ##
        ##ET.SubElement('attalias', attrib={'Sync' : 'TRUE'}).text = 'Listing Status'
        ##
        ##ET.SubElement('attrtype', attrib={'Sync' : 'TRUE'}).text = 'String'
        ##
        ##ET.SubElement('attwidth', attrib={'Sync' : 'TRUE'}).text = '20'
        ##
        ##ET.SubElement('atprecis', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attscale', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attrdef', attrib={'Sync' : 'TRUE'}).text = 'Current Endangered Species Act listing status.'
        ##
        ##ET.SubElement('attrdefs', attrib={'Sync' : 'TRUE'}).text = 'National Marine Fisheries Service'
        ##
        ##ET.SubElement('attrdomv').text = ''
        ##ET.SubElement('edom').text = ''
        ##ET.SubElement('edomv').text = 'Endangered'
        ##
        ##ET.SubElement('edomvd').text = 'Species that are in danger of extinction throughout all or a significant portion of their range.'
        ##
        ##ET.SubElement('edomvds').text = 'Endangered Species Act of 1973'
        ##
        ##
        ##ET.SubElement('edom').text = ''
        ##ET.SubElement('edomv').text = 'Threatened'
        ##
        ##ET.SubElement('edomvd').text = 'Species that are likely to become endangered in the foreseeable future.'
        ##
        ##ET.SubElement('edomvds').text = 'Endangered Species Act of 1973'
        ##
        ##
        ##ET.SubElement('edom').text = ''
        ##ET.SubElement('edomv').text = 'Delisted'
        ##
        ##ET.SubElement('edomvd').text = 'Species that were removed from the Endangered Species Act list.'
        ##
        ##ET.SubElement('edomvds').text = 'Endangered Species Act of 1973'
        ##
        ##
        ##
        ##
        ##ET.SubElement('attr').text = ''
        ##ET.SubElement('attrlabl', attrib={'Sync' : 'TRUE'}).text = 'TAXON'
        ##
        ##ET.SubElement('attalias', attrib={'Sync' : 'TRUE'}).text = 'Taxon'
        ##
        ##ET.SubElement('attrtype', attrib={'Sync' : 'TRUE'}).text = 'String'
        ##
        ##ET.SubElement('attwidth', attrib={'Sync' : 'TRUE'}).text = '50'
        ##
        ##ET.SubElement('atprecis', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attscale', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attrdef', attrib={'Sync' : 'TRUE'}).text = 'Taxonomic unit.'
        ##
        ##ET.SubElement('attrdefs', attrib={'Sync' : 'TRUE'}).text = 'National Marine Fisheries Service'
        ##
        ##ET.SubElement('attrdomv').text = ''
        ##ET.SubElement('edom').text = ''
        ##ET.SubElement('edomv').text = 'baleen whale'
        ##
        ##ET.SubElement('edomvd').text = 'Any of a suborder (Mysticeti) of large whales that have baleen plates in the upper jaw which are used to filter chiefly small crustaceans out of large quantities of seawater.'
        ##
        ##ET.SubElement('edomvds').text = 'Merriam-Webster dictionary'
        ##
        ##
        ##ET.SubElement('edom').text = ''
        ##ET.SubElement('edomv').text = 'toothed whale'
        ##
        ##ET.SubElement('edomvd').text = 'Any of a suborder (Odontoceti) of cetaceans bearing usually numerous simple conical teeth.'
        ##
        ##ET.SubElement('edomvds').text = 'Merriam-Webster dictionary'
        ##
        ##
        ##ET.SubElement('edom').text = ''
        ##ET.SubElement('edomv').text = 'fish'
        ##
        ##ET.SubElement('edomvd').text = 'Any of numerous cold-blooded strictly aquatic craniate vertebrates that include the bony fishes and the cartilaginous and jawless fishes and that have typically an elongated somewhat spindle-shaped body terminating in a broad caudal fin, limbs in the form of fins when present at all, and a 2-chambered heart by which blood is sent through thoracic gills to be oxygenated.'
        ##
        ##ET.SubElement('edomvds').text = 'Merriam-Webster dictionary'
        ##
        ##
        ##ET.SubElement('edom').text = ''
        ##ET.SubElement('edomv').text = 'pinniped'
        ##
        ##ET.SubElement('edomvd').text = 'Any of an order or suborder (Pinnipedia) of aquatic carnivorous mammals with all four limbs modified into flippers.'
        ##
        ##ET.SubElement('edomvds').text = 'Merriam-Webster dictionary'
        ##
        ##
        ##ET.SubElement('edom').text = ''
        ##ET.SubElement('edomv').text = 'marine reptile'
        ##
        ##ET.SubElement('edomvd').text = 'Any of a class (Reptilia) of cold-blooded, air-breathing, usually egg-laying vertebrates that have adapted for an aquatic or semiaquatic life in a marine environment and have a body typically covered with scales or bony plates and a bony skeleton with a single occipital condyle, a distinct quadrate bone usually immovably articulated with the skull, and ribs attached to the sternum.'
        ##
        ##ET.SubElement('edomvds').text = 'Merriam-Webster dictionary'
        ##
        ##
        ##ET.SubElement('edom').text = ''
        ##ET.SubElement('edomv').text = 'invertebrate'
        ##
        ##ET.SubElement('edomvd').text = 'Any animal that lacks a spinal column.'
        ##
        ##ET.SubElement('edomvds').text = 'Merriam-Webster dictionary'
        ##
        ##
        ##ET.SubElement('edom').text = ''
        ##ET.SubElement('edomv').text = 'plant'
        ##
        ##ET.SubElement('edomvd').text = 'Any of a kingdom (Plantae) of multicellular eukaryotic mostly photosynthetic organisms typically lacking locomotive movement or obvious nervous or sensory organs and possessing cellulose cell walls.'
        ##
        ##ET.SubElement('edomvds').text = 'Merriam-Webster dictionary'
        ##
        ##
        ##
        ##
        ##ET.SubElement('attr').text = ''
        ##ET.SubElement('attrlabl', attrib={'Sync' : 'TRUE'}).text = 'LEADOFFICE'
        ##
        ##ET.SubElement('attalias', attrib={'Sync' : 'TRUE'}).text = 'Lead Office'
        ##
        ##ET.SubElement('attrtype', attrib={'Sync' : 'TRUE'}).text = 'String'
        ##
        ##ET.SubElement('attwidth', attrib={'Sync' : 'TRUE'}).text = '50'
        ##
        ##ET.SubElement('atprecis', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attscale', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attrdef', attrib={'Sync' : 'TRUE'}).text = 'NMFS Office responsible for the species’ range within feature.'
        ##
        ##ET.SubElement('attrdefs', attrib={'Sync' : 'TRUE'}).text = 'National Marine Fisheries Service'
        ##
        ##ET.SubElement('attrdomv').text = ''
        ##ET.SubElement('edom').text = ''
        ##ET.SubElement('edomv').text = 'Office of Protected Resources'
        ##
        ##ET.SubElement('edomvd').text = 'Headquarters office responsible for nationwide conservation, protection, and recovery of endangered and threatened marine species listed under the Endangered Species Act.'
        ##
        ##ET.SubElement('edomvds').text = 'National Marine Fisheries Service'
        ##
        ##
        ##ET.SubElement('edom').text = ''
        ##ET.SubElement('edomv').text = 'Alaska Region'
        ##
        ##ET.SubElement('edomvd').text = 'Includes Alaska and adjacent marine waters extending outwards to the 200 nautical mile boundary of the Exclusive Economic Zone.'
        ##
        ##ET.SubElement('edomvds').text = 'National Marine Fisheries Service'
        ##
        ##
        ##ET.SubElement('edom').text = ''
        ##ET.SubElement('edomv').text = 'West Coast Region'
        ##
        ##ET.SubElement('edomvd').text = 'Includes Idaho, Washington, Oregon, California and adjacent marine waters extending outwards to the 200 nautical mile boundary of the Exclusive Economic Zone.'
        ##
        ##ET.SubElement('edomvds').text = 'National Marine Fisheries Service'
        ##
        ##
        ##ET.SubElement('edom').text = ''
        ##ET.SubElement('edomv').text = 'Greater Atlantic Region'
        ##
        ##ET.SubElement('edomvd').text = 'Includes Minnesota, Wisconsin, Michigan, Illinois, Indiana, Ohio, Kentucky, West Virginia, Pennsylvania, New York, Vermont, New Hampshire, Maine, Massachusetts, Rhode Island, Connecticut, New Jersey, Delaware, Maryland, Virginia, North Carolina (north of Cape Hatteras) and adjacent marine waters extending outwards to the 200 nautical mile boundary of the Exclusive Economic Zone.'
        ##
        ##ET.SubElement('edomvds').text = 'National Marine Fisheries Service'
        ##
        ##
        ##ET.SubElement('edom').text = ''
        ##ET.SubElement('edomv').text = 'Southeast Region'
        ##
        ##ET.SubElement('edomvd').text = 'Includes North Carolina (south of Cape Hatteras), South Carolina, Georgia, Florida, Alabama, Mississippi, Louisiana, Texas, Arkansas, Iowa, Kansas, Kentucky, Missouri, Nebraska, New Mexico, Oklahoma, Tennessee, the Commonwealth of Puerto Rico, the U.S. Virgin Islands and adjacent marine waters extending outwards to the 200 nautical mile boundary of the Exclusive Economic Zone.'
        ##
        ##ET.SubElement('edomvds').text = 'National Marine Fisheries Service'
        ##
        ##
        ##ET.SubElement('edom').text = ''
        ##ET.SubElement('edomv').text = 'Pacific Islands Region'
        ##
        ##ET.SubElement('edomvd').text = 'Includes Hawai'i, American Samoa, Guam, the Commonwealth of the Northern Mariana Islands, Kingman Reef, Howland Island, Baker Island, Jarvis Island, Wake Island, Johnston Atoll, Palmyra Atoll and adjacent marine waters extending outwards to the 200 nautical mile boundary of the Exclusive Economic Zone.'
        ##
        ##ET.SubElement('edomvds').text = 'National Marine Fisheries Service'
        ##
        ##
        ##
        ##
        ##ET.SubElement('attr').text = ''
        ##ET.SubElement('attrlabl', attrib={'Sync' : 'TRUE'}).text = 'FR'
        ##
        ##ET.SubElement('attalias', attrib={'Sync' : 'TRUE'}).text = 'Federal Register Rule'
        ##
        ##ET.SubElement('attrtype', attrib={'Sync' : 'TRUE'}).text = 'String'
        ##
        ##ET.SubElement('attwidth', attrib={'Sync' : 'TRUE'}).text = '255'
        ##
        ##ET.SubElement('atprecis', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attscale', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attr').text = ''
        ##ET.SubElement('attrlabl', attrib={'Sync' : 'TRUE'}).text = 'PUBDATE'
        ##
        ##ET.SubElement('attalias', attrib={'Sync' : 'TRUE'}).text = 'Publication Date'
        ##
        ##ET.SubElement('attrtype', attrib={'Sync' : 'TRUE'}).text = 'String'
        ##
        ##ET.SubElement('attwidth', attrib={'Sync' : 'TRUE'}).text = '10'
        ##
        ##ET.SubElement('atprecis', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attscale', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attrdef', attrib={'Sync' : 'TRUE'}).text = 'Federal Register Notice publication date for the ESA-listed entity. MM/DD/YYYY format'
        ##
        ##ET.SubElement('attrdefs', attrib={'Sync' : 'TRUE'}).text = 'National Marine Fisheries Service'
        ##
        ##ET.SubElement('attr').text = ''
        ##ET.SubElement('attrlabl', attrib={'Sync' : 'TRUE'}).text = 'EFFECTDATE'
        ##
        ##ET.SubElement('attalias', attrib={'Sync' : 'TRUE'}).text = 'Effective Date'
        ##
        ##ET.SubElement('attrtype', attrib={'Sync' : 'TRUE'}).text = 'String'
        ##
        ##ET.SubElement('attwidth', attrib={'Sync' : 'TRUE'}).text = '10'
        ##
        ##ET.SubElement('atprecis', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attscale', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attrdef', attrib={'Sync' : 'TRUE'}).text = 'Effective date for an ESA-listed entity. Null for proposed listings. MM/DD/YYYY format'
        ##
        ##ET.SubElement('attrdefs', attrib={'Sync' : 'TRUE'}).text = 'National Marine Fisheries Service'
        ##
        ##ET.SubElement('attr').text = ''
        ##ET.SubElement('attrlabl', attrib={'Sync' : 'TRUE'}).text = 'CREATEDATE'
        ##
        ##ET.SubElement('attalias', attrib={'Sync' : 'TRUE'}).text = 'Create Date'
        ##
        ##ET.SubElement('attrtype', attrib={'Sync' : 'TRUE'}).text = 'String'
        ##
        ##ET.SubElement('attwidth', attrib={'Sync' : 'TRUE'}).text = '10'
        ##
        ##ET.SubElement('atprecis', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attscale', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attrdef', attrib={'Sync' : 'TRUE'}).text = 'Date spatial feature was created or geometry was last edited. MM/DD/YYYY format'
        ##
        ##ET.SubElement('attrdefs', attrib={'Sync' : 'TRUE'}).text = 'National Marine Fisheries Service'
        ##
        ##ET.SubElement('attr').text = ''
        ##ET.SubElement('attrlabl', attrib={'Sync' : 'TRUE'}).text = 'NOTES'
        ##
        ##ET.SubElement('attalias', attrib={'Sync' : 'TRUE'}).text = 'Notes'
        ##
        ##ET.SubElement('attrtype', attrib={'Sync' : 'TRUE'}).text = 'String'
        ##
        ##ET.SubElement('attwidth', attrib={'Sync' : 'TRUE'}).text = '255'
        ##
        ##ET.SubElement('atprecis', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attscale', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attrdef', attrib={'Sync' : 'TRUE'}).text = 'Additional information about the feature that is not contained in other fields.'
        ##
        ##ET.SubElement('attrdefs', attrib={'Sync' : 'TRUE'}).text = 'National Marine Fisheries Service'
        ##
        ##
        ##ET.SubElement('attr').text = ''
        ##ET.SubElement('attrlabl', attrib={'Sync' : 'TRUE'}).text = 'INPORTURL'
        ##
        ##ET.SubElement('attalias', attrib={'Sync' : 'TRUE'}).text = 'InPort URL'
        ##
        ##ET.SubElement('attrtype', attrib={'Sync' : 'TRUE'}).text = 'String'
        ##
        ##ET.SubElement('attwidth', attrib={'Sync' : 'TRUE'}).text = '255'
        ##
        ##ET.SubElement('atprecis', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attscale', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attrdef', attrib={'Sync' : 'TRUE'}).text = "Feature class metadata URL. InPort is the National Marine Fisheries Service's official metadata catalog found at: https://inport.nmfs.noaa.gov/inport/"
        ##
        ##ET.SubElement('attrdefs', attrib={'Sync' : 'TRUE'}).text = 'National Marine Fisheries Service'
        ##
        ##ET.SubElement('attr').text = ''
        ##ET.SubElement('attrlabl', attrib={'Sync' : 'TRUE'}).text = 'SHAPE_Length'
        ##
        ##ET.SubElement('attalias', attrib={'Sync' : 'TRUE'}).text = 'Shape_Length'
        ##
        ##ET.SubElement('attrtype', attrib={'Sync' : 'TRUE'}).text = 'Double'
        ##
        ##ET.SubElement('attwidth', attrib={'Sync' : 'TRUE'}).text = '8'
        ##
        ##ET.SubElement('atprecis', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attscale', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attrdef', attrib={'Sync' : 'TRUE'}).text = 'Length of feature in internal units.'
        ##
        ##ET.SubElement('attrdefs', attrib={'Sync' : 'TRUE'}).text = 'Esri'
        ##
        ##ET.SubElement('attrdomv').text = ''
        ##
        ##ET.SubElement('udom', attrib={'Sync' : 'TRUE'}).text = 'Positive real numbers that are automatically generated.'
        ##
        ##ET.SubElement('attr').text = ''
        ##ET.SubElement('attrlabl', attrib={'Sync' : 'TRUE'}).text = 'SHAPE_Area'
        ##
        ##ET.SubElement('attalias', attrib={'Sync' : 'TRUE'}).text = 'Shape_Area'
        ##
        ##ET.SubElement('attrtype', attrib={'Sync' : 'TRUE'}).text = 'Double'
        ##
        ##ET.SubElement('attwidth', attrib={'Sync' : 'TRUE'}).text = '8'
        ##
        ##ET.SubElement('atprecis', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attscale', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attrdef', attrib={'Sync' : 'TRUE'}).text = 'Area of feature in internal units squared.'
        ##
        ##ET.SubElement('attrdefs', attrib={'Sync' : 'TRUE'}).text = 'Esri'
        ##
        ##ET.SubElement('attrdomv').text = ''
        ##ET.SubElement('udom', attrib={'Sync' : 'TRUE'}).text = 'Positive real numbers that are automatically generated.'
        ##
        ##ET.SubElement('attr').text = ''
        ##ET.SubElement('attrlabl', attrib={'Sync' : 'TRUE'}).text = 'PUBLIC'
        ##
        ##ET.SubElement('attalias', attrib={'Sync' : 'TRUE'}).text = 'Public Mapper'
        ##
        ##ET.SubElement('attrtype', attrib={'Sync' : 'TRUE'}).text = 'String'
        ##
        ##ET.SubElement('attwidth', attrib={'Sync' : 'TRUE'}).text = '3'
        ##
        ##ET.SubElement('atprecis', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attscale', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##
        ##ET.SubElement('attr').text = ''
        ##ET.SubElement('attrlabl', attrib={'Sync' : 'TRUE'}).text = 'REFERENCE'
        ##
        ##ET.SubElement('attalias', attrib={'Sync' : 'TRUE'}).text = 'Reference'
        ##
        ##ET.SubElement('attrtype', attrib={'Sync' : 'TRUE'}).text = 'String'
        ##
        ##ET.SubElement('attwidth', attrib={'Sync' : 'TRUE'}).text = '500'
        ##
        ##ET.SubElement('atprecis', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attscale', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attrdef', attrib={'Sync' : 'TRUE'}).text = 'In-text citations or full bibliographic citations of references used for feature.'
        ##
        ##ET.SubElement('attrdefs', attrib={'Sync' : 'TRUE'}).text = 'National Marine Fisheries Service'
        ##
        ##ET.SubElement('attr').text = ''
        ##ET.SubElement('attrlabl', attrib={'Sync' : 'TRUE'}).text = 'NMFSPAGE'
        ##
        ##ET.SubElement('attalias', attrib={'Sync' : 'TRUE'}).text = 'Species Webpage'
        ##
        ##ET.SubElement('attrtype', attrib={'Sync' : 'TRUE'}).text = 'String'
        ##
        ##ET.SubElement('attwidth', attrib={'Sync' : 'TRUE'}).text = '500'
        ##
        ##ET.SubElement('atprecis', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attscale', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attrdef', attrib={'Sync' : 'TRUE'}).text = 'NMFS Species Webpage found here: https://www.fisheries.noaa.gov/find-species'
        ##
        ##ET.SubElement('attrdefs', attrib={'Sync' : 'TRUE'}).text = 'National Marine Fisheries Service'
        ##
        ##ET.SubElement('attr').text = ''
        ##ET.SubElement('attrlabl').text = 'FEATNAME'
        ##
        ##ET.SubElement('attalias').text = 'Feature Name'
        ##
        ##ET.SubElement('attrdef', attrib={'Sync' : 'TRUE'}).text = 'Descriptive name for feature.'
        ##
        ##ET.SubElement('attrdefs', attrib={'Sync' : 'TRUE'}).text = 'National Marine Fisheries Service'
        ##
        ##ET.SubElement('attrtype').text = 'String'
        ##
        ##ET.SubElement('attwidth').text = '200'
        ##
        ##ET.SubElement('atprecis', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attscale', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attr').text = ''
        ##ET.SubElement('attrlabl').text = 'LIFESTAGE'
        ##ET.SubElement('attalias').text = 'Lifestage'
        ##ET.SubElement('attrdef', attrib={'Sync' : 'TRUE'}).text = 'Lifestage of ESA-listed entity depicted in feature. This is an optional attribute field.'
        ##
        ##ET.SubElement('attrdefs', attrib={'Sync' : 'TRUE'}).text = 'National Marine Fisheries Service'
        ##
        ##ET.SubElement('attrtype').text = 'String'
        ##
        ##ET.SubElement('attwidth').text = '500'
        ##ET.SubElement('atprecis', attrib={'Sync' : 'TRUE'}).text = '0'
        ##ET.SubElement('attscale', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attr').text = ''
        ##ET.SubElement('attrlabl').text = 'BEHAVIOR'
        ##
        ##ET.SubElement('attalias').text = 'Behavior'
        ##
        ##ET.SubElement('attrdef', attrib={'Sync' : 'TRUE'}).text = 'Behavior (i.e., migrating, feeding, mating) of ESA-listed entity depicted in feature. This is an optional attribute field.'
        ##
        ##ET.SubElement('attrdefs', attrib={'Sync' : 'TRUE'}).text = 'National Marine Fisheries Service'
        ##
        ##ET.SubElement('attrtype').text = 'String'
        ##
        ##ET.SubElement('attwidth').text = '500'
        ##
        ##ET.SubElement('atprecis', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##ET.SubElement('attscale', attrib={'Sync' : 'TRUE'}).text = '0'
        ##
        ##
        ##
        ##
        ##ET.SubElement('mdDateSt', attrib={'Sync' : 'TRUE'}).text = '20241124'
        ##
        ##ET.SubElement('mdMaint').text = ''
        ##ET.SubElement('maintFreq').text = ''
        ##ET.SubElement('MaintFreqCd').set('value', '009')
        ##
        ##ET.SubElement('dqInfo').text = ''
        ##ET.SubElement('dqScope').text = ''
        ##ET.SubElement('scpLvl').text = ''
        ##ET.SubElement('ScopeCd').set('value', '005')
        ##ET.SubElement('mdContact').text = ''
        ##ET.SubElement('rpIndName').text = 'Jonathan Molineaux'
        ##
        ##ET.SubElement('rpOrgName').text = 'NOAA Fisheries Office of Protected Resources'
        ##
        ##ET.SubElement('rpPosName').text = 'Fisheries Biologist'
        ##
        ##ET.SubElement('displayName').text = 'Jonathan Molineaux'
        ##
        ##ET.SubElement('role').text = ''
        ##ET.SubElement('RoleCd').set('value', '001')
        ##
        ##ET.SubElement('rpCntInfo').text = ''
        ##ET.SubElement('cntAddress').set('addressType', '').text = ''
        ##ET.SubElement('eMailAdd').text = 'jonathan.molineaux@noaa.gov'
        ##
        ##ET.SubElement('mdContact').text = ''
        ##ET.SubElement('rpIndName').text = 'Jennifer Schultz'
        ##
        ##ET.SubElement('rpOrgName').text = 'NOAA Fisheries Office of Protected Resources'
        ##
        ##ET.SubElement('rpPosName').text = 'Fisheries Biologist'
        ##
        ##ET.SubElement('displayName').text = 'Jennifer Schultz'
        ##
        ##ET.SubElement('role').text = ''
        ##ET.SubElement('RoleCd').set('value', '001')
        ##
        ##ET.SubElement('rpCntInfo').text = ''
        ##ET.SubElement('cntAddress').set('addressType', '').text = ''
        ##ET.SubElement('eMailAdd').text = 'jennifer.schultz@noaa.gov'

        tree = ET.ElementTree(root)
        ET.indent(tree, space="", level=0)
        #tree.write("filename.xml", encoding="utf-8", xml_declaration=True)
        #tree.write("filename.xml", encoding="unicode", xml_declaration=True)
        tree.write("filename.xml")

        # Convert to string
        #xml_string = ET.tostring(root, encoding="unicode")
        xml_string = ET.tostring(root)

        # Pretty-print the XML string
        reparsed = minidom.parseString(xml_string)
        print(reparsed.toprettyxml(indent="    ", newl=''))

### Read XML file
##        doc = minidom.parse(out_xml)
##
##        # Pretty print the XML
##        pretty_xml = doc.toprettyxml(indent="  ", newl="")
##
##        # Write the pretty XML to a file
##        with open(out_xml, "w") as f:
##            f.write(pretty_xml)


    except:
        traceback.print_exc()
        raise Exception

# Main function
def main():
    try:
        CheckFolderExists = False
        if CheckFolderExists:
            # Folder / GDB setup
            create_folder(project_folder)
            create_folder(scratch_folder)
            create_gdb(project_gdb)
            create_gdb(scratch_gdb)
        del CheckFolderExists

        CreateMetadataXml = False
        if CreateMetadataXml:
            create_metadata_xml()
        del CreateMetadataXml

        # Pretty Print
        PrettyPrint = False
        if PrettyPrint:
            arcpy.AddMessage("Pretty Print XMLs")
            arcpy.env.workspace = rf"{project_folder}"
            xml_files = [f for f in arcpy.ListFiles("*.xml") if f not in ["metadata outline.xml"]]
            for xml_file in xml_files:
                pretty_format_xml_file(rf"{project_folder}\{xml_file}")
                del xml_file
            del xml_files
            arcpy.env.workspace = rf"{project_folder}\Export"
            xml_files = [f for f in arcpy.ListFiles("*.xml") if f not in ["metadata outline.xml"]]
            for xml_file in xml_files:
                pretty_format_xml_file(rf"{project_folder}\Export\{xml_file}")
                del xml_file
            del xml_files
            arcpy.AddMessage("Pretty Print XMLs DONE")
        del PrettyPrint


    except Exception as e:
        print(e)
    except:
        traceback.print_exc()
        raise Exception

if __name__ == '__main__':
    try:
        from time import gmtime, localtime, strftime, time

        # Set a start time so that we can see how log things take
        start_time = time()

        print(f"{'-' * 80}")
        print(f"Python Script:  {os.path.basename(__file__)}")
        print(f"Location:       {os.path.dirname(__file__)}")
        print(f"Python Version: {sys.version} Environment: {os.path.basename(sys.exec_prefix)}")
        print(f"{'-' * 80}\n")
        current_folder = os.path.dirname(__file__)
        project_folder = rf"{current_folder}\Metadata Folder"
        project_gdb    = rf"{project_folder}\Metadata.gdb"
        scratch_folder = rf"{project_folder}\Scratch"
        scratch_gdb    = rf"{scratch_folder}\scratch.gdb"

        main()

        del current_folder
        del project_folder, project_gdb
        del scratch_folder, scratch_gdb

        # Elapsed time
        end_time = time()
        elapse_time =  end_time - start_time

        print(f"\n{'-' * 80}")
        print(f"Python script: {os.path.basename(__file__)} successfully completed {strftime('%a %b %d %I:%M %p', localtime())}")
        print(u"Elapsed Time {0} (H:M:S)".format(strftime("%H:%M:%S", gmtime(elapse_time))))
        print(f"{'-' * 80}")
        del elapse_time, end_time, start_time
        del gmtime, localtime, strftime, time

    except Exception as e:
        print(e)
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