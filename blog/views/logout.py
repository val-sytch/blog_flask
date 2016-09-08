from flask import session, flash, redirect, url_for
from flask.views import MethodView


class LogoutView(MethodView):

    def get(self):
        session.pop('logged_in', None)
        flash('You were logged out')
        return redirect(url_for('show_entries'))
