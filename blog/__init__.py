import os
from flask import Flask
from configurations.config import SECRET_KEY, DEBUG
from database.db import WorkWithDatabase

app = Flask(__name__, static_url_path='/static')

app.config.update(SECRET_KEY=SECRET_KEY,
                  DEBUG=DEBUG)

from views.show_entries import EntryView
from views.login import LoginView
from views.logout import LogoutView
from views.add_entry import AddEntryView
from servises.exception_decorator import write_bug_to_file


app.add_url_rule('/',
                 view_func=write_bug_to_file(EntryView.as_view("show_entries")), methods=['GET'])
app.add_url_rule('/login',
                 view_func=write_bug_to_file(LoginView.as_view("login")), methods=['GET','POST'])
app.add_url_rule('/logout',
                 view_func=write_bug_to_file(LogoutView.as_view("logout")), methods=['GET'])
app.add_url_rule('/add_entry',
                 view_func=write_bug_to_file(AddEntryView.as_view("add_entry")), methods=['POST'])

# create db file if it isn't exist
db_obj = WorkWithDatabase()
if not os.path.isfile(db_obj.db_file):
    db_obj.create_db_file_if_none()
