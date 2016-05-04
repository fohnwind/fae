__author__ = 'fohnwind'

from fae.extensions import db
from fae.models.project import Project
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'user'

    uid = db.Column(db.Integer(), unique=True, primary_key=True)
    username = db.Column(db.String(40), nullable=False)
    # user_level = db.Column(db.Integer(), default=0)
    # project_count = db.Column(db.Integer(), default=0)

    # projects = db.relationship("project", backref='user', lazy='dynamic')

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    @property
    def levels(self):
        return self.get_levels()

    @property
    def project_count(self):
        return self.project_count

    def getid(self):
        return self.uid

    def all_project(self):
        return Project.query.filter_by(Project.owner == self.uid)

    def save(self):
        db.session.add(self)
        db.session.commit()

        return self
