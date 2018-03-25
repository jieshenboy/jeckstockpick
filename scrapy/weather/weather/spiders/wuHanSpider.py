# -*- coding: utf-8 -*-
import scrapy

from weather.items import WeatherItem

class WuhanspiderSpider(scrapy.Spider):
    name = 'wuHanSpider'
    allowed_domains = ['www.tianqi.com/wuhan']
    start_urls = ['http://www.tianqi.com/wuhan/']

    def parse(self, response):
        subSelector = response.xpath('//div[@class="day7"]')
        items = []
        for sub in subSelector:
            item = WeatherItem()
            cityDates = ''
            for cityDate in sub.xpath('./ul[@class="week"]/li/b//text()').extract():
                cityDates += cityDate
            item['cityDate'] = cityDates
            weeks = ''
            for week in sub.xpath('./ul[@class="week"]/li/span//text()').extract():
                weeks += week
            item['week'] = weeks
            imgs = ''
            for img in sub.xpath('./ul[@class="week"]/li/img/@src').extract():
                imgs += img
            item['img'] = imgs
            weathers = ''
            for weather in sub.xpath('./ul[@class="txt"][1]/li/text()').extract():
                weathers += weather
            item['weather'] = weathers
            winds = ''
            for wind in sub.xpath('./ul[@class="txt"]/li/text()').extract():
                winds += wind
            item['wind'] = winds
            items.append(item)
        return items