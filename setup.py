#!/usr/bin/env python
# coding: utf-8
from setuptools import setup, find_packages
from tamsen import __author__, __version__, __license__
 
setup(
        name             = 'tamsen',
        version          = __version__,
        description      = 'Minimal Library for https://ambidata.io/',
        license          = __license__,
        author           = __author__,
        author_email     = 'msr.tmr+github@gmail.com',
        url              = 'https://github.com/gorakuru/tamsen',
        keywords         = 'https://ambidata.io/',
        packages         = find_packages(),
        install_requires = ['requests'],
        )