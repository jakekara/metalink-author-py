from MetalinkAuthor.MetalinkAuthor import MetalinkEntry, MetalinkDocument, MetalinkProperties

print(MetalinkDocument()\
      .add_entry(
        MetalinkEntry("somefile.mov")\
        .add_property(MetalinkProperties.SizeProperty(100 * 1000 * 100))\
        .add_property(MetalinkProperties.URLProperty("https://example.com"))\
        .add_property(MetalinkProperties.HashProperty("123456789ABCDEF"))
      )\
      .add_entry(
        MetalinkEntry("somefile-2.mov")\
        .add_property(MetalinkProperties.SizeProperty(200 * 1000 * 100))\
        .add_property(MetalinkProperties.URLProperty("https://example.com/1"))\
        .add_property(MetalinkProperties.HashProperty("ABCDEFG-12345"))
      ).tostring()
     )
