from flask import session, flash, redirect, url_for
from flask.views import View

class LogoutView(View):

    def dispatch_request(self):
        session.pop('logged_in', None)
        flash('You were logged out')
        return redirect(url_for('show_entries'))
