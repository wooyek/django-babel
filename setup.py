#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import codecs
from setuptools import setup, find_packages


def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()


setup(
    name='django2-babel',
    description='Utilities for using Babel in Django, without and upper Django version constraint.',
    long_description=read('README.rst') + u'\n\n' + read('CHANGELOG.rst'),
    version='0.6.3',
    license='BSD',
    author='Christopher Grebs',
    author_email='cg@webshox.org',
    maintainer='Thomas Grainger',
    maintainer_email='django-babel@graingert.co.uk',
    url='https://github.com/python-babel/django-babel/',
    packages=find_packages(exclude=('tests',)),
    install_requires=[
        'django>=1.4',
        'babel>=1.3',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Framework :: Django',
        'Framework :: Django :: 1.4',
        'Framework :: Django :: 1.5',
        'Framework :: Django :: 1.6',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    entry_points={
        'babel.extractors': [
            'django = django_babel.extract:extract_django',
        ]
    }
)
