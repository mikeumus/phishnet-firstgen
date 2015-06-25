# from __future__ import absolute_import

# # This will make sure the app is always imported when
# # Django starts so that shared_task will use this app.
# from .celery import app as celery_app

# celery config is in a non-standard location
# import os
# os.environ['CELERY_CONFIG_MODULE'] = 'processes.celeryconfig'