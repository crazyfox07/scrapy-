# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LiebiaoItem(scrapy.Item):
    title=scrapy.Field()
    update_time= scrapy.Field()
    category = scrapy.Field()
    price= scrapy.Field()
    address= scrapy.Field()
    linkman= scrapy.Field()
    phone= scrapy.Field()
    detail_description= scrapy.Field()
    add_time=scrapy.Field()
    url=scrapy.Field()
    url_hash=scrapy.Field()


