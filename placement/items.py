# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Product(scrapy.Item):
    link = scrapy.Field()
    name = scrapy.Field()
    year = scrapy.Field()
