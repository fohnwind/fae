__author__ = 'fohnwind'

import os, platform
from mako.template import Template
from fae.configs.default import DefaultConfig
from sh import nginx

class Ngconf(object):

    def __init__(self, name, ip):
        super(Ngconf, self).__init__()
        self.name = name
        self.ip = ip

    def save(self):
        if self.name and self.ip:
            os.chdir('/home/fohnwind/ng/conf/')
            filename = self.name + "." + DefaultConfig.SITE_NAME + ".conf"
            fp = open(filename, 'w')
            conf = Template(filename="ngconf.default").render(ip=self.ip, name=self.name)
            print >> fp, conf
            fp.close()

            nginx("-s","reload")

