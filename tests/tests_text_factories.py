# https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.text_factory

import unittest

from rdbms.rdbms import RDBMS
from rdbms.rdbms.text_factories import text_factory_bytes, text_factory_str

AUSTRIA = "Österreich"


class TestTextFactories(RDBMS):

    def get_country(self, name):
        """
        select * FROM (VALUES ("{name}"))
        """


class TestQuery(unittest.TestCase):
    def setUp(self):
        self.test_rdbms = TestTextFactories()
        self.test_rdbms.set_row_factory(None)

    def test_lambda_text_factory(self):
        self.test_rdbms.set_text_factory(lambda x: x.decode("utf-8") + "foo")
        result = self.test_rdbms.get_country(name='bar')
        self.assertEqual(result[0][0], 'barfoo')

    def test_none_text_factory(self):
        result = self.test_rdbms.get_country(name=AUSTRIA)
        self.assertEqual(result[0][0], AUSTRIA)

    def test_text_factory_bytes(self):
        self.test_rdbms.set_text_factory(text_factory_bytes)
        result = self.test_rdbms.get_country(name=AUSTRIA)
        self.assertIsInstance(result[0][0], bytes)
        self.assertEqual(result[0][0], AUSTRIA.encode("utf-8"))


if __name__ == '__main__':
    unittest.main()
