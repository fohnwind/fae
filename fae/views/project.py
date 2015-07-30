__author__ = 'fohnwind'


from flask import Blueprint, render_template
from flask_login import login_required

project = Blueprint("project", __name__)


@project.route("/<name>")
def project_info(name):
    return "cname"


@project.route('/add', methods=['POST'])
def add_project():
    return "add"


@project.route('/delete', methods=['POST', 'DELETE'])
def delete_project():
    return "delete"


@project.route('/update', methods=['POST', 'UPDATE'])
def update_project():
    return "update"

