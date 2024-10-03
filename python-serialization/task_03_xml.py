#!usr/bin/python3

import xml.etree.ElementTree as ET

"""Serialization and deserialization using XML as an alternative
format to JSON."""


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to an XML file."""
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    with open(filename, 'wb') as xml_file:
        tree.write(xml_file, encoding='utf-8', xml_declaration=True)


def desirialize_from_xml(filename):
    """Deserialize an XML file to a dictionary."""
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text
    return dictionary
