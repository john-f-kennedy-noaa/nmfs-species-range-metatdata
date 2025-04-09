#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john.f.kennedy
#
# Created:     29/03/2025
# Copyright:   (c) john.f.kennedy 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os, sys  # built-ins first
import traceback
import importlib
import inspect

def main(contact_name, contact_org_name, contact_email):
    try:
        from lxml import etree
        import copy

        contacts_xml = rf"{os.environ['USERPROFILE']}\Documents\ArcGIS\Descriptions\contacts.xml"
        contacts_xml_tree = etree.parse(contacts_xml, parser=etree.XMLParser(encoding='UTF-8', remove_blank_text=True)) # To parse from a string, use the fromstring() function instead.
        del contacts_xml
        contacts_xml_root = contacts_xml_tree.getroot()
        etree.indent(contacts_xml_root, space="  ")
        #print(etree.tostring(contacts_xml_root, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())

        # Example #1
##        output = [(elem.text,elem.xpath('following-sibling::values/value/text()')) for elem in tree.getiterator(tag='name')  if elem.text.startswith('v_')]
##        print(output)
##        output = [(elem.xpath(f'//contact[./rpIndName="{contact_name}" and ./rpOrgName="{contact_org_name}" and ./rpCntInfo/cntAddress/eMailAdd="{contact_email}" and editorSave="True"]')) for elem in contacts_xml_tree.getiterator(tag='contact')]
##        for i in range(0, len(output)):
##            #print(etree.tostring(output[i][0], encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
##            del i
##        print(etree.tostring(output[0][0], encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())

        # Example #2

        new_contact_tree = contacts_xml_tree.xpath(f'//contact[./rpIndName="{contact_name}" and ./rpOrgName="{contact_org_name}" and ./rpCntInfo/cntAddress/eMailAdd="{contact_email}" and editorSave="True"]')

        if isinstance(new_contact_tree, type(list())):
            print(len(new_contact_tree))
            if len(new_contact_tree) == 0:
                print("Nothing Found!!")
                return False
            elif len(new_contact_tree) == 1:
                print("Found it!!")
                return new_contact_tree[0]
                ##print(etree.tostring(new_contact_tree[0], encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
            elif len(new_contact_tree) > 1:
                print("Too Many Man!!")
                return new_contact_tree[0]
                for new_contact in new_contact_tree:
                    #print(etree.tostring(new_contact, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
                    del new_contact
            else:
                pass
        elif isinstance(new_contact_tree, type(bool())):
            print(new_contact_tree)
        del new_contact_tree
    except:
        traceback.print_exc()

if __name__ == '__main__':
    contact_name     = "NMFS Office of Protected Resources"
    contact_org_name = "NMFS Office of Protected Resources"
    contact_email    = "jonathan.molineaux@noaa.gov"

    print(main(contact_name, contact_org_name, contact_email))
