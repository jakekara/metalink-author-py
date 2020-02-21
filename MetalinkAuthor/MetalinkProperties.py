from .MetalinkEntry import MetalinkEntryProperty as EntryProperty

class BasicProperty(EntryProperty):
    key = "unknown"

    def __init__(self, value: str):
        super(BasicProperty, self).__init__(self.key)
        super(BasicProperty, self).set_text(value)


class SizeProperty(BasicProperty):
    key = "size"

    # Override to require size to be an integer
    def __init__(self, size: int):
        super(SizeProperty, self).__init__(str(size))


class IdentityProperty(BasicProperty):
    key = "identity"


class VersionProperty(BasicProperty):
    key = "version"


class LanguageProperty(BasicProperty):
    key = "language"


class DescriptionProperty(BasicProperty):
    key = "description"


class HashProperty(BasicProperty):
    key = "hash"

    # Override to require a string value and allow an optional hash_type
    def __init__(self, value: str, hash_type="md5"):
        super(HashProperty, self).__init__(value)
        super(HashProperty, self).set_attribute("type", hash_type)


class URLProperty(BasicProperty):
    key = "url"

