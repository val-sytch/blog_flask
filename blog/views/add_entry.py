from flask import redirect,render_template, url_for
from flask.views import MethodView
from blog.model.add_entry_model import AddEntryViewModel


class AddEntryView(MethodView):

    def __init__(self,model=AddEntryViewModel):
        self.model = model()

    def get(self):
        return render_template('add_entry.html')

    def post(self):
        self.model.add_entry_to_database()
        return redirect(url_for('show_entries'))
