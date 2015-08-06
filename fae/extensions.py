__author__ = 'fohnwind'

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_redis import FlaskRedis
from flask_babelex import Babel
#import docker

db = SQLAlchemy()

redis_store = FlaskRedis()

login_manager = LoginManager()

babel = Babel()
#docker_manager = docker.Client(base_url="unix://var/run/docker.sock")