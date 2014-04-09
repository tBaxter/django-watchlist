# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

#with open('docs/requirements.txt') as f:
#    required = f.read().splitlines()

setup(
    name='django-watchlist',
    version='0.1',
    author=u'Tim Baxter',
    author_email='mail.baxter@gmail.com',
    url='http://github.com/tBaxter/django-watchlist',
    license='LICENSE',
    description='Stupid simple django watch and favorite',
    long_description=open('README.md').read(),
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
)
