from .base import *

SECRET_KEY = config('SECRET_KEY', default='InTheNameOfAllahWhoIsMostGracious&Merciful', cast=str)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

try:
    from .local import *
except ImportError:
    pass