import functools
import sqlite3

from .row_factories import simpleitem_factory
from .text_factories import optimized_unicode_factory


class SQLExecuteDecorator(object):
    def __init__(self, func, con):
        functools.update_wrapper(self, func)
        self.con = con
        self.func = func

    def make_generator(self, cursor):
        yield from cursor

    def __call__(self, *args, **kwargs):
        query = self.func.__doc__.format(**kwargs).lstrip()
        query_type = query[:6].lower()
        size = kwargs.get('size')
        iterable = kwargs.get('iterable')

        if kwargs.get('script'):
            cursor = self.con.executescript(query)
        else:
            cursor = self.con.execute(query)

        if query_type.startswith('insert'):
            self.con.commit()

        if query_type.startswith('select'):
            if size:
                return cursor.fetchmany(size)
            elif iterable:
                return self.make_generator(cursor)
            else:
                return cursor.fetchall()


class RDBMS(object):
    path = ':memory:'

    def __init__(self):
        self.__con = sqlite3.connect(self.path)

        # filter dunder and base methods
        for func_name in dir(self):
            func = getattr(self, func_name)
            if func_name.startswith('_') or func_name in (
                    'path',
                    'set_row_factory',
                    'set_text_factory',
                    'add_function',
                    'add_aggregate',
                    'add_collation',
            ):
                continue
            setattr(self, func_name, SQLExecuteDecorator(func, self.__con))

        self.setup(script=True)

        self.set_row_factory(simpleitem_factory)
        self.set_text_factory(optimized_unicode_factory)

    def set_row_factory(self, row_factory):
        self.__con.row_factory = row_factory

    def set_text_factory(self, text_factory):
        self.__con.text_factory = text_factory

    def add_function(self, func):
        self.__con.create_function(func.__name__, -1, func)

    def add_aggregate(self, func):
        self.__con.create_aggregate(func.__name__, -1, func)

    def add_collation(self, func):
        self.__con.create_collation(func.__name__, func)

    def setup(self):
        ...
