# -*- coding: utf-8 -*-
# Create your views here.
import urllib2, re, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://simwood.tmall.com/p/rd756186.htm")

''' 慢慢下拉到底部 '''
for row in range(5):
    driver.execute_script("window.scrollBy(0,2000)")
    time.sleep(1)

''' 获取源码 '''
html_source = driver.page_source

''' 获取要得到的商品链接 '''
dict1={}
p=re.compile('\/\/detail.tmall.com/item.htm.*?id\=(\d+)')
for row in p.findall(html_source):
    dict1[row]='https://item.taobao.com/item.htm?id={}'.format(row)

for row in dict1:
    print dict1[row]

driver.close()
