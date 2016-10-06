#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import, print_function

from setuptools import find_packages, setup

setup(
    name="blog",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "twisted",
    ],
    entry_points={
        'console_scripts': [
            'blog = blog.__main__:main',
        ]
    },
)
