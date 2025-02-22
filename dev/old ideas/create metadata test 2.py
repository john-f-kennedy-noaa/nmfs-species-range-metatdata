import xml.etree.ElementTree as ET

def recreate_xml(xml_file):
    """Reads an XML file and generates Python code to recreate it."""

    tree = ET.parse(xml_file)
    root = tree.getroot()

    def generate_code(element, indent=0):
        """Recursively generates code for an element and its children."""
        code = " " * indent + f"ET.Element('{element.tag}')"

        # Add attributes
        if element.attrib:
            code += ".set(" + ", ".join([f"'{k}', '{v}'" for k, v in element.attrib.items()]) + ")"

        # Add text
        if element.text:
            code += f".text = '{element.text.strip()}'"

        # Add children
        for child in element:
            code += "\n" + generate_code(child, indent + 4)
            code += "\n" + " " * indent + f"root.append(child)"

        return code

    code = generate_code(root)
    return code

if __name__ == "__main__":
    #xml_file = "example.xml"  # Replace with your XML file path
    xml_file = r"{os.environ['USERPROFILE']}\Documents\ArcGIS\Projects\National Mapper\Export\AbaloneBlack_20210712.xml"
    code = recreate_xml(xml_file)
    print(code)