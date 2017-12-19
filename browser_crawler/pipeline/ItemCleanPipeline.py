# -*- coding: utf-8 -*-

from scrapy.exceptions import DropItem




class ItemCleanPipeline(object):

    def __init__(self):
        pass

    def process_item(self, item, spider):
        if item['isEmpty']:
            raise DropItem("invaild item found: %s" % item)
        else:
            return item