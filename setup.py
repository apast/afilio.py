#!/usr/bin/env python

from setuptools import setup

setup(name='Afilio API Client',
            version='0.1',
            description='Afilio API Client & Bindings',
            author='Andre Pastore',
            author_email='andrepgs@gmail.com',
            url='https://www.afilio.com.br',
            packages=['afilioapi'],
            package_dir= {'': 'src/main/py/'}
           )
