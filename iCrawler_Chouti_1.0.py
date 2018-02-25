# -*- coding: utf-8 -*-
#!/usr/bin/env python2.7

import requests
from bs4 import BeautifulSoup
import os
import re
import xlwt
import time
import datetime
ver=datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')


header = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36','Referer': "http:://http://www.mzitu.com/"}
parser = 'html.parser'

j=1
for i in range(1):
    url = "http://dig.chouti.com/all/hot/recent/"+str(i)  # 爬取目标
    cur_page = requests.get(url, headers=header)
    soup = BeautifulSoup(cur_page.text, parser)
    newsConts=soup.find_all(attrs={'class':'news-content'})
    for newsCont in newsConts:
        newsTit=newsCont.find("a").text.replace("","")
        newsLink=newsCont.find("a")['href']
        print "编号："+str(j)
        print newsTit
        print newsLink
        j=j+1
