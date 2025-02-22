from lxml import etree


parser = etree.XMLParser(remove_blank_text=True)
# Parse the XML
tree = etree.parse("species_range_boilerplate.xml", parser=parser)

# Pretty print
xml_string = etree.tostring(tree, encoding="utf-8", pretty_print=True).decode()


print(xml_string)

# Reverse the lines
#reversed_xml = "\n".join(reversed(xml_string.splitlines()))
#print(reversed_xml)