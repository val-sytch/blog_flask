from flask import render_template
from flask.views import MethodView
from blog_flask.blog.model.show_entries_model import EntryViewModel


class EntryView(MethodView):

    def get(self):
        view = EntryViewModel()
        entries = view.get_entries_from_database()
        return render_template('show_entries.html', entries=entries)
