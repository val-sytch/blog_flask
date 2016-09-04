from flask import request,redirect, flash, url_for
from flask.views import MethodView
from blog_flask.blog.database.db import WorkWithDatabase


class AddEntryView(MethodView):

    def post(self):
        db = WorkWithDatabase()
        db.execute_post_query('insert into entries (title, content) values (?, ?)',
               [request.form['title'], request.form['content']])
        flash('New post was successfully posted')
        return redirect(url_for('show_entries'))
