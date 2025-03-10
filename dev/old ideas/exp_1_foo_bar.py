from lxml import etree
xml = '''<root>
<foo id="0">
    <foo id="1">
        <bar attr="xxx" />
    </foo>
    <foo id="2">
        <bar attr="val" />
    </foo>
    <foo id="3">
        <tar>
            <bar attr="val" />
        </tar>
    </foo>
</foo>
</root>'''

tree = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))

print("Not Descendant foo")
foos = tree.xpath('//foo[descendant::bar[@attr="val"] and not(descendant::foo)]')
for foo in foos:
    print(foo.attrib)

print("position 1 foo")
foos = tree.xpath('.//ancestor::foo[bar[@attr="val"] and position() = 1]')
for foo in foos:
    print(foo.attrib)

print("position 1 foo alternative")
foos = tree.xpath('.//ancestor::foo[bar[@attr="val"]][1]')
for foo in foos:
    print(foo.attrib)

etree.indent(tree, space="    ")

print(etree.tostring(tree, pretty_print=True, method='html', encoding='UTF-8').decode())

#for elem in tree.xpath('//foo[descendant::bar[@attr="val"] and not(descendant::foo)]'):
#    print(f"Name: {elem.attrib}")
