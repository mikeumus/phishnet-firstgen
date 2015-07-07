# -*- coding: utf-8 -*-
from __future__ import absolute_import

# from processes.celery import app
from celery import shared_task
import requests, io, json


from .models import FreshPhish

url = 'http://data.phishtank.com/data/online-valid.json'

@shared_task(name="StorePhishURL")
def StorePhishURL():
    r = requests.get(url)
    r.encoding = 'utf-8'
    threats = json.loads(r.text)
    for threat in threats:
        freshphish = FreshPhish.objects.get_or_create(fresh_url=threat['url'])
        if threat['phish_id']:
            freshphish.fresh_id = threat['phish_id']
        freshphish.fresh_target = threat['target']
        freshphish.country = threat['details']['country']
        if threat['online'] == 'yes':
            freshphish.live_phish = True   # u'online': u'yes'
        freshphish.verification_time = threat['verification_time']
        freshphish.detail_time = threat['details']['detail_time']
        freshphish.announcing_network = threat['details']['announcing_network']
        freshphish.fresh_ip =  threat['details']['ip_address'] # details.ip_address
        freshphish.cidr_block = threat['datails']['cidr_block']
        freshphish.phishtank_url = threat['phish_detail_url']
        freshphish.submission_time = threat['submission_time']
        freshphish.save()
        print threat['url']
        
        
    