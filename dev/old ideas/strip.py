from lxml import etree


parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)
# Parse the XML
tree = etree.parse("species_range_boilerplate.xml", parser=parser)

# Pretty print
xml_string = etree.tostring(tree, encoding='UTF-8',  method='xml', pretty_print=True).decode()


print(xml_string)

# Reverse the lines
#reversed_xml = "\n".join(reversed(xml_string.splitlines()))
#print(reversed_xml)