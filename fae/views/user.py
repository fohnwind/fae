__author__ = 'fohnwind'


from flask import Blueprint,render_template
from fae.models.user import User

user = Blueprint("user", __name__)


@user.route("/<username>")
@user.route("/profile/<username>")
def profile(username):
    pass
