#!/usr/bin/env python

import setuptools
from distutils.core import setup

LONG_DESCRIPTION = \
    '''
    pd2pout is a simple file conversion tool that converts ProteomeDiscoverer-files into pout-files (as produced by
    Percolator). This converter accompagnies the pout2prot-tool that can be used to perform protein grouping on
    pout-files. By using this utility, we enable the possibility for other researchers to start grouping proteins
    that are derived from a ProteomeDiscoverer-project.
    '''

setup(
    name='pd2pout',
    version='1.0.0',
    description='A file converter to convert ProteomeDiscoverer-files to pout-files (Percolator format).',
    long_description=LONG_DESCRIPTION,
    author='Pieter Verschaffelt',
    author_email='pieter.verschaffelt@ugent.be',
    packages=['pd2pout'],
    package_dir={'pd2pout': 'pd2pout'},
    entry_points={
        'console_scripts': ['pd2pout = pd2pout:main.main']
    }
)
