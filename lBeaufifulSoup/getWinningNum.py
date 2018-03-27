#!/usr/bin/evn python
#-*- coding:utf-8 -*-

import re
from bs4 import BeautifulSoup
import urllib2
from mylog import MyLog as mylog
from save2excel import SaveBallDate

import sys
reload(sys)#python的str默认是ascii编码，和unicode编码冲突,这一部分可以载入utf8
sys.setdefaultencoding('utf8')


#http://kaijiang.zhcw.com/zhcw/inc/ssq/ssq_wqhg.jsp
class DoubleColorBallItem(object):
    date = None #开奖日期
    order = None #当年的顺序
    red1 = None #第一个红球号码
    red2 = None #第二个红球的号码
    red3  = None #第三个红球的号码
    red4  = None #第四个红球的号码
    red5 = None #第五个红球的号码
    red6 = None #第六个红球的号码
    blue = None #篮球的号码
    money = None #奖池金额

    firstPrize = None #一等奖中奖人数
    secondPrize = None #二等奖中奖人数

class GetDoubleColorBallNumber(object):
    """
    这个类用于获取双色球中奖号码，返回一个txt文件
    """
    def __init__(self):
        self.urls = []
        self.log = mylog()
        self.getUrls()
        self.items = self.spider(self.urls)
        self.piplines(self.items)
        self.log.info('beging save data to excel \r\n')
        SaveBallDate(self.items)
        self.log.info('save data to excel end ... \r\n')

    def getUrls(self):
        """
        获取数据来源
        :return: self.urls.append()、self.log.info()
        """
        URL = r'http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html'
        htmlContent = self.getResponseContent(URL)
        soup = BeautifulSoup(htmlContent,'lxml')
        tag = soup.find_all(re.compile('p'))[-1]#返回最后一个P标签的值
        pages = tag.strong.get_text()
        for i in xrange(1, int(pages)+1):
            url = r'http://kaijiang.zhcw.com/zhcw/html/ssq/list_' + str(i) + '.html'
            self.urls.append(url)
            self.log.info(u'添加URL:%s 到URLS \r\n' %url)

    def getResponseContent(self,url):
        """
        单独使用一个函数返回页面的返回值，为了后期方便的加入proxy和headers等
        :param url:
        :return:response.read()
        """
        try:
            response = urllib2.urlopen(url.encode('utf8'))
        except:
            self.log.error(u'Python 返回URL：%s 数据失败 \r\n' %url)
        else:
            self.log.info(u'Python 返回URL:%s 数据成功 \r\n' %url)
            return response.read()
    def spider(self,urls):
        """
        这个函数的作用是从获取的数据中过滤得到中奖信息
        :param urls:
        :return: items
        """
        items = []
        for url in urls:
            htmlConten = self.getResponseContent(url)
            soup = BeautifulSoup(htmlConten,'lxml')
            tags = soup.find_all('tr', attrs={})
            for tag in tags:
                if tag.find('em'):
                    item = DoubleColorBallItem()
                    tagTd = tag.find_all('td')
                    item.date = tagTd[0].get_text()
                    item.order = tagTd[1].get_text()
                    tagEm = tagTd[2].find_all('em')
                    item.red1 = tagEm[0].get_text()
                    item.red2 = tagEm[1].get_text()
                    item.red3 = tagEm[2].get_text()
                    item.red4 = tagEm[3].get_text()
                    item.red5 = tagEm[4].get_text()
                    item.red6 = tagEm[5].get_text()
                    item.blue = tagEm[6].get_text()
                    item.money = tagTd[3].find('strong').get_text()
                    item.firstPrize = tagTd[4].find('strong').get_text()
                    item.secondPrize = tagTd[5].find('strong').get_text()
                    items.append(item)
                    self.log.info('获取日期为:%s 的数据成功' %(item.date))
        return items

    def piplines(self,items):
        fileName = u'双色球.txt'.encode('GBK')
        with open(fileName, 'w') as fp:
            for item in items:
                fp.write('%s %s \t %s %s %s %s %s %s %s \t %s \t %s %s \n'
                         %(item.date, item.order, item.red1, item.red2, item.red3, item.red4,item.red5, item.red6,
                           item.blue, item.money, item.firstPrize, item.secondPrize))
                self.log.info(u'将日期为:%s 的数据存入"%s"...' %(item.date, fileName.decode('GBK')))

if __name__ == "__main__":
    GDCBN = GetDoubleColorBallNumber()
