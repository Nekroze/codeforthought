#!/usr/bin/env python
from distutils.core import setup
import sys


if 'register' in sys.argv:
    print('This project should never be registered on pypi!')
    sys.exit(1)


setup(name='Code for Thought',
      version='0.1.0',
      description='Code for Thought is designed to guide your first steps into programming.',
      author='Taylor "Nekroze" Lawson',
      author_email='nekroze@eturnilnetwork.com',
      url='http://code-for-thought.rtfd.org',
    )
