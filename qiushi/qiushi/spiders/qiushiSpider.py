# -*- coding: utf-8 -*-
import scrapy
from qiushi.items import QiushiItem

class QiushispiderSpider(scrapy.Spider):
    name = 'qiushiSpider'
    allowed_domains = ['qiushibaike.com']
    wds = ['text','hot','imgrank','history','pic','textnew']
    pages = 10
    start_urls = []
    #https://www.qiushibaike.com/textnew/page/2/?s=5073509
    for type in wds:
        for i in xrange(2, pages+1):
            start_urls.append('https://www.qiushibaike.com/' + type + '/page/' + str(i))


    def parse(self, response):
        subSelector = response.xpath('//div[@class="article"]')
        items = []
        for sub in subSelector:
            item = QiushiItem()
            item['author'] = sub.xpath('//h2/text()').extract()[0]
            item['content'] = sub.xpath('//a/div[@class="content"]/span/text()').extract()[0]
            if sub.xpath('//div[@class="thumb"]/a/img/@src'):
                item['img'] = sub.xpath('//div[@class="thumb"]/a/img/@src').extract()[0]
            item['funNum'] = sub.xpath('//div[@class="stats"]/span/i/text()').extract()[0]
            item['talkNum'] = sub.xpath('//div[@class="stats"]/span/a/i/text()').extract()[0]

            items.append(item)
        return items


