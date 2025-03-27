#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john.f.kennedy
#
# Created:     24/02/2025
# Copyright:   (c) john.f.kennedy 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os, sys  # built-ins first
import traceback
import inspect

#import arcpy  # third-parties second

def get_new_contact(contact="", contact_type=""):
    try:
        #print(contact, contact_type)
        from lxml import etree
        import copy

        RoleCd_dict = {"001" : "Resource Provider", "002" : "Custodian",
                       "003" : "Owner",             "004" : "User",
                       "005" : "Distributor",       "006" : "Originator",
                       "007" : "Point of Contact",  "008" : "Principal Investigator",
                       "009" : "Processor",         "010" : "Publisher",
                       "011" : "Author",            "012" : "Collaborator",
                       "013" : "Editor",            "014" : "Mediator",
                       "015" : "Rights Holder",}

        RoleCd_dict = {v:k for k,v in RoleCd_dict.items()}

        role_code     = RoleCd_dict[contact["role"]]
        email_address = contact["eMailAdd"]
        user_name     = contact["rpIndName"]

        #print(user_name, email_address)
        del RoleCd_dict

        contacts_xml = rf"{os.environ['USERPROFILE']}\Documents\ArcGIS\Descriptions\contacts.xml"
        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
        contacts_xml_tree = etree.parse(contacts_xml, parser=parser) # To parse from a string, use the fromstring() function instead.
        del parser
        del contacts_xml
        contacts_xml_root = contacts_xml_tree.getroot()
        #etree.indent(contacts_xml_root, space="  ")
        #print(etree.tostring(contacts_xml_root, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())

        new_contact              = None
        __new_contact_xml_string = None

        new_contact_root = contacts_xml_root.xpath(f".//eMailAdd[text()='{email_address}']/ancestor::contact/rpIndName[text()='{user_name}']/ancestor::contact/editorSave[text()='True']/..")
        if not isinstance(new_contact_root, type(None)) and len(new_contact_root) == 0:
            print("There has been a mistake. No contact found")
            raise Exception
        elif not isinstance(new_contact_root, type(None)) and len(new_contact_root) == 1:
            #print(etree.tostring(new_contact_root[0], encoding='UTF-8',  method='xml', pretty_print=True).decode())
            #print(f"\tInserting Role into new contact")
            new_contact = copy.deepcopy(new_contact_root[0])
            new_contact.tag = f"{contact_type}"
            _xml = etree.XML(f'<role><RoleCd value="{role_code}"/></role>')
            # Append element
            new_contact.append(_xml)
            __new_contact_xml_string = etree.tostring(new_contact, encoding='UTF-8',  method='xml', pretty_print=True).decode()
            #print(etree.tostring(new_contact, encoding='UTF-8',  method='xml', pretty_print=True).decode())
            del _xml
        elif not isinstance(new_contact_root, type(None)) and len(new_contact_root) > 1:
            print(f"\tFound too many contacts")
            raise Exception
        else:
            pass

        # Declared Variables
        del email_address, user_name, role_code
        del new_contact, new_contact_root
        del contacts_xml_tree, contacts_xml_root
        # Imports
        del etree, copy
        # Function Parameters
        del contact, contact_type

    except Exception:
        traceback.print_exc()
    except:
        traceback.print_exc()
    else:
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return __new_contact_xml_string
    finally:
        if "__new_contact_xml_string" in locals().keys(): del __new_contact_xml_string

def main():
    try:
        from lxml import etree

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

        contact_type = "mdContact"
        _contacts = contacts[contact_type]

        if isinstance(_contacts, type(dict())):
            pass

##            new_contact_xml_string = get_new_contact(contact=_contacts, contact_type=contact_type)
##            parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
##            new_contact_xml_root = etree.fromstring(new_contact_xml_string, parser=parser) # To parse from a string, use the fromstring() function instead.
##            del parser
##            etree.indent(new_contact_xml_root, space="  ")
##            print(etree.tostring(new_contact_xml_root, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
##
##            del new_contact_xml_root, new_contact_xml_string

        elif isinstance(_contacts, type(list())):
            contact_type = "mdContact"
            _contacts = contacts[contact_type]
            for _contact in _contacts:
                new_contact_xml_string = get_new_contact(contact=_contact, contact_type=contact_type)
                parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
                new_contact_xml_root = etree.fromstring(new_contact_xml_string, parser=parser) # To parse from a string, use the fromstring() function instead.
                del parser
                etree.indent(new_contact_xml_root, space="  ")
                print(etree.tostring(new_contact_xml_root, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
                del new_contact_xml_root, new_contact_xml_string
                del _contact
        else:
            print(type(_contacts))

        del _contacts, contact_type

##        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
##        new_contact_xml_root = etree.fromstring(new_contact_xml_string, parser=parser) # To parse from a string, use the fromstring() function instead.
##        del parser
##        etree.indent(new_contact_xml_root, space="  ")
##        print(etree.tostring(new_contact_xml_root, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
##
##        del new_contact_xml_root
##        del new_contact_xml_string
##        del contact_type
        #
        #print(etree.tostring(contacts_xml_root, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())

##        from lxml import etree
##        import copy
##
##        email_address = contacts[f"{contact_type}"]["eMailAdd"]
##        user_name = contacts[f"{contact_type}"]["rpIndName"]
##        print(user_name, email_address)
##
##        contacts_xml = rf"{os.environ['USERPROFILE']}\Documents\ArcGIS\Descriptions\contacts.xml"
##        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
##        contacts_xml_tree = etree.parse(contacts_xml, parser=parser) # To parse from a string, use the fromstring() function instead.
##        del parser
##        del contacts_xml
##        contacts_xml_root = contacts_xml_tree.getroot()
##        #etree.indent(contacts_xml_root, space="  ")
##        #print(etree.tostring(contacts_xml_root, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
##
##        new_contact = None
##
##        new_contact_root = contacts_xml_root.xpath(f".//eMailAdd[text()='{email_address}']/ancestor::contact/rpIndName[text()='{user_name}']/ancestor::contact/editorSave[text()='True']/..")
##        if not isinstance(new_contact_root, type(None)) and len(new_contact_root) == 0:
##            print("There has been a mistake. No contact found")
##        elif not isinstance(new_contact_root, type(None)) and len(new_contact_root) == 1:
##            print(etree.tostring(new_contact_root[0], encoding='UTF-8',  method='xml', pretty_print=True).decode())
##            #print(f"\tInserting Role into new contact")
##            new_contact = copy.deepcopy(new_contact_root[0])
##            new_contact.tag = f"{contact_type}"
##            _xml = etree.XML('<role><RoleCd value="011"/></role>')
##            # Append element
##            new_contact.append(_xml)
##            print(etree.tostring(new_contact, encoding='UTF-8',  method='xml', pretty_print=True).decode())
##            del _xml
##        elif not isinstance(new_contact_root, type(None)) and len(new_contact_root) > 1:
##            print(f"\tFound too many contacts found")
##        else:
##            pass
##
##        # Declared Variables
##        del email_address, user_name
##        del new_contact, new_contact_root
##        del contacts_xml_tree, contacts_xml_root

        # Imports
        del etree
        # Function Parameters
        del contacts

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

if __name__ == '__main__':
    try:
        main()
    except:
        traceback.print_exc()
    else:
        pass
    finally:
        pass