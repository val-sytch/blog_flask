import os
from blog.configurations.config import SQL_QUERIES_PATH
from blog.database.db import WorkWithDatabase


class EntryViewModel():

    def __init__(self,db = WorkWithDatabase):
        self.db = db()

    def get_entries_from_database(self):
        query_path = os.path.join(SQL_QUERIES_PATH, 'get_entries_from_database_query.sql')
        query = open(query_path,mode='r').read()
        entries = self.db.execute_get_query(query)
        self.db.close_connection()
        return entries
