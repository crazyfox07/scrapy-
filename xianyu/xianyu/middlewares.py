# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random

from scrapy import signals
from scrapy.downloadermiddlewares.retry import RetryMiddleware
from xianyu.utils.comm_log  import logger

from xianyu.aws_proxies import get_proxies

class RandomUserAgent(object):
    """随机选择UserAgent"""

    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        ua = random.choice(self.agents)
        request.headers.setdefault('User-Agent', ua)

class XianyuSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

    def process_request(self, request, spider):
        request.meta['proxy'] = get_proxies()['http']
        #request.meta['proxy'] = get_proxies_from_redis() #http://54.222.241.163:3128
        #request.meta['proxy'] = 'https://54.222.241.163:3128'

class BlankPageRetryMiddleware(RetryMiddleware):
    def __init__(self, *args, **kw):
        super(BlankPageRetryMiddleware, self).__init__(*args, **kw)
        self.length_threshold = 100

    def process_response(self, request, response, spider):
        if response.text.find(u'亲，你太潮了，闲鱼.淘宝二手里暂时还找不到你搜索的东西呢～') != -1:
            logger.info("blank page: %s" % response.url)
            retries = request.meta.get('retry_times', 0) + 1
            print("**********blank page: %s retries: %s" % (response.url, retries))
            logger.info("**********blank page: %s retries: %s" % (response.url, retries))
            reason = 'blank page %s' % response.url
            return self._retry(request, reason, spider) or response
        return response



