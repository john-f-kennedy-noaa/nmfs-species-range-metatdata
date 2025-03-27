#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john.f.kennedy
#
# Created:     03/03/2025
# Copyright:   (c) john.f.kennedy 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os, sys  # built-ins first
import traceback
import importlib
import inspect

def main():
    try:
        from lxml import etree
        from copy import deepcopy
        from io import BytesIO, StringIO

        xml_file = b'''<?xml version='1.0' encoding='UTF-8'?>
                       <metadata xml:lang="en">
                        <dqInfo>
                            <dataLineage>
                                <statement></statement>
                                <dataSource type="">
                                    <srcDesc></srcDesc>
                                    <srcCitatn>
                                        <resTitle></resTitle>
                                        <resAltTitle></resAltTitle>
                                        <collTitle></collTitle>
                                        <citOnlineRes>
                                            <linkage></linkage>
                                            <protocol></protocol>
                                            <orName></orName>
                                            <orDesc></orDesc>
                                            <orFunct>
                                                <OnFunctCd></OnFunctCd>
                                            </orFunct>
                                        </citOnlineRes>
                                        <date>
                                            <createDate></createDate>
                                            <pubDate></pubDate>
                                            <reviseDate></reviseDate>
                                        </date>
                                        <otherCitDet></otherCitDet>
                                        <presForm>
                                            <fgdcGeoform></fgdcGeoform>
                                            <PresFormCd value="001"></PresFormCd>
                                        </presForm>
                                        <citRespParty></citRespParty>
                                    </srcCitatn>
                                    <srcMedName>
                                        <MedNameCd value="015"/>
                                    </srcMedName>
                                </dataSource>
                                <prcStep>
                                    <stepDesc>Metadata Update</stepDesc>
                                    <stepDateTm></stepDateTm>
                                    <stepProc></stepProc>
                                </prcStep>
                            </dataLineage>
                        </dqInfo>
                    </metadata>
                     '''

        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
        source_tree = etree.parse(BytesIO(xml_file), parser=parser)
        source_root = source_tree.getroot()
        del parser
        del xml_file

        xml_file = b'''<?xml version='1.0' encoding='UTF-8'?>
                       <metadata xml:lang="en">
                         <dqInfo>
                            <dataLineage>
                                <statement>statement</statement>
                            </dataLineage>
                        </dqInfo>
                    </metadata>
                     '''

        # Parse the XML
        parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
        target_tree = etree.parse(BytesIO(xml_file), parser=parser)
        target_root = target_tree.getroot()
        del parser
        del xml_file

        #print(etree.tostring(source_tree.xpath(".")[0], encoding='UTF-8', method='xml', pretty_print=True).decode())

        for element in source_root.iter():
            if isinstance(element.getparent(), type(None)):
                pass # Nothing to do, at the root of the tree
            elif not isinstance(element.getparent(), type(None)):
                pass
                # Get the parent of the source element, this should be in target
                #parent = element.getparent()
                #print(element.getparent())
                element_path = element.getroottree().getpath(element)
                parent_path  = element.getroottree().getpath(element.getparent())
                #print(element_path)

                # Get the elements from the target using the source path
                target_element = target_tree.xpath(f"{element_path}")

                if isinstance(target_element, type(None)):
                    pass # Nothing to do, at the root of the tree
                elif not isinstance(target_element, type(None)):
                    if len(target_element) == 0:
                        print(f"target_element is missing")
                        print(f"\t{element_path}")
                        print(f"\t{parent_path}")
                        source_element = source_root.xpath(f"{element_path}")
                        target_parent  = target_root.xpath(f"{parent_path}")
                        if len(target_parent) == 0:
                            pass
                        elif len(target_parent) == 1:
                            pass
                            target_parent[0].append(source_element[0])
                            #print(target_parent[0])
                            #print(etree.tostring(target_parent[0], encoding='UTF-8', method='xml', pretty_print=True).decode())
                        elif len(target_parent) > 0:
                            raise Exception
                        else:
                            pass
                        del target_parent

                        #print(etree.tostring(source_element[0], encoding='UTF-8', method='xml', pretty_print=True).decode())
                        #print(etree.tostring(source_root.xpath(f"{parent_path}")[0], encoding='UTF-8', method='xml', pretty_print=True).decode())
                        #print(etree.tostring(source_element[0], encoding='UTF-8', method='xml', pretty_print=True).decode())
                        #print(etree.tostring(_target_element[0], encoding='UTF-8', method='xml', pretty_print=True).decode())
                        del source_element
                    elif len(target_element) == 1:
                        pass
                        #print(f"found one target_element {element_path}")
                        # Get the parent of the source element, this should be in ta
                        #print(etree.tostring(target_element[0], encoding='UTF-8', method='xml', pretty_print=True).decode())
                    elif len(target_element) > 1:
                        print(f"found too many target_elements {element_path}")
                        raise Exception
                    else:
                        pass
                del target_element
                del parent_path
                del element_path

##            element_path = source_tree.getpath(element)
##            if element_path not in element_paths:
##                element_paths.append(element_path)
            else:
                pass

            del element

##        for element_path in element_paths:
##            pass
##            #print(element_path)
##            if len(source_tree.xpath(f"/{element_path}")) > 0:
##                _element = source_tree.xpath(f"/{element_path}")[0]
##                _element_path = source_tree.getpath(_element)
##                #print(_element.xpath(_element_path)[0])
##                #print(_element_path)
##
##                if isinstance(_element.getparent(), type(None)):
##                    pass # Nothing to do, at the root of the tree
##                elif not isinstance(_element.getparent(), type(None)):
##                    # Get the parent of the source element, this should be in target
##                    parent = _element.getparent()
##                    # Get the ancestors of the current element
##                    ancestors = source_tree.getpath(parent)
##                    #print()
##                    #print("Element Path")
##                    #print(_element_path)
##                    #print(ancestors)
##
##                    # Get the elements from the target using the source path
##                    target_elements = target_tree.xpath(f"/{source_tree.getpath(_element)}")
##                    #print(len(target_elements))
##                    if len(target_elements) == 0:
##                        #print(_element.getroottree().getpath(_element))
##                        #print(target_tree.xpath(_element.getroottree().getpath(_element.getparent())))
##                        target_parent_elements = target_tree.xpath(_element.getroottree().getpath(_element.getparent()))
##                        for target_parent_element in target_parent_elements:
##                            #print(target_tree.getpath(target_parent_element))
##                            target_parent_element.insert(-1, _element)
##                            #print(etree.tostring(target_parent_element, encoding='UTF-8', method='xml', pretty_print=True).decode())
##                            del target_parent_element
##                        del target_parent_elements
##
##                    elif len(target_elements) == 1:
##                        for target_element in target_elements:
##                            pass
##                            #print(target_tree.getpath(target_element))
##                            del target_element
##
##                    elif len(target_elements) > 1:
##                        for target_element in target_elements:
##                            #print(target_tree.getpath(target_element))
##                            for i in range(1, len(target_elements)):
##                                try:
##                                    target_elements[i].getparent().remove(target_elements[i])
##                                except:
##                                    pass
##                                i+=1
##                                del i
##
##                            del target_element
##                    else:
##                        pass
##
##                    del target_elements
##                    del ancestors, parent
##                del _element_path, _element
##            del element_path
##        del element_paths


        print("\nTarget Tree\n")
        #print(etree.tostring(source_tree, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())
        print(etree.tostring(target_tree, encoding='UTF-8', method='xml', xml_declaration=True, pretty_print=True).decode())

        # Declared variables
        del source_tree, source_root, target_tree, target_root
        # Imports
        del etree, deepcopy, BytesIO, StringIO

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
    main()

