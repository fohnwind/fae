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

    #def create(self2):
    #    pass

    def get_ip(self):
        return self.ip

    def get_relation(self):
        return self.relation

    def __init__(self, *args, **kwargs):
        super(Container, self).__init__(*args, **kwargs)

    def startup(self,filepath):
        f_binds = "%s:/usr/share/nginx/html" % filepath
        host_config = docker.utils.create_host_config(binds=[f_binds])

        #disable container network
        container = docker_manager.create_container(image=self.image, volumes="/usr/share/nginx/html",host_config=host_config, network_disables=True)
        # TODO change file volumns position

        tmp = docker_manager.containers(latest=True)
        self.cname = tmp[0]['Names']
        docker_manager.start(container=container.get('Id'))
        #exec_item = docker_manager.exec_create(container=container.get("Id"), cmd="/root/getip.sh")
        #self.ip = docker_manager.exec_start(exec_id=exec_item.get("Id"))


    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def linkup(self):
        #TODO
        #find ip in table
        #else get a new one
        #linkup with the netdevice
