#-*- coding:utf-8 -*-

import MySQLdb
import os.path

class WeatherPipline(object):
    def process_item(self,item, spider):
        cityDate = item['cityDate'].encode('utf8')
        week = item['week'].encode('utf8')
        img = os.path.basename(item['img'])
        weaher = item['weather'].encode('utf8')
        wind = item['wind'].encode('utf8')

        conn = MySQLdb.connect(
            host = 'localhost',
            port = 3306,
            user = 'crawlUSER',
            passwd = 'crawl123',
            db = 'scrapyDB',
            charset = 'utf8'
        )
        cur = conn.cursor()
        cur.execute("INSERT INTO weather(cityDate, week, img, weather, wind) VALUES(%s,%s,%s,%s,%s)",
                    (cityDate, week, img, weaher,wind))
        cur.close()
        conn.commit()
        conn.close()
        return item