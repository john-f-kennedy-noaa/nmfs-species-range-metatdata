import arcpy
from arcpy import metadata as md

arcpy.env.overwriteOutput = True
arcpy.env.workspace = "C:/Projects/BeckerEtAl2020b_CCE/swfsc_cce_becker_et_al_2020b_2021022302.gdb"

fcs = arcpy.ListFeatureClasses("*")

template_path = r'C:\Projects\BeckerEtAl2020b_CCE\swfsc_cce_becker_et_al_2020b_metadata_template_02.xml'
src_item_md = md.Metadata(template_path)

for fc in fcs:
    cursor = arcpy.da.SearchCursor(fc,['SPECIES','Season'])
    row = cursor.next()
    species = row[0]
    season = row[1]
    layer_metadata = md.Metadata(fc)
    layer_metadata.importMetadata(template_path,'ARCGIS_METADATA')
    layer_metadata.save()
    layer_metadata.synchronize('SELECTIVE')
    layer_metadata.save()
    tempTitle = '<Species> Density - <Season> - CCE 2020b'
    tempTitle = tempTitle.replace("<Species>",species)
    tempTitle = tempTitle.replace("<Season>",season)
    layer_metadata.title = tempTitle
    layer_metadata.save()

    print(fc, layer_metadata.title)

    del cursor