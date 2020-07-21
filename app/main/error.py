from flask import render_template
from views import views

@views.errorhandler(404)
def four_Ow_four(error):