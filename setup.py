#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
from cmsplugin_date import __version__

setup(
    name='cmsplugin-date',
    version=__version__,
    description='Date plugin for django CMS',
    author='Florian Schweikert',
    author_email='cmsplugin_date',
    url='https://github.com/kelvan/cmsplugin_date',
    packages=['cmsplugin_date', 'cmsplugin_date.migrations'],
    license='LICENSE',
    platforms=['OS Independent'],
    long_description=open('README.md').read(),
    include_package_data=True,
    zip_safe=False
)
