#!/usr/bin/env python
# -*- coding:utf-8 -*-

import scrapy
from MangarSpider.items import MangarspiderItem

class HhmmooSpider(scrapy.Spider):
    name = 'juruzhanduix'
    start_urls = ['http://www.hhmmoo.com/manhua5433.html']

    def parse(self, response):
        sel = scrapy.Selector(response)
        MangarspiderItem(manga_title=u'巨乳战队')
        MangarspiderItem(vol_num=u'1')
        MangarspiderItem(page_num=u'1')
        MangarspiderItem(page_url=u'1')
        return MangarspiderItem