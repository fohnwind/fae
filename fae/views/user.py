__author__ = 'fohnwind'


from flask import Blueprint,render_template
from fae.models.user import User
from flask_login import login_required

user = Blueprint("user", __name__)


@user.route("/index")
#@login_required
def index():
    return "user index"
    #pass


# @user.route("/<username>")
# @user.route("/profile/<username>")
@login_required
@user.route("/profile/<username>")
def profile(username):
    return "lalal" + username



@user.route("/project/<pname>")
@login_required
def project_item(pname):
    pass