import xml.etree.ElementTree as ET

from .MetalinkEntry import MetalinkEntry

class MetalinkDocument:

    def __init__(self):
        self.entries = []

    def get_tree(self):
        tree = ET.ElementTree(element=ET.Element("metalink"))
        tree.getroot().set("xmlns", "urn:ietf:params:xml:ns:metalink")

        for entry in self.entries:
            tree.getroot().append(entry.get_element())

        return tree

    def tostring(self):
        return ET.tostring(self.get_tree().getroot(), encoding="utf8", method="xml").decode("utf-8")

    def add_entry(self, entry: MetalinkEntry):
        self.entries.append(entry)
        return self