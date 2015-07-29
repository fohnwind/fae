__author__ = 'fohnwind'


from flask import Blueprint, render_template
from flask_login import login_required

container = Blueprint("container", __name__)


@container.route("/<c_name>")
def container_info(c_name):
    return "cname"