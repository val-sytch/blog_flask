from flask import (request, session, redirect,
                   url_for, render_template, flash)
from flask.views import MethodView
from blog_flask.blog.configurations.config import USERNAME, PASSWORD


class LoginView(MethodView):

    def get(self, error=None):
        return render_template('login.html', error=error)

    def post(self):
        error = None
        if request.form['username'] != USERNAME or request.form['password'] != PASSWORD:
            error = 'Invalid username/password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
        return render_template('login.html', error=error)
