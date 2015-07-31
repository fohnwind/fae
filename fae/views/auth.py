__author__ = 'fohnwind'

from flask import Blueprint,render_template, redirect, url_for ,request, flash
from flask_login import (current_user, login_user, login_required,
                         logout_user, confirm_login, login_fresh)
from fae.forms.auth import LoginForm
from fae.models.user import User


auth = Blueprint("auth", __name__)


@auth.route("/login",methods=["GET","POST"])
def login():
    if current_user is not None and current_user.is_authenticated():
        return redirect(url_for("user.profile"))

    form = LoginForm(request.form)
    if form.validate_on_submit():
        user, authenticated = User.authenticate(form.login.data,
                                                form.password.data)
        if user and authenticated:
            login_user(user, remember=form.remember_me.data)
            return redirect(request.args.get("next") or
                            url_for("user.index"))

        flash(_("wrong Username of Password."), "danger")
    fae_config = {'PROJECT_TITLE':"Auth", "PROJECT_SUBTITLE":"login"}
    return render_template("auth/login.html", form=form,fae_config=fae_config, page_title="FAE")


@auth.route("/oauth", methods=["GET", "POST"])
def oauth():
    return "oauth"


@auth.route("/logout", methods=["GET", "POST"])
def logout():
    logout_user()
    flash("Logged out", "success")
    return redirect(url_for("homepage.index"))


@auth.route("/register", methods=["GET", "POST"])
def register():
    pass


