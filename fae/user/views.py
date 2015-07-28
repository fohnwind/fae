from flask import Blueprint, flash, request, render_template
#from models import User
user = Blueprint("user", __name__)

@user.route("/user/<username>")
def profile(username):
    return render_template("user/profile.html", username=username)


