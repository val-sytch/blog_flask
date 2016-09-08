import os
from blog_flask.blog.database.db import WorkWithDatabase


class EntryViewModel():

    def __init__(self,db = WorkWithDatabase):
        self.db = db()

    def get_entries_from_database(self):
        directory_path = os.path.dirname(__file__)
        query_path = os.path.join(directory_path, 'SQL/get_entries_from_database_query.sql')
        query = open(query_path,mode='r').read()
        entries = self.db.execute_get_query(query)
        self.db.close_connection()
        return entries
