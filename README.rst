RDBMS
---------

Relational Database Management System


Installing
------------

Install and update using `pip3`_:

.. code-block:: text

    $ pip3 install rdbms

Python 3 and newer.

.. _pip3: https://pip.pypa.io/en/stable/quickstart/


Simple Usage
----------------

.. code-block:: python

    from rdbms import RDBMS


    class User(RDBMS):
        path = './test_sqlite.db' # default in-memory usage

        def setup(self):
            """
            CREATE TABLE IF NOT EXISTS  user
            (
             id INTEGER   PRIMARY KEY   AUTOINCREMENT,
             name         TEXT          NOT NULL UNIQUE,
             password     CHAR(200)
             );
            """

        def create_user(self, name, password):
            """
            INSERT INTO user (name, password)
            VALUES ('{name}', '{password}')
            """

        def get_user(self, name):
            """
            SELECT * FROM user
            WHERE name = '{name}'
            """

        def execute_script_example(script=True):
           """
           Run script
           """


    if __name__ == '__main__':
        user = User()
        user.create_user(name='username', password='1234')
        users = user.get_user(name='username')
        assert users[0].name == users[0]['name']

Parameters Example
----------------------

.. code-block:: python

    from rdbms import RDBMS


    class Test(RDBMS):
        def setup(self): # not required | script parameter defaults to True for setup function
            """
            Some SQL script
            """

        def script_execute(self, script=True): # run script | script default False
            """
            Some SQL script
            """

        def iterable_object(self, iterable=True): # return generator | iterable default False
            """
            Some SQL query
            """

        def fixed_size(self, size=1): # fixed size data return | size default None
            """
            Some SQL query
            """



Function Example
-------------------

.. code-block:: python

    from rdbms import RDBMS


    def titlecase(text):
        return text.title()

    class Test(RDBMS):
        ...

        def get_test_function_data(self, data):
            """
            SELECT titlecase(name) FROM test WHERE name='{data}'
            """


    if __name__ == '__main__':
        test = Test()
        test.add_function(titlecase)
        result = self.test.get_test_function_data(data='test name')
        assert result[0].name == 'Test Name'


Aggregate Example
-------------------

.. code-block:: python

    from rdbms import RDBMS


    class mysum:
        def __init__(self):
            self.count = 0

        def step(self, value):
            self.count += value

        def finalize(self):
            return self.count

    class Test(RDBMS):
        ...

        def get_test_aggregate_data(self):
            """
            SELECT mysum(age) FROM test
            """


    if __name__ == '__main__':
        test = Test()
        test.add_collaction(mysum)
        result = test.get_test_aggregate_data()
        assert result[0]['mysum(age)'] == 100

Collaction Example
-------------------

.. code-block:: python

    from rdbms import RDBMS


    def collate_reverse(string1, string2):
        if string1 == string2:
            return 0
        elif string1 < string2:
            return 1
        else:
            return -1

    class Test(RDBMS):
        ...

        def get_test_collation_data(self):
            """
            SELECT name FROM test ORDER BY name COLLATE collate_reverse
            """


    if __name__ == '__main__':
        test = Test()
        test.add_collaction(collate_reverse)
        result = test.get_test_collation_data()
        assert result[0]['name'] == 'b'
        assert result[1]['name'] == 'a'


Text Factory Example
---------------------

.. code-block:: python

    from rdbms import RDBMS
    from rdbms.text_factories import text_factory_bytes


    class Test(RDBMS):
        ...


    if __name__ == '__main__':
        test = Test()
        test.set_text_factory(text_factory_bytes)
        data = test.get_data()
        assert result[0].attribute, bytes

Row Factory Example
--------------------

.. code-block:: python

    from rdbms import RDBMS
    from rdbms.text_factories import dict_factory


    class Test(RDBMS):
        ...


    if __name__ == '__main__':
        test = Test()
        test.set_row_factory(dict_factory)
        data = test.get_data()
        assert 'attribute' in result[0]


Support
-------

*   Python 3.x
*   Supports all operating systems

Links
-----

*   License: `MIT License <https://github.com/dinceraslancom/rdbms/blob/master/LICENSE>`_
*   Code: https://github.com/dinceraslancom/rdbms
