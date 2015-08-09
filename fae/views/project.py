__author__ = 'fohnwind'


from flask import Blueprint, render_template, request, redirect
from flask_login import login_required, current_user, login_user
from fae.configs.default import DefaultConfig
#from fae.extensions import docker_manager
from fae.models.project import Project

project = Blueprint("project", __name__)


@project.route("/<name>")
#@login_required
def project_info(name):
    #return docker_manager.containers()
    return current_user
    # projects = Project.query.filter_by(owner == current_user)
    # return "pname"


@project.route('/add', methods=['POST'])
def add_project():
    return "add"


@project.route('/delete', methods=['POST', 'DELETE'])
def delete_project():
    return "delete"


@project.route('/update', methods=['POST', 'UPDATE'])
def update_project():
    return "update"


@project.route('/<pname>/upload', methods=['GET', 'POST'])
def upload_code():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_file(file.filename)
            filepath = os.path.join(DefaultConfig['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            return filepath

    return render_template("project/upload.html")