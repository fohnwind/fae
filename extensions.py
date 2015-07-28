from flask-redis import redis
from flask-SqlAlchemy import SQLAlchemy
from flask-login import LoginManager

db = SQLAlchemy()

login_manager = LoginManager()
