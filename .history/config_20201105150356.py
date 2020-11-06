import os
basedir = os.path.abspath(os.path.dirname(__file))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
