#! /usr/bin/env python
#-*- coding:utf-8 -*-

import sys

class ShowSysModule(object):
    """
    这个类用于展示python标准库中的sys模块
    """
    def __init__(self):
        print(u'sys模块最常用的功能是获取程序的参数')
        self.getArg()
        print(u'其次就是获取当前系统的平台')
        self.getOS()

    def getArg(self):
        print(u'开始获取参数的个数')
        print(u'当前参数有 %d 个' %len(sys.argv))
        print(u'这些参数分别是 %s' %sys.argv)

    def getOS(self):
        print(u'当前系统为：%s' %sys.platform)

if __name__=="__main__":
    ssm = ShowSysModule()