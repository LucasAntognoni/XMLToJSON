import xml.etree.ElementTree as ET

from collections import defaultdict


def process(element):

    dictionary = {
        element.tag: []
    }

    element_children = list(element)

    if element_children:

        default_dict = defaultdict(list)

        for map_dict in map(process, element_children):
            for key, value in map_dict.items():
                default_dict[key].append(value)

        for key, value in default_dict.items():
            if len(value) == 1:
                dictionary[element.tag].append({key: value[0]})
            else:
                for v in value:
                    dictionary[element.tag].append({key: v})

    if element.text:
        text = element.text.strip()
        if element_children:
            if text:
                dictionary[element.tag]["#text"] = text
        else:
            dictionary[element.tag] = text

    return dictionary


def convert(xml_string):

    try:
        root = ET.XML(xml_string)

        if not list(root):
            return {root.tag: ""}

        dictionary = process(root)

        return dictionary

    except Exception:
        return {
            "Success": False,
            "Error": "Error processing file"
        }
