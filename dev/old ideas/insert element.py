#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john.f.kennedy
#
# Created:     13/12/2024
# Copyright:   (c) john.f.kennedy 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import xml.etree.ElementTree as ET
import os

def main():
    doc = ET.parse('00390.xml')
    root = doc.getroot()
    s = '/image/00390.jpg'
    filename = (os.path.basename(s))
    userElement = ET.Element("annotation")
    newSub = ET.SubElement(userElement, "filename")
    #newSub.set(filename, '')#<----- *****
    newSub.text = filename#Assigns text
    root.insert(0,newSub)
    tree = ET.ElementTree(root)
    tree.write(open('3.xml', 'w'), encoding='unicode')

if __name__ == '__main__':
    main()

