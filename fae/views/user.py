__author__ = 'fohnwind'


from flask import Blueprint, render_template, session, jsonify
from fae.models.user import User
from fae.models.project import Project
from fae.models.container import Container
from fae.utils.login import login_r

user = Blueprint("user", __name__)


@user.route("/")
@user.route("/index")
@login_r
def index():

    uname = session.get('id')
    user = User.query.filter(User.username == uname).first()
    if not user:
        newU = User(username = uname)
        user = newU.save()

    uid = user.getid()
    print uid
    ptmp = Project.query.filter(Project.owner == uid)
    ctmp = Container.query.filter(Container.relation == uid)

    pcount = len([i for i in ptmp])
    ccount = len([i for i in ctmp])
    #ccount = 0
    return render_template("user/index.html", project_count = pcount, container_count = ccount)


@user.route("/profile/<username>")
@login_r
def profile(username):
    return "lalal" + username



@user.route("/project/<pname>")
def project_item(pname):
    return jsonify(msg = "init")


@user.route("/setting")
@login_r
def setting():
    return jsonify(msg = "init")
