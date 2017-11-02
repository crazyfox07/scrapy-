# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import datetime
import sys
import time
import traceback

import pymysql
from scrapy.exceptions import DropItem
from twisted.enterprise import adbapi
from twisted.internet import defer

from liebiao.utils.comm_log import logger
from liebiao.utils.tools import remove_hash_url

reload(sys)
sys.setdefaultencoding("utf-8")

class LiebiaoPipeline(object):

    def process_item(self, item, spider):
        if (item['price']=='面议' or float(item['price'])>=500) and cmp(item['update_time'],'2016-12-01')>=0 and item['category'].find('服装')==-1:
            return item
        else:
            raise DropItem('price<500 or updata_time has been out-of-date: {}'.format(item))

class MySQLStorePipeline(object):
    def __init__(self, host, user, passwd, db):
        self.conn = pymysql.connect(host=host, user=user, passwd=passwd, db=db, charset='utf8')
        self.cursor = self.conn.cursor()

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            user=crawler.settings.get('MYSQL_USER'),
            passwd=crawler.settings.get('MYSQL_PASSWD'),
            db=crawler.settings.get('MYSQL_DBNAME')
        )

    def process_item(self, item, spider):

        sql = """insert	into crawl_liebiao
                        (title,update_time,category,price,address,linkman,phone,detail_description,add_time,url_hash,url)
                         VALUES	(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        args = (
            item['title'],
            item["update_time"],
            item["category"],
            item["price"],
            item["address"],
            item['linkman'],
            item['phone'],
            item['detail_description'][:4000],
            datetime.datetime.now(),
            item["url_hash"],
            item["url"],
        )

        try:
            self.cursor.execute(sql, args)
            self.conn.commit()
            logger.info("insert a record into database")
        except pymysql.Error, e:
            logger.info("mysql error: {}".format(str(e)))
            remove_hash_url(item['url_hash'])
        return item


class MysqlWriter(object):

    def __init__(self, dbpool):
        self.start_time = ''
        self.end_time = ''
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbargs = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
        return cls(dbpool)

    def open_spider(self, spider):
        print 'begin:'
        self.start_time = time.time()

    def close_spider(self, spider):
        self.dbpool.close()
        self.end_time = time.time()
        print 'end'
        print 'time use: {}'.format(self.end_time - self.start_time)

    @defer.inlineCallbacks
    def process_item(self, item, spider):
        try:
            yield self.dbpool.runInteraction(self.do_replace, item)
        except:
            logger.error(traceback.format_exc())
        else:
            logger.info('insert a record')
        defer.returnValue(item)

    @staticmethod
    def do_replace(tx, item):
        #print item["title"],item["title"],item["category"],item["address"],'333333333'
        sql = """insert	into crawl_liebiao
                (title,update_time,category,price,address,linkman,phone,detail_description,add_time,url_hash,url)
                 VALUES	(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        args = (
            item['title'],
            item["update_time"],
            item["category"],
            item["price"],
            item["address"],
            item['linkman'],
            item['phone'],
            item['detail_description'][:4000],
            datetime.datetime.now(),
            item["url_hash"],
            item["url"],
        )
        tx.execute(sql, args)

if __name__ == '__main__':
    a='面议'
    if a=='面议':
        print '111'
    if a==u'面议':
        print '222'


