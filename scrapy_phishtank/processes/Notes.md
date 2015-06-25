### Celery Processes Notes
- Celery + Django Project Template by @dvl: https://github.com/dvl/celerytest 
 - Thanks @dvl :)
 - and celery docs django template: https://github.com/celery/celery/tree/3.1/examples/django
- Retry Policy
 - http://docs.celeryproject.org/en/master/userguide/calling.html#retry-policy 
- Starting tasks in the background with `celery multi`: http://docs.celeryproject.org/en/master/getting-started/next-steps.html?highlight=multi#in-the-background
 - `celery multi start w1 -A proj -l info`
 - Starting a process locally in the terminal: `celery -A proj worker -l info`
 
Also see https://github.com/mikeumus/django-celery-example/blob/master/README.md#get-django-celery-working