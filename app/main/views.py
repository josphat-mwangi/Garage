from flask import render_template,request,redirect,url_for
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
