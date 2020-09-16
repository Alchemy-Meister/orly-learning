#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2020 Alchemy-Meister
#
# SPDX-License-Identifier: GPL-3.0-or-later

from setuptools import setup, find_packages

install_requires = [
    'beautifulsoup4',
    'lxml',
    'requests >= 2.0'
]

tests_require = [
    'coverage',
    'responses',
    'pytest',
    'pytest-cov'
]

extras_require = {'tests': tests_require}

setup(
    name='orlylearning',
    version='0.1.0',
    url='https://github.com/Alchemy-Meister/orly-learning',
    author='Alchemy-Meister',
    license='GPLv3+',
    description="Unofficial O'Reilly Learning API for Python 3",
    keywords="O'Reilly, O'Reilly Learning, Safari, Unoficial API",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: '
        'GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3.8',
        'Intended Audience :: Developers',
        "Operating System :: OS Independent"
    ],
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require=extras_require
)
