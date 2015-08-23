# coding=utf-8
__author__ = 'fohnwind'


from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user, login_user
from fae.configs.default import DefaultConfig
from werkzeug.utils import secure_filename
from fae.forms.project import CreateProjectForm, UpdateProjectForm
from fae.models.project import Project
from fae.models.container import Container
import os
from fae.utils.ng import Ngconf
from sh import mv, cp
project = Blueprint("project", __name__)


@project.route("/")
@login_required
def index():
    projects = []
    tmp = Project.query.filter(Project.owner==current_user.id)
    for i in tmp:
        projects.append(i)

    #print projects
    return render_template("project/index.html",projects=projects)


@project.route("/<name>")
@login_required
def project_info(name):
    # projects = Project.query.filter_by(Project.owner == current_user)
    # return render_template("project/info.html", projects=projects)
    return "pname"


@project.route('/add', methods=['GET','POST'])
def add_project():

    project_form = CreateProjectForm(request.form)

    if request.method == 'POST':
        print request.form.__dict__
        pname = request.form['pname']
        intro = request.form['intro']
        ptype =  request.form['ptype']
        file_url = request.form.get('fileurl','a')
        print ptype
        if 2 > 1:
            container = Container(image=ptype)
            filepath = "/home/fohnwind/files/%d/%s/" %(current_user.id, pname)
            if not os.path.exists(filepath):
                os.makedirs(filepath)
            if file_url != 'a':
                mv(file_url,filepath)
            else:
                cp("/home/fohnwind/files/fohnwind/index.html",filepath)

            container.startup(filepath=filepath)
            print str(container.ip) + "--------"

            ng = Ngconf(name=pname,ip=container.ip).save()
            project = project_form.save(current_user)
            container.relation = project.get_pid()
            container.save()
            return url_for("user.index")

        return "no"

    return render_template("project/add.html", form=project_form)

@project.route('/delete', methods=['POST', 'DELETE'])
def delete_project():
    return "delete"


@project.route('/update', methods=['POST', 'UPDATE'])
def update_project():
    return "update"


@project.route('/upload', methods=['GET', 'POST'])
def upload_code():
    if request.method == 'POST':
        upload_file = request.files['file']
        if upload_file:
            filename = secure_filename(upload_file.filename)
            filepath = os.path.join('/home/fohnwind/fae/html/uploads', filename)
            upload_file.save(filepath)
            return filepath
        return "no"
    return render_template("project/upload.html")
