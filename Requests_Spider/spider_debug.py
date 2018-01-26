#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from lxml import html
import re

page = requests.get("http://www.hhmmoo.com/manhua5433.html")
tree = html.fromstring(page.text)
elm_list = tree.xpath("//a[@class='l_s']")
vol_dic = {}
vol_list = {}
for elm in elm_list:
    vol_list[elm.text] = elm.attrib['href']
    print vol_list
