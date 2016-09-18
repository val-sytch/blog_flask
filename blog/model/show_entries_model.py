from blog.database.db import WorkWithDatabase
from blog.model.SQL.get_entries_from_database_query import get_query


class EntryViewModel:

    def __init__(self, db=WorkWithDatabase):
        self.db = db()

    def get_entries_from_database(self):
        entries = self.db.execute_get_query(get_query)
        self.db.close_connection()
        return entries
