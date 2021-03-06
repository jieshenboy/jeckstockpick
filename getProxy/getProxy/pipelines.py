# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class GetproxyPipeline(object):
    def process_item(self, item, spider):
        fileName = 'proxy.txt'
        with open(fileName, 'a') as fp:
            fp.write(item['ip'].encode('utf8').strip() + '\t')
            fp.write(item['port'].encode('utf8').strip() + '\t')
            fp.write(item['protocol'].encode('utf8').strip() + '\t')
            fp.write('\n')
            fp.write(item['type'].encode('utf8').strip() + '\t')
            fp.write(item['loction'].encode('utf8').strip() + '\t')
            fp.write(item['source'].encode('utf8').strip())
            fp.write('\n')

        return item
