#!/usr/bin/env python
#-*- coding:utf-8 -*-

from selenium import webdriver
from mylog import MyLog as mylog
import os
import time

class GetCartoon(object):
    def __init__(self):
        self.startUrl = u'http://www.1kkk.com/ch1-518896/'
        print("11")
        self.log = mylog()
        print("12")
        self.browser = self.getBrowser()
        print("13")
        self.saveCartoon(self.browser)
        print("14")


    def getBrowser(self):
        browser = webdriver.Firefox()
        print("15")
        try:
            browser.get(self.startUrl)
            print("16")
        except:
            mylog.info('open the %s failed' %self.startUrl)
        browser.implicitly_wait(20)
        return browser

    def saveCartoon(self, browser):
        cartoonTitle = browser.title.split('_')[0]
        self.createDir(cartoonTitle)
        os.chdir(cartoonTitle)
        print("1")
        sumPage = int(self.browser.find_element_by_xpath('//div[@class="chapterpager"][1]/a[-1]').text)
        i = 1
        while i<=sumPage:
            print("2")
            imgName = str(i) + ".png"
            browser.get_screenshot_as_file(imgName)
            self.log.info('save img %s' %imgName)
            i += 1
            NextTag = browser.find_element_by_xpath('//div[@class="container"][2]/a[-1]')
            NextTag.chick()
            time.sleep(5)
        self.log.info('save img sccess')
        exit()

    def createDir(self, dirName):
        if os.path.exists(dirName):
            self.log.error('create directory %s failed, have a same name file or directory' %dirName)
        else:
            try:
                os.makedirs(dirName)
            except:
                self.log.error('create directory %s failed' %dirName)
            else:
                self.log.info('create directory %s success' %dirName)

if __name__=="__main__":
    GC = GetCartoon()
