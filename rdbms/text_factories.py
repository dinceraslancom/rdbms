from sqlite3 import OptimizedUnicode


def text_factory_utf_8(data):
    return data.decode("utf-8")


def text_factory_str(data):
    return str(data)


def text_factory_bytes(data):
    return bytes(data)


optimized_unicode_factory = OptimizedUnicode
