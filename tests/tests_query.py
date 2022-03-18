import unittest

from rdbms.rdbms import RDBMS

from types import GeneratorType


class User(RDBMS):
    def setup(self):
        """
        CREATE TABLE USER
        (
         ID INTEGER   PRIMARY KEY   AUTOINCREMENT,
         NAME         TEXT          NOT NULL UNIQUE,
         PASSWORD     CHAR(200)
         );
        """

    def create_user(self, name, password):
        """
        INSERT INTO USER (NAME, PASSWORD)
        VALUES ('{name}', '{password}')
        """

    def get_user(self, name):
        """
        SELECT name FROM user
        WHERE name = '{name}'
        """

    def get_all_users(self):
        """
        SELECT name FROM user
        """


class TestQuery(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_insert_and_select_execute(self):
        self.user.create_user(name='username', password='1234')
        users = self.user.get_user(name='username')
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].name, 'username')

    def test_size_param(self):
        self.user.create_user(name='username1', password='1234')
        self.user.create_user(name='username2', password='1234')
        users_all = self.user.get_all_users()
        self.assertEqual(len(users_all), 2)
        users_size_1 = self.user.get_all_users(size=1)
        self.assertEqual(len(users_size_1), 1)

    def test_size_iterable(self):
        self.user.create_user(name='username1', password='1234')
        users_iterable = self.user.get_all_users(iterable=True)
        self.assertIsInstance(users_iterable, GeneratorType)
        self.assertDictEqual(next(users_iterable).to_dict,
                             {'name': 'username1'})

        users_list = self.user.get_all_users(iterable=False)
        self.assertIsInstance(users_list, list)
        self.assertDictEqual(users_list[0].to_dict, {'name': 'username1'})


if __name__ == '__main__':
    unittest.main()
