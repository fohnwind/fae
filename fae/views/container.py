# coding=utf-8
__author__ = 'fohnwind'


from flask import ( Blueprint, render_template, request, redirect, url_for,
                        jsonify )
from flask_login import login_required, current_user, login_user
from fae.configs.default import DefaultConfig
from werkzeug.utils import secure_filename
from fae.forms.project import CreateProjectForm, UpdateProjectForm
from fae.models.project import Project
from fae.models.container import Container
from fae.utils.ng import Ngconf
from sh import mv, cp
import os


container = Blueprint("container", __name__)

@container.route("/")
def index():
    projects = []
    tmp = Project.query.filter(Project.owner==current_user.id)
    for i in tmp:
        projects.append(i)

    #print projects
    return render_template("project/index.html",projects=projects)


@container.route("/<name>")
def container_info(name):
    project_item = []
    container_items = []

    tmp = Project.query.filter(Project.pname==name)

    if not tmp:
        abort(404)
    
    project_item = tmp[0]

    tmp_containers = Container.query.filter(Container.relation == tmp[0].pid)
    for i in tmp_containers:
        container_items.append(i)

    return render_template("project/info.html", project=project_item, containers=container_items)
    #return "pname"


@container.route('/add', methods=['GET','POST'])
def add_container():
    return render_template("project/add.html", form=project_form)

@container.route('/delete', methods=['POST', 'DELETE'])
def delete_project():
    if not session.get("id"):
        return jsonify("")
    return "delete"


@container.route('/update', methods=['POST', 'UPDATE'])
def update_project():
    return "update"


