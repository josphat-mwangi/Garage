from flask import render_template
from . import main

@main.errorhandler(404)
def four_ow_four(error):
    '''
    function to render the 404 error page

    '''

    render_template('fourOwfour.html'),404