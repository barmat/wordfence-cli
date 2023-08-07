#!/usr/bin/env python3
from setuptools import setup, find_packages

from wordfence import __version__

with open('README.md', 'r') as file:
    long_description = file.read()

setup(
    name='wordfence',
    version=__version__,
    description='Command-line malware scanner powered by Wordfence',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/wordfence/wordfence-cli',
    author='Wordfence',
    author_email='devs@wordfence.com',
    maintainer='Wordfence',
    maintainer_email='devs@wordfence.com',
    license='GPL 2.0',
    license_files='LICENSE',
    entry_points={
        'console_scripts': [
            'wordfence = wordfence.cli.cli:main',
        ]
    },
    packages=find_packages(),
    install_requires=['regex']
)
