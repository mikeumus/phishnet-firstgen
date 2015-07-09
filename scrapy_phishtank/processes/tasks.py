""" USING /pishing/tasks/py

# -*- coding: utf-8 -*-
from __future__ import absolute_import

# from processes.celery import app
from celery import shared_task
import requests, io, json
from .phishtank_key import PHISHTANK_API_KEY

from pishing.models import FreshPhish

# Using the @shared_task decorator
# The tasks you write will probably live in reusable apps,
# and reusable apps cannot depend on the project itself, so you also cannot import your app instance directly.
# The @shared_task decorator lets you create tasks without having any concrete app instance:
# from celery import shared_task

url = 'http://data.phishtank.com/data/online-valid.json'

#@shared_task(name="shared_tasks.add")
#def add(x, y):
#    return x + y

@shared_task(name="shared_tasks.getPhishtankJson")
def getPhishtankJson():
    # url = 'http://data.phishtank.com/data/{}/online-valid.json.bz2'.format(PHISHTANK_API_KEY)
    # https://googledrive.com/host/0B9LVk4xbDIJTY0Z6dVVjUTAwYnM # Google Drive hosted valid_online.json (except it's not encoded in json any longer on Google Drive for some reason)
    #r = requests.get('https://googledrive.com/host/0B9LVk4xbDIJTY0Z6dVVjUTAwYnM', stream=True)
    # data = r.json()
    # note to self, try stream io.open
    # pretty print json: http://stackoverflow.com/a/20776329/1762493
    # with open('data.json', 'w') as f:
    #     json.dump(data, f, sort_keys = True, indent = 4, ensure_ascii=False)
    #
    # http://stackoverflow.com/questions/17518937/saving-a-json-file-to-computer-python
    # http://stackoverflow.com/questions/16694907/how-to-download-large-file-in-python-with-requests-yp
    #local_filename = 'valid_online.json'
    #with open(local_filename, 'wb') as f:
    #    for chunk in r.iter_content(chunk_size=1024):
    #        if chunk: # filter out keep-alive new chunks
    #            f.write(chunk)
    #            f.flush()
    #return local_filename

    r = requests.get(url)
    r.encoding = 'utf-8'
    threats = json.loads(r.text)
    for threat in threats:
        #company = Company.objects.get_or_create(name=threat['target'])
        freshphish = FreshPhish.objects.get_or_create(fresh_url=threat['fresh_url'])
        freshphish.fresh_id = threat['fresh_id']
        freshphish.fresh_target = threat['target']
        #freshphish.fresh_url = threat['url']
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
        print "*" * 50
        print "New Phish %s" %(threat['url'])
        print "*" * 50
        # go ahead test :)
        # k

# Task Names: http://docs.celeryproject.org/en/latest/userguide/tasks.html?highlight=task.name#names
# @app.task(name="tasks.add")
# def add(x, y):
#     return x + y

"""
