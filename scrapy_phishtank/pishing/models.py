# https://docs.djangoproject.com/en/1.8/topics/db/models/
# http://doc.scrapy.org/en/latest/topics/djangoitem.html?highlight=database
from django.db import models

class Phish(models.Model):
    phishyid = models.CharField(max_length=255, unique=True)
    # age = models.IntegerField()
    
    def __str__(self):
        return unicode(self.phishyid)
