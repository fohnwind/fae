# coding=utf-8
__author__ = 'fohnwind'


from flask import Blueprint, render_template, request, redirect
from flask_login import login_required, current_user, login_user
from fae.configs.default import DefaultConfig
from werkzeug.utils import secure_filename
from fae.forms.project import CreateProjectForm, UpdateProjectForm
from fae.models.project import Project
import os
from fae.utils.ng import Ngconf

project = Blueprint("project", __name__)


@project.route("/")
@login_required
def index():
    # return ""
    return ""


@project.route("/<name>")
@login_required
def project_info(name):
    # projects = Project.query.filter_by(Project.owner == current_user)
    # return render_template("project/info.html", projects=projects)
    return "pname"


@project.route('/add', methods=['GET','POST'])
def add_project():
    if request.method is 'POST':

        project_form = CreateProjectForm(request.form)

        if project_form.validate_on_submit():
            pass
            """

             init contianer
             ng conf映射
            """
        return "test"
    ng = Ngconf()
    ng.name = "testapp"
    ng.ip = "192.168.107.1"
    ng.save()
    return "success"
    #return render_template("project/add.html")


@project.route('/delete', methods=['POST', 'DELETE'])
def delete_project():
    return "delete"


@project.route('/update', methods=['POST', 'UPDATE'])
def update_project():
    return "update"


@project.route('/<pname>/upload', methods=['GET', 'POST'])
def upload_code():
    if request.method is 'POST':
        update_file = request.files['file']
        if update_file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(DefaultConfig['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            return filepath

    return render_template("project/upload.html")