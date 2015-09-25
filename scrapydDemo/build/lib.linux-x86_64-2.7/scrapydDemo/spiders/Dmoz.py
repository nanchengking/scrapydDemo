#coding=utf-8
'''
@author: nancheng
'''

#coding=utf-8
from scrapy.contrib.loader import ItemLoader
import logging
import scrapy
from scrapydDemo.items import  *
class demozSpider(scrapy.Spider):
    name="dmoz"
   # allowed_domains = ["baidu.com"]
    start_urls = [
       "http://tieba.baidu.com/f?kw=嘉祥一中&ie=utf-8&tab=good&cid=7"
    ] 
    def parse(self,response):
        logging.info("==爬虫dmoz的 parse start!==")
        self.num=0
        self.wanted_num=5
        item=TieziItem()
        infos=response.xpath('//div[@class="threadlist_lz clearfix"]/div/a[@class="j_th_tit "]')
        for info in infos:
            item['title']=info.xpath("text()").extract()[0]
            item['url']="http://tieba.baidu.com"+info.xpath("@href").extract()[0]
            item['author']=info.xpath('..').xpath('..').xpath("div[@class='threadlist_author pull_right']/span/a/text()").extract()[0]
            self.num=self.num+1
            if self.num>=self.wanted_num:
                return 
            yield item
            
          
        

