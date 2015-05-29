# -*- coding: utf-8 -*-

# Scrapy settings for scrapetank project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import sys
sys.path.append('/home/ubuntu/workspace/scrapy_phishtank')

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'scrapy_phishtank.settings'

BOT_NAME = 'scrapetank'

SPIDER_MODULES = ['scrapetank.spiders']
NEWSPIDER_MODULE = 'scrapetank.spiders'
DEFAULT_ITEM_CLASS = 'scrapetank.items.PhishID'
ITEM_PIPELINES = {
    'scrapetank.pipelines.MyImagesPipeline': 1,
}
IMAGES_STORE = 'phishshots'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Pixm.net (+http://pixm.net)'
