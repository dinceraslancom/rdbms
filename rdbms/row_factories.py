"""
https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.row_factory
"""

from simpleitem import SimpleItem
from sqlite3 import Row

row_factory = Row


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def simpleitem_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0].lower()] = row[idx]
    return SimpleItem(**d)
