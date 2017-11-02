# -*- coding:utf-8 -*-
"""
File Name: liebiao
Version:
Description:
Author: liuxuewen
Date: 2017/5/25 15:15
"""
import re
import sys
import requests
import scrapy
from bs4 import BeautifulSoup
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from liebiao.items import LiebiaoItem
from liebiao.utils.tools import get_hash, is_in,add_hash_url
from liebiao.utils.comm_log import logger

reload(sys)
sys.setdefaultencoding("utf-8")


class SpiderLiebiao(scrapy.spiders.Spider):
    name = 'liebiao'
    start_urls = ['http://www.liebiao.com']

    def __init__(self):
        self.bags = ['danjianbao', 'shuangjianbao', 'qianba', 'shoutibao']
        self.categoris = ['xiangbao', 'shoushi']

    def parse_detail(self, response):
        # mn res=requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        try:
            title = soup.find('h1', class_='detail-title').text.strip()
        except:
            title = ''
        update_time = soup.find('span', attrs={'title': True}).text.strip()

        try:
            category = soup.find('span', text=u'分类').find_parent('dt').find_next_sibling('dd').text.strip()
        except:
            category = ''
        price = soup.find('span', text=u'价格').find_parent('dt').find_next_sibling('dd').text.replace('元', '').strip()
        address = soup.find('span', text=u'地址').find_parent('dt').find_next_sibling('dd').text.\
            replace(' ', '').replace(' ', '').replace('	','').replace('\n', '').strip()

        try:
            linkman = soup.select('.lx-name .name')[0].text.strip()
        except:
            linkman = ''

        phone = soup.select('.lxr-phone p span')[0].text
        detail_description = soup.find('div', class_='xiangqing').text.strip()
        url_hash = response.meta['url_hash']
        add_hash_url(url_hash)
        item = LiebiaoItem(title=title, update_time=update_time, category=category, price=price, address=address,
                           linkman=linkman, phone=phone, detail_description=detail_description, url=response.url,
                           url_hash=url_hash)
        yield item

    def parse_city(self, response):
        for category in self.categoris:
            for page in range(1, 100):
                res = requests.get(response.url + '{}/index{}.html'.format(category, page))
                soup = BeautifulSoup(res.text, 'lxml')
                items = soup.select('.info-list .f-img a')
                for item in items:
                    url = item['href']
                    url_hash = get_hash(url)
                    if not is_in(url_hash):
                        yield scrapy.Request(url, callback=self.parse_detail, meta={'url_hash': url_hash})
                page_next = soup.find('li', class_='next disabled')
                if page_next:
                    break
                    # print len(s)

    def parse(self, response):

        soup = BeautifulSoup(response.text, 'lxml')
        city_items = soup.find('div', class_='box w_d').select('dl dd a')
        for item in city_items:
            city_link = item['href']
            yield scrapy.Request(city_link, callback=self.parse_city)
            # self.parse_city(city_link)


def run(name=SpiderLiebiao.name):
    process = CrawlerProcess(get_project_settings())
    process.crawl(name)
    # the script will block here until the crawling is finished
    process.start()
    process.join()


if __name__ == '__main__':
    run()
