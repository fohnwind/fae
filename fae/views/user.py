__author__ = 'fohnwind'


from flask import Blueprint,render_template
from fae.models.user import User
from flask_login import login_required

user = Blueprint("user", __name__)


@user.route("/")
@user.route("/index")
@user.route("/project")
@login_required
def project_list():
    pass


@user.route("/<username>")
@user.route("/profile/<username>")
@login_required
def profile(username):
    pass



@user.route("/project/<pname>")
@login_required
def project_item(pname):
    pass