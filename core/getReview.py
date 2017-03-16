#! /usr/bin/env python
# -*- coding utf-8 -*-
from core.getHTML import getPageHtml
from core.searchProducts import searchProducts
import requests as rq
import re
def getReview(productAndSellerID,productName,reviewPageNumber):

    for item in range(len(productAndSellerID)):
        urls = []
        for i in list(range(reviewPageNumber)):
            urls.append(
                'https://rate.tmall.com/list_detail_rate.htm?itemId={}&sellerId={}&currentPage={}'
                .format(productAndSellerID[item][0],productAndSellerID[item][3],i))
            # urls.append('https://rate.tmall.com/list_detail_rate.htm?itemId=538921269672&spuId=702279218&sellerId=1714128138&order=3&currentPage=%s'
            # %i)
        reviewContent = []
        username = []
        reviewDate = []
        runningTimes = 1
        # print(urls)

        for url in urls:
            content = rq.get(url).text
            print('正在搜索第{}页的评论，请稍后。。。'.format(runningTimes))
            username.extend(re.findall('"displayUserNick":"(.*?)"', content))
            reviewDate.extend(re.findall(re.compile('"rateDate":"(.*?)","reply"'), content))
            reviewContent.extend(re.findall(re.compile('"rateContent":"(.*?)","rateDate"'), content))
            runningTimes += 1
            if runningTimes == reviewPageNumber:
                runningTimes = 0

        #for j in range(0, len(reviewContent)):
            #print(reviewContent[j] + '\n')
        file = open("F:\E-Site Web Crawler\Reviews\{}.csv".format(productAndSellerID[item][0]), 'w', encoding='utf-8')
        for i in list(range(0, len(username))):
            file.write(','.join((username[i], reviewDate[i], reviewContent[i])) + '\n')
        file.close()