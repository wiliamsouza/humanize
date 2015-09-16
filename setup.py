#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Setup script for humanize."""

from setuptools import setup, find_packages
import io

version = '0.5.4'

# some trove classifiers:


setup(
    name='tg-humanize',
    version=version,
    description="python humanize utilities",
    long_description=io.open('README.rst', 'r', encoding="UTF-8").read(),
    # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python',
    ],
    keywords='humanize time size',
    author='Jason Moiron',
    author_email='jmoiron@jmoiron.net',

    url='http://github.com/jmoiron/humanize',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    test_suite="nose.collector",
    tests_require=['mock', 'nose'],
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,
)
