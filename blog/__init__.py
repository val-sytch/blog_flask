from flask import Flask
from configurations.config import DATABASE, SECRET_KEY, USERNAME, PASSWORD, DEBUG


app = Flask(__name__)

app.config.update(DATABASE=DATABASE,
                  SECRET_KEY=SECRET_KEY,
                  USERNAME=USERNAME,
                  PASSWORD=PASSWORD,
                  DEBUG = DEBUG)

from views.show_entries import EntryView
from views.login import LoginView
from views.logout import LogoutView
from views.add_entry import AddEntryView
from servises.exception_decorator import write_bug_to_file


app.add_url_rule('/',
                 view_func=write_bug_to_file(EntryView.as_view("show_entries")))
app.add_url_rule('/login',
                 view_func=write_bug_to_file(LoginView.as_view("login")))
app.add_url_rule('/logout',
                 view_func=write_bug_to_file(LogoutView.as_view("logout")))
app.add_url_rule('/add_entry',
                 view_func=write_bug_to_file(AddEntryView.as_view("add_entry")))
