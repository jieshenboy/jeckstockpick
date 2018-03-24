#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
注意：因为不同的网站会根据user-agent返回网页，所以如果有条件的话
尽可能的使用一个固定的user-agent
'''
import urllib2
import userAgents

class Urllib2ModifyHeader(object):
    def __init__(self):
        #这个是PC+IE 的User-Agent
        PIUA = userAgents.pcUserAgent.get('IE 9.0')
        #这个是mobile+UC的User-Agent
        MUUA = userAgents.mobileUserAgent.get('UC standard')

        #测试用的网站选择有道翻译
        self.url = 'http://fanyi.youdao.com'
        self.useUserAgent(PIUA,1)
        self.useUserAgent(MUUA,2)

    def useUserAgent(self,userAgent,name):
        request = urllib2.Request(self.url)
        request.add_header(userAgent.split(':')[0],userAgent.split(':')[1])
        response = urllib2.urlopen(request)
        fileName = str(name) + '.html'
        with open(fileName, 'a') as fp:
            fp.write("%s\n\n" %userAgent)
            fp.write(response.read())

if __name__=="__main__":
    umh = Urllib2ModifyHeader()


