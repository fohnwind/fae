__author__ = 'fohnwind'


from flask import Blueprint,render_template
from fae.models.user import User
from fae.models.project import Project
from flask_login import login_required, current_user

user = Blueprint("user", __name__)


@user.route("/index")
@login_required
def index():
    projects = []
    tmp = Project.query.filter(Project.owner == current_user.id)
    for i in tmp:
        projects.append(i)

    return render_template("user/index.html", projects=projects)
    #pass


# @user.route("/<username>")
# @user.route("/profile/<username>")
@user.route("/profile/<username>")
@login_required
def profile(username):
    return "lalal" + username



@user.route("/project/<pname>")
@login_required
def project_item(pname):
    pass
