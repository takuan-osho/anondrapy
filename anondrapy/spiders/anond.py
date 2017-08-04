# -*- coding: utf-8 -*-
import scrapy


class AnondSpider(scrapy.Spider):
    name = 'anond'
    allowed_domains = ['anond.hatelabo.jp']
    start_urls = ['https://anond.hatelabo.jp/']

    def parse(self, response):
        pass
