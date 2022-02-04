#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

import sys
from email.utils import parseaddr

kwargs = {}
if not hasattr(sys, 'pypy_version_info'):
    kwargs['install_requires'] = ['Pillow']

__version__ = '0.1.2'
__author__ = 'Jigar Varma <Jigarverma2002@gmail.com>'
__homepage__ = 'https://github.com/Jigarvarma2005/EmojiCaptcha'
    
author, author_email = parseaddr(__author__)

with open("requirements.txt", encoding="utf-8") as r:
    requires = [i.strip() for i in r]

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

setup(
    name='EmojiCaptcha',
    version=__version__,
    author=author,
    author_email=author_email,
    url=__homepage__,
    packages=find_packages(),
    description='A python3 library that generates Emoji CAPTCHAs.',
    long_description=readme,
    long_description_content_type="text/markdown",
    license='MIT',
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    keywords="telegram emoji library python captcha api",
    project_urls={
        "Tracker": f"{__homepage__}/issues",
        "Source": __homepage__,
    },
    python_requires="~=3.6",
    install_requires=requires
)
