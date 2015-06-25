from __future__ import absolute_import

# from processes.celery import app
from celery import shared_task

# Using the @shared_task decorator
# The tasks you write will probably live in reusable apps,
# and reusable apps cannot depend on the project itself, so you also cannot import your app instance directly.
# The @shared_task decorator lets you create tasks without having any concrete app instance:
# from celery import shared_task

@shared_task(name="shared_tasks.add")
def add(x, y):
    return x + y

# Task Names: http://docs.celeryproject.org/en/latest/userguide/tasks.html?highlight=task.name#names
# @app.task(name="tasks.add")
# def add(x, y):
#     return x + y