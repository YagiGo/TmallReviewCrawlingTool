#! /usr/bin/env python
# -*- coding utf-8 -*-
import requests as rq
import re
import time
import random
def checkIfCAPTCHATriggered(content):
    noContent = []
    # 可能是触发了验证码也可能没有更多评论显示，需要判断一下
    pattern = re.compile(r'[a-zA-z]+://[^\s]*')
    firstUrl = pattern.findall(content)  # 找到第一个域名,如果是正常的应该是tmall.com
    if(len(firstUrl) == 0):
        return noContent
    else:
        print(firstUrl)
        pattern2 = re.compile(r'(?i)^https?://(?:\w+\.)*?(\w*\.(?:com\.cn|cn|com|net))[\\\/]*')  # 匹配顶级域名
        isItCAPTCHA = pattern2.findall(firstUrl[0])  # 如果是触发了验证码，此时的域名应该是taobao.com
        return isItCAPTCHA
urls = []
for i in list(range(1,1000)):
    urls.append('https://rate.tmall.com/list_detail_rate.htm?itemId=543035827310&sellerId=702279218&currentPage=%s' %i)
    #urls.append('https://rate.tmall.com/list_detail_rate.htm?itemId=538921269672&spuId=702279218&sellerId=1714128138&order=3&currentPage=%s'
 #%i)
reviewContent = []
username = []
reviewDate = []
runningTimes = 1
#print(urls)
previousPage = []
currentPage = []
for url in urls:
    content = rq.get(url).text
    currentPage = re.findall(re.compile('"rateDate":"(.*?)","reply"'), content)
    print(previousPage)
    print(currentPage)
    print('正在搜索第{}页的评论，请稍后。。。'.format(runningTimes))
    if (len(re.findall(re.compile('"rateDate":"(.*?)","reply"'), content)) == 0):
        # 可能是触发了验证码也可能没有更多评论显示，需要判断一下
        delayMin = 2
        delayMax = 4
        '''pattern = re.compile(r'[a-zA-z]+://[^\s]*')
        firstUrl = pattern.findall(content)  # 找到第一个域名,如果是正常的应该是tmall.com
        pattern2 = re.compile(r'(?i)^https?://(?:\w+\.)*?(\w*\.(?:com\.cn|cn|com|net))[\\\/]*')  # 匹配顶级域名
        isItCAPTCHA = pattern2.findall(firstUrl[0])  # 如果是触发了验证码，此时的域名应该是taobao.com'''
        isItCAPTCHA = checkIfCAPTCHATriggered(content)
        while (isItCAPTCHA == ['taobao.com']):  # 延迟几秒重新加载，直至不再触发
            print('爬取速度过快，验证码输入被触发！等待重试')
            #print(isItCAPTCHA[0])
            time.sleep(random.randint(delayMin, delayMax))
            delayMin += 1
            delayMax += 1
            content = rq.get(url).text
            # print(content)
            isItCAPTCHA = checkIfCAPTCHATriggered(content)
            # urlOnHold.append(url)
        currentPage = re.findall(re.compile('"rateDate":"(.*?)","reply"'), content)
    if (len(re.findall(re.compile('"rateDate":"(.*?)","reply"'), content)) == 0) \
            or previousPage == currentPage :
        print('Empty!')
        break
        #print(previousPage)
        #print(currentPage)
    username.extend(re.findall('"displayUserNick":"(.*?)"', content))
    previousPage = re.findall(re.compile('"rateDate":"(.*?)","reply"'), content)
    reviewDate.extend(previousPage)
    reviewContent.extend(re.findall(re.compile('"rateContent":"(.*?)","rateDate"'), content))
    runningTimes += 1

#for j in range(0, len(reviewContent)):
#    print(reviewContent[j] + '\n')
file = open('F:\E-Site Web Crawler\Test.csv', 'w')
for i in list(range(0,len(username))):
        file.write(','.join((username[i],reviewDate[i],reviewContent[i])) + '\n')
file.close()

