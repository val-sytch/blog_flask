import os
import sqlite3
from blog.configurations.config import DB_FILENAME, DB_FILE_SQL


class WorkWithDatabase(object):
    connection_obj = None
    DATABASE = os.path.join(os.path.dirname(__file__), DB_FILENAME)

    def _create_connection(self):
        """
        Check if connection is exists. If not, call __connect_db
        """
        if self.connection_obj is None:
            self.connection_obj = self._connect_db()

    def _connect_db(self):
        """
         Create connection to database.
         Row provides both index-based and case-insensitive name-based access to columns
         with almost no memory overhead.
        """
        self.connection_obj = sqlite3.connect(self.DATABASE)
        self.connection_obj.row_factory = sqlite3.Row
        return self.connection_obj

    def execute_get_query(self,query):
        """
        Execute GET query.
        """
        self._create_connection()
        cursor_obj = self.connection_obj.execute(query)
        entries = cursor_obj.fetchall()
        return entries

    def execute_post_query(self,query,param):
        """
        Execute POST query
        """
        self._create_connection()
        self.connection_obj.execute(query,param)
        self.connection_obj.commit()

    def close_connection(self):
        """
         Close connection to database
        """
        return self.connection_obj.close()

    def create_db_file_if_none(self):
        """
        Check if db file is exists, if not, create it.
        """
        if not os.path.isfile(self.DATABASE):
            self.connection_obj = sqlite3.connect(self.DATABASE)
            path_to_create_db_sql = os.path.join(os.path.dirname(__file__), DB_FILE_SQL)
            create_db_sql = open(path_to_create_db_sql, mode='r').read()
            self.connection_obj.executescript(create_db_sql)
            self.close_connection()
