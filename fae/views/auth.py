__author__ = 'fohnwind'

from flask import Blueprint,render_template, redirect, url_for ,request, flash
from flask_login import (current_user, login_user, login_required,
                         logout_user, confirm_login, login_fresh)


auth = Blueprint("auth", __name__)


@auth.route("/login",methods=["GET","POST"])
def login():
    return "login"
    # if current_user is not None and current_user.is_authenticated():
    #     return redirect(url_for("user.profile"))
    #
    # form = LoginForm(request.form)

@auth.route("/oauth", methods=["GET", "POST"])
def oauth():
    return "oauth"


@auth.route("/logout", methods=["GET", "POST"])
def logout():
    logout_user()
    flash(("Logged out"), "success")
    return redirect(url_for("homepage.index"))


@auth.route("/register", methods=["GET", "POST"])
def register():
    pass


