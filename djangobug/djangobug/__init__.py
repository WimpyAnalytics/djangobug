from __future__ import absolute_import  # So that our celery.py module will not clash with the library

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app