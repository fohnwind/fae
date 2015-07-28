
from flask import Blueprint, flash, request, render_template,
#from models import User
user = Blueprint("user", __name__)

@user.route("/<username>")
def profile(username):
    return render_template("user/profile.html", username=username)

@user.route("/<username>/<appname>")
def application(username, appname):
    return render_template("user/app.html", username=username, appname=appname)