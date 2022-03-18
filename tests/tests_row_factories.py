# https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.row_factory

import unittest
from simpleitem import SimpleItem
from rdbms.rdbms import RDBMS
from rdbms.rdbms.row_factories import simpleitem_factory, dict_factory


class TestRowFactories(RDBMS):

    def get_result(self):
        """
        select 1 as a
        """


class TestQuery(unittest.TestCase):
    def setUp(self):
        self.test_rdbms = TestRowFactories()
        self.test_rdbms.set_row_factory(None)

    def test_none_row_factory(self):
        result = self.test_rdbms.get_result()
        self.assertTupleEqual(result[0], (1,))

    def test_dict_row_factory(self):
        self.test_rdbms.set_row_factory(dict_factory)
        result = self.test_rdbms.get_result()
        self.assertDictEqual(result[0], {'a': 1})

    def test_simpleitem_row_factory(self):
        self.test_rdbms.set_row_factory(simpleitem_factory)
        result = self.test_rdbms.get_result()
        self.assertIsInstance(result[0], SimpleItem)
        self.assertDictEqual(result[0].to_dict, {'a': 1})


if __name__ == '__main__':
    unittest.main()
