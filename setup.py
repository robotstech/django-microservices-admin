#!/usr/bin/env python
import sys
from io import open

from setuptools import find_packages, setup
from django_microservices_admin import VERSION

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 6)

UNSUPPORTED_VERSION_INFO = f'''
==========================
Unsupported Python version
==========================
This version of Django Microservices Admin requires Python {REQUIRED_PYTHON}, but you're trying
to install it on Python {CURRENT_PYTHON}.
This may be because you are using a version of pip that doesn't
understand the python_requires classifier. Make sure you
have pip >= 9.0 and setuptools >= 24.2, then try again:
    $ python -m pip install --upgrade pip setuptools
    $ python -m pip install django-microservices-admin
This will install the latest version of Django Microservices Admin which works on
your version of Python.
'''

# This check and everything above must remain compatible with Python 2.7.
if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write(UNSUPPORTED_VERSION_INFO)
    sys.exit(1)

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='django-microservices-admin',
    version=VERSION,
    url='https://github.com/robotstech/django-microservices-admin',
    description=(
        "Utilizing Django Admin to manage microservices data"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="Django, django-admin, microservices",
    license='MIT',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    install_requires=[
        'django>=3.2',
        'dj-database-url>=0.5.0',
    ],
    extras_require={
        'postgres': ['psycopg2-binary>=2.9.3'],
        'mysql': ['mysqlclient>=2.1.0'],
    },
    # See http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'License :: OSI Approved :: MIT No Attribution License (MIT-0)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
