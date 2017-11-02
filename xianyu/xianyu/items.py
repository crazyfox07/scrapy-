# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XianyuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    catid=scrapy.Field()
    category=scrapy.Field()
    seller_name= scrapy.Field()
    pub_time= scrapy.Field()
    product_name= scrapy.Field()
    price= scrapy.Field()
    address= scrapy.Field()
    url_hash= scrapy.Field()
    url= scrapy.Field()
