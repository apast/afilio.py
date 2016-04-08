#!/usr/bin/env python

from setuptools import setup

setup(name='Afilio API Client',
            version='0.1',
            description='Afilio API Client & Bindings',
            author='Andre Pastore',
            author_email='andrepgs@gmail.com',
            url='https://github.com/apast/afilio.py',
            download_url='https://github.com/apast/afilio.py/tarball/0.1',
            packages=['afilioapi'],
            package_dir= {'': 'src/main/py/'}
           )
