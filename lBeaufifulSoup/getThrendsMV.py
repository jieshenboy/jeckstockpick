#!/usr/bin/env python
#-*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import urllib2
import codecs
import time
from mylog import MyLog as mylog
import resource
import random
from save2mysql import savebooksData
import sys
reload(sys)#python的str默认是ascii编码，和unicode编码冲突,这一部分可以载入utf8
sys.setdefaultencoding('utf8')


class Item(object):
    top_num = None #排名
    score = None #打分
    mvName = None #MV的名字
    singer = None #演唱者
    releasTime = None #释放时间

class GetMvList(object):
    """
    The all data from www.yinyuetai.com
    所有数据来自www.yinyuetai.com
    """
    def __init__(self):
        self.urlBase = 'http://vchart.yinyuetai.com/vchart/trends?'
        self.areasDic = {'ML':'Mainland','HT':'Hongkong&Taiwan','US':'Americ','KR':'Korea','JP':'Japan'}
        self.log = mylog()
        self.getUrls()


    def getUrls(self):
        areas = ['ML','HT','US','KR','JP']
        pages = [str(i) for i in range(1,4)]
        for area in areas:
            urls = []
            for page in pages:
                urlEnd = 'area=' + area + '&page='+page
                url = self.urlBase + urlEnd
                urls.append(url)
                self.log.info(u'添加URL：%s 到URLS' %url)
            self.spider(area,urls)


    def getResponseContent(self, url):
        """从页面返回数据"""
        fakeHeaders = {'User-Agent':self.getRandomHeaders()}
        request = urllib2.Request(url.encode('utf8'), headers=fakeHeaders)
        proxy = urllib2.ProxyHandler({'http':'http://'+self.getRandomProxy()})
        openner = urllib2.build_opener(proxy)
        urllib2.install_opener(openner)
        try:
            response = urllib2.urlopen(request)
            time.sleep(1)
        except:
            self.log.error(u'Python 返回URL：%s 数据失败' %url)
            return ''
        else:
            self.log.info(u'Python 返回URL:%s 数据成功' %url)
            return response.read()

    def spider(self, area, urls):
        items = []
        for url in urls:
            responseContent = self.getResponseContent(url)
            if not responseContent:
                continue
            soup = BeautifulSoup(responseContent, 'lxml')
            tags = soup.find_all('li', attrs={'class':'vitem'})#li.vitem
            for tag in tags:
                item = Item()
                item.top_num = tag.find('div', attrs={'class':'top_num'}).get_text()
                if tag.find('h3', attrs={'class':'desc_score'}):
                    item.score = tag.find('h3', attrs={'class':'desc_score'}).get_text()
                else:
                    item.score=tag.find('h3',attrs={'class':'asc_score'}).get_text()
                item.mvName = tag.find('img').get('alt')
                item.singer = tag.find('a', attrs={'class':'special'}).get_text()
                item.releasTime = tag.find('p', attrs = {'class':'c9'}).get_text()
                items.append(item)
                self.log.info(u'添加mvName为<<>%s>的数据成功' %(item.mvName))
            self.piplines(items, area)





    def getRandomProxy(self):
        return random.choice(resource.PROXIES)

    def getRandomHeaders(self):
        return random.choice(resource.UserAgents)





    def piplines(self, items,area):
        fileName = 'mvTopList.txt'
        nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        with codecs.open(fileName, 'a') as fp:
            fp.write('%s ------%s\r\n' %(self.areasDic.get(area),
                                         nowTime))

            for item in items:
                fp.write('%s %s \t %s \t %s \t %s \r\n'
                         %(item.top_num, item.score, item.releasTime, item.singer, item.mvName))

                self.log.info(u'添加mvName为<<%s>>的MV到%s...' %(item.mvName, fileName))
            fp.write('\r\n'*4)

        savebooksData(items)



if __name__=="__main__":
    GML=GetMvList()




