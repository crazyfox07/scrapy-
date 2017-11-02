# -*- coding:utf-8 -*-
"""
File Name: spider_xianyu
Version:
Description:
Author: liuxuewen
Date: 2017/5/31 16:54
"""
import sys

import re

import datetime
import requests
import time
from bs4 import BeautifulSoup
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from xianyu.items import XianyuItem
import urlparse
from xianyu.utils.tools import get_hash, is_in, add_url_hash
import json

reload(sys)
sys.setdefaultencoding("utf-8")


class SpiderXianyu(scrapy.spiders.Spider):
    name = 'xianyu'
    start_urls = [
        # 女包
        'https://s.2.taobao.com/list/list.htm?spm=2007.1000337.0.0.Qe63N5&catid=50456012&st_edtime=1&page=1&ist=1',
        # 男包
        'https://s.2.taobao.com/list/list.htm?spm=2007.1000337.0.0.vtEoc5&catid=50430022&st_trust=1&page=1&ist=1',
        # 腰带
        'https://s.2.taobao.com/list/list.htm?spm=2007.1000337.0.0.CIVh9X&catid=50430023&st_trust=1&page=1&q=%D1%FC%B4%F8&ist=1',
        # 皮带
        'https://s.2.taobao.com/list/list.htm?spm=2007.1000337.0.0.ObaAbc&catid=50430023&st_trust=1&page=1&q=%C6%A4%B4%F8&ist=1',
        # 机械表
        'https://s.2.taobao.com/list/list.htm?spm=2007.1000337.0.0.QIMowf&catid=50100500&st_trust=1&page=1&q=%BB%FA%D0%B5&ist=1',
        # 石英表
        'https://s.2.taobao.com/list/list.htm?spm=2007.1000337.0.0.4uYiTW&catid=50100500&st_trust=1&page=1&q=%CA%AF%D3%A2%B1%ED&ist=1',
        # 黄金
        'https://s.2.taobao.com/list/list.htm?spm=2007.1000337.0.0.hjyjCF&catid=50100497&st_trust=1&page=1&ist=1',
        # 钻石
        'https://s.2.taobao.com/list/list.htm?spm=2007.1000337.0.0.BeAozi&catid=50100499&st_trust=1&page=1&ist=1',
        # 铂金
        'https://s.2.taobao.com/list/list.htm?spm=2007.1000337.0.0.bWGYnu&catid=50100414&st_trust=1&page=1&q=%B2%AC%BD%F0&ist=1',
        # 珍珠
        'https://s.2.taobao.com/list/list.htm?spm=2007.1000337.0.0.CLtjSN&catid=50100414&st_trust=1&page=1&q=%D5%E4%D6%E9&ist=1',
        # 眼镜
        'https://s.2.taobao.com/list/list.htm?spm=2007.1000337.0.0.GS8W4l&stype=1&st_trust=1&page=1&q=%D1%DB%BE%B5&ist=1',
        # 手链
        'https://s.2.taobao.com/list/list.htm?spm=2007.1000337.0.0.Tteplm&stype=1&st_trust=1&page=1&q=%CA%D6%C1%B4&ist=1',
        # 项链
        'https://s.2.taobao.com/list/list.htm?spm=2007.1000337.0.0.AyAj9b&st_trust=1&page=1&q=%CF%EE%C1%B4&ist=1',
        # 吊坠
        'https://s.2.taobao.com/list/list.htm?spm=2007.1000337.0.0.iF7pwK&st_trust=1&page=1&q=%B5%F5%D7%B9&ist=1',
        # 手镯
        'https://s.2.taobao.com/list/list.htm?spm=2007.1000337.0.0.Bi3Ukf&st_trust=1&page=1&q=%CA%D6%EF%ED&ist=1',
        # 戒指
        'https://s.2.taobao.com/list/list.htm?spm=2007.1000337.0.0.R1WISW&st_trust=1&page=1&q=%BD%E4%D6%B8&ist=1',
        # 水晶
        'https://s.2.taobao.com/list/list.htm?spm=2007.1000337.0.0.m9UCHB&st_trust=1&page=1&q=%CB%AE%BE%A7&ist=1'
    ]  

    

    def handle_time(self, latest_time):
        if latest_time.find('小时前') != -1:
            timestamp = time.time()-int(latest_time.split('小时前')[0])*3600
        elif latest_time.find('分钟前') != -1:
            timestamp = time.time() - int(latest_time.split('分钟前')[0]) * 60
        elif latest_time.find('天前') != -1:
            timestamp = time.time() - int(latest_time.split('天前')[0]) * 3600*24
        else:
            return latest_time.replace('.','-')
        publish_time = datetime.date.fromtimestamp(timestamp)
        return str(publish_time)

    def get_page(self, url):
        page = urlparse.parse_qs(urlparse.urlparse(url).query)['page'][0]
        return int(page)

    def parse_page(self, response):
        pat = re.compile('.*?\((.*)\)', re.S)
        content = re.findall(pat, response.text)[0]
        items = json.loads(content)['idle']
        catid = response.meta['catid']
        category = response.meta['category']
        for item in items:
            url = 'https:' + item['item']['itemUrl'].split(';')[0]
            url_hash = get_hash(url)
            if not is_in(url_hash):
                seller_name = item['user']['userNick']
                latest_time1 = item['item']['publishTime']
                pub_time = self.handle_time(latest_time1)
                product_name = item['item']['title']
                price = item['item']['price']
                address = item['item']['provcity']
                add_url_hash(url_hash)
                xyitem = XianyuItem(catid=catid,
                                    category=category,
                                    seller_name=seller_name,
                                    pub_time=pub_time,
                                    product_name=product_name,
                                    price=price,
                                    address=address,
                                    url_hash=url_hash,
                                    url=url)
                yield xyitem

    def parse(self, response):
        print response.url
        try:
            catid = re.findall('catid=(\d+)', response.url)[0]
        except:
            catid ='50100442'
        soup = BeautifulSoup(response.text, 'lxml')

        try:
            category = soup.find('h3', class_='search-keywords').text.strip() or soup.find('span', class_='cur-category').find('h1').text.strip()
        except:
            category = response.url+'333'

        items = soup.find_all('div', class_='item-block item-idle sh-roundbox')

        for item in items:
            url = 'https:' + item.find('div', class_='item-pic').find('a')['href'].strip()
            url_hash = get_hash(url)
            if not is_in(url_hash):
                seller_name = item.find('div', class_='seller-nick').find('a').text.strip()
                latest_time = item.find('span', class_='item-pub-time').text.strip()
                pub_time = self.handle_time(latest_time)
                product_name = item.find('div', class_='item-pic').find('a')['title'].strip()
                product_name = re.sub('&lt.*?gt;|<.*?>', '', product_name)
                price = item.find('span', class_='price').text.strip().replace('&yen', '')
                address = item.find('div', class_='item-location').text.strip()
                xyitem = XianyuItem(catid=catid,
                                    category=category,
                                    seller_name=seller_name,
                                    pub_time=pub_time,
                                    product_name=product_name,
                                    price=price,
                                    address=address,
                                    url_hash=url_hash,
                                    url=url)
                add_url_hash(url_hash)
                yield xyitem

        page = self.get_page(response.url)
        url2 = re.sub('list\.htm.*?&', 'waterfall/waterfall.htm?wp={}&_ksTS=1496296595232_140&callback=jsonp141&stype=1&', response.url).format(3*page-1, page)
        url3 = re.sub('list\.htm.*?&', 'waterfall/waterfall.htm?wp={}&_ksTS=1496296595232_140&callback=jsonp141&stype=1&', response.url).format(3*page, page)
        #url2='https://s.2.taobao.com/list/waterfall/waterfall.htm?wp={}&_ksTS=1496296595232_140&callback=jsonp141&stype=1&catid=50456012&st_edtime=1&page={}&ist=1'.format(3*page-1,page)
        #url3='https://s.2.taobao.com/list/waterfall/waterfall.htm?wp={}&_ksTS=1496296678218_246&callback=jsonp247&stype=1&catid=50456012&st_edtime=1&page={}&ist=1'.format(3*page,page)
        yield scrapy.Request(url2, callback=self.parse_page, meta={'catid': catid, 'category': category})
        yield scrapy.Request(url3, callback=self.parse_page, meta={'catid': catid, 'category': category})

        if soup.find(text=u'下一页'):
            url = re.sub('page=\d+', 'page=' + str(page + 1), response.url)
            yield scrapy.Request(url, callback=self.parse)


def run(name=SpiderXianyu.name):
    process = CrawlerProcess(get_project_settings())
    process.crawl(name)
    # the script will block here until the crawling is finished
    process.start()
    process.join()


if __name__ == '__main__':
    run()

