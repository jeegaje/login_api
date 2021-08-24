import os

base_dir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    JSON_SORT_KEYS = False
    JWT_SECRET_KEY = str(os.environ.get('JWT_SECRET'))