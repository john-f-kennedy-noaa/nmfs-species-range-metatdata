#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john.f.kennedy
#
# Created:     07/01/2025
# Copyright:   (c) john.f.kennedy 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    try:
        # Imports
        import traceback
        from lxml import etree
        from io import StringIO
        from src.project_tools import pretty_format_xml_file

        target_xml = r"{os.environ['USERPROFILE']}\Documents\ArcGIS\Projects\ArcPy Studies\XML\nmfs-species-range-metatdata\Export\AbaloneBlack_20210712.xml"
        target_tree = etree.parse(target_xml)
        # print(etree.tostring(tree.getroot(), pretty_print=True).decode(), end='')
        target_root = target_tree.getroot()
        new_item_name = target_root.find("./Esri/DataProperties/itemProps/itemName").text
        # linkage[linkage.find("/services/")+len("/services/"):linkage.find("/FeatureServer")]
        #linkages = target_root.findall("./distInfo/distributor/distorTran/onLineSrc/linkage")

        UpdateOnLineSrcs = True
        if UpdateOnLineSrcs:
            onLineSrcs = target_root.findall("./distInfo/distributor/distorTran/onLineSrc")
            new_item_name = target_root.find("./Esri/DataProperties/itemProps/itemName").text
            for onLineSrc in onLineSrcs:
                if onLineSrc.find('./protocol').text == "ESRI REST Service":
                    old_linkage_element = onLineSrc.find('./linkage')
                    old_linkage = old_linkage_element.text
                    print(old_linkage)
                    old_item_name = old_linkage[old_linkage.find("/services/")+len("/services/"):old_linkage.find("/FeatureServer")]
                    new_linkage = old_linkage.replace(old_item_name, new_item_name)
                    print(new_linkage)
                    old_linkage_element.text = new_linkage
                    print(old_linkage_element.text)
                    new_item_name

                    del old_linkage_element
                    del old_item_name, old_linkage, new_linkage
                del onLineSrc
            del onLineSrcs
        del UpdateOnLineSrcs
        #protocol = target_root.xpath('.//protocol[text()="ESRI REST Service"]')
        #print(protocol[0].text)

        #print(target_tree.find('.//protocol[text()="ESRI REST Service"]').tag)

        # Exact text match
        #e = root.xpath('.//a[text()="TEXT A"]')
        # Text contain a match
        #e = root.xpath('.//a[contains(text(),"TEXT A")]')
        # Text starts with a match
        #e = root.xpath('.//a[starts-with(text(),"TEXT A")]')

        #pretty_format_xml_file(target_xml)

        # Write the XML to the file
        #target_tree.write(target_xml, pretty_print=True)  # Use 'pretty_print=True' for formatted output


        del target_xml, target_tree, target_root, new_item_name
        # Import
        del traceback, etree, StringIO, pretty_format_xml_file

    ##    for _, element in etree.iterparse(target_xml, tag='onLineSrc'):
    ##        print(f"{element.findtext('ESRI REST Service')}") #, element[1].text))
    ##        element.clear(keep_tail=True)
    except:
        traceback.print_exc()

if __name__ == '__main__':
    main()
