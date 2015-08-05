__author__ = 'fohnwind'

from fae.extensions import db
from datetime import datetime

class Project(db.Model):
    __tablename__ = 'project'

    pid = db.Column(db.Integer(), primary_key=True, nullable=False)
    pname = db.Column(db.String(40), nullable=False)
    container_ip = db.Column(db.String(40), nullable=False, default="172.17.0.1")
    create_at = db.Column(db.DateTime, default=datetime.now())
    type = db.Column(db.String(40), nullable=False)
    intro = db.Column(db.Text)
    owner = db.Column(db.Integer(), unique=True, nullable=False)


    pass