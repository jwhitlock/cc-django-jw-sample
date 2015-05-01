#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Packaging setup for cc-django-jw-sample."""

from sample import __version__ as version

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

def get_long_description(title):
    readme = open('README.rst').read()
    history = open('HISTORY.rst').read()

    body_tag = ".. Omit badges from docs"
    readme_body_start = readme.index(body_tag)
    assert readme_body_start
    readme_body = readme[readme_body_start + len(body_tag):]

    history_body = history.replace('.. :changelog:', '')
    bars = '=' * len(title)
    long_description = """
%(bars)s
%(title)s
%(bars)s
%(readme_body)s

%(history_body)s
""" % locals()
    return long_description

requirements = [
    'Django>=1.6',
]

test_requirements = [
    'dj_database_url',
    'django_nose',
    'django_extensions',
    'jingo',
]

setup(
    name='cc-django-jw-sample',
    version=version,
    description='Sample Project created from cookiecutter-django-jw',
    long_description=get_long_description('Sample Project created from cookiecutter-django-jw'),
    author='John Whitlock',
    author_email='john@factorialfive.com',
    url='https://github.com/jwhitlock/cc-django-jw-sample',
    packages=[
        'sample',
    ],
    package_dir={
        'sample': 'sample',
    },
    include_package_data=True,
    install_requires=requirements,
    license="MPL 2.0",
    zip_safe=False,
    keywords='cc-django-jw-sample',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='sample_site.runtests.runtests',
    tests_require=test_requirements
)

