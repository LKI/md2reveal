#!/usr/bin/python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='md2reveal',
    version='1.1.3',
    author='Lirian Su',
    author_email='liriansu@gmail.com',
    url='https://github.com/LKI/md2reveal',
    license='WTFPL',
    description='Converting markdown to reveal.js html page',
    long_description=open('README.rst').read(),
    entry_points={
        'console_scripts': ['md2reveal = md2reveal.cmdline:execute']
    },
    packages=['md2reveal'],
    include_package_data=True,
    package_data={'md2reveal': ['template.html']}
)
