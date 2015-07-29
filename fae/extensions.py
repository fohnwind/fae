__author__ = 'fohnwind'

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_redis import FlaskRedis

db = SQLAlchemy()

redis_store = FlaskRedis()

login_manager = LoginManager()


