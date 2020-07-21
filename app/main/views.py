from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User
from flask_login import login_required, current_user
from ..import db

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    welcome_message = 'Welcome to the Home!'

    return render_template('index.html', welcome_message = welcome_message )

@main.route('/user/<uname>')
def profile(uname):
    user = user.query.filter_by(username = uname).first()

    if user in None:
        abort(404)
    return render_template("profile/profile.html", user = user)
