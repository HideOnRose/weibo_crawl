# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import time
from scrapy import signals
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
import json


class ReviewSpiderMiddleware(object):
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
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ReviewDownloaderMiddleware(object):
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
        return response
          # 参数url指当前浏览器访问的url(通过current_url方法获取), 在这里参数url也可以用request.url
        # 参数body指要封装成符合HTTP协议的源数据, 后两个参数可有可无
        # return response  # 是原来的主页的响应对象
        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest

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


class SeleniumMiddleware(object):
    def __init__(self, timeout=None, service_args=[]):

        self.browser = webdriver.Chrome(r'chromedriver.exe', options=chrome_options)

    def __del__(self):
        self.browser.close()

    def process_request(self, request, spider):

        self.browser.get(request.url)

        with open(r'cookies.txt', 'r') as cookiefile:
            cookieslist = json.load(cookiefile)
            for cookie in cookieslist:
                if 'expiry' in cookie:
                    del cookie['expiry']
                self.browser.add_cookie(cookie)
        self.browser.refresh()
        time.sleep(5)
        
        # 此部分内容用来点击评论按钮，以展开评论内容
        # selectors = self.browser.find_elements_by_xpath("//div[@class='m-wrap']/div[@class='m-con-l']"
        #                                                 "//div[@class='card-wrap']")
        # number = len(selectors)
        # for i in range(1, number+1):
        #     try:
        #         btn = self.browser.find_element_by_xpath("//body[@class='wbs-feed']/div[@class='m-main']/div[@id='pl_"
        #                         "feed_main']/div[@class='m-wrap']/div[@id='pl_feedlist_index']/div[2]"
        #                         "/div[@class='card-wrap'][" + str(i) + "]/div[@class='card']/div[@class='card-act']/"
        #                         "ul/li[3]/a")  # 更多按钮
        #         btn.click()
        #         time.sleep(1)
        #     except:
        #         continue
        # # js = "window.scrollTo(0,document.body.scrollHeight)"
        # # spider.browser.execute_script(js)
        # time.sleep(5)  # 等待加载,  可以用显示等待来优化.

        row_response = self.browser.page_source
        return HtmlResponse(url=self.browser.current_url, body=row_response, encoding="utf8",
                            request=request)


    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
