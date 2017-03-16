#! /usr/bin/env python
# -*- coding utf-8 -*-
from core.getHTML import getPageHtml
from core.searchProducts import searchProducts,createDatabase

if __name__ == '__main__':
    username = str(input("输入您的天猫账号用户名："))
    password = str(input("输入您的天猫账户密码："))
    keyword = str(input("输入搜索商品的关键字："))
    pageNumber = int(input("请输入想要搜索的页数："))
    getPageHtml(username,password,keyword,pageNumber)
    print('网页源码爬取已完成，准备进行商品信息分析。。。')
    createDatabase(pageNumber)

    #url = 'https://list.tmall.com/search_product.htm?q={}&type=p&vmarket=&spm=875.7931836%2FB.a2227oh.d100' \
          #'&from=mallfp..pc_1_searchbutton'.format(keyword)
    #searchProducts(cookies,url)
