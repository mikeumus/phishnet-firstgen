# http://docs.celeryproject.org/en/master/reference/celery.schedules.html#celery.schedules.crontab
#from __future__ import absolute_import
#from celery.schedules import crontab # http://docs.celeryproject.org/en/master/userguide/periodic-tasks.html#crontab-schedules

# http://docs.celeryproject.org/en/master/configuration.html#configuration
CELERY_TIMEZONE = 'US/Eastern'
CELERY_INCLUDE = 'processes.tasks'
CELERY_DISABLE_RATE_LIMITS = True # http://docs.celeryproject.org/en/master/userguide/tasks.html#disable-rate-limits-if-they-re-not-used


BROKER_URL = "localhost"
BROKER_BACKEND = "redis"
BROKER_USER = ""
BROKER_PASSWORD = ""
# BROKER_VHOST = "0"

REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_CONNECT_RETRY = True


# http://docs.celeryproject.org/en/latest/getting-started/brokers/redis.html#caveats
BROKER_TRANSPORT_OPTIONS = {
    'fanout_prefix': True,
    'visibility_timeout': 3600 # 1 hour for redis: http://docs.celeryproject.org/en/latest/getting-started/brokers/redis.html#visibility-timeout
} 

#: Only add pickle to this list if your broker is secured
#: from unwanted access (see userguide/security.html)
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
# CELERY_RESULT_BACKEND = 'redis'
CELERY_RESULT_BACKEND = "djcelery.backends.database:DatabaseBackend" #django-celery database result backend
# CELERY_RESULT_BACKEND='djcelery.backends.cache:CacheBackend' #django-celery cached database result backend
CELERY_SEND_EVENTS = True
CELERY_TASK_RESULT_EXPIRES = 10
CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"
#CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend' # http://docs.celeryproject.org/en/master/django/first-steps-with-django.html#using-the-django-orm-cache-as-a-result-backend
#CELERY_SEND_EVENTS = True # http://docs.celeryproject.org/en/latest/configuration.html?highlight=events#celery-send-events



# CELERYBEAT_SCHEDULE = {
#     'add-every-monday': {
#         'shared_task': 'shared_tasks.add',
#         'schedule': crontab(minute=0, hour=0, day_of_week="monday"),
#         'args': (16, 16)
#     },
#     'add-every-monday': {
#         'task': 'tasks.add',
#         'schedule': crontab(minute=0, hour=0, day_of_week="monday"),
#         'args': (16, 16)
#     },
# }

# This is how you would route a misbehaving task to a dedicated queue:
# CELERY_ROUTES = {
#     'tasks.add': 'low-priority',
# }


# rate limiting the task so that only 10 tasks of this type can be processed in a minute (10/m):
# CELERY_ANNOTATIONS = {
#     'tasks.add': {'rate_limit': '10/m'}
# }

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'filters': {
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse'
#         }
#     },
#     'handlers': {
#         'mail_admins': {
#             'level': 'ERROR',
#             'filters': ['require_debug_false'],
#             'class': 'django.utils.log.AdminEmailHandler'
#         }
#     },
#     'loggers': {
#         'django.request': {
#             'handlers': ['mail_admins'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#     }
# }