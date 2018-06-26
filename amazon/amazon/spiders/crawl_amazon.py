# -*- coding:utf-8 -*-
"""
File Name: crawl_amazon
Version:
Description:
Author: liuxuewen
Date: 2018/6/25 17:50
"""
import re
import scrapy
from bs4 import BeautifulSoup

from amazon.items import AmazonItem


class CrawlAmazon(scrapy.Spider):
    name = 'amazon'

    def start_requests(self):
        for page in range(1,10):
            url = 'https://www.amazon.cn/s/ref=sr_pg_2?rh=n:2016156051,n:!2016157051,n:865184051,n:100275071,n:100276071&page={}&bbn=100276071&ie=UTF8&qid=1529918847'.format(page)
            yield scrapy.Request(url=url, callback=self.parse_page)

    def parse_page(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        items = soup.select('#s-results-list-atf li .s-item-container')
        for item in items:
            title = item.find('h2', attrs={'data-attribute':True}).get('data-attribute')
            try:
                price = item.find('span', class_=re.compile("a-size-base")).text.strip()
            except:
                price = ''
            link = item.find('a', class_=re.compile('a-link-normal')).get('href')
            amazon_item = AmazonItem(
                item_title = title,
                item_price = price,
                item_url = link,
            )
            yield amazon_item