# -*- coding: utf-8 -*-

from browser_crawler.config.useragent import agents
import random


class RandomUserAgent(object):
    """Randomly rotate user agents based on a list of predefined ones"""

    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(agents)

    def process_request(self, request, spider):
        useragent = random.choice(self.agents)
        print("**********UserAgent*********" + useragent)
        request.headers.setdefault('User-Agent', useragent)


