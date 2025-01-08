import xml.etree.ElementTree as ET

root = ET.Element('metadata')

ET.Element('metadata').set('{http://www.w3.org/XML/1998/namespace}lang', 'en')
child = ET.Element('Esri')
##ET.Element('CreaDate').text = '20210712'
##root.append(child)
##ET.Element('CreaTime').text = '10033400'
##root.append(child)
##ET.Element('ArcGISFormat').text = '1.0'
##root.append(child)
##ET.Element('ArcGISstyle').text = 'ISO 19139 Metadata Implementation Specification'
##root.append(child)
##ET.Element('SyncOnce').text = 'FALSE'
root.append(child)
ET.Element('DataProperties').text = ''
##            ET.Element('itemProps').text = ''
##                ET.Element('itemName').set('Sync', 'TRUE').text = 'AbaloneBlack_20210712'
##            root.append(child)
##                ET.Element('imsContentType').set('Sync', 'TRUE', 'export', 'False').text = '002'
##            root.append(child)
##                ET.Element('nativeExtBox').text = ''
##                    ET.Element('westBL').set('Sync', 'TRUE').text = '-125.138309'
##                root.append(child)
##                    ET.Element('eastBL').set('Sync', 'TRUE').text = '-109.670789'
##                root.append(child)
##                    ET.Element('southBL').set('Sync', 'TRUE').text = '22.342045'
##                root.append(child)
##                    ET.Element('northBL').set('Sync', 'TRUE').text = '42.001571'
##                root.append(child)
##                    ET.Element('exTypeCode').set('Sync', 'TRUE').text = '1'
##                root.append(child)
##            root.append(child)
##        root.append(child)
##            ET.Element('coordRef').text = ''
##                ET.Element('type').set('Sync', 'TRUE').text = 'Geographic'
##            root.append(child)
##                ET.Element('geogcsn').set('Sync', 'TRUE').text = 'GCS_WGS_1984'
##            root.append(child)
##                ET.Element('csUnits').set('Sync', 'TRUE').text = 'Angular Unit: Degree (0.017453)'
##            root.append(child)
##                ET.Element('peXml').set('Sync', 'TRUE').text = '<GeographicCoordinateSystem xsi:type='typens:GeographicCoordinateSystem' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xmlns:xs='http://www.w3.org/2001/XMLSchema' xmlns:typens='http://www.esri.com/schemas/ArcGIS/3.4.0'><WKT>GEOGCS[&quot;GCS_WGS_1984&quot;,DATUM[&quot;D_WGS_1984&quot;,SPHEROID[&quot;WGS_1984&quot;,6378137.0,298.257223563]],PRIMEM[&quot;Greenwich&quot;,0.0],UNIT[&quot;Degree&quot;,0.0174532925199433],AUTHORITY[&quot;EPSG&quot;,4326]]</WKT><XOrigin>-400</XOrigin><YOrigin>-400</YOrigin><XYScale>999999999.99999988</XYScale><ZOrigin>-100000</ZOrigin><ZScale>10000</ZScale><MOrigin>-100000</MOrigin><MScale>10000</MScale><XYTolerance>8.983152841195215e-09</XYTolerance><ZTolerance>0.001</ZTolerance><MTolerance>0.001</MTolerance><HighPrecision>true</HighPrecision><LeftLongitude>-180</LeftLongitude><WKID>4326</WKID><LatestWKID>4326</LatestWKID></GeographicCoordinateSystem>'
##            root.append(child)
##        root.append(child)
##    root.append(child)
##        ET.Element('SyncDate').text = '20241124'
##    root.append(child)
##        ET.Element('SyncTime').text = '12383200'
##    root.append(child)
##        ET.Element('ModDate').text = '20241124'
##    root.append(child)
##        ET.Element('ModTime').text = '12383200'
##    root.append(child)
##        ET.Element('scaleRange').text = ''
##            ET.Element('minScale').text = '150000000'
##        root.append(child)
##            ET.Element('maxScale').text = '5000'
##        root.append(child)
##    root.append(child)
##        ET.Element('ArcGISProfile').text = 'ISO19139'
##    root.append(child)
##root.append(child)
##    ET.Element('dataIdInfo').text = ''
##        ET.Element('envirDesc').set('Sync', 'TRUE').text = 'Esri ArcGIS 13.4.0.55405'
##    root.append(child)
##        ET.Element('dataLang').text = ''
##            ET.Element('languageCode').set('value', 'eng', 'Sync', 'TRUE')
##        root.append(child)
##            ET.Element('countryCode').set('value', 'USA', 'Sync', 'TRUE')
##        root.append(child)
##    root.append(child)
##        ET.Element('idCitation').text = ''
##            ET.Element('resTitle').set('Sync', 'TRUE').text = '[insert file name here]'
##        root.append(child)
##            ET.Element('presForm').text = ''
##                ET.Element('PresFormCd').set('value', '005', 'Sync', 'TRUE')
##            root.append(child)
##                ET.Element('fgdcGeoform').text = 'vector digital data'
##            root.append(child)
##        root.append(child)
##            ET.Element('citRespParty').text = ''
##                ET.Element('rpIndName').text = 'Jonathan Molineaux'
##            root.append(child)
##                ET.Element('rpOrgName').text = 'NMFS Office Of Protected Resources'
##            root.append(child)
##                ET.Element('rpPosName').text = 'Fisheries Biologist'
##            root.append(child)
##                ET.Element('role').text = ''
##                    ET.Element('RoleCd').set('value', '001')
##                root.append(child)
##            root.append(child)
##                ET.Element('rpCntInfo').text = ''
##                    ET.Element('cntAddress').set('addressType', '').text = ''
##                        ET.Element('eMailAdd').text = 'jonathan.molineaux@noaa.gov'
##                    root.append(child)
##                root.append(child)
##            root.append(child)
##                ET.Element('displayName').text = 'Jonathan Molineaux'
##            root.append(child)
##        root.append(child)
##            ET.Element('date').text = ''
##                ET.Element('pubDate').text = '2024-11-22T00:00:00'
##            root.append(child)
##        root.append(child)
##    root.append(child)
##        ET.Element('spatRpType').text = ''
##            ET.Element('SpatRepTypCd').set('value', '001', 'Sync', 'TRUE')
##        root.append(child)
##    root.append(child)
##        ET.Element('idPurp').text = 'This is new text for an existing Purpose metadata element.'
##    root.append(child)
##        ET.Element('dataChar').text = ''
##            ET.Element('CharSetCd').set('value', '004')
##        root.append(child)
##    root.append(child)
##        ET.Element('resMaint').text = ''
##            ET.Element('maintFreq').text = ''
##                ET.Element('MaintFreqCd').set('value', '009')
##            root.append(child)
##        root.append(child)
##    root.append(child)
##        ET.Element('idPoC').text = ''
##            ET.Element('rpIndName').text = 'Jonathan Molineaux'
##        root.append(child)
##            ET.Element('rpOrgName').text = 'NOAA Fisheries Office of Protected Resources'
##        root.append(child)
##            ET.Element('rpPosName').text = 'Fisheries Biologist'
##        root.append(child)
##            ET.Element('role').text = ''
##                ET.Element('RoleCd').set('value', '001')
##            root.append(child)
##        root.append(child)
##            ET.Element('rpCntInfo').text = ''
##                ET.Element('cntAddress').set('addressType', '').text = ''
##                    ET.Element('eMailAdd').text = 'jonathan.molineaux@noaa.gov'
##                root.append(child)
##            root.append(child)
##        root.append(child)
##    root.append(child)
##        ET.Element('idPoC').text = ''
##            ET.Element('rpIndName').text = 'Jennifer Schultz'
##        root.append(child)
##            ET.Element('rpOrgName').text = 'NOAA Fisheries Office of Protected Resources'
##        root.append(child)
##            ET.Element('rpPosName').text = 'Fisheries Biologist'
##        root.append(child)
##            ET.Element('role').text = ''
##                ET.Element('RoleCd').set('value', '001')
##            root.append(child)
##        root.append(child)
##            ET.Element('rpCntInfo').text = ''
##                ET.Element('cntAddress').set('addressType', '').text = ''
##                    ET.Element('eMailAdd').text = 'jennifer.schultz@noaa.gov'
##                root.append(child)
##            root.append(child)
##        root.append(child)
##    root.append(child)
##        ET.Element('idAbs').text = '<DIV STYLE="text-align:Left;"><DIV><DIV><P><SPAN>This range includes [all; marine; freshwater; adult; immature/juvenile; larval] life stages of the species [add any caveats, e.g., why something is not included]. The range was based on the following [tracking, tagging, bycatch, and sighting] data: [Provide data and citations used to create range, including name/version/date of shoreline data.] Disclaimer: the spatial data provided here display an approximate distribution; they should not be conflated with the definitive range of the listed entity under the ESA. The spatial data provided here display an approximate distribution of the listed entity based on the best available information at the time of creation; they do not constitute should not be conflated with the definitive range of the listed entity under the ESA. As such, the distribution of the listed entity may not be exclusively limited to the range identified herein, and we have not verified the listed entity’s occurrence in every area comprising the range. Please notify us if you have recent information that is not reflected in our data (see Citation contacts). Use of these data do not replace the ESA section 7 consultation process; however, these data may be a first step in determining whether a proposed federal action overlaps with listed species’ ranges or critical habitat.</SPAN></P><P><SPAN /></P></DIV></DIV></DIV>'
##    root.append(child)
##        ET.Element('idCredit').text = 'This is new text for an existing Purpose metadata element.'
##    root.append(child)
##        ET.Element('searchKeys').text = ''
##            ET.Element('keyword').text = '[inert ESA-listed entity name here]; ESA; range; NMFS'
##        root.append(child)
##    root.append(child)
##        ET.Element('themeKeys').text = ''
##            ET.Element('thesaName').text = ''
##                ET.Element('resTitle').text = 'N/A'
##            root.append(child)
##                ET.Element('date').text = ''
##                    ET.Element('pubDate').text = '2024-11-22T00:00:00'
##                root.append(child)
##            root.append(child)
##        root.append(child)
##            ET.Element('keyword').text = 'ESA, NMFS, Species' Range'
##        root.append(child)
##    root.append(child)
##        ET.Element('placeKeys').text = ''
##            ET.Element('keyword').text = 'Global, National'
##        root.append(child)
##    root.append(child)
##        ET.Element('idStatus').text = ''
##            ET.Element('ProgCd').set('value', '004')
##        root.append(child)
##    root.append(child)
##        ET.Element('resConst').text = ''
##            ET.Element('Consts').text = ''
##                ET.Element('useLimit').text = '<DIV STYLE="text-align:Left;"><DIV><DIV><DIV STYLE="font-size:12pt"><P><SPAN>*** Attribution *** Whenever NMFS material is reproduced and re-disseminated, we request that users attribute the material appropriately. Pursuant to 17 U.S. C. 403, parties who produce copyrighted works consisting predominantly of material created by the Federal Government are encouraged to provide notice with such work(s) identifying the U.S. Government material incorporated and stating that such material is not subject to copyright protection. Please cite the species range datasets as indicated in the metadata for each species, or if not indicated, as follows with the appropriate information substituted for all text in {CURLY BRACKETS}: </SPAN></P><P><SPAN>NOAA Fisheries Service. Endangered Species Act Species Range Geodatabase. Silver Spring, MD: National Oceanic and Atmospheric Administration (NOAA), National Marine Fisheries Service (NMFS), Office of Protected Resources (OPR) [producer] {GEODATABASE PUBLICATION DATE}. {ADD URL}</SPAN></P><P><SPAN>***No Warranty*** The user assumes the entire risk related to its use of these data. NMFS is providing these data "as is," and NMFS disclaims any and all warranties, whether express or implied, including (without limitation) any implied warranties of merchantability or fitness for a particular purpose. No warranty expressed or implied is made regarding the accuracy or utility of the data on any other system or for general or scientific purposes, nor shall the act of distribution constitute any such warranty. It is strongly recommended that careful attention be paid to the contents of the metadata file associated with these data to evaluate dataset limitations, restrictions or intended use. In no event will NMFS be liable to you or to any third party for any direct, indirect, incidental, consequential, special or exemplary damages or lost profit resulting from any use or misuse of this data. </SPAN></P><P><SPAN>*** Proper Usage *** The information on government servers are in the public domain, unless specifically annotated otherwise, and may be used freely by the public. Before using information obtained from this server, special attention should be given to the date and time of the data and products being displayed. This information shall not be modified in content and then presented as official government material. This dataset was created to generally represent our best professional judgment of the ranges of listed species based on the best available information at the time of publication, including: geographic factors, time of year, and the biology of each species. The dataset should not be used to infer information regarding the existence or details of other marine features or resources, including, but not limited to, navigable waters, coastlines, bathymetry, submerged features, or man-made structures. Users assume responsibility for determining the appropriate use of this dataset. </SPAN></P><P><SPAN>*** Temporal Considerations *** Species’ ranges are subject to change or modification. Generally, we become aware of these changes during the 5-year review of the species’ status, as required under the ESA. If changes to the range are deemed necessary, we will make such changes in the database, which will be archived and replaced by an updated version as soon as feasible. It is the user’s responsibility to ensure the most recent species’ range data are being used. </SPAN></P><P><SPAN>*** Shorelines/Base Layers *** The accuracy of this dataset is dependent upon the accuracy and resolution of the datasets (e.g. shoreline, hydrography, bathymetry, shared administrative boundaries) used in the creation process. Source datasets used are specified in the metadata. These data sources were selected for their suitability to a broad audience, and may not be suitable for specific uses requiring higher-resolution information. Coastlines and water body boundaries change. Unless otherwise noted, where the National Hydrography Dataset or NOAA Medium Resolution Shoreline is used, assume the boundary reaches the most current river, estuary, or coastal shoreline delineation available.</SPAN></P><P><SPAN>*** Data Limitations ***</SPAN></P><P><SPAN>Our data may lack the spatial resolution to capture the entire range of a species, especially outside of a major waterway (e.g., in a very small tributary, or shallow area near a marsh). For section 7 consultations, we recommend that Federal action agencies request technical assistance to verify presence/absence of listed species within their action area.</SPAN></P></DIV></DIV></DIV></DIV>'
##            root.append(child)
##        root.append(child)
##    root.append(child)
##        ET.Element('dataExt').text = ''
##            ET.Element('geoEle').text = ''
##                ET.Element('GeoBndBox').set('esriExtentType', 'search').text = ''
##                    ET.Element('exTypeCode').set('Sync', 'TRUE').text = '1'
##                root.append(child)
##                    ET.Element('westBL').set('Sync', 'TRUE').text = '-125.138309'
##                root.append(child)
##                    ET.Element('eastBL').set('Sync', 'TRUE').text = '-109.670789'
##                root.append(child)
##                    ET.Element('northBL').set('Sync', 'TRUE').text = '42.001571'
##                root.append(child)
##                    ET.Element('southBL').set('Sync', 'TRUE').text = '22.342045'
##                root.append(child)
##            root.append(child)
##        root.append(child)
##    root.append(child)
##        ET.Element('tpCat').text = ''
##            ET.Element('TopicCatCd').set('value', '002')
##        root.append(child)
##    root.append(child)
##        ET.Element('tpCat').text = ''
##            ET.Element('TopicCatCd').set('value', '007')
##        root.append(child)
##    root.append(child)
##        ET.Element('tpCat').text = ''
##            ET.Element('TopicCatCd').set('value', '014')
##        root.append(child)
##    root.append(child)
##        ET.Element('idCredit').text = 'This is new text for an existing Purpose metadata element.'
##    root.append(child)
##root.append(child)
##    ET.Element('mdLang').text = ''
##        ET.Element('languageCode').set('value', 'eng', 'Sync', 'TRUE')
##    root.append(child)
##        ET.Element('countryCode').set('value', 'USA', 'Sync', 'TRUE')
##    root.append(child)
##root.append(child)
##    ET.Element('mdChar').text = ''
##        ET.Element('CharSetCd').set('value', '004', 'Sync', 'TRUE')
##    root.append(child)
##root.append(child)
##    ET.Element('distInfo').text = ''
##        ET.Element('distFormat').text = ''
##            ET.Element('formatName').set('Sync', 'TRUE').text = 'File Geodatabase Feature Class'
##        root.append(child)
##            ET.Element('formatVer').text = 'NMFS ESA Range Geodatabase 2021'
##        root.append(child)
##    root.append(child)
##        ET.Element('distributor').text = ''
##            ET.Element('distorCont').text = ''
##                ET.Element('rpOrgName').text = 'NMFS Office Of Protected Resources'
##            root.append(child)
##                ET.Element('displayName').text = 'Department of Commerce (DOC), National Oceanic and Atmospheric Administration (NOAA), National Marine Fisheries Service (NMFS)'
##            root.append(child)
##                ET.Element('role').text = ''
##                    ET.Element('RoleCd').set('value', '005')
##                root.append(child)
##            root.append(child)
##                ET.Element('rpCntInfo').text = ''
##                    ET.Element('cntAddress').set('addressType', '').text = ''
##                        ET.Element('eMailAdd').text = 'jonathan.molineaux@noaa.gov'
##                    root.append(child)
##                root.append(child)
##            root.append(child)
##        root.append(child)
##            ET.Element('distorFormat').text = ''
##                ET.Element('formatName').text = 'File Geodatabase Feature Class'
##            root.append(child)
##                ET.Element('formatVer').text = 'NMFS ESA Range Geodatabase 2021'
##            root.append(child)
##        root.append(child)
##            ET.Element('distorTran').text = ''
##                ET.Element('onLineSrc').text = ''
##                    ET.Element('linkage').text = 'https://www.fisheries.noaa.gov/science-and-data'
##                root.append(child)
##            root.append(child)
##        root.append(child)
##    root.append(child)
##root.append(child)
##    ET.Element('mdHrLv').text = ''
##        ET.Element('ScopeCd').set('value', '005', 'Sync', 'TRUE')
##    root.append(child)
##root.append(child)
##    ET.Element('mdHrLvName').set('Sync', 'TRUE').text = 'dataset'
##root.append(child)
##    ET.Element('refSysInfo').text = ''
##        ET.Element('RefSystem').set('dimension', '').text = ''
##            ET.Element('refSysID').text = ''
##                ET.Element('identCode').set('code', '4326', 'Sync', 'TRUE')
##            root.append(child)
##                ET.Element('idCodeSpace').set('Sync', 'TRUE').text = 'EPSG'
##            root.append(child)
##                ET.Element('idVersion').set('Sync', 'TRUE').text = '6.2(3.0.1)'
##            root.append(child)
##        root.append(child)
##    root.append(child)
##root.append(child)
##    ET.Element('spatRepInfo').text = ''
##        ET.Element('VectSpatRep').text = ''
##            ET.Element('geometObjs').set('Name', 'AbaloneBlack_20210712').text = ''
##                ET.Element('geoObjTyp').text = ''
##                    ET.Element('GeoObjTypCd').set('value', '002', 'Sync', 'TRUE')
##                root.append(child)
##            root.append(child)
##                ET.Element('geoObjCnt').set('Sync', 'TRUE').text = '2'
##            root.append(child)
##        root.append(child)
##            ET.Element('topLvl').text = ''
##                ET.Element('TopoLevCd').set('value', '001', 'Sync', 'TRUE')
##            root.append(child)
##        root.append(child)
##    root.append(child)
##root.append(child)
##    ET.Element('spdoinfo').text = ''
##        ET.Element('ptvctinf').text = ''
##            ET.Element('esriterm').set('Name', 'AbaloneBlack_20210712').text = ''
##                ET.Element('efeatyp').set('Sync', 'TRUE').text = 'Simple'
##            root.append(child)
##                ET.Element('efeageom').set('code', '4', 'Sync', 'TRUE')
##            root.append(child)
##                ET.Element('esritopo').set('Sync', 'TRUE').text = 'FALSE'
##            root.append(child)
##                ET.Element('efeacnt').set('Sync', 'TRUE').text = '2'
##            root.append(child)
##                ET.Element('spindex').set('Sync', 'TRUE').text = 'TRUE'
##            root.append(child)
##                ET.Element('linrefer').set('Sync', 'TRUE').text = 'FALSE'
##            root.append(child)
##        root.append(child)
##    root.append(child)
##root.append(child)
##    ET.Element('eainfo').text = ''
##        ET.Element('detailed').set('Name', 'AbaloneBlack_20210712').text = ''
##            ET.Element('enttyp').text = ''
##                ET.Element('enttypl').set('Sync', 'TRUE').text = 'AbaloneBlack_20210712'
##            root.append(child)
##                ET.Element('enttypt').set('Sync', 'TRUE').text = 'Feature Class'
##            root.append(child)
##                ET.Element('enttypc').set('Sync', 'TRUE').text = '2'
##            root.append(child)
##                ET.Element('enttypd').text = 'A collection of geographic features with the same geometry type.'
##            root.append(child)
##                ET.Element('enttypds').text = 'Esri'
##            root.append(child)
##        root.append(child)
##            ET.Element('attr').text = ''
##                ET.Element('attrlabl').set('Sync', 'TRUE').text = 'OBJECTID'
##            root.append(child)
##                ET.Element('attalias').set('Sync', 'TRUE').text = 'OBJECTID'
##            root.append(child)
##                ET.Element('attrtype').set('Sync', 'TRUE').text = 'OID'
##            root.append(child)
##                ET.Element('attwidth').set('Sync', 'TRUE').text = '4'
##            root.append(child)
##                ET.Element('atprecis').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##                ET.Element('attscale').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##                ET.Element('attrdef').set('Sync', 'TRUE').text = 'Internal feature number.'
##            root.append(child)
##                ET.Element('attrdefs').set('Sync', 'TRUE').text = 'Esri'
##            root.append(child)
##                ET.Element('attrdomv').text = ''
##                    ET.Element('udom').set('Sync', 'TRUE').text = 'Sequential unique whole numbers that are automatically generated.'
##                root.append(child)
##            root.append(child)
##        root.append(child)
##            ET.Element('attr').text = ''
##                ET.Element('attrlabl').set('Sync', 'TRUE').text = 'SHAPE'
##            root.append(child)
##                ET.Element('attalias').set('Sync', 'TRUE').text = 'Shape'
##            root.append(child)
##                ET.Element('attrtype').set('Sync', 'TRUE').text = 'Geometry'
##            root.append(child)
##                ET.Element('attwidth').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##                ET.Element('atprecis').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##                ET.Element('attscale').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##                ET.Element('attrdef').set('Sync', 'TRUE').text = 'Feature geometry.'
##            root.append(child)
##                ET.Element('attrdefs').set('Sync', 'TRUE').text = 'Esri'
##            root.append(child)
##                ET.Element('attrdomv').text = ''
##                    ET.Element('udom').set('Sync', 'TRUE').text = 'Coordinates defining the features.'
##                root.append(child)
##            root.append(child)
##        root.append(child)
##            ET.Element('attr').text = ''
##                ET.Element('attrlabl').set('Sync', 'TRUE').text = 'ID'
##            root.append(child)
##                ET.Element('attalias').set('Sync', 'TRUE').text = 'ID'
##            root.append(child)
##                ET.Element('attrtype').set('Sync', 'TRUE').text = 'Double'
##            root.append(child)
##                ET.Element('attwidth').set('Sync', 'TRUE').text = '8'
##            root.append(child)
##                ET.Element('atprecis').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##                ET.Element('attscale').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##                ET.Element('attrdef').set('Sync', 'TRUE').text = '9 digit unique identifier for each feature in the geodatabase.
##Used to relate or join supplemental attribute tables.'
##            root.append(child)
##                ET.Element('attrdefs').set('Sync', 'TRUE').text = 'National Marine Fisheries Service'
##            root.append(child)
##        root.append(child)
##            ET.Element('attr').text = ''
##                ET.Element('attrlabl').set('Sync', 'TRUE').text = 'SCIENAME'
##            root.append(child)
##                ET.Element('attalias').set('Sync', 'TRUE').text = 'Scientific Name'
##            root.append(child)
##                ET.Element('attrtype').set('Sync', 'TRUE').text = 'String'
##            root.append(child)
##                ET.Element('attwidth').set('Sync', 'TRUE').text = '100'
##            root.append(child)
##                ET.Element('atprecis').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##                ET.Element('attscale').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##                ET.Element('attrdef').set('Sync', 'TRUE').text = 'Binomial or trinomial scientific name.
##
##Value formatted as written in the Code of Federal Regulations.'
##            root.append(child)
##                ET.Element('attrdefs').set('Sync', 'TRUE').text = 'National Marine Fisheries Service'
##            root.append(child)
##        root.append(child)
##            ET.Element('attr').text = ''
##                ET.Element('attrlabl').set('Sync', 'TRUE').text = 'COMNAME'
##            root.append(child)
##                ET.Element('attalias').set('Sync', 'TRUE').text = 'Common Name'
##            root.append(child)
##                ET.Element('attrtype').set('Sync', 'TRUE').text = 'String'
##            root.append(child)
##                ET.Element('attwidth').set('Sync', 'TRUE').text = '100'
##            root.append(child)
##                ET.Element('atprecis').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##                ET.Element('attscale').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##                ET.Element('attrdef').set('Sync', 'TRUE').text = 'Legal common name of species.
##
##Value formatted as written in the Code of Federal Regulations.'
##            root.append(child)
##                ET.Element('attrdefs').set('Sync', 'TRUE').text = 'National Marine Fisheries Service'
##            root.append(child)
##        root.append(child)
##            ET.Element('attr').text = ''
##                ET.Element('attrlabl').set('Sync', 'TRUE').text = 'LISTENTITY'
##            root.append(child)
##                ET.Element('attalias').set('Sync', 'TRUE').text = 'Listed Entity'
##            root.append(child)
##                ET.Element('attrtype').set('Sync', 'TRUE').text = 'String'
##            root.append(child)
##                ET.Element('attwidth').set('Sync', 'TRUE').text = '100'
##            root.append(child)
##                ET.Element('atprecis').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##                ET.Element('attscale').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##                ET.Element('attrdef').set('Sync', 'TRUE').text = 'Full text of the ESA listed entity: Species, Subspecies, Distinct Population Segment (DPS), or Evolutionarily Significant Unit (ESU).
##
##Value formatted as written in the Code of Federal Regulations.
##*Note: for entire species listings, this value will be the same as COMNAME value.'
##            root.append(child)
##                ET.Element('attrdefs').set('Sync', 'TRUE').text = 'National Marine Fisheries Service'
##            root.append(child)
##        root.append(child)
##            ET.Element('attr').text = ''
##                ET.Element('attrlabl').set('Sync', 'TRUE').text = 'LISTSTATUS'
##            root.append(child)
##                ET.Element('attalias').set('Sync', 'TRUE').text = 'Listing Status'
##            root.append(child)
##                ET.Element('attrtype').set('Sync', 'TRUE').text = 'String'
##            root.append(child)
##                ET.Element('attwidth').set('Sync', 'TRUE').text = '20'
##            root.append(child)
##                ET.Element('atprecis').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##                ET.Element('attscale').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##                ET.Element('attrdef').set('Sync', 'TRUE').text = 'Current Endangered Species Act listing status.'
##            root.append(child)
##                ET.Element('attrdefs').set('Sync', 'TRUE').text = 'National Marine Fisheries Service'
##            root.append(child)
##                ET.Element('attrdomv').text = ''
##                    ET.Element('edom').text = ''
##                        ET.Element('edomv').text = 'Endangered'
##                    root.append(child)
##                        ET.Element('edomvd').text = 'Species that are in danger of extinction throughout all or a significant portion of their range.'
##                    root.append(child)
##                        ET.Element('edomvds').text = 'Endangered Species Act of 1973'
##                    root.append(child)
##                root.append(child)
##                    ET.Element('edom').text = ''
##                        ET.Element('edomv').text = 'Threatened'
##                    root.append(child)
##                        ET.Element('edomvd').text = 'Species that are likely to become endangered in the foreseeable future.'
##                    root.append(child)
##                        ET.Element('edomvds').text = 'Endangered Species Act of 1973'
##                    root.append(child)
##                root.append(child)
##                    ET.Element('edom').text = ''
##                        ET.Element('edomv').text = 'Delisted'
##                    root.append(child)
##                        ET.Element('edomvd').text = 'Species that were removed from the Endangered Species Act list.'
##                    root.append(child)
##                        ET.Element('edomvds').text = 'Endangered Species Act of 1973'
##                    root.append(child)
##                root.append(child)
##            root.append(child)
##        root.append(child)
##            ET.Element('attr').text = ''
##                ET.Element('attrlabl').set('Sync', 'TRUE').text = 'TAXON'
##            root.append(child)
##                ET.Element('attalias').set('Sync', 'TRUE').text = 'Taxon'
##            root.append(child)
##                ET.Element('attrtype').set('Sync', 'TRUE').text = 'String'
##            root.append(child)
##                ET.Element('attwidth').set('Sync', 'TRUE').text = '50'
##            root.append(child)
##                ET.Element('atprecis').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##                ET.Element('attscale').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##                ET.Element('attrdef').set('Sync', 'TRUE').text = 'Taxonomic unit.'
##            root.append(child)
##                ET.Element('attrdefs').set('Sync', 'TRUE').text = 'National Marine Fisheries Service'
##            root.append(child)
##                ET.Element('attrdomv').text = ''
##                    ET.Element('edom').text = ''
##                        ET.Element('edomv').text = 'baleen whale'
##                    root.append(child)
##                        ET.Element('edomvd').text = 'Any of a suborder (Mysticeti) of large whales that have baleen plates in the upper jaw which are used to filter chiefly small crustaceans out of large quantities of seawater.'
##                    root.append(child)
##                        ET.Element('edomvds').text = 'Merriam-Webster dictionary'
##                    root.append(child)
##                root.append(child)
##                    ET.Element('edom').text = ''
##                        ET.Element('edomv').text = 'toothed whale'
##                    root.append(child)
##                        ET.Element('edomvd').text = 'Any of a suborder (Odontoceti) of cetaceans bearing usually numerous simple conical teeth.'
##                    root.append(child)
##                        ET.Element('edomvds').text = 'Merriam-Webster dictionary'
##                    root.append(child)
##                root.append(child)
##                    ET.Element('edom').text = ''
##                        ET.Element('edomv').text = 'fish'
##                    root.append(child)
##                        ET.Element('edomvd').text = 'Any of numerous cold-blooded strictly aquatic craniate vertebrates that include the bony fishes and the cartilaginous and jawless fishes and that have typically an elongated somewhat spindle-shaped body terminating in a broad caudal fin, limbs in the form of fins when present at all, and a 2-chambered heart by which blood is sent through thoracic gills to be oxygenated.'
##                    root.append(child)
##                        ET.Element('edomvds').text = 'Merriam-Webster dictionary'
##                    root.append(child)
##                root.append(child)
##                    ET.Element('edom').text = ''
##                        ET.Element('edomv').text = 'pinniped'
##                    root.append(child)
##                        ET.Element('edomvd').text = 'Any of an order or suborder (Pinnipedia) of aquatic carnivorous mammals with all four limbs modified into flippers.'
##                    root.append(child)
##                        ET.Element('edomvds').text = 'Merriam-Webster dictionary'
##                    root.append(child)
##                root.append(child)
##                    ET.Element('edom').text = ''
##                        ET.Element('edomv').text = 'marine reptile'
##                    root.append(child)
##                        ET.Element('edomvd').text = 'Any of a class (Reptilia) of cold-blooded, air-breathing, usually egg-laying vertebrates that have adapted for an aquatic or semiaquatic life in a marine environment and have a body typically covered with scales or bony plates and a bony skeleton with a single occipital condyle, a distinct quadrate bone usually immovably articulated with the skull, and ribs attached to the sternum.'
##                    root.append(child)
##                        ET.Element('edomvds').text = 'Merriam-Webster dictionary'
##                    root.append(child)
##                root.append(child)
##                    ET.Element('edom').text = ''
##                        ET.Element('edomv').text = 'invertebrate'
##                    root.append(child)
##                        ET.Element('edomvd').text = 'Any animal that lacks a spinal column.'
##                    root.append(child)
##                        ET.Element('edomvds').text = 'Merriam-Webster dictionary'
##                    root.append(child)
##                root.append(child)
##                    ET.Element('edom').text = ''
##                        ET.Element('edomv').text = 'plant'
##                    root.append(child)
##                        ET.Element('edomvd').text = 'Any of a kingdom (Plantae) of multicellular eukaryotic mostly photosynthetic organisms typically lacking locomotive movement or obvious nervous or sensory organs and possessing cellulose cell walls.'
##                    root.append(child)
##                        ET.Element('edomvds').text = 'Merriam-Webster dictionary'
##                    root.append(child)
##                root.append(child)
##            root.append(child)
##        root.append(child)
##            ET.Element('attr').text = ''
##                ET.Element('attrlabl').set('Sync', 'TRUE').text = 'LEADOFFICE'
##            root.append(child)
##                ET.Element('attalias').set('Sync', 'TRUE').text = 'Lead Office'
##            root.append(child)
##                ET.Element('attrtype').set('Sync', 'TRUE').text = 'String'
##            root.append(child)
##                ET.Element('attwidth').set('Sync', 'TRUE').text = '50'
##            root.append(child)
##                ET.Element('atprecis').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##                ET.Element('attscale').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##                ET.Element('attrdef').set('Sync', 'TRUE').text = 'NMFS Office responsible for the species’ range within feature.'
##            root.append(child)
##                ET.Element('attrdefs').set('Sync', 'TRUE').text = 'National Marine Fisheries Service'
##            root.append(child)
##                ET.Element('attrdomv').text = ''
##                    ET.Element('edom').text = ''
##                        ET.Element('edomv').text = 'Office of Protected Resources'
##                    root.append(child)
##                        ET.Element('edomvd').text = 'Headquarters office responsible for nationwide conservation, protection, and recovery of endangered and threatened marine species listed under the Endangered Species Act.'
##                    root.append(child)
##                        ET.Element('edomvds').text = 'National Marine Fisheries Service'
##                    root.append(child)
##                root.append(child)
##                    ET.Element('edom').text = ''
##                        ET.Element('edomv').text = 'Alaska Region'
##                    root.append(child)
##                        ET.Element('edomvd').text = 'Includes Alaska and adjacent marine waters extending outwards to the 200 nautical mile boundary of the Exclusive Economic Zone.'
##                    root.append(child)
##                        ET.Element('edomvds').text = 'National Marine Fisheries Service'
##                    root.append(child)
##                root.append(child)
##                    ET.Element('edom').text = ''
##                        ET.Element('edomv').text = 'West Coast Region'
##                    root.append(child)
##                        ET.Element('edomvd').text = 'Includes Idaho, Washington, Oregon, California and adjacent marine waters extending outwards to the 200 nautical mile boundary of the Exclusive Economic Zone.'
##                    root.append(child)
##                        ET.Element('edomvds').text = 'National Marine Fisheries Service'
##                    root.append(child)
##                root.append(child)
##                    ET.Element('edom').text = ''
##                        ET.Element('edomv').text = 'Greater Atlantic Region'
##                    root.append(child)
##                        ET.Element('edomvd').text = 'Includes Minnesota, Wisconsin, Michigan, Illinois, Indiana, Ohio, Kentucky, West Virginia, Pennsylvania, New York, Vermont, New Hampshire, Maine, Massachusetts, Rhode Island, Connecticut, New Jersey, Delaware, Maryland, Virginia, North Carolina (north of Cape Hatteras) and adjacent marine waters extending outwards to the 200 nautical mile boundary of the Exclusive Economic Zone.'
##                    root.append(child)
##                        ET.Element('edomvds').text = 'National Marine Fisheries Service'
##                    root.append(child)
##                root.append(child)
##                    ET.Element('edom').text = ''
##                        ET.Element('edomv').text = 'Southeast Region'
##                    root.append(child)
##                        ET.Element('edomvd').text = 'Includes North Carolina (south of Cape Hatteras), South Carolina, Georgia, Florida, Alabama, Mississippi, Louisiana, Texas, Arkansas, Iowa, Kansas, Kentucky, Missouri, Nebraska, New Mexico, Oklahoma, Tennessee, the Commonwealth of Puerto Rico, the U.S. Virgin Islands and adjacent marine waters extending outwards to the 200 nautical mile boundary of the Exclusive Economic Zone.'
##                    root.append(child)
##                        ET.Element('edomvds').text = 'National Marine Fisheries Service'
##                    root.append(child)
##                root.append(child)
##                    ET.Element('edom').text = ''
##                        ET.Element('edomv').text = 'Pacific Islands Region'
##                    root.append(child)
##                        ET.Element('edomvd').text = 'Includes Hawai'i, American Samoa, Guam, the Commonwealth of the Northern Mariana Islands, Kingman Reef, Howland Island, Baker Island, Jarvis Island, Wake Island, Johnston Atoll, Palmyra Atoll and adjacent marine waters extending outwards to the 200 nautical mile boundary of the Exclusive Economic Zone.'
##                    root.append(child)
##                        ET.Element('edomvds').text = 'National Marine Fisheries Service'
##                    root.append(child)
##                root.append(child)
##            root.append(child)
##        root.append(child)
##            ET.Element('attr').text = ''
##                ET.Element('attrlabl').set('Sync', 'TRUE').text = 'FR'
##            root.append(child)
##                ET.Element('attalias').set('Sync', 'TRUE').text = 'Federal Register Rule'
##            root.append(child)
##                ET.Element('attrtype').set('Sync', 'TRUE').text = 'String'
##            root.append(child)
##                ET.Element('attwidth').set('Sync', 'TRUE').text = '255'
##            root.append(child)
##                ET.Element('atprecis').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##                ET.Element('attscale').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##        root.append(child)
##            ET.Element('attr').text = ''
##                ET.Element('attrlabl').set('Sync', 'TRUE').text = 'PUBDATE'
##            root.append(child)
##                ET.Element('attalias').set('Sync', 'TRUE').text = 'Publication Date'
##            root.append(child)
##                ET.Element('attrtype').set('Sync', 'TRUE').text = 'String'
##            root.append(child)
##                ET.Element('attwidth').set('Sync', 'TRUE').text = '10'
##            root.append(child)
##                ET.Element('atprecis').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##                ET.Element('attscale').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##                ET.Element('attrdef').set('Sync', 'TRUE').text = 'Federal Register Notice publication date for the ESA-listed entity.
##
##MM/DD/YYYY format'
##            root.append(child)
##                ET.Element('attrdefs').set('Sync', 'TRUE').text = 'National Marine Fisheries Service'
##            root.append(child)
##        root.append(child)
##            ET.Element('attr').text = ''
##                ET.Element('attrlabl').set('Sync', 'TRUE').text = 'EFFECTDATE'
##            root.append(child)
##                ET.Element('attalias').set('Sync', 'TRUE').text = 'Effective Date'
##            root.append(child)
##                ET.Element('attrtype').set('Sync', 'TRUE').text = 'String'
##            root.append(child)
##                ET.Element('attwidth').set('Sync', 'TRUE').text = '10'
##            root.append(child)
##                ET.Element('atprecis').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##                ET.Element('attscale').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##                ET.Element('attrdef').set('Sync', 'TRUE').text = 'Effective date for an ESA-listed entity. Null for proposed listings.
##
##MM/DD/YYYY format'
##            root.append(child)
##                ET.Element('attrdefs').set('Sync', 'TRUE').text = 'National Marine Fisheries Service'
##            root.append(child)
##        root.append(child)
##            ET.Element('attr').text = ''
##                ET.Element('attrlabl').set('Sync', 'TRUE').text = 'CREATEDATE'
##            root.append(child)
##                ET.Element('attalias').set('Sync', 'TRUE').text = 'Create Date'
##            root.append(child)
##                ET.Element('attrtype').set('Sync', 'TRUE').text = 'String'
##            root.append(child)
##                ET.Element('attwidth').set('Sync', 'TRUE').text = '10'
##            root.append(child)
##                ET.Element('atprecis').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##                ET.Element('attscale').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##                ET.Element('attrdef').set('Sync', 'TRUE').text = 'Date spatial feature was created or geometry was last edited.
##
##MM/DD/YYYY format'
##            root.append(child)
##                ET.Element('attrdefs').set('Sync', 'TRUE').text = 'National Marine Fisheries Service'
##            root.append(child)
##        root.append(child)
##            ET.Element('attr').text = ''
##                ET.Element('attrlabl').set('Sync', 'TRUE').text = 'NOTES'
##            root.append(child)
##                ET.Element('attalias').set('Sync', 'TRUE').text = 'Notes'
##            root.append(child)
##                ET.Element('attrtype').set('Sync', 'TRUE').text = 'String'
##            root.append(child)
##                ET.Element('attwidth').set('Sync', 'TRUE').text = '255'
##            root.append(child)
##                ET.Element('atprecis').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##                ET.Element('attscale').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##                ET.Element('attrdef').set('Sync', 'TRUE').text = 'Additional information about the feature that is not contained in other fields.'
##            root.append(child)
##                ET.Element('attrdefs').set('Sync', 'TRUE').text = 'National Marine Fisheries Service'
##            root.append(child)
##        root.append(child)
##            ET.Element('attr').text = ''
##                ET.Element('attrlabl').set('Sync', 'TRUE').text = 'INPORTURL'
##            root.append(child)
##                ET.Element('attalias').set('Sync', 'TRUE').text = 'InPort URL'
##            root.append(child)
##                ET.Element('attrtype').set('Sync', 'TRUE').text = 'String'
##            root.append(child)
##                ET.Element('attwidth').set('Sync', 'TRUE').text = '255'
##            root.append(child)
##                ET.Element('atprecis').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##                ET.Element('attscale').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##                ET.Element('attrdef').set('Sync', 'TRUE').text = 'Feature class metadata URL.
##
##InPort is the National Marine Fisheries Service's official metadata catalog found at:
##https://inport.nmfs.noaa.gov/inport/'
##            root.append(child)
##                ET.Element('attrdefs').set('Sync', 'TRUE').text = 'National Marine Fisheries Service'
##            root.append(child)
##        root.append(child)
##            ET.Element('attr').text = ''
##                ET.Element('attrlabl').set('Sync', 'TRUE').text = 'SHAPE_Length'
##            root.append(child)
##                ET.Element('attalias').set('Sync', 'TRUE').text = 'Shape_Length'
##            root.append(child)
##                ET.Element('attrtype').set('Sync', 'TRUE').text = 'Double'
##            root.append(child)
##                ET.Element('attwidth').set('Sync', 'TRUE').text = '8'
##            root.append(child)
##                ET.Element('atprecis').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##                ET.Element('attscale').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##                ET.Element('attrdef').set('Sync', 'TRUE').text = 'Length of feature in internal units.'
##            root.append(child)
##                ET.Element('attrdefs').set('Sync', 'TRUE').text = 'Esri'
##            root.append(child)
##                ET.Element('attrdomv').text = ''
##                    ET.Element('udom').set('Sync', 'TRUE').text = 'Positive real numbers that are automatically generated.'
##                root.append(child)
##            root.append(child)
##        root.append(child)
##            ET.Element('attr').text = ''
##                ET.Element('attrlabl').set('Sync', 'TRUE').text = 'SHAPE_Area'
##            root.append(child)
##                ET.Element('attalias').set('Sync', 'TRUE').text = 'Shape_Area'
##            root.append(child)
##                ET.Element('attrtype').set('Sync', 'TRUE').text = 'Double'
##            root.append(child)
##                ET.Element('attwidth').set('Sync', 'TRUE').text = '8'
##            root.append(child)
##                ET.Element('atprecis').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##                ET.Element('attscale').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##                ET.Element('attrdef').set('Sync', 'TRUE').text = 'Area of feature in internal units squared.'
##            root.append(child)
##                ET.Element('attrdefs').set('Sync', 'TRUE').text = 'Esri'
##            root.append(child)
##                ET.Element('attrdomv').text = ''
##                    ET.Element('udom').set('Sync', 'TRUE').text = 'Positive real numbers that are automatically generated.'
##                root.append(child)
##            root.append(child)
##        root.append(child)
##            ET.Element('attr').text = ''
##                ET.Element('attrlabl').set('Sync', 'TRUE').text = 'PUBLIC'
##            root.append(child)
##                ET.Element('attalias').set('Sync', 'TRUE').text = 'Public Mapper'
##            root.append(child)
##                ET.Element('attrtype').set('Sync', 'TRUE').text = 'String'
##            root.append(child)
##                ET.Element('attwidth').set('Sync', 'TRUE').text = '3'
##            root.append(child)
##                ET.Element('atprecis').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##                ET.Element('attscale').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##        root.append(child)
##            ET.Element('attr').text = ''
##                ET.Element('attrlabl').set('Sync', 'TRUE').text = 'REFERENCE'
##            root.append(child)
##                ET.Element('attalias').set('Sync', 'TRUE').text = 'Reference'
##            root.append(child)
##                ET.Element('attrtype').set('Sync', 'TRUE').text = 'String'
##            root.append(child)
##                ET.Element('attwidth').set('Sync', 'TRUE').text = '500'
##            root.append(child)
##                ET.Element('atprecis').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##                ET.Element('attscale').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##                ET.Element('attrdef').set('Sync', 'TRUE').text = 'In-text citations or full bibliographic citations of references used for feature.'
##            root.append(child)
##                ET.Element('attrdefs').set('Sync', 'TRUE').text = 'National Marine Fisheries Service'
##            root.append(child)
##        root.append(child)
##            ET.Element('attr').text = ''
##                ET.Element('attrlabl').set('Sync', 'TRUE').text = 'NMFSPAGE'
##            root.append(child)
##                ET.Element('attalias').set('Sync', 'TRUE').text = 'Species Webpage'
##            root.append(child)
##                ET.Element('attrtype').set('Sync', 'TRUE').text = 'String'
##            root.append(child)
##                ET.Element('attwidth').set('Sync', 'TRUE').text = '500'
##            root.append(child)
##                ET.Element('atprecis').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##                ET.Element('attscale').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##                ET.Element('attrdef').set('Sync', 'TRUE').text = 'NMFS Species Webpage found here: https://www.fisheries.noaa.gov/find-species'
##            root.append(child)
##                ET.Element('attrdefs').set('Sync', 'TRUE').text = 'National Marine Fisheries Service'
##            root.append(child)
##        root.append(child)
##            ET.Element('attr').text = ''
##                ET.Element('attrlabl').text = 'FEATNAME'
##            root.append(child)
##                ET.Element('attalias').text = 'Feature Name'
##            root.append(child)
##                ET.Element('attrdef').set('Sync', 'TRUE').text = 'Descriptive name for feature.'
##            root.append(child)
##                ET.Element('attrdefs').set('Sync', 'TRUE').text = 'National Marine Fisheries Service'
##            root.append(child)
##                ET.Element('attrtype').text = 'String'
##            root.append(child)
##                ET.Element('attwidth').text = '200'
##            root.append(child)
##                ET.Element('atprecis').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##                ET.Element('attscale').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##        root.append(child)
##            ET.Element('attr').text = ''
##                ET.Element('attrlabl').text = 'LIFESTAGE'
##            root.append(child)
##                ET.Element('attalias').text = 'Lifestage'
##            root.append(child)
##                ET.Element('attrdef').set('Sync', 'TRUE').text = 'Lifestage of ESA-listed entity depicted in feature. This is an optional attribute field.'
##            root.append(child)
##                ET.Element('attrdefs').set('Sync', 'TRUE').text = 'National Marine Fisheries Service'
##            root.append(child)
##                ET.Element('attrtype').text = 'String'
##            root.append(child)
##                ET.Element('attwidth').text = '500'
##            root.append(child)
##                ET.Element('atprecis').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##                ET.Element('attscale').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##        root.append(child)
##            ET.Element('attr').text = ''
##                ET.Element('attrlabl').text = 'BEHAVIOR'
##            root.append(child)
##                ET.Element('attalias').text = 'Behavior'
##            root.append(child)
##                ET.Element('attrdef').set('Sync', 'TRUE').text = 'Behavior (i.e., migrating, feeding, mating) of ESA-listed entity depicted in feature. This is an optional attribute field.'
##            root.append(child)
##                ET.Element('attrdefs').set('Sync', 'TRUE').text = 'National Marine Fisheries Service'
##            root.append(child)
##                ET.Element('attrtype').text = 'String'
##            root.append(child)
##                ET.Element('attwidth').text = '500'
##            root.append(child)
##                ET.Element('atprecis').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##                ET.Element('attscale').set('Sync', 'TRUE').text = '0'
##            root.append(child)
##        root.append(child)
##    root.append(child)
##root.append(child)
##    ET.Element('mdDateSt').set('Sync', 'TRUE').text = '20241124'
##root.append(child)
##    ET.Element('mdMaint').text = ''
##        ET.Element('maintFreq').text = ''
##            ET.Element('MaintFreqCd').set('value', '009')
##        root.append(child)
##    root.append(child)
##root.append(child)
##    ET.Element('dqInfo').text = ''
##        ET.Element('dqScope').text = ''
##            ET.Element('scpLvl').text = ''
##                ET.Element('ScopeCd').set('value', '005')
##            root.append(child)
##        root.append(child)
##    root.append(child)
##root.append(child)
##    ET.Element('mdContact').text = ''
##        ET.Element('rpIndName').text = 'Jonathan Molineaux'
##    root.append(child)
##        ET.Element('rpOrgName').text = 'NOAA Fisheries Office of Protected Resources'
##    root.append(child)
##        ET.Element('rpPosName').text = 'Fisheries Biologist'
##    root.append(child)
##        ET.Element('displayName').text = 'Jonathan Molineaux'
##    root.append(child)
##        ET.Element('role').text = ''
##            ET.Element('RoleCd').set('value', '001')
##        root.append(child)
##    root.append(child)
##        ET.Element('rpCntInfo').text = ''
##            ET.Element('cntAddress').set('addressType', '').text = ''
##                ET.Element('eMailAdd').text = 'jonathan.molineaux@noaa.gov'
##            root.append(child)
##        root.append(child)
##    root.append(child)
##root.append(child)
##    ET.Element('mdContact').text = ''
##        ET.Element('rpIndName').text = 'Jennifer Schultz'
##    root.append(child)
##        ET.Element('rpOrgName').text = 'NOAA Fisheries Office of Protected Resources'
##    root.append(child)
##        ET.Element('rpPosName').text = 'Fisheries Biologist'
##    root.append(child)
##        ET.Element('displayName').text = 'Jennifer Schultz'
##    root.append(child)
##        ET.Element('role').text = ''
##            ET.Element('RoleCd').set('value', '001')
##        root.append(child)
##    root.append(child)
##        ET.Element('rpCntInfo').text = ''
##            ET.Element('cntAddress').set('addressType', '').text = ''
##                ET.Element('eMailAdd').text = 'jennifer.schultz@noaa.gov'
##            root.append(child)
##        root.append(child)
##    root.append(child)
##root.append(child)

tree = ET.ElementTree(root)
tree.write("filename.xml")