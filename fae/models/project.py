__author__ = 'fohnwind'

from fae.extensions import db
from datetime import datetime
from sh import cd, mkdir
class Project(db.Model):
    __tablename__ = 'project'

    pid = db.Column(db.Integer(), primary_key=True, nullable=False)
    pname = db.Column(db.String(40), nullable=False)
    create_at = db.Column(db.DateTime, default=datetime.now())
    type = db.Column(db.String(40), nullable=False)
    intro = db.Column(db.Text)
    owner = db.Column(db.Integer(), unique=True, nullable=False)
	
    def create_location():
	    cd("/home/fohnwind/files")
	    path = "\"%s/%s\"" % (self.owner,self.pname) 
	    mkdir(path)
	
    def save(self):
        db.session.add(self)
        db.session.commit()
