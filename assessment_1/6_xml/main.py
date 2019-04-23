"""
description:
A python script to practice interacting with xml for advanced programming.
@author: ksuchak1990
"""
# Imports
from lxml import etree

# Functions
def get_xml(map_xml):
    """
    A function to get hold of xml from an open file.
    """
    xml_file = map_xml.read()
    # Replace to get rid of head
    return xml_file.replace('<?xml version="1.0" encoding="UTF-8"?>', "")

def validate_map1():
    """
    A function to validate map1.xml.
    """
    # Use context managers to open files
    with open('map1.dtd') as map_dtd:
        with open('map1.xml') as map_xml:
            xml1 = get_xml(map_xml)
            dtd = etree.DTD(map_dtd)
            root = etree.XML(xml1)
            print(dtd.validate(root))

def validate_map2():
    """
    A function to validate map2.xml.
    """
    # Use context managers to open files
    with open('map2.xsd') as map_xsd:
        with open('map2.xml') as map_xml:
            xml1 = get_xml(map_xml)
            xsd = etree.XMLSchema(etree.parse(map_xsd))
            root = etree.XML(xml1)
            print(xsd.validate(root))

def list_elements():
    """
    A function to list elements of some xml.
    """
    with open('map1.xml') as map_xml:
        xml1 = get_xml(map_xml)
        root = etree.XML(xml1)
        et = etree.ElementTree(root)
        for element in et.iter():
            print(element)

def add_polygon():
    """
    A function to add a new polygon.
    """
    with open('map1.xml') as map_xml:
        xml1 = get_xml(map_xml)
        root = etree.XML(xml1)
        p = etree.Element("polygon")
        p.set("id", "p2")
        p.append(etree.Element("points"))
        p[0].text = "100,100 100,200 200,200 200,100"
        root.append(p)
        return root

def write_xml():
    """
    A function to write some xml to a file.
    """
    x = add_polygon()
    out = etree.tostring(x, pretty_print=True)
    with open('my_xml.xml', 'wb') as writer:
        writer.write(out)

def transform_to_html():
    """
    A function to take some xml and convert it to html.
    """
    x = add_polygon()
    with open('map3.xsl') as map_xml:
        xsl3 = map_xml.read()
        root = etree.XML(xsl3)
        transform = etree.XSLT(root)
        out_tree = transform(x)
        text = str(out_tree)

        with open('map3.html', 'w') as writer:
            writer.write(text)

def runner():
    """
    A function to run everything for this practical.
    """
    # validate_map1()
    # validate_map2()
    # list_elements()
    # add_polygon()
    # write_xml()
    transform_to_html()

runner()
