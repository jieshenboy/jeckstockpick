#!/usr/bin/env python
#-*- coding:utf-8 -*-
from myLog import MyLog

if __name__ == "__main__":
    ml = MyLog()
    ml.debug('debug')
    ml.info('info')
    ml.warn('warn')
    ml.error('error')
    ml.critical('critical')