from lxml import etree

xml = '''<?xml version="1.0" standalone="yes"?>
<prodinfo>
<prod id="1">
<name>MAC VINEY</name>
<Origin State="USA" Year="4 year">Face products</Origin>
<email>mac123@myemail.com</email>
</prod>
<prod id="2">
<name>Olay Primee</name>
<Origin State="Canada" Year="10 year">Cosmetics</Origin>
<email>ckhj@gmail.com</email>
</prod>
<prod id="3">
<name>Maybelline</name>
<Origin State="Thailand" Year="15 year">Skinny</Origin>
<email>may34@myemail.com</email>
</prod>
</prodinfo>'''

tree = etree.XML(_xml, etree.XMLParser(encoding='UTF-8', remove_blank_text=True))

etree.indent(tree, space="    ")

print(etree.tostring(tree, pretty_print=True, method='html', encoding='UTF-8').decode())

##for elem in tree.xpath('//name/self::*'):
##    print(f"Name: {elem.text}")
##
##for elem in tree.xpath('//name//ancestor-or-self::*'):
##    if elem.tag == "name":
##        print(f"Self: {elem.tag}")
##    else:
##        print(f"Ancestor: {elem.tag}")

for elem in tree.xpath('//prod/ancestor::*'):
    print(f"Common ancestor: {elem.tag}")

##for elem in tree.xpath('//name[text()="Olay Primee"]/../preceding-sibling::*'): # Find the selected element ('group') and then the siblings of the proceeding element ('chart')
##    if elem.tag == "name":
##        print(f"Tag: '{elem.tag}' Text: '{elem.text}'")
##    else:
##        print(f"Ancestor: '{elem.tag}'")

#for elem in tree.xpath('//prod/ancestor::*'):
#    print(f"Tag: {elem.tag}")


for elem in tree.xpath('//ancestor::name'):
    print(f"Name: {elem.text}")