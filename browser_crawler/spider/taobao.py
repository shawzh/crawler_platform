# -*- coding: utf-8 -*-


from scrapy.spider import Spider
from browser_crawler.item.taobaoItem import TaobaoItem
from browser_crawler.config.proxy import PROXY_POOL_URL
import json
import requests
import random


class TaobaoSpider(Spider):
    '''spider that reads urls from redis queue (myspider:start_urls).'''
    name = 'taobao'

    def __init__(self, *args, **kwargs):
        super(TaobaoSpider, self).__init__(*args, **kwargs)

    def parse(self, response):

        item = TaobaoItem()
        jsonresponse = json.loads(response.body_as_unicode())

        if jsonresponse['ret'][0] == 'FAIL_SYS_USER_VALIDATE::哎哟喂,被挤爆啦,请稍后重试!':
            # todo retry
            item['isEmpty'] = True
            return  item

        if 'trade' in jsonresponse['data'] :
            item['isEmpty'] = True
            return item

        d = jsonresponse["data"]
        productInfo = d['item']
        seller = d['seller']

        item['itemId'] = productInfo['itemId']

        # 商品名称
        item['title'] = productInfo['title'].replace(" ",'')
        # 商品二级名称
        if 'subtitle' not in productInfo:
            item['subtitle'] = 'null'
        elif productInfo['subtitle'] == '':
            item['subtitle'] = 'null'
        else:
            item['subtitle'] =  productInfo['subtitle']
        #累计评论
        item['commentCount'] = productInfo['commentCount'].replace(" ",'')
        # 销售商id
        item['shopid'] =  seller['shopId'].replace(" ",'')
        # 销售名称
        item['shopName'] = seller['shopName'].replace(" ",'')
        #关注店铺人数
        item['sellerFans'] = seller['fans'].replace(" ",'')
        #店铺在销商品数量
        item['allItemCount'] = seller['allItemCount'].replace(" ",'')
        #店铺评分-宝贝描述
        item['descScore'] = seller['evaluates'][0]['score'].replace(" ",'')
        #店铺评分-卖家服务
        item['serviceScore'] = seller['evaluates'][1]['score'].replace(" ",'')
        #店铺评分-物流服务
        item['postScore'] = seller['evaluates'][2]['score'].replace(" ",'')
        #信誉等级
        item['creditLevel'] = seller['creditLevel'].replace(" ",'')
        # 好评率
        item['goodRatePercentage'] = seller['goodRatePercentage'].replace(" ",'')



        # freeship
        free_url = 'https://detailskip.taobao.com/json/deliveryFee.htm?&itemId=' + item['itemId']
        callback = requests.get(free_url, proxies=random.choice(PROXY_POOL_URL)).text[13:-3]
        data = json.loads(callback)['data']['serviceInfo']
        if 'sku' in data:
            i = data['sku']['default'][0]['info']
        else:
            i = data['list'][0]['info']
        if '免运费' in i:
            item['deliveryFee'] = 0
        else:
            item['deliveryFee'] = i.split('>')[-1]

        #Commnet
        comment = 'https://rate.taobao.com/detailCommon.htm?auctionNumId=' + item['itemId']
        callback = requests.get(comment, proxies=random.choice(PROXY_POOL_URL))
        data = json.loads(callback.text[3:-1])['data']
        count = data['count']

        item['impress'] = data['impress']
        item['totalComment'] = count['totalFull']
        item['goodComment'] = count['goodFull']
        item['badComment'] = count['bad']
        item['normalComment'] = count['normal']
        item['additionalComment'] = count['additional']
        item['picComment'] = count['pic']

        item['isEmpty'] = False

        return item

