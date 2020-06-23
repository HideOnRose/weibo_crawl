# -*- coding: utf-8 -*-
import scrapy
from ..items import ReviewItem

class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['weibo.com']
    start_urls = ['weibo.com/1644114654/ImPMKhXVw']
    # def start_requests(self):
    #     url_list = []
    #     with open("url.csv") as file:
    #         for line in file:
    #             url_list.append(line)
    #
    #     for url in url_list:
    #         yield scrapy.Request(url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        item = ReviewItem()
        comments = response.xpath("//div[@class='WB_repeat S_line1']/div[@class='repeat_list']/div[2]/div[@class='list_box']/div[@class='list_ul']/div[@class='list_li S_line1 clearfix']")
        for one in comments:
            #发博账号和微博内容
            name = one.xpath("./div[@class='list_con']/div[@class='WB_text']/a[1]/text()").get()
            content = one.xpath("./div[@class='list_con']/div[@class='WB_text']/text()").get()
            content = content[content.find(':'):]

            if name is not None:
                item['name'] = name
                item['content'] = content

            time = one.xpath("./div[@class='WB_func clearfix']/div[@class='WB_from S_txt2']/text()").get()
            item['time'] = time

            yield item



