# -*- coding: utf-8 -*-
"""
Application configuration
"""

import os

# get settings from environment, or credstash if running in AWS
env = os.environ

DEBUG = bool(env.get('DEBUG', True))

# XXX Don't change the following settings unless necessary

# Skips concatenation of bundles if True, which breaks everything
ASSETS_DEBUG = False

ASSETS_LOAD_PATH = [
    'app/static',
    'app/templates']
