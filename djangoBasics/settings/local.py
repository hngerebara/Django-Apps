from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='rs*mnbdy34f$2ppj71wy#!@b3o^=2x5xhcf_gxoyf1v1!*e3g!')

DEBUG = env.bool('DJANGO_DEBUG', True)