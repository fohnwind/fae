__author__ = 'fohnwind'

from fae.extensions import db
from datetime import datetime
from sh import cd, mkdir
class Project(db.Model):
    __tablename__ = 'project'

    pid = db.Column(db.Integer(), primary_key=True, nullable=False)
    pname = db.Column(db.String(40), nullable=False)
    create_at = db.Column(db.DateTime, default=datetime.now())
    ptype = db.Column(db.String(40), nullable=False)
    intro = db.Column(db.Text)
    owner = db.Column(db.Integer(), unique=True, nullable=False)
	
    def get_pid(self):
        return self.pid

    def create_location():
	    cd("/home/fohnwind/files")
	    path = "\"%d/%s\"" % (self.owner,self.pname) 
	    mkdir(path)
	
    def save(self):
        print self.__dict__
        db.session.add(self)
        db.session.commit()
        return self
