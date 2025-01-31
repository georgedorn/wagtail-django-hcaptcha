from __future__ import absolute_import, unicode_literals

import os

from setuptools import find_packages, setup

from wagtailcaptcha import __version__

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# Testing dependencies
testing_extras = [
    # Required for running the tests
    'tox>=2.3.1,<2.4',

    # For coverage and PEP8 linting
    'coverage>=4.1.0,<4.2',
    'flake8>=3.2.0,<3.3',
    'isort==4.2.5',

    # For test site
    'wagtail==2.0',
]

# Documentation dependencies
documentation_extras = [

]

setup(
    name='wagtail-django-hcaptcha',
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='A simple hCaptcha field for Wagtail form pages.',
    long_description=README,
    url='http://github.com/georgedorn/wagtail-django-hcaptcha',
    author='Springload, Timothy Bautista (acarasimon96), George Dorn (georgedorn)',
    author_email='hello@springload.co.nz',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=['django-hcaptcha'],
    extras_require={
        'testing': testing_extras,
        'docs': documentation_extras,
    },
    zip_safe=False
)
