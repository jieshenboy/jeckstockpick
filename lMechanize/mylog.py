#!/usr/bin/env python
#-*- coding:utf-8 -*-


import logging
import getpass
import sys
#定义MyLog类
class MyLog(object):
    #类MyLog的构造函数
    def __init__(self):
        self.user = getpass.getuser()
        self.logger = logging.getLogger(self.user)
        self.logger.setLevel(logging.DEBUG)

        #日志文件名
        self.logFile = sys.argv[0][0:-3] + '.log'
        self.formatter = logging.Formatter('%(asctime)-12s %(levelname)-8s %(name)-10s %(message)-12s\r\n')

        #日志显示到屏幕上并输出到日志文件内
        self.logHand = logging.FileHandler(self.logFile, encoding='utf8')
        self.logHand.setFormatter(self.formatter)
        self.logHand.setLevel(logging.DEBUG)

        self.logHandSt = logging.StreamHandler()
        self.logHandSt.setFormatter(logging._defaultFormatter)
        self.logHandSt.setLevel(logging.DEBUG)

        self.logger.addHandler(self.logHand)
        self.logger.addHandler(self.logHandSt)

        #日志对应的5个级别如下：
    def debug(self, msg):
        self.logger.debug(msg)

    def info(self,msg):
        self.logger.info(msg)

    def warn(self, msg):
        self.logger.warn(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)

if __name__=="__main__":
    mylog = MyLog()
    mylog.debug(u"I'm debug 测试中文")
    mylog.info(u"I'm info")
    mylog.warn(u"I'm warn")
    mylog.error(u"I'm error")
    mylog.critical("I'm critical")

