# https://docs.djangoproject.com/en/1.8/topics/db/models/
# http://doc.scrapy.org/en/latest/topics/djangoitem.html?highlight=database
# https://docs.djangoproject.com/en/1.8/ref/models/fields/
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save, post_delete

class Phish(models.Model):
    phishyid = models.CharField(max_length=255, unique=True)
    company = models.CharField(max_length=255, default='default', null=True)
    # image_urls = models.URLField(max_length=255, unique=True)
    
    class Meta:
        # https://docs.djangoproject.com/en/1.8/ref/models/options/
        # http://stackoverflow.com/questions/2201598/how-to-define-two-fields-unique-as-couple
        unique_together = ("phishyid", "company")
    
    def __str__(self):
        return unicode(self.phishyid)
        
class FixedPhish(models.Model):
    phishyid = models.CharField(max_length=255)
    company = models.CharField(max_length=255, default='default', null=True)
    # image_url = models.CharField(max_length=255, unique=True)
    
class ClonedPhish(models.Model):
    cloned_phishyid = models.CharField(max_length=255, unique=True)
    cloned_company = models.CharField(max_length=255, default='default', null=True)
    cloned_phishdate = models.CharField(max_length=255)
    cloned_timestamp = models.DateField(default=timezone.now)
    # image_urls = models.URLField(max_length=255, unique=True)

    def __str__(self):
        return unicode(self.cloned_phishyid)
