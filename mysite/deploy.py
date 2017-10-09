"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
import os
import sys
from whitenoise.django import DjangoWhiteNoise
#whitenoise is following treehouse for PA

path = "/home/bezport/django_tut/mysite"
if path not in sys.path:
    sys.path.append(path)


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
