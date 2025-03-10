from lxml import etree
data = r'''<clade>
<name>MnPV1</name>
<annotation>
<desc>Iotapapillomavirus 1</desc>
</annotation>
<chart>
<group>Iota</group>
</chart>
<branch_length>1.0</branch_length>
<name>MnPV2</name>
<annotation>
<desc>Iotapapillomavirus 1</desc>
</annotation>
<chart>
<group>Iota</group>
</chart>
<branch_length>1.0</branch_length>
</clade>'''

tree = etree.XML(data)

etree.indent(tree, space="    ")

print(etree.tostring(tree, pretty_print=True, method='html', encoding='UTF-8').decode())

#for elem in tree.xpath('//group[text()="Iota"]/../preceding-sibling::*'):
#    elem.attrib['bgstyle'] = 'green'

#for elem in tree.xpath('//group[text()="Iota"]/../preceding-sibling::*'): # Find the selected element ('group') and then the siblings of the proceeding element ('chart')
#    if elem.tag == "group":
#        print(f"Tag: '{elem.tag}' Text: '{elem.text}'")
#    else:
#        print(f"Ancestor: '{elem.tag}'")

#for elem in tree.xpath('//group//ancestor-or-self::*'): # Find the selected element ('group') and then each ancestor
#    if elem.tag == "group":
#        print(f"Tag: '{elem.tag}' Text: '{elem.text}'")
#    else:
#        print(f"Ancestor: '{elem.tag}'")

#print(etree.tostring(tree, pretty_print=True, method='html', encoding='UTF-8').decode())

#for elem in tree.xpath('//group/ancestor::*'):
#    print(f"Common ancestor: {elem.tag}")

#for elem in tree.xpath('//group/self::*'):
#    print(f"Name: {elem.text}")

for elem in tree.xpath('//group/../preceding-sibling::name'):
    print(f"Tag: {elem.tag} Text: {elem.text}")

