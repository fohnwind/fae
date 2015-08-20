__author__ = 'fohnwind'

from fae.extensions import db, docker_manager
import docker

class Container(db.Model):

    __tablename__ = 'container'

    cid = db.Column(db.Integer(), primary_key=True)
    cname = db.Column(db.String(40), nullable=False)
    ip = db.Column(db.String(40), nullable=False, default="172.17.0.0")
    image = db.Column(db.String(40), nullable=False)
    relation = db.Column(db.Integer(), unique=True, nullable=False)

    def create(self, ):
        pass

    def get_ip(self):
        return self.ip

    def get_relation(self):
        return self.relation

    def __init__(self, *args, **kwargs):
        super(Container, self).__init__(*args, **kwargs)

    def startup(self,filepath):
        f_binds = "%s:/usr/share/nginx/html" % filepath
        host_config = docker.utils.create_host_config(binds=[f_binds])
        container = docker_manager.create_container(image=self.image, volumes="/usr/share/nginx/html",host_config=host_config)
        # TODO change file volumns position
        docker_manager.start(container=container.get('Id'))
        exec_item = docker_manager.exec_create(container=container.get("Id"), cmd="/root/getip.sh")
        self.ip = docker_manager.exec_start(exec_id=exec_item.get('Id'))

    def save(self):
        db.session.save(self)
        db.session.commit()

