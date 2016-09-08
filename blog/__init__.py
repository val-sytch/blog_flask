from flask import Flask
from blog_flask.blog.configurations.config import DATABASE, SECRET_KEY, USERNAME, PASSWORD, DEBUG


app = Flask(__name__)

app.config.update(DATABASE=DATABASE,
                  SECRET_KEY=SECRET_KEY,
                  USERNAME=USERNAME,
                  PASSWORD=PASSWORD,
                  DEBUG = DEBUG)

from blog_flask.blog.views.show_entries import EntryView
from blog_flask.blog.views.login import LoginView
from blog_flask.blog.views.logout import LogoutView
from blog_flask.blog.views.add_entry import AddEntryView
from blog_flask.blog.servises.exception_decorator import write_bug_to_file


app.add_url_rule('/',
                 view_func=write_bug_to_file(EntryView.as_view("show_entries")), methods=['GET'])
app.add_url_rule('/login',
                 view_func=write_bug_to_file(LoginView.as_view("login")), methods=['GET','POST'])
app.add_url_rule('/logout',
                 view_func=write_bug_to_file(LogoutView.as_view("logout")), methods=['GET'])
app.add_url_rule('/add_entry',
                 view_func=write_bug_to_file(AddEntryView.as_view("add_entry")), methods=['POST'])
