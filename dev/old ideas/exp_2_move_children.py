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

    # collect elements in container
    container = root.findall(".//container/*")
    # print([x.tag for x in container])

    # position of container tag to insert
    le = root.findall("./")
    i = [le.index(i) for i in le if i.tag == "container"]
    # print(i)

    # Remove child from parent if the position is unknown
    # root.find('.//container/..').remove(root.find('.//container'))
    root.remove(root.find('.//container'))

    # insert elements from container
    for n in range(len(container)):
        root.insert(int(*i)+n, container[n])

    etree.indent(root, space = '  ')
    etree.dump(root)

if __name__ == '__main__':
    main()
