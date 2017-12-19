# -*- coding: utf-8 -*-

FRONTERA_SETTINGS = 'browser_crawler.config.spider'

SCHEDULER = 'frontera.contrib.scrapy.schedulers.frontier.FronteraScheduler'
SPIDER_MIDDLEWARES = {
    'frontera.contrib.scrapy.middlewares.schedulers.SchedulerSpiderMiddleware': 999,
    'frontera.contrib.scrapy.middlewares.seeds.file.FileSeedLoader': 1,
}
DOWNLOADER_MIDDLEWARES = {
    'browser_crawler.middleware.ProxyMiddleware.ProxyMiddleware': 100,
    'browser_crawler.middleware.RandomUAMiddleware.RandomUserAgent': 200,
    'frontera.contrib.scrapy.middlewares.schedulers.SchedulerDownloaderMiddleware': 999,
}

ITEM_PIPELINES = {
    'browser_crawler.pipeline.ItemCleanPipeline.ItemCleanPipeline': 300,
    'browser_crawler.pipeline.ScribePipeline.ScribePipeline': 400
}

BOT_NAME = 'browser_crawler'

SPIDER_MODULES = ['browser_crawler.spider']
NEWSPIDER_MODULE = 'browser_crawler.spider'

CONCURRENT_REQUESTS=256
CONCURRENT_REQUESTS_PER_DOMAIN=1

DOWNLOAD_DELAY=1.0
DOWNLOAD_TIMEOUT=180
RANDOMIZE_DOWNLOAD_DELAY = False

REACTOR_THREADPOOL_MAXSIZE = 30
DNS_TIMEOUT = 120

COOKIES_ENABLED=False
RETRY_ENABLED = False
REDIRECT_ENABLED = True
AJAXCRAWL_ENABLED = False

AUTOTHROTTLE_ENABLED=True
AUTOTHROTTLE_START_DELAY=0.01
AUTOTHROTTLE_MAX_DELAY = 3.0
AUTOTHROTTLE_DEBUG=False

LOG_LEVEL='INFO'


