# -*- coding: utf-8 -*-
from __future__ import absolute_import

# from processes.celery import app
from celery import shared_task
import requests
import io
import json


from .models import FreshPhish

url = 'http://data.phishtank.com/data/online-valid.json'


@shared_task(name="StorePhishURL")
def StorePhishURL():
    r = requests.get(url)
    r.encoding = 'utf-8'
    threats = json.loads(r.text)
    counter = 0
    for threat in threats:
        freshphish, created = FreshPhish.objects.get_or_create(
            fresh_url=threat['url'], fresh_id=threat['phish_id'])
        if created:
            # freshphish.fresh_id = threat['phish_id']
            freshphish.fresh_target = threat['target']
            freshphish.country = threat['details'][0]['country']
            if threat['online'] == 'yes':
                freshphish.live_phish = True   # u'online': u'yes'
            else:
                freshphish.live_phish = False
            freshphish.verification_time = threat['verification_time']
            freshphish.detail_time = threat['details'][0]['detail_time']
            freshphish.announcing_network = threat[
                'details'][0]['announcing_network']
            freshphish.fresh_ip = threat['details'][0][
                'ip_address']  # details.ip_address
            freshphish.cidr_block = threat['details'][0]['cidr_block']
            freshphish.phishtank_url = threat['phish_detail_url']
            freshphish.submission_time = threat['submission_time']
            freshphish.save()
            counter += 1

    return "%s new phishing records has been created." % (counter)
