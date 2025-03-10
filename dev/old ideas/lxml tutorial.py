#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john.f.kennedy
#
# Created:     14/12/2024
# Copyright:   (c) john.f.kennedy 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from lxml import etree

def prettyprint(element, **kwargs):
    xml = etree.tostring(element, pretty_print=True, **kwargs)
    print(xml.decode(), end='')

def main():
    print("Examples")
    root = etree.Element("root")
    print(f"Root tag: {root.tag}")

    # Two ways to add subelements
    root.append( etree.Element("child1") )
    child2 = etree.SubElement(root, "child2")
    child3 = etree.SubElement(root, "child3")

    print(f"Root to string: {etree.tostring(root)}")

    # Pretty Print
    print("Pretty Print")
    prettyprint(root)

    child = root[0]
    print(child.tag)
    print(len(root))
    print(root.index(root[1]))  # lxml.etree only!

    children = list(root)

    for child in root:
        print(f"Child: {child.tag}")

    root.insert(0, etree.Element("child0"))
    start = root[:1]
    end   = root[-1:]

    print(f"Start: {start[0].tag}")
    print(f"End: {end[0].tag}")

    print(etree.iselement(root))  # test if it's some kind of Element

    if len(root):                 # test if it has children
        print("The root element has children")

    print(f"\n{'--PRINT' * 10}--\n")

    for child in root:
        print(f"Child: {child.tag}")

    print(f"\n{'--PRINT' * 10}--\n")

    root[0] = root[-1]  # this moves the element in lxml.etree!

    for child in root:
        print(f"Child: {child.tag}")

    print(f"\n{'--PRINT' * 10}--\n")

    print(f"Root to string: {etree.tostring(root)}")

    print(root is root[0].getparent())  # lxml.etree only!

    print(f"\n{'--PRINT' * 10}--\n")

    from copy import deepcopy

    element = etree.Element("neu")
    element.append( deepcopy(root[1]) )

    print(element[0].tag)

    print([ c.tag for c in root ])

    print(etree.tostring(element))

    print(f"\n{'--PRINT' * 10}--\n")

    print(root[0] is root[1].getprevious()) # lxml.etree only!
    print(root[1] is root[0].getnext()) # lxml.etree only!
    print(root[0].getnext().tag)

    print(f"\n{'--PRINT' * 10}--\n")

    root = etree.Element("root", interesting="totally")
    print(etree.tostring(root))
    print(root.get("interesting"))
    print(root.get("hello"))
    root.set("hello", "Huhu")
    print(root.get("hello"))
    print(etree.tostring(root))
    print(sorted(root.keys()))

    for name, value in sorted(root.items()):
        print('%s = %r' % (name, value))

    print(f"\n{'--PRINT' * 10}--\n")

    attributes = root.attrib
    print(attributes["interesting"])
    print(attributes.get("no-such-attribute"))
    attributes["hello"] = "Guten Tag"
    print(attributes["hello"])
    print(root.get("hello"))

    d = dict(root.attrib)
    print(sorted(d.items()))

    print(f"\n{'--PRINT' * 10}--\n")

    root = etree.Element("root")
    root.text = "TEXT"
    print(root.text)

    print(etree.tostring(root))

    print(f"\n{'--PRINT' * 10}--\n")

    html = etree.Element("html")
    body = etree.SubElement(html, "body")
    body.text = "TEXT"

    print(etree.tostring(html))

    br = etree.SubElement(body, "br")
    print(etree.tostring(html))

    br.tail = "TAIL"
    print(etree.tostring(html))

    print(etree.tostring(br))

    print(etree.tostring(br, with_tail=False)) # lxml.etree only!

    print(etree.tostring(html, method="text"))

    print(html.xpath("string()")) # lxml.etree only!
    print(html.xpath("//text()")) # lxml.etree only!

    build_text_list = etree.XPath("//text()") # lxml.etree only!
    print(build_text_list(html))

    texts = build_text_list(html)
    print(texts[0])

    parent = texts[0].getparent()
    print(parent.tag)

    print(texts[1])
    print(texts[1].getparent().tag)
    print(texts[0].is_text)
    print(texts[1].is_text)
    print(texts[1].is_tail)

    stringify = etree.XPath("string()")
    print(stringify(html))
    print(stringify(html).getparent())

    print(f"\n{'--PRINT' * 10}--\n")

    root = etree.Element("root")
    etree.SubElement(root, "child").text = "Child 1"
    etree.SubElement(root, "child").text = "Child 2"
    etree.SubElement(root, "another").text = "Child 3"

    prettyprint(root)

    for element in root.iter():
        print(f"{element.tag} - {element.text}")

    for element in root.iter("child"):
        print(f"{element.tag} - {element.text}")

    for element in root.iter("another", "child"):
        print(f"{element.tag} - {element.text}")

    print(f"\n{'--PRINT' * 10}--\n")

    root.append(etree.Entity("#234"))
    root.append(etree.Comment("some comment"))

    for element in root.iter():
        if isinstance(element.tag, str):
            print(f"{element.tag} - {element.text}")
        else:
            print(f"SPECIAL: {element} - {element.text}")

    prettyprint(root)
    #print(etree.tostring(root))

    for element in root.iter(tag=etree.Element):
        print(f"{element.tag} - {element.text}")

    print(f"\n{'--PRINT' * 10}--\n")

    print("Serialisation")

    root = etree.XML('<root><a><b/></a></root>')

    print(etree.tostring(root))

    xml_string = etree.tostring(root, xml_declaration=True)
    print(xml_string.decode(), end='')

    #latin1_bytesstring = etree.tostring(root, encoding='unicode')
    #print(latin1_bytesstring.decode('unicode'), end='')

    print(etree.tostring(root, pretty_print=True).decode(), end='')

    root = etree.XML('<root><a><b/>\n</a></root>')
    print(etree.tostring(root).decode())

    etree.indent(root)
    print(etree.tostring(root).decode())

    print(root.text)

    print(root[0].text)

    etree.indent(root, space="    ")
    print(etree.tostring(root).decode())

    etree.indent(root, space="\t")
    print(etree.tostring(root))

    root = etree.XML('<html><head/><body><p>Hello<br/>World</p></body></html>')

    print(etree.tostring(root))  # default: method = 'xml'

    print(etree.tostring(root, method='xml'))  # same as above

    print(etree.tostring(root, method='html'))

    prettyprint(root, method='html')

    print(etree.tostring(root, method='text'))

    br = next(root.iter('br'))  # get first result of iteration
    br.tail = 'Wörld'

    #print(etree.tostring(root, method='text'))  # doctest: +ELLIPSIS

    print(etree.tostring(root, method='text', encoding='UTF-8'))

    print(etree.tostring(root, encoding='unicode', method='text'))

    print(etree.tostring(root, encoding='unicode'))

    print(f"\n{'--PRINT' * 10}--\n")

    print("The ElementTree class")

    root = etree.XML('''<?xml version="1.0"?><!DOCTYPE root SYSTEM "test" [ <!ENTITY tasty "parsnips"> ]><root><a>&tasty;</a></root>''')

    tree = etree.ElementTree(root)
    print(tree.docinfo.xml_version)

    print(tree.docinfo.doctype)

    tree.docinfo.public_id = '-//W3C//DTD XHTML 1.0 Transitional//EN'
    tree.docinfo.system_url = 'file://local.dtd'
    print(tree.docinfo.doctype)

    prettyprint(tree)  # lxml 1.3.4 and later

    prettyprint(tree.getroot())

    print(f"\n{'--PRINT' * 10}--\n")

    print("Parsing from strings and files")
    print("The fromstring() function")
    some_xml_data = "<root>data</root>"
    root = etree.fromstring(some_xml_data)
    print(root.tag)
    print(etree.tostring(root))

    print("\nThe XML() function\n")
    root = etree.XML("<root>data</root>")
    print(root.tag)
    print(etree.tostring(root))

    root = etree.HTML("<p>data</p>")
    print(etree.tostring(root))

    print("\nThe parse() function\n")

    from io import BytesIO
    some_file_or_file_like_object = BytesIO(b"<root>data</root>")
    tree = etree.parse(some_file_or_file_like_object)
    print(etree.tostring(tree))

    root = tree.getroot()
    print(root.tag)
    print(etree.tostring(root))

    print("\nParser objects\n")
    parser = etree.XMLParser(encoding='UTF-8', remove_blank_text=True)  # lxml.etree only!
    root = etree.XML("<root>  <a/>   <b>  </b>     </root>", parser)
    print(etree.tostring(root))

    for element in root.iter("*"):
        if element.text is not None and not element.text.strip():
            element.text = None

    print(etree.tostring(root))

    print("\nIncremental parsing\n")

    class DataSource:
        data = [ b"<roo", b"t><", b"a/", b"><", b"/root>" ]
        def read(self, requested_size):
            try:
                return self.data.pop(0)
            except IndexError:
                return b''

    tree = etree.parse(DataSource())
    print(etree.tostring(tree))

    parser = etree.XMLParser()
    parser.feed("<roo")
    parser.feed("t><")
    parser.feed("a/")
    parser.feed("><")
    parser.feed("/root>")
    root = parser.close()

    print(etree.tostring(root))

    parser.feed("<root/>")
    root = parser.close()
    print(etree.tostring(root))

    print("\nEvent-driven parsing\n")
    some_file_like = BytesIO(b"<root><a>data</a></root>")

    for event, element in etree.iterparse(some_file_like):
        print(f"{event}, {element.tag:>4}, {element.text}")

    some_file_like = BytesIO(b"<root><a>data</a></root>")

    for event, element in etree.iterparse(some_file_like, events=("start", "end")):
        print(f"{event:>5}, {element.tag:>4}, {element.text}")

    some_file_like = BytesIO(b"<root><a><b>data</b></a><a><b/></a></root>")
    for event, element in etree.iterparse(some_file_like):
        if element.tag == 'b':
            print(element.text)
        elif element.tag == 'a':
            print("** cleaning up the subtree")
            element.clear(keep_tail=True)

    xml_file = BytesIO(b'''<root><a><b>ABC</b><c>abc</c></a><a><b>MORE DATA</b><c>more data</c></a><a><b>XYZ</b><c>xyz</c></a></root>''')
    for _, element in etree.iterparse(xml_file, tag='a'):
        print('%s -- %s' % (element.findtext('b'), element[1].text))
        element.clear(keep_tail=True)

    class ParserTarget:
        events = []
        close_count = 0
        def start(self, tag, attrib):
            self.events.append(("start", tag, attrib))
        def close(self):
            events, self.events = self.events, []
            self.close_count += 1
            return events

    parser_target = ParserTarget()

    parser = etree.XMLParser(target=parser_target)
    events = etree.fromstring('<root test="true"/>', parser)

    print(parser_target.close_count)

    for event in events:
        print(f'event: {event[0]} - tag: {event[1]}')
        for attr, value in event[2].items():
            print(f' * {attr} = {value}')

    events = etree.fromstring('<root test="true"/>', parser)
    print(parser_target.close_count)

    events = etree.fromstring('<root test="true"/>', parser)
    print(parser_target.close_count)

    events = etree.fromstring('<root test="true"/>', parser)
    print(parser_target.close_count)

    for event in events:
        print(f'event: {event[0]} - tag: {event[1]}')
        for attr, value in event[2].items():
            print(f' * {attr} = {value}')

    print(f"\n{'--PRINT' * 10}--\n")

    print("\nElementPath\n")
    root = etree.XML("<root><a x='123'>aText<b/><c/><b/></a></root>")
    print(root.find("b"))
    print(root.find("a").tag)
    print(root.find(".//b").tag)
    print([ b.tag for b in root.iterfind(".//b") ])

    print(root.findall(".//a[@x]")[0].tag)
    print(root.findall(".//a[@y]"))

    print("\n---\n")
    tree = etree.ElementTree(root)
    a = root[0]
    #print(a[0].tag)
    print(tree.getelementpath(a[0]))

    print(tree.getelementpath(a[1]))

    print(tree.getelementpath(a[2]))

    print(tree.find(tree.getelementpath(a[2])) == a[2])

    #print(etree.tostring(root))

    print(etree.tostring(root, pretty_print=True).decode(), end='')

    print(root.find(".//b").tag)
    print(next(root.iterfind(".//b")).tag)
    print(next(root.iter("b")).tag)

    print("\n----------------\n")
    from io import StringIO, BytesIO
    xml = '<a xmlns="test"><b xmlns="test"/></a>'
    root = etree.fromstring(xml)
    print(etree.tostring(root, pretty_print=True).decode(), end='')

    print("\n----------------\n")
    tree = etree.parse(StringIO(xml))
    print(etree.tostring(tree.getroot(), pretty_print=True).decode(), end='')

    print("\n----------------\n")

    #tree = etree.parse("doc/test.xml")
    #root = etree.fromstring(xml, base_url="http://where.it/is/from.xml")
    #parser = etree.XMLParser(ns_clean=True)
    #xml_root = etree.fromstring(xml, parser)
    #print(etree.tostring(xml_root, pretty_print=True).decode(), end='')

    print(f"\n{'--PRINT' * 10}--\n")

if __name__ == '__main__':
    main()
