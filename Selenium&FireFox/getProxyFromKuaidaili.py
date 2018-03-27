#! /usr/bin/env python
#-*- coding:utf-8 -*-

from selenium import webdriver
from mylog import MyLog as mylog

class Item(object):
    ip = None #代理IP
    port = None #代理端口
    anonymous = None #是否匿名
    support = None #支持的协议
    local = None #物理地址
    speed = None #代理速度

class GetProxy(object):
    def __init__(self):
        #https://www.kuaidaili.com/free/inha/1/
        self.startUrl = 'https://www.kuaidaili.com/free/'
        self.log = mylog()
        self.urls = self.getUrls()
        self.proxyList = self.getProxyList(self.urls)
        self.fileName = 'proxy.txt'
        self.saveFile(self.fileName, self.proxyList)

    def getUrls(self):
        urls = []
        for i in xrange(1,11):
            url = self.startUrl + 'inha/' + str(i) + '/'
            urls.append(url)
            self.log.info('get url %s to urls' %url)
        return urls

    def getProxyList(self, urls):
        browser = webdriver.Firefox()
        proxyList = []
        item = Item()
        for url in urls:
            browser.get(url)
            browser.implicitly_wait(5)
            elements = browser.find_elements_by_xpath('//tbody/tr')
            for element in elements:
                item.ip = element.find_element_by_xpath('./td[1]').text.encode('utf8')
                item.port= element.find_element_by_xpath('./td[2]').text.encode('utf8')
                item.anonymous = element.find_element_by_xpath('./td[3]').text.encode('utf8')
                item.support = element.find_element_by_xpath('./td[4]').text.encode('utf8')
                item.local = element.find_element_by_xpath('./td[5]').text.encode('utf8')
                item.speed = element.find_element_by_xpath('./td[6]').text.encode('utf8')
                proxyList.append(item)
                self.log.info('add proxy %s:%s to list' %(item.ip,
                                                          item.port))
        browser.quit()
        return proxyList

    def saveFile(self, fileName, proxyList):
        self.log.info('add all proxy to %s' %fileName)
        with open(fileName, 'w') as fp:
            for item in proxyList:
                fp.write(item.ip + '\t')
                fp.write(item.port+'\t')
                fp.write(item.anonymous  + '\t')
                fp.write(item.support + '\t')
                fp.write(item.local + '\t')
                fp.write(item.speed + '\r\n')

if __name__=="__main__":
    GP = GetProxy()





