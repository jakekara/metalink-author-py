import xml.etree.ElementTree as ET


class MetalinkEntryProperty:

    def __init__(self, tag: str):
        self.attrib = {}
        self.children = []
        self.text = None

        self.tag = tag

    def set_text(self, text):
        self.text = str(text)
        return self

    def set_attribute(self, key, value):
        self.attrib[key] = value
        return self

    def add_child(child):
        self.children.append(child)
        return self

    def get_element(self):

        # Create an element
        el = ET.Element(self.tag)

        # set attributes
        for k in self.attrib.keys():
            v = self.attrib[k]
            el.set(k, v)

        el.text = self.text

        # Add children
        for child in self.children:
            el.append(child.get_element())

        return el

    def tostring(self):
        return ET.tostring(self.get_element(), encoding="utf-8", method="xml").decode("utf-8")
