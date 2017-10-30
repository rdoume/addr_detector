#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
'click',
'Sphinx',
'coverage',
'awscli',
'flake8',
'python-dotenv>=0.5.1',
'numpy==1.13.3',
'pandas==0.20.1',
'scipy==0.19.0',
'postal==1.0',
'scikit_learn==0.19.0',
'pyfasttext'

]

setup_requirements = [
    # TODO(rdoume): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='addr_detector',
    version='0.1.0',
    description="Python address detector ",
    long_description=readme + '\n\n' + history,
    author="Qwant",
    author_email='robin@qwantresearch.com',
    url='https://github.com/rdoume/addr_detector',
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['*.ftz']},
    data_files=[('model',['data/model.ftz'])],
    install_requires=requirements,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='addr_detector',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',

    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
