__author__ = 'fohnwind'

import os, platform
from mako.template import Template

class Ngconf(object):

    def __init__(self):
        self.file_path = '/home/fohnwind/ng/conf/'

    def save(self):
        if self.name and self.ip:
            os.chdir(self.file_path)
            filename = self.name + ".conf"
            fp = open(filename, 'w')

            print >> fp, Template("ngconf.default").render(ip=self.ip, name=self.name)

            fp.close()

