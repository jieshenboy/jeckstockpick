#!/usr/bin/evn python
#-*- coding:utf-8 -*-

import re
from bs4 import BeautifulSoup
import urllib2
from mylog import MyLog as mylog

#http://kaijiang.zhcw.com/zhcw/inc/ssq/ssq_wqhg.jsp
class DoubleColorBallItem(object):
    date = None #开奖日期
    order = None #当年的顺序
    red1 = None #第一个红球号码