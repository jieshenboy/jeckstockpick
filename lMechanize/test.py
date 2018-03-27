#!/usr/bin/env python
#-*- coding: utf-8 -*-

import mechanize
import sys
reload(sys)#python的str默认是ascii编码，和unicode编码冲突,这一部分可以载入utf8
sys.setdefaultencoding('utf8')

br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_gzip(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20')]

br.open('https://www.baidu.com')

for form in br.forms():
    print(form)
br.select_form(name='f')
br.form['wd'] = 'Python 网络爬虫'
br.submit()
print(br.response().read())