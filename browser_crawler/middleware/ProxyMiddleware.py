# -*- coding: utf-8 -*-
import random

from browser_crawler.config.proxy import PROXY_POOL_URL


class ProxyMiddleware(object):
    def process_request(self, request, spider):
        request.meta['proxy'] = "http://%s" % random.choice(PROXY_POOL_URL)