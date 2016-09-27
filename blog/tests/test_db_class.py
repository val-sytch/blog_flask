import os
import unittest
from blog.database.db import WorkWithDatabase
from blog.model.SQL.add_entry_to_database_query import insert_query
from blog.model.SQL.get_entries_from_database_query import get_query


class WorkWithDatabaseTestCase(unittest.TestCase):
    """
    Test that all methods in class WorkWithDatabase work as expected.
    Use sql template for db creation, GET and INSERT queries which is used in models.
    Create temporary database for testing.
    """

    def setUp(self):
        self.db_temp_file = os.path.join(os.path.dirname(__file__), 'temp_db.db')
        self.db_obj = WorkWithDatabase()
        # replace link to db from config file with temporary file
        self.db_obj.db_file = self.db_temp_file
        # create db in temporary file
        self.db_obj.create_db_file_if_none()

    def tearDown(self):
        os.remove(self.db_temp_file)

    def test_db_methods_and_queries_syntax(self):
        test_param_for_query = ['title blog', 'text blog', 'audiofile name',
                                'another audiofile name', 'imagefile name']
        self.db_obj.execute_post_query(insert_query, test_param_for_query)
        data_from_temp_db = self.db_obj.execute_get_query(get_query)
        self.assertIn('title blog', data_from_temp_db[0]['title'])
        self.assertIn('text blog', data_from_temp_db[0]['content'])
        self.assertIn('audiofile name', data_from_temp_db[0]['audiofile_cust'])
        self.assertIn('another audiofile name', data_from_temp_db[0]['audiofile'])
        self.assertIn('imagefile name', data_from_temp_db[0]['imagefile'])

if __name__ == '__main__':
    unittest.main()
