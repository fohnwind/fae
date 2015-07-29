__author__ = 'fohnwind'

from flask import Flask,render_template
from views.homepage import homepage
from views.auth import auth
from views.user import user
from views.container import container

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
    app.register_blueprint(container, url_prefix=app.config["CONTAINER_URL_PREFIX"])


def configure_extensions(app):
    pass