from __future__ import absolute_import

#celery config is in a non-standard location
import os
os.environ['CELERY_CONFIG_MODULE'] = 'processes.celeryconfig'

# # This will make sure the app is always imported when
# # Django starts so that shared_task will use this app.
from .celery import app as celery_app
