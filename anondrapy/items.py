# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticleByDate(scrapy.Item):
    """
    Item for each article from date page
    """
    title = scrapy.Field()
    link = scrapy.Field()
    key = scrapy.Field()
    body = scrapy.Field()
