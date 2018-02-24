# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from os.path import dirname, join


class Reveal:
    def __init__(self, lines, theme):
        lines = map(lambda l: '        ' + l if l.strip() else '\n', lines)
        self.html = open(join(dirname(__file__), 'template.html'), 'rb').read().decode().replace(
            '---theme---', theme).replace('---section---', '\n{}'.format(''.join(lines)))

    def generate(self, filename, title):
        open(filename, 'wb').write(self.html.replace('---title---', title).encode())
