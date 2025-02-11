#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john.f.kennedy
#
# Created:     22/01/2025
# Copyright:   (c) john.f.kennedy 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    from lxml import etree

    xml_ = """\
    <parent>
      <child-a/>
      <container>
         <child-b/>
         <child-c/>
      </container>
      <child-d/>
      <child-e/>
    </parent>"""

    root = etree.fromstring(xml_)

    childs = root.findall(".//*")
    [childs.pop(childs.index(x)) for x in childs if x.tag == "container"]

    parent = etree.Element("parent")
    parent.extend(childs)

    etree.indent(parent, space='  ')
    etree.dump(parent)

if __name__ == '__main__':
    main()
