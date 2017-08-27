# -*- coding: utf-8 -*-
from urllib.parse import urljoin

import scrapy
from bs4 import BeautifulSoup

from anondrapy.items import Article

ANOND_BASE_URL = 'https://anond.hatelabo.jp'


class AnondSpider(scrapy.Spider):
    name = 'anond'
    allowed_domains = ['anond.hatelabo.jp']
    start_urls = ['https://anond.hatelabo.jp']

    def parse(self, response):
        for section in response.css('.body>.section'):

            item = Article()
            item['title'] = self.extract_title_from_section(section)
            item['link'] = self.extract_link_from_section(section)
            item['key'] = item['link'].strip(ANOND_BASE_URL).strip('/')
            item['body'] = self.extract_body_from_section(section)
            yield item

    def extract_title_from_section(self, section):
        title_html = section.css('h3').extract_first()
        # get rid of first squared string ('■')
        title = BeautifulSoup(title_html, 'lxml').get_text().strip()[1:]
        return title

    def extract_link_from_section(selfs, section):
        link = section.css('h3 a:not(.keyword)').css('a::attr("href")').extract_first()
        link = urljoin(ANOND_BASE_URL, link)
        return link

    def extract_body_from_section(self, section):
        body_htmls = section.css('p:not(.share-button)').css('p:not(.sectionfooter)').extract()
        body = [BeautifulSoup(body, 'lxml').get_text() for body in body_htmls]
        return body
