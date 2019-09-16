#!/usr/bin/env python

<<<<<<< HEAD
=======
from __future__ import absolute_import
>>>>>>> cutter/master
from setuptools import setup, find_packages
import json

if __name__ == '__main__':
    # Provide static information in setup.json
    # such that it can be discovered automatically
    with open('setup.json', 'r') as info:
        kwargs = json.load(info)
    setup(
        packages=find_packages(),
<<<<<<< HEAD
=======
        # this doesn't work when placed in setup.json (something to do with str type)
        package_data={
            "": ["*"],
            # TODO be more specific with package data (but the line below isn't working)
            # "tests.input_files": ["*"],
        },
>>>>>>> cutter/master
        long_description=open('README.md').read(),
        long_description_content_type='text/markdown',
        **kwargs)
