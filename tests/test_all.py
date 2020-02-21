from MetalinkAuthor.MetalinkEntry import MetalinkEntry
from MetalinkAuthor.MetalinkDocument import MetalinkDocument

from xml.etree import ElementTree as ET

def test_metalink_entry_creates_valid_xml():

    entry = MetalinkEntry("sample-file.mov")

    ET.fromstring(entry.tostring())

    # If it gets here it passed


def test_document_creates_valid_xml():

    document = MetalinkDocument()

    doc_str = document.tostring()

    ET.fromstring(doc_str)

    # If it gets here, it hasn't crashed


def test_can_add_entry_to_document():

    document = MetalinkDocument()
    entry = MetalinkEntry("file-1.mov")

    document.add_entry(entry)

    ET.fromstring(document.tostring())

