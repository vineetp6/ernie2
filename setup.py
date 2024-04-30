#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

import ernie

setup(
    name='ernie',
    version=ernie.__version__,
    description=(
        'An Accessible Python Library for State-of-the-art '
        'Natural Language Processing. Built with HuggingFace\'s Transformers.'
    ),
    url='https://github.com/labteral/ernie',
    author='Rodrigo Martínez Castaño',
    author_email='dev@brunneis.com',
    license='Apache License (Version 2.0)',
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.6",
    install_requires=[
        'tf-keras',
        'transformers',
        'scikit-learn',
        'pandas',
        'py-cpuinfo',
    ])
