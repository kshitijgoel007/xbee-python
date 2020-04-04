#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

setup_args = generate_distutils_setup(
    packages=['xbee_python'],
    package_dir={'': 'digi'}
)

setup(**setup_args)
