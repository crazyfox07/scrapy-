# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
from scrapy.log import logger
import pymysql
import datetime

class AmazonPipeline(object):
    def open_spider(self, spider):
        logger.info('open_spider: {}'.format(datetime.datetime.now()))
        self.conn = pymysql.connect(host='99.48.58.95', port=3306, user='root', passwd='mime@123', db='spider',
                                    charset='utf8')
        # 创建游标
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = '''
            insert into spider.crawl_amazon(title,price,url,create_time) VALUES (%s, %s, %s, %s);
            '''
        try:
            self.cursor.execute(sql,(item['item_title'], item['item_price'], item['item_url'], datetime.datetime.now()))
            self.conn.commit()
        except:
            raise DropItem('12345')
        else:
            return item

    def close_spider(self, spider):
        self.conn.close()
        logger.info('close_spider: {}'.format(datetime.datetime.now()))

