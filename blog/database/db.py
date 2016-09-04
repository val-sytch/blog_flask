import sqlite3
from blog_flask.blog.configurations.config import DATABASE


class WorkWithDatabase(object):
    connection_obj = None

    def check_connection(self):
        if self.connection_obj is None:
            self.connection_obj = self.connect_db()

    def connect_db(self):
        self.connection_obj = sqlite3.connect(DATABASE)
        self.connection_obj.row_factory = sqlite3.Row
        return self.connection_obj

    def execute_get_query(self,query):
        self.check_connection()
        cursor_obj = self.connection_obj.execute(query)
        entries = cursor_obj.fetchall()
        return entries

    def execute_post_query(self,query,param):
        self.check_connection()
        cursor_obj = self.connection_obj.execute(query,param)
        self.connection_obj.commit()
