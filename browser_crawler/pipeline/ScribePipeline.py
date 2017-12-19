# -*- coding: utf-8 -*-
from scrapy.exceptions import DropItem


class ScribePipeline(object):
    def process_item(self,item,spider):
        #  todo scribe update data


        # tansfer data to scribe ,actually scribe is backend,so we don't need
        # Hbase anymore,just drop it ,is ok
        raise DropItem("invaild item found: %s" % item)
