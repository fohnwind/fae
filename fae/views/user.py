__author__ = 'fohnwind'


from flask import Blueprint, render_template, session, jsonify
from fae.models.user import User
from fae.models.project import Project
#from fae.models.container import Container
from fae.utils.login import login_r

user = Blueprint("user", __name__)


@user.route("/")
@user.route("/index")
def index():
    if not session.get("id"):
        return redirect(url_for('homepage.index'))
    ptmp = Project.query.filter(Project.owner == '1')
    #ctmp = Container.query.filter(Project.owner == '1')

    pcount = len([i for i in ptmp])
    #ccount = len([i for i in ctmp])
    ccount = 0
    return render_template("user/index.html", project_count = pcount, container_count = ccount)


@user.route("/profile/<username>")
def profile(username):
    return "lalal" + username



@user.route("/project/<pname>")
def project_item(pname):
    return jsonify(msg = "init")


@user.route("/setting")
@login_r
def setting():
    return jsonify(msg = "init")
