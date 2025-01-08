import xml.etree.ElementTree as ET

# Create the root element
root = ET.Element("root")

# Create multiple subelements
child1 = ET.Element("child1")
child2 = ET.Element("child2")
child3 = ET.Element("child3")

# Add multiple subelements to the root at once using extend()
root.extend([child1, child2, child3])

# Create a tree from the root element
tree = ET.ElementTree(root)

# Write the XML to a file
tree.write("output.xml")