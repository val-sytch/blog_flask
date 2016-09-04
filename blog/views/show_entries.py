from flask import render_template
from flask.views import MethodView
from blog_flask.blog.database.db import WorkWithDatabase


class EntryView(MethodView):

    def get(self):
        db = WorkWithDatabase()
        entries = db.execute_get_query('select title, content from entries order by id desc')
        return render_template('show_entries.html', entries=entries)
