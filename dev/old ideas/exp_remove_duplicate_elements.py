from lxml import etree

def remove_duplicate_elements(root):
    seen = {}
    for element in root.iter():
        key = (element.tag, element.text, tuple(element.attrib.items()))
        if key in seen:
            element.getparent().remove(element)
        else:
            seen[key] = True

# Example usage
xml_string = """
<root>
    <item>
        <name>Apple</name>
        <price>1.00</price>
    </item>
    <item>
        <name>Banana</name>
        <price>0.50</price>
    </item>
    <item>
        <name>Apple</name>
        <price>1.00</price>
    </item>
</root>
"""

root = etree.fromstring(xml_string)
remove_duplicate_elements(root)

print(etree.tostring(root, pretty_print=True).decode())