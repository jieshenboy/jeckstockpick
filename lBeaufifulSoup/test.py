#!/usr/bin/evn python
#-*- coding:utf-8 -*-
import re
from bs4 import BeautifulSoup
import urllib2
from mylog import MyLog as mylog


def getResponseContent( url):

    try:
        response = urllib2.urlopen(url.encode('utf8'))
    except:
        print('1')

    else:

        return response.read()
URL = r'http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html'
htmlContent = getResponseContent(URL)
soup = BeautifulSoup(htmlContent,'lxml')
tag = soup.find_all(re.compile('p'))[-1]
print(tag)
