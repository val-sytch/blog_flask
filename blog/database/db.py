import os
import sqlite3
from blog_flask.blog.configurations.config import DB_FILENAME, DB_FILE_SQL


class WorkWithDatabase(object):
    connection_obj = None
    DATABASE = os.path.join(os.path.dirname(__file__), DB_FILENAME)

    def _create_connection(self):
        if self.connection_obj is None:
            self.connection_obj = self._connect_db()

    def _connect_db(self):
        self.connection_obj = sqlite3.connect(self.DATABASE)
        self.connection_obj.row_factory = sqlite3.Row
        return self.connection_obj

    def execute_get_query(self,query):
        self._create_connection()
        cursor_obj = self.connection_obj.execute(query)
        entries = cursor_obj.fetchall()
        self.connection_obj.close()
        return entries

    def execute_post_query(self,query,param):
        self._create_connection()
        self.connection_obj.execute(query,param)
        self.connection_obj.commit()

    def close_connection(self):
        return self.connection_obj.close()

    def create_db_file_if_none(self):
        if not os.path.isfile(self.DATABASE):
            self.connection_obj = sqlite3.connect(self.DATABASE)
            path_to_create_db_sql = os.path.join(os.path.dirname(__file__), DB_FILE_SQL)
            create_db_sql = open(path_to_create_db_sql, mode='r').read()
            self.connection_obj.executescript(create_db_sql)
            self.close_connection()

