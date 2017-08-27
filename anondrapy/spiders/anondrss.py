# -*- coding: utf-8 -*-

import scrapy
import feedparser
from bs4 import BeautifulSoup

from anondrapy.items import ArticleByDate

ANOND_BASE_URL = 'https://anond.hatelabo.jp'


class AnondRSSSpider(scrapy.Spider):
    name = 'anondrss'
    allowed_domains = ['anond.hatelabo.jp']
    start_urls = ['https://anond.hatelabo.jp/rss']

    def parse(self, response):
        entries = feedparser.parse(response.text)['entries']

        for entry in entries:
            item = ArticleByDate()
            item['title'] = entry['title']
            item['link'] = entry['link']
            item['key'] = item['link'].strip(ANOND_BASE_URL).strip('/')
            item['body'] = BeautifulSoup(entry['content'][0]['value'], 'lxml').get_text().split('\n')
            yield item
