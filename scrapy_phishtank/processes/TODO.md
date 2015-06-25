### TO DO
- Use celery's `track_started` for the scrapy broad scrapes
 - http://docs.celeryproject.org/en/master/userguide/tasks.html#Task.track_started
- Celery Progress state via `update_state()` for broad scrape
 - http://docs.celeryproject.org/en/master/userguide/tasks.html#custom-states 
- Read the Celery Optimization Guide: http://docs.celeryproject.org/en/master/userguide/optimizing.html#guide-optimizing
- Read about Celery process deamonization: http://docs.celeryproject.org/en/master/tutorials/daemonizing.html#daemonizing
- django-celery scheduler in django admin: http://docs.celeryproject.org/en/master/userguide/periodic-tasks.html#using-custom-scheduler-classes
- Linking one task one after another (use chains instead)
 - http://docs.celeryproject.org/en/master/userguide/calling.html#linking-callbacks-errbacks
 - Used to download the PhishTank json dump, then the next task to crawl it
 - 
 
_ _ _ 

