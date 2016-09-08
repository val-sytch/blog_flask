import os
from flask import request, flash
from blog_flask.blog.database.db import WorkWithDatabase


class AddEntryViewModel():

    def __init__(self,db = WorkWithDatabase):
        self.db = db()

    def add_entry_to_database(self):
        directory_path = os.path.dirname(__file__)
        query_path = os.path.join(directory_path, 'SQL/add_entry_to_database_query.sql')
        query = open(query_path, mode='r').read()
        self.db.execute_post_query(query,[request.form['title'], request.form['content']])
        self.db.close_connection()
        return flash('New post was successfully posted')
