# https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.create_function
# https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.create_aggregate
# https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.create_collation

import unittest
from rdbms.rdbms import RDBMS


def titlecase(text):
    return text.title()


class mysum:
    def __init__(self):
        self.count = 0

    def step(self, value):
        self.count += value

    def finalize(self):
        return self.count


def collate_reverse(string1, string2):
    if string1 == string2:
        return 0
    elif string1 < string2:
        return 1
    else:
        return -1


class TestTextFactories(RDBMS):
    def setup(self):
        """
        CREATE TABLE user
        (
         ID INTEGER,
         NAME         TEXT
         );

        INSERT INTO user (id, name)
        VALUES (1, 'a'), (2,'b')


        """

    def get_test_function_data(self, data):
        """
        SELECT titlecase(name) FROM user WHERE name='{data}'
        """

    def get_test_aggregate_data(self):
        """
        SELECT mysum(id) FROM user
        """

    def get_test_collation_data(self):
        """
        select name from user order by name collate collate_reverse
        """


class TestQuery(unittest.TestCase):
    def setUp(self):
        self.test_rdbms = TestTextFactories()
        self.test_rdbms.set_row_factory(None)

    def test_function(self):
        self.test_rdbms.add_function(titlecase)
        result = self.test_rdbms.get_test_function_data(data='a')
        self.assertEqual(result[0][0], 'A')

    def test_aggregate(self):
        self.test_rdbms.add_aggregate(mysum)
        result = self.test_rdbms.get_test_aggregate_data()
        self.assertEqual(result[0][0], 3)

    def test_collation(self):
        self.test_rdbms.add_collation(collate_reverse)
        result = self.test_rdbms.get_test_collation_data()
        self.assertTupleEqual(result[0], ('b',))
        self.assertTupleEqual(result[1], ('a',))


if __name__ == '__main__':
    unittest.main()
