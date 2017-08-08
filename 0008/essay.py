#!/usr/bin/python
# -*- coding:utf-8 -*-

#一个HTML文件，找出里面的正文

from bs4 import BeautifulSoup

def find_content(path):
      with open(path) as f:
      	text=BeautifulSoup(f,'lxml')
      	content=text.get_text().strip('\n')
      	return content.encode('gbk','ignore')

if __name__=='__main__':
      print find_content(base_site.html)