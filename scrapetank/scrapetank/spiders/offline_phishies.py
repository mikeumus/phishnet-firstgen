
""" All content from PhishTank.com is under a Creative Commons Attribution-ShareAlike 2.5 License. """

import scrapy
from scrapy.contrib.spiders.init import Spider 
from scrapy.http import Request, FormRequest
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import Rule
from scrapy.selector import Selector

from scrapetank.items import PhishIdItem


class MySpider(scrapy.Spider):
    name = 'offline_phishies'
    allowed_domains = ['phishtank.com']
    login_page = 'https://www.phishtank.com/index.php'

    def __init__(self, target_id=''):
        # http://doc.scrapy.org/en/latest/topics/spiders.html#spider-arguments
        self.start_urls = ['https://www.phishtank.com/target_search.php?page=%s&target_id={0}&active=n&valid=y&Search=Search'.format(target_id) % page for page in xrange(1,300)]
 
    """ Spider Legend
    Nice, thanks ArseniyK! :)
    Moved it to Spider-Arguments-Key.md
    """
    
    # http://doc.scrapy.org/en/latest/topics/spiders.html#crawlspider-example
    rules = (
        Rule(LinkExtractor(restrict_xpaths=('/a[text() = "Older >"]')), callback='parse_item', follow=True )
    )
    
    def init_request(self):
        """This function is called before crawling starts."""
        return Request(url=self.login_page, callback=self.login)
    
    def login(self, response):
        """Generate a login request."""
        # http://doc.scrapy.org/en/latest/topics/request-response.html#formrequest-objects 
        return FormRequest.from_response(response,
                    #formnumber=1,
                    formdata={'username': 'parsehubby', 'password': ':(sorry:('},
                    #formxpath='class="loginbox"',
                    callback=self.check_login_response,
                    dont_filter=True)
    
    def check_login_response(self, response):
        """Check the response returned by a login request to see if we are
        successfully logged in.
        """
        if "parsehubby" in response.body:
            self.log("Successfully logged in. Let's start crawling!")
            # Now the crawling can begin..
            return self.initialized()
        else:
            self.log("Bad times :(")
            # Something went wrong, we couldn't log in, so nothing happens.
    
    def parse(self, response):
        # Scrape data from page
        sel = Selector(response)
        # http://stackoverflow.com/questions/20224998/scrapy-cant-find-xpath-content?answertab=votes#tab-top
        # //div[starts-with(@id, "site_comment_"]), i.e. all divs that have an "id" attribute beginning with string ""site_comment_"
        phishs = sel.xpath('//td[@class="value"]/a[starts-with(@href, "phish_detail.php?phish_id=")]')
        items = []
        
        for phish in phishs:
            item = PhishIdItem()
            item['phishyid'] = phish.xpath('text()').extract()
            img_id = item['phishyid']
            item['image_urls'] = ["http://phishtank-screenshots.e1.usw1.opendns.com.s3-website-us-west-1.amazonaws.com/{}.jpg".format(img_id) for img_id in item['phishyid']] 
            items.append(item)
            
        return items

