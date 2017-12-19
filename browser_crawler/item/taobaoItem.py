# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field


class TaobaoItem(scrapy.Item):

    impress = Field()
    totalComment = Field()
    goodComment = Field()
    badComment = Field()
    normalComment = Field()
    additionalComment = Field()
    picComment = Field()
    deliveryFee = Field()

    itemId = Field()
    title = Field()
    subtitle = Field()
    commentCount = Field()
    shopid = Field()
    shopName = Field()
    sellerFans = Field()
    allItemCount = Field()
    descScore = Field()
    serviceScore = Field()
    postScore = Field()
    creditLevel = Field()
    goodRatePercentage = Field()
    isEmpty = Field()
