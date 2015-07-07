# https://docs.djangoproject.com/en/1.8/topics/db/models/
# http://doc.scrapy.org/en/latest/topics/djangoitem.html?highlight=database
# https://docs.djangoproject.com/en/1.8/ref/models/fields/
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save, post_delete


# model to abstract out Companies from phish models
#class Company(models.Model):
#    """
#        Company Model
#    """
#    name = models.CharField(max_length=255, unique=True)
#    
#    def __str__(self):
#        return unicode(self.name)


# model for hourly PhishTank API Json dump saving to database
class FreshPhish(models.Model):
    #company = models.ForeignKey(Company)
    fresh_url = models.URLField(max_length=3000, unique=True)
    fresh_id = models.CharField(max_length=255, unique=True)
    fresh_target = models.CharField(max_length=255)
    live_phish = models.BooleanField(default=False)
    verification_time = models.DateField(null=True, blank=True)
    detail_time = models.DateField(null=True, blank=True) #details.detail_time
    country = models.CharField(max_length=255) # details.country 
    announcing_network = models.CharField(max_length=255) #details.announcing_network
    fresh_ip = models.CharField(max_length=255) # details.ip_address. Swith to use "GenericIPAddressField" later
    cidr_block = models.CharField(max_length=255) # details.cidr_block
    phishtank_url = models.CharField(max_length=255) # phish_detail_url
    submission_time = models.DateField(null=True, blank=True)
    # WHOIS, afterwards from scraping 
    

class Phish(models.Model):
    phishyid = models.CharField(max_length=255, unique=True)
    company = models.CharField(max_length=255, default='default', null=True)
    # image_urls = models.URLField(max_length=255, unique=True)
    
    # class Meta:
        # https://docs.djangoproject.com/en/1.8/ref/models/options/
        # http://stackoverflow.com/questions/2201598/how-to-define-two-fields-unique-as-couple
        # unique_together = ("phishyid", "company")
    
    def __str__(self):
        return unicode(self.phishyid)
    
# model for tasking offline phishtank scrape with FIXTURES
class FixedPhish(models.Model):
    phishyid = models.CharField(max_length=255)
    company = models.CharField(max_length=255, default='default', null=True)
    # image_url = models.CharField(max_length=255, unique=True)
    
# model for scraping from fixed "clonezone" offline phishes PhishTank.com webpage clone
class ClonedPhish(models.Model):
    cloned_phishyid = models.CharField(max_length=255, unique=True)
    cloned_company = models.CharField(max_length=255, default='default', null=True)
    cloned_phishdate = models.CharField(max_length=255)
    cloned_timestamp = models.DateField(default=timezone.now)
    # image_urls = models.URLField(max_length=255, unique=True)

    def __str__(self):
        return unicode(self.cloned_phishyid)
        
# model for scrapy broad web spiders
class BroadWeb(models.Model):
    broad_url = models.URLField()
    broad_ip = models.GenericIPAddressField()
    broad_submissiontime = models.DateField()
