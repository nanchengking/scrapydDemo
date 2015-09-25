# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from  pymongo import *
import logging
class ScrapyddemoPipeline(object):
    def process_item(self, item, spider):
        self.tieba.insert_one(dict(item))
        return item
    def open_spider(self,spider):
        logging.info("==open_spider调用成功==")
        self.connect_mongodb()
    def close_spider(self,spider):
        logging.info("==close_spider调用成功==")
    def connect_mongodb(self):
        logging.info("==ScrapyddemoPipeline初始化 创建mongodb数据库连接==")
        self.client = MongoClient()
        self.db =self.client.tieba
        self.tieba = self.db.tieba
