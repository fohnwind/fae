__author__ = 'fohnwind'

from flask import Flask,render_template
from views.homepage import homepage
from views.auth import auth
from views.user import user
from views.project import project
from extensions import *

def create_app(config=None):
    """Create the app."""

    app = Flask(__name__)

    app.config.from_object('fae.configs.default.DefaultConfig')
    app.config.from_object(config)
    configure_blueprint(app)
    configure_extensions(app)

    return app


def configure_blueprint(app):
    app.register_blueprint(homepage)
    app.register_blueprint(auth, url_prefix=app.config["AUTH_URL_PREFIX"])
    app.register_blueprint(user, url_prefix=app.config["USER_URL_PREFIX"])
    app.register_blueprint(project, url_prefix=app.config["PROJECT_URL_PREFIX"])


def configure_extensions(app):
    db.init_app(app)

    login_manager.login_view = app.config["LOGIN_VIEW"]
    login_manager.init_app(app)

    redis_store.init_app(app)
    pass

