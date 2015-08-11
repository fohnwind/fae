__author__ = 'fohnwind'

import os, platform
from mako.template import Template
from fae.configs.default import DefaultConfig


class Ngconf(object):

    def save(self):
        if self.name and self.ip:
            os.chdir('/home/fohnwind/ng/conf/')
            filename = self.name + "." + DefaultConfig.SITE_NAME + ".conf"
            fp = open(filename, 'w')
            conf = Template(filename="ngconf.default").render(ip=self.ip, name=self.name)
            print >> fp, conf
            fp.close()

    def reload(self):
        os.system("nginx -s reload")

