#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john.f.kennedy
#
# Created:     19/03/2025
# Copyright:   (c) john.f.kennedy 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os, sys  # built-ins first
import traceback
import importlib
import inspect

def main(xml_file):
    from lxml import etree
    from io import BytesIO

    parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
    target_tree = etree.parse(xml_file, parser=parser)
    target_root = target_tree.getroot()
    del parser

    #print(etree.tostring(target_root, encoding='UTF-8', method='xml', pretty_print=True).decode())

    #for stepProc in target_root.xpath(f"/metadata/dqInfo/dataLineage/prcStep[./stepProc/rpIndName/text()='John F Kennedy']"):
    for stepProc in target_root.xpath(f"/metadata/dqInfo/dataLineage/prcStep[./stepProc/rpIndName/text() and ./stepProc/rpCntInfo/cntAddress/eMailAdd/text()]"):
        #print(etree.tostring(stepProc, encoding='UTF-8', method='xml', pretty_print=True).decode())
        del stepProc


    for stepProc in target_root.xpath(f"/metadata/dqInfo/dataLineage/prcStep/stepProc/stepProc"):
        target_root.xpath(f"/metadata/dqInfo/dataLineage/prcStep")[-1].insert(0, stepProc)
        del stepProc

    for prcStep in target_root.xpath(f"/metadata/dqInfo/dataLineage/prcStep"):
        #print(etree.tostring(prcStep, encoding='UTF-8', method='xml', pretty_print=True).decode())
        del prcStep

    for stepProc in target_root.xpath(f"/metadata/dqInfo/dataLineage/prcStep[./stepProc/rpIndName/text() and ./stepProc/rpCntInfo/cntAddress/eMailAdd/text()]"):
        print(etree.tostring(stepProc, encoding='UTF-8', method='xml', pretty_print=True).decode())
        del stepProc

    del xml_file

if __name__ == '__main__':
    #xml_file = r"C:\Users\john.f.kennedy\Documents\ArcGIS\Projects\DisMap\ArcGIS-Analysis-Python\July 1 2024\ArcGIS Metadata\DisMAP_Regions.xml"
    xml_file = r"C:\Users\john.f.kennedy\Documents\ArcGIS\Projects\ArcPy Studies\XML\nmfs-species-range-metatdata\Export\AbaloneWhite_20210728.xml"
    main(xml_file)
