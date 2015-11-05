# -*- coding: utf-8 -*-
from __future__ import absolute_import

# from processes.celery import app
from celery import shared_task
import requests
import io
import os
import json
from selenium import webdriver
from .phishtank_key import PHISHTANK_API_KEY


from .models import FreshPhish

# Google Drive hosted valid_offline.json https://googledrive.com/host/0B9LVk4xbDIJTY0Z6dVVjUTAwYnM # (except it's not encoded in json any longer on Google Drive for some reason)
# localhost valid_online.json file http://127.0.0.1:8000/static/verified_online.json
# Hourly PhishTank Json API dump http://data.phishtank.com/data/online-valid.json
# Phishtank API key: http://data.phishtank.com/data/{}/online-valid.json.bz2'.format(PHISHTANK_API_KEY)
url = 'http://data.phishtank.com/data/{}/online-valid.json'.format(PHISHTANK_API_KEY)

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

            try:
                # take screenshot if status code is good
                if r.status_code != requests.codes.ok:
                    return "Error: Unexpected response {}".format(r)
                # take screenshot of fresh_url
                #driver = webdriver.Firefox()
                #executable_path="/usr/bin/chromedriver"
                driver = webdriver.Chrome()
                # we dont have driver_arguments varialble!!!
                # selenium just uses the webdriver APIs so why could we use driver_arguments ?
                # python will raise an error asking where did you come with that varialble XD
                # I see. but.. I bet it's posible somehow lol
                # lol coding is so logical not feeling XD
                # :p
                # lets try ipython and we call selenium inside of it and th chromderiver too
                # good idea, why isn't ipython my default when I do `./manage.py shell` on this tower?
                # becasue you dont have ipython and it runs python interprester :D
                # :p

                #driver_arguments['chrome_options'].add_argument('--no-sandbox')
                driver.set_page_load_timeout(30)
                driver.get(threat['url'])
                # save "phishshots" (screenshots) in folder http://stackoverflow.com/questions/27874002/python-selenium-save-screenshot-in-newly-created-folder
                driver.save_screenshot('phishots/{0}_{1}_screenshot.png'.format(threat['target'], threat['phish_id']))
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
            if threat['details']:
                freshphish.country = threat['details'][0]['country']
                freshphish.detail_time = threat['details'][0]['detail_time']
                freshphish.announcing_network = threat['details'][0]['announcing_network']
                freshphish.fresh_ip = threat['details'][0]['ip_address']  # details.ip_address
                freshphish.cidr_block = threat['details'][0]['cidr_block']
            freshphish.phishtank_url = threat['phish_detail_url']
            freshphish.submission_time = threat['submission_time']
            freshphish.save()
            counter += 1

    return "%s new phishing records has been created." % (counter)
