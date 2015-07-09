# -*- coding: utf-8 -*-
from __future__ import absolute_import

# from processes.celery import app
from celery import shared_task
import requests
import io
import os
import json
from selenium import webdriver


from .models import FreshPhish

# Google Drive hosted valid_offline.json https://googledrive.com/host/0B9LVk4xbDIJTY0Z6dVVjUTAwYnM # (except it's not encoded in json any longer on Google Drive for some reason)
# localhost valid_online.json file http://127.0.0.1:8000/static/verified_online.json
# Hourly PhishTank Json API dump http://data.phishtank.com/data/online-valid.json
url = 'http://127.0.0.1:8000/static/verified_online.json'


@shared_task(name="StorePhishURL")
def StorePhishURL():
    r = requests.get(url)
    r.encoding = 'utf-8'
    threats = json.loads(r.text)
    counter = 0
    for threat in threats:
        freshphish, created = FreshPhish.objects.get_or_create( # docs for get_or_create https://docs.djangoproject.com/en/1.8/ref/models/querysets/#get-or-create
            fresh_url=threat['url'], fresh_id=threat['phish_id']
        )
        print "Fetching URL '{}'".format(threat['url'])
        if created:
            # freshphish.fresh_id = threat['phish_id']
            freshphish.fresh_target = threat['target']
            freshphish.country = threat['details'][0]['country']
            try:
                # take screenshot if http 200: http://stackoverflow.com/questions/24518944/try-except-when-using-python-requests-module
                if not r.status_code // 100 == 2:
                    return "Error: Unexpected response {}".format(response)
                # take screenshot of fresh_url
                driver = webdriver.Firefox()
                driver.get(threat['url'])
                # driver.save_screenshot('{0}_{1}_screenshot.png'.format(threat['target'], threat['phish_id']))
                # save "phishshots" (screenshots) in folder http://stackoverflow.com/questions/27874002/python-selenium-save-screenshot-in-newly-created-folder
                driver.save_screenshot('phishshots/{0}_{1}_screenshot.png'.format(threat['target'], threat['phish_id']))
                driver.quit()
            except requests.exceptions.RequestException as e:
                # A serious problem happened, like an SSLError or InvalidURL
                return "Error: {}".format(e)
            if threat['online'] == 'yes':
                freshphish.live_phish = True   # u'online': u'yes'
            # Consider any status other than 2xx an error

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
