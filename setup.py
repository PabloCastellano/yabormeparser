#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
import yabormeparser

long_description = ""
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except:
    long_description = open('README.md').read()

version = yabormeparser.__version__

setup(
    name='yabormeparser',
    version=version,
    packages=['yabormeparser', 'yabormeparser.annoucement'],
    entry_points={
        'console_scripts': ['yabormeparser1 = yabormeparser.parser:main',
                            'yabormeparser2 = yabormeparser.parser2:main']},
    install_requires=['pdfminer==20140328',
                      'ply==3.4'],
    # metadata for upload to PyPI
    author="Daniel A. Dorado",
    author_email="daniel@funeslab.com",
    description=("A parser than transform PDF "
                 "BORME files into a BORME JSON files."),
    license='GPLv3+',
    keywords=['BORME', 'transparency', 'opendata', 'Spain',
              'Registro mercantil', 'Boletín Oficial del Registro Mercantil'],
    url='https://github.com/funeslab/yabormeparser/',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: Spanish',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Text Processing'

    ],
    long_description=long_description
)
