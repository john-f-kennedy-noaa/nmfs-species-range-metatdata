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
    html = '''
    <parent>
      <child-a/>
      <container><child-b/><child-c/></container>
      <child-d/>
      <container><child-e/><child-f/></container>
      <child-g/>
    </parent>
    '''

    import lxml.html

    tree = lxml.html.fromstring(html)

    for container in tree.findall('container'):
        parent = container.getparent()
        #for child in reversed(container.getchildren()):  # getchildren() - deprecated
        #for child in reversed(container):
        for child in container.iterchildren(reversed=True):
            #child.tail = None   # clean indentations  # elements in one line
            #child.tail = "\n"   # clean indentations  # next tag starts in first column
            #child.tail = container.tail   # clean indentations
            container.addnext(child)
        parent.remove(container)

    # https://lxml.de/apidoc/lxml.etree.html#lxml.etree.indent
    import lxml.etree as ET
    #ET.indent(tree, space='    ')  # clean all indentations - use 4 spaces
    #ET.indent(tree, space='....')  # clean all indentations - use 4 dots - looks like TOC (Table Of Contents) in book :)
    ET.indent(tree)   # clean all indentations - use (default) 2 spaces

    html = lxml.html.tostring(tree, pretty_print=True).decode()
    #html = lxml.html.tostring(tree).decode()
    #html = lxml.html.tostring(tree, encoding='unicode')  # not `utf-8` but `unicode` ???

    print(html)

if __name__ == '__main__':
    main()
