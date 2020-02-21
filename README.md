# Metalink-author

A library for generating Metalink files. Metalink is a format for describing where files can be downloaded. The RFC is 
available here: https://tools.ietf.org/html/rfc5854. 

This library does not support the full Metalink format, but it's easily extensible by adding classes for each property
supported in the RFC. I've only implemented the ones I needed for the project that I built this tool for.

# Usage

This code is in example.py:

    from MetalinkAuthor.MetalinkAuthor import MetalinkEntry, MetalinkDocument, MetalinkProperties
    
    print(MetalinkDocument()\
          .addEntry(
            MetalinkEntry("somefile.mov")\
            .addProperty(MetalinkProperties.SizeProperty(100 * 1000 * 100))\
            .addProperty(MetalinkProperties.URLProperty("https://example.com"))\
            .addProperty(MetalinkProperties.HashProperty("123456789ABCDEF"))
          )\
          .addEntry(
            MetalinkEntry("somefile-2.mov")\
            .addProperty(MetalinkProperties.SizeProperty(200 * 1000 * 100))\
            .addProperty(MetalinkProperties.URLProperty("https://example.com/1"))\
            .addProperty(MetalinkProperties.HashProperty("ABCDEFG-12345"))
          ).tostring()
         )

# Extending

I have only supported a few properties that I needed for a project, but to make this fully support the Metalink spec, 
this just needs appropriate subclasses added to MetalinkAuthor/MetalinkProperties.py folder. Most of them are extremely 
basic. If it's just a property that has a tag with text content, you can just set the class property "key". For instance:

    class LanguageProperty(BasicProperty):
        key = "language"
    
    
    class DescriptionProperty(BasicProperty):
        key = "description"
    
    
For slightly more complicated elements, like the HashProperty, which has an attribute, you may need to override the 
constructor. It's only a couple more lines of code:

   

    class HashProperty(BasicProperty):
        key = "hash"
    
        # Override to require a string value and allow an optional hash_type
        def __init__(self, value: str, hash_type="md5"):
            super(HashProperty, self).__init__(value)
            super(HashProperty, self).setAttribute("type", hash_type)
