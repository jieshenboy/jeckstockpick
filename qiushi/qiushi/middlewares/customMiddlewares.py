#!/usr/bin/env bin
#-*- coding:utf-8 -*-
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware

class CustomUserAgent(UserAgentMiddleware):
    def process_request(self, request, spider):
        ua = 'Mozilla/5.0 (Windows NT 6.1;WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/563.3'
        request.headers.setdefault('User-Agent', ua)
class CustomProxy(object):
    def process_request(self, request, spider):
        request.meta['proxy'] = '110.73.35.17:8123'



