#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    # 因为settings.py文件被拆分了，这一行替换为下面两行
    # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'typeidea_sys.settings')
    profile = os.environ.get('TYPEIDEA_PROFILE', 'develop')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'typeidea_sys.settings.%s' % profile)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
