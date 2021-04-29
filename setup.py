# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='conda_template',
    version='0.1.0',
    description='conda and pip project template',
    long_description=readme,
    author='Dauloudet Olivier',
    url='https://github.com/Smeaol22/conda_template',
    license=license,
    packages=find_packages(exclude=('tests', 'docs', 'example', 'conda'))
)
