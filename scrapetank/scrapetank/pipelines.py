# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
# from scrapy.http import Request

# class ScrapetankPipeline(object):
#     def process_item(self, item, spider):
#         return item

# http://stackoverflow.com/a/22263951/1762493
class MyImagesPipeline(ImagesPipeline):

    #Name download version
    def file_path(self, request, response=None, info=None):
        #item=request.meta['item'] # Like this you can use all from item, not just url.
        image_guid = request.url.split('/')[-1]
        return 'full/%s' % (image_guid)
        
    # http://stackoverflow.com/a/19073347/1762493
    # def process_item(self, item, spider):
    #     item.save() 
    #     return item

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)
            
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok] # what? Checking if image_paths are okay I guess. 
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        item.save()
        return item

    
    #Name thumbnail version
    """
    def thumb_path(self, request, thumb_id, response=None, info=None):
        image_guid = thumb_id + response.url.split('/')[-1]
        return 'thumbs/%s/%s.jpg' % (thumb_id, image_guid)
    """
    
    
    
    