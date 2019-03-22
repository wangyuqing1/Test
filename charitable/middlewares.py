# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.http.request import Request
from .Process_Duperfilter import Website
from .start_Duperfilter import Before_Reqest
import pymssql
import re

class CharitableSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):

        for i in result:
            if isinstance(i,Request):
                url = i.url.split('/')[2]
                if url == 'www.cswef.cn':
                    data = Website.cswefs(Website(),i.url,i)
                    yield data
                elif url == 'www.ccafc.org.cn':
                    data = Website.ccafc(Website(),i.url,i)
                    yield data
                elif url == 'www.cfpa.org.cn':
                    data = Website.cfpa(Website(),i.url,i)
                    yield data
                else:
                    yield i
            else:
                yield i


    def process_spider_exception(self, response, exception, spider):
        pass

    def process_start_requests(self, start_requests, spider):
        for r in start_requests:
            url = r.url.split('/')[2]
            if url == 'www.cswef.cn':
                data = Before_Reqest.cswef(Before_Reqest(),r.url,r)
                yield data
            elif url == 'www.ccafc.org.cn':
                data = Before_Reqest.ccafc(Before_Reqest(),r.url,r)
                yield data
            elif url == 'www.cfpa.org.cn':
                data = Before_Reqest.cfpa(Before_Reqest(),r.url,r)

                yield data
            else:
                yield r
            # yield r


    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class CharitableDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
