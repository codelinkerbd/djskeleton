from .base import *

SECRET_KEY = 'django-insecure-md#&dh69a0s15i^$has917&__#s#_tnn&1sbv!9!%c8c(@j6b9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

try:
    from .local import *
except ImportError:
    pass