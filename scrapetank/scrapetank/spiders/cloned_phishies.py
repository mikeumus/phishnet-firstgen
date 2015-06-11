
""" All content from PhishTank.com is under a Creative Commons Attribution-ShareAlike 2.5 License. """
# Forked from offline_phishies scrapy spider

import scrapy
from scrapy.contrib.spiders.init import Spider 
from scrapy.http import Request #, FormRequest
from scrapy.contrib.linkextractors import LinkExtractor
# from scrapy.contrib.spiders import Rule
from scrapy.selector import Selector

from scrapetank.items import ClonedPhishItem


class MySpider(scrapy.Spider):
    name = 'cloned_phishies'
    allowed_domains = ['http://www.phishtank.com.clonezone.link']
    # login_page = 'https://www.phishtank.com/index.php'

    start_urls = [
        'http://www.phishtank.com.clonezone.link/wellsfargo',
        'http://www.phishtank.com.clonezone.link/boa'
        ]
    
    
    # http://doc.scrapy.org/en/latest/topics/spiders.html#crawlspider-example
    # rules = (
    #     Rule(LinkExtractor(restrict_xpaths=('/a[text() = "Older >"]')), callback='parse_item', follow=True )
    # )
    
    # def init_request(self):
    #     """This function is called before crawling starts."""
    #     return Request(url=self.login_page, callback=self.login)
    
    # def login(self, response):
    #     """Generate a login request."""
    #     # http://doc.scrapy.org/en/latest/topics/request-response.html#formrequest-objects 
    #     return FormRequest.from_response(response,
    #                 #formnumber=1,
    #                 formdata={'username': 'parsehubby', 'password': ':(sorry:('},
    #                 #formxpath='class="loginbox"',
    #                 callback=self.check_login_response,
    #                 dont_filter=True)
    
    # def check_login_response(self, response):
    #     """Check the response returned by a login request to see if we are
    #     successfully logged in.
    #     """
    #     if "parsehubby" in response.body:
    #         self.log("Successfully logged in. Let's start crawling!")
    #         # Now the crawling can begin..
    #         return self.initialized()
    #     else:
    #         self.log("Bad times :(")
    #         # Something went wrong, we couldn't log in, so nothing happens.
    
    def parse(self, response):
        # Scrape data from page
        sel = Selector(response)
        # http://stackoverflow.com/questions/20224998/scrapy-cant-find-xpath-content?answertab=votes#tab-top
        # //div[starts-with(@id, "site_comment_"]), i.e. all divs that have an "id" attribute beginning with string ""site_comment_"
        phishs = sel.xpath('//td[@class="value cz-parent-editable"]/a[starts-with(@href, "phish_detail.php?phish_id=")]')
        items = []
        
        for phish in phishs:
            item = ClonedPhishItem()
            item['cloned_company'] = sel.xpath('//select[@name="target_id"]/option[@selected]/text()').extract()[0]
            item['cloned_phishyid'] = str(phish.xpath('text()').extract()[0]) # http://stackoverflow.com/a/3329651/1762493
            """ WORKING ON PHISHTANK DATE line #70 below """
            # item['cloned_phishdate'] = str(sel.xpath('//span[@class="small cz-editable"]/text()').extract()[0])
            # img_id = item['cloned_phishyid']
            # item['cloned_image_urls'] = ["http://phishtank-screenshots.e1.usw1.opendns.com.s3-website-us-west-1.amazonaws.com/{}.jpg".format(img_id) for img_id in item['cloned_phishyid']] 
            items.append(item)
            
        return items

