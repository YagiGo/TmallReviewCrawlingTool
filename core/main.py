#! /usr/bin/env python
# -*- coding utf-8 -*-
from core.getHTML import getPageHtml
from core.searchProducts import searchProducts,createDatabase
from core.getReview import getReview
import time

if __name__ == '__main__':
    start = time.clock()
    productName = []
    productNumber = 0
    reviewsNumber = 0
    username = str(input("输入您的天猫账号用户名："))
    password = str(input("输入您的天猫账户密码："))
    keyword = str(input("输入搜索商品的关键字："))
    pageNumber = int(input("请输入想要搜索的页数："))
    reviewPageNumber = int(input("请输入想要爬取得评论的页数："))
    getPageHtml(username,password,keyword,pageNumber)
    for i in range(pageNumber):
        htmlFile = open('F:\E-Site Web Crawler\HTMLSource\第{}页网页代码.html'.format(i+1), 'rb')
        productAndSellerID = searchProducts(htmlFile, i, productName)
        print('第{}页网页源码爬取已完成，准备进行商品信息分析。。。'.format(i+1))
        getReview(productAndSellerID,productName,reviewPageNumber)
        print('第{}页网页商品评论获取已完成！'.format(i+1))
        htmlFile.close()
        productNumber += len(productName)
        reviewsNumber += len(productName) * reviewPageNumber * 20
    end = time.clock()
    print("抓取完毕，一共抓取了{}个商品信息，"
          "共{}条评论，耗时{} min".format(productNumber,reviewsNumber,((end - start) / 60)))
    #url = 'https://list.tmall.com/search_product.htm?q={}&type=p&vmarket=&spm=875.7931836%2FB.a2227oh.d100' \
          #'&from=mallfp..pc_1_searchbutton'.format(keyword)
    #searchProducts(cookies,url)
