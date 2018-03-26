# -*- coding: utf-8 -*-
import scrapy


class WuhanspiderSpider(scrapy.Spider):
    name = 'wuHanSpider'
    allowed_domains = ['www.tianqi.com/wuhan']
    start_urls = ['http://www.tianqi.com/wuhan/']

    def parse(self, response):
        pass
