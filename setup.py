#!/usr/bin/env python
import os
from setuptools import setup, find_packages

setup(
    name='{{package}}',
    version='0.1',
    description='{{description}}',
    author='{{author}}',
    author_email='{{email}}',
    packages=find_packages(),
    install_requires=open(
        os.path.join(
            os.path.dirname(__file__),
            "requirements.txt"
        ),
        'r'
    ).readlines()
)
