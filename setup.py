# -*- coding: UTF-8 -*-

from os.path import dirname
import sys

import setuptools
from distutils.core import setup

# http://stackoverflow.com/a/7071358/735926
import re
VERSIONFILE='term2048-AI/__init__.py'
verstrline = open(VERSIONFILE, 'rt').read()
VSRE = r'^__version__\s+=\s+[\'"]([^\'"]+)[\'"]'
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % VERSIONFILE)

setup(
    name='term2048-AI',
    version=verstr,
    author='Nicola Pezzotti',
    author_email='nicola.pezzotti@gmail.com',
    packages=['term2048-AI'],
    url='https://github.com/Nicola17/term2048-AI',
    license=open('LICENSE', 'r').read(),
    description='2048 in your terminal with an Artificial Intelligence',
    long_description=open('README.rst', 'r').read(),
    install_requires=[
        'colorama >= 0.2.7',
    ],
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ],
    entry_points={
        'console_scripts':[
            'term2048-AI = term2048.ui:start_game'
        ]
    },
)
