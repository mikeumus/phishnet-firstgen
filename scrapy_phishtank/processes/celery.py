from __future__ import absolute_import

import os

from celery import Celery

# http://docs.celeryproject.org/en/master/userguide/application.html?highlight=config_from_object#example-2-using-a-configuration-module
from processes import celeryconfig

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scrapy_phishtank.settings')

from django.conf import settings

app = Celery('processes') # Celery app name

# Using a string here means the worker will not have to
# pickle the object when using Windows.
# app.config_from_object('celeryconfig')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


# if __name__ == '__main__':
#     app.start()
    
# a common practice for reusable apps is to define all tasks in a separate tasks.py module,
# and Celery does have a way to autodiscover these modules.
# With the line above Celery will automatically discover tasks in reusable apps if you follow the tasks.py convention
#app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
  
# debug_task example is a task that dumps its own request information.
# This is using the new bind=True task option introduced in Celery 3.1
# to easily refer to the current task instance.  
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))