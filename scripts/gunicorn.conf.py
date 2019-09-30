# file gunicorn.conf.py
# coding=utf-8
# Reference: https://github.com/benoitc/gunicorn/blob/master/examples/example_config.py
import os

_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..'))

timeout = 30 * 60 # 3 minutes
keepalive = 24 * 60 * 60 # 1 day

capture_output = True