
from flask import render_template,request,redirect,url_for, jsonify

from . import main
from ..models import User
from flask_login import login_required, current_user
from ..import db
import requests
from .key import key

search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
details_url = "https://maps.googleapis.com/maps/api/place/details/json"

@main.route("/", methods=["GET"])
@login_required
def retreive():
    return render_template('layout.html') 

@main.route("/sendRequest/<string:query>")
def results(query):
	search_payload = {"key":key, "query":query}
	search_req = requests.get(search_url, params=search_payload)
	search_json = search_req.json()

	place_id = search_json["results"][0]["place_id"]

	details_payload = {"key":key, "placeid":place_id}
	details_resp = requests.get(details_url, params=details_payload)
	details_json = details_resp.json()

	url = details_json["result"]["url"]
	return jsonify({'result' : url})

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    welcome_message = 'Welcome to Home!'

    return render_template('index.html', welcome_message = welcome_message )

@main.route('/user/<uname>')
def profile(uname):
    user = user.query.filter_by(username = uname).first()

    if user in None:
        abort(404)
    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form)
