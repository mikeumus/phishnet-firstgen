# -*- coding: utf-8 -*-
# Define here the models for your scraped items
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
# http://doc.scrapy.org/en/latest/topics/djangoitem.html?highlight=database
# http://stackoverflow.com/questions/19068308/access-django-models-with-scrapy-defining-path-to-django-project
from scrapy.contrib.djangoitem import DjangoItem
#from scrapy_phishtank.models import Phish
# Add the django app to settings and import the model here :)
from pishing.models import Phish
import scrapy

""" old scrapy item (still works! just trying to use djangoitem now)
class PhishID(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    phishyid = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    # pass
"""    
class PhishIdItem(DjangoItem):
    django_model = Phish
    image_urls = scrapy.Field()
    images = scrapy.Field()
    image_paths = scrapy.Field()
