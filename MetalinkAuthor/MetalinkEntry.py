import xml.etree.ElementTree as ET
from .MetalinkEntryProperty import MetalinkEntryProperty


class MetalinkEntry:

    def __init__(self, filename):
        self.filename = filename
        self.children = []

    def get_element(self):
        root = ET.Element("file")
        root.set("name", self.filename)

        for child in self.children:
            root.append(child.get_element())

        return root

    def add_property(self, prop: MetalinkEntryProperty):
        self.children.append(prop)
        return self

    def tostring(self):
        return ET.tostring(self.get_element(), encoding="utf-8", method="xml").decode("utf-8")

