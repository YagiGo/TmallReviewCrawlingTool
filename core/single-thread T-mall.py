#! /usr/bin/env python
# -*- coding utf-8 -*-
import requests as rq
import re
import time
urls = []
for i in list(range(1,5)):
    urls.append('https://rate.tmall.com/list_detail_rate.htm?itemId=538921269672&sellerId=702279218&currentPage=%s' %i)
    #urls.append('https://rate.tmall.com/list_detail_rate.htm?itemId=538921269672&spuId=702279218&sellerId=1714128138&order=3&currentPage=%s'
 #%i)
reviewContent = []
username = []
reviewDate = []
runningTimes = 1
#print(urls)

for url in urls:
    content = rq.get(url).text
    print('正在搜索第{}页的评论，请稍后。。。'.format(runningTimes))
    username.extend(re.findall('"displayUserNick":"(.*?)"', content))
    reviewDate.extend(re.findall(re.compile('"rateDate":"(.*?)","reply"'), content))
    reviewContent.extend(re.findall(re.compile('"rateContent":"(.*?)","rateDate"'), content))
    runningTimes += 1

for j in range(0, len(reviewContent)):
    print(reviewContent[j] + '\n')
file = open('F:\E-Site Web Crawler\E-Site Web Crawler\Reviews\Xiaomi5S.csv', 'w')
for i in list(range(0,len(username))):
        file.write(','.join((username[i],reviewDate[i],reviewContent[i])) + '\n')
file.close()

