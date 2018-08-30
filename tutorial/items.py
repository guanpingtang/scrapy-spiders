# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# cms_content内容
class zhdj_cms_content(scrapy.Item):
    title = scrapy.Field()
    time = scrapy.Field()
    detail = scrapy.Field()
    url = scrapy.Field()
    created_at = scrapy.Field()
