#!/usr/bin/env python
import os
import sys
from decouple import config

if __name__ == "__main__":
    if not config('DEBUG', cast=bool):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aaa.settings.production")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aaa.settings.dev")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
