#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

import ascii_art


with open('README.rst') as f:
    long_description = f.read()


setup(
    name="ascii_art",
    version=ascii_art.__version__,
    description="Ascii art for python: chart, bar, histogram.",
    long_description=long_description,
    url="https://github.com/lord63/ascii_art",
    author="lord63",
    author_email="lord63.j@gmail.com",
    license="MIT",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords="ascii art chart bar histogram commandline cli",
    packages=['ascii_art'],
    include_package_data=True
)
