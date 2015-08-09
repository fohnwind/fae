__author__ = 'fohnwind'

from fae.extensions import db
from fae.models.project import Project
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer(), unique=True, primary_key=True)
    username = db.Column(db.String(40), nullable=False)
    sina_uid = db.Column(db.Integer(), unique=True)
    _password = db.Column('password', db.String(128), nullable=False)
    # user_level = db.Column(db.Integer(), default=0)
    # project_count = db.Column(db.Integer(), default=0)

    # projects = db.relationship("project", backref='user', lazy='dynamic')

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    # @property
    # def levels(self):
    #     return self.get_levels()
    #
    # @property
    # def project_count(self):
    #     return self.project_count
    #
    # def _get_password(self):
    #     return self._password
    #
    # def _set_password(self, password):
    #     self._password = generate_password_hash(password)

    def check_password(self, password):

        if self._password is None:
            return False

        if password is None:
            return False

        return True
        # return check_password_hash(self._password, password)

    @classmethod
    def authenticate(cls, login, password):
        print "tmp"
        user = cls.query.filter(db.or_(User.username == login,
                                       User.sina_uid == login)).first()

        print type(user)
        if user:
            authenticated = user.check_password(password)
        else:
            authenticated = False

        return user, authenticated

    # def all_project(self):
    #     return Project.query.filter_by(Project.owner == self.id)
    #
    # def save(self):
    #     db.session.add(self)
    #     db.session.commit()
    #
    #     return self
