import xml.etree.ElementTree as ET

# Create the root element
root = ET.Element("data")

# Create child elements and add them to the root
country1 = ET.SubElement(root, "country", name="Liechtenstein")
rank1 = ET.SubElement(country1, "rank", updated="yes")
rank1.text = "2"
year1 = ET.SubElement(country1, "year")
year1.text = "2008"
gdppc1 = ET.SubElement(country1, "gdppc")
gdppc1.text = "141100"
neighbor1 = ET.SubElement(country1, "neighbor", name="Austria", direction="E")
neighbor2 = ET.SubElement(country1, "neighbor", name="Switzerland", direction="W")

country2 = ET.SubElement(root, "country", name="Singapore")
rank2 = ET.SubElement(country2, "rank", updated="yes")
rank2.text = "5"
year2 = ET.SubElement(country2, "year")
year2.text = "2011"
gdppc2 = ET.SubElement(country2, "gdppc")
gdppc2.text = "59900"
neighbor3 = ET.SubElement(country2, "neighbor", name="Malaysia", direction="N")

# Create the tree and write to file
tree = ET.TreeBuilder()
tree.start("data", {})  # Start the root element
tree.end("data")  # End the root element
tree = ET.ElementTree(root)
tree.write("output.xml")