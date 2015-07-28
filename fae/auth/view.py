__author__ = 'fohnwind'

from flask import Blueprint, flash, redirect, url_for, request, current_app, render_template
from flask_login import (current_user, login_user, login_required,
                         logout_user, confirm_login, login_fresh)

from flaskbb.auth.forms import (LoginForm, ReauthForm, ForgotPasswordForm,
                                ResetPasswordForm)
from flaskbb.user.models import User

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    """
    Logs the user in
    """

    if current_user is not None and current_user.is_authenticated():
        return redirect(url_for("user.profile"))

    form = LoginForm(request.form)
    if form.validate_on_submit():
        user, authenticated = User.authenticate(form.login.data,
                                                form.password.data)

        if user and authenticated:
            login_user(user, remember=form.remember_me.data)
            return redirect(request.args.get("next") or
                            url_for("forum.index"))

        flash(_("Wrong Username or Password."), "danger")
    return render_template("auth/login.html", form=form)

