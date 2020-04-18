"""
WSGI config for typeidea_sys project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# 因为settings.py文件被拆分了，这一行替换为下面两行
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'typeidea_sys.settings')
profile = os.environ.get('TYPEIDEA_PROFILE', 'develop')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'typeidea_sys.settings.%s' % profile)

application = get_wsgi_application()
