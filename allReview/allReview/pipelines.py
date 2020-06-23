# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import csv


class ReviewPipeline(object):
    def __init__(self):
        # csv文件的位置,无需事先创建
        store_file = os.path.dirname(__file__) + '/spiders/review.csv'
        # 打开(创建)文件
        self.file = open(store_file, 'w')

        self.writer = csv.writer(self.file, dialect="excel")
        self.writer.writerow(['账号', '内容', '时间'])


    def process_item(self, item, spider):

        print(item['link'])
        self.writer.writerow([item['name'], item['content'], item['time']])
        return item

    def spider_closed(self, spider):
        self.file.close()



