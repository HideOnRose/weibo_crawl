# -*- coding: utf-8 -*-
import scrapy
from ..items import ReviewItem

class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['weibo.com']
    start_urls = ['https://s.weibo.com/weibo?q=%E7%8E%8B%E5%87%A4%E9%9B%85&typeall=1&suball=1&Refer=g']

    def parse(self, response):
        item = ReviewItem()
        weibo = response.xpath("//div[@class='m-wrap']/div[@class='m-con-l']//div[@class='card-wrap']")
        for one in weibo:
            #发博账号和微博内容
            name = one.xpath('.//a[@class="name"]/text()').get()
            text = one.xpath(".//p[@node-type='feed_list_content_full']//text()")
            content = ''
            for i in text:
                content = content + i.get().strip()
            if name is not None:
                item['name'] = name
                item['content'] = content

            if content == '':
                text2 = one.xpath(".//p[@node-type='feed_list_content']//text()")
                for i in text2:
                    content = content + i.get().strip()
                item['content'] = content

            #转发数和评论数
            transmit = one.xpath(".//div[@class='card-act']//li[2]/a/text()").get()
            review = one.xpath(".//div[@class='card-act']//li[3]/a/text()").get()
            if transmit is not None:
                item['transmit_count'] = transmit
                item['review_count'] = review

            #发布时间
            publish_time = one.xpath(".//p[@class='from']/a[@target='_blank']/text()").get().strip()
            if publish_time is not None:
                item['time'] = publish_time

            # #更多评论链接
            # link = one.xpath(".//div[@class='card-more-a']/a/@href").get()
            # if link is not None:
            #     item['link'] = link
            # else:
            #     item['link'] = ''

            yield item

        next_page = response.xpath('//a[@class="next"]/@href').get()
        if next_page:
            next_url = 'https://s.weibo.com' + next_page
            yield scrapy.Request(next_url, callback=self.parse, dont_filter=False)


