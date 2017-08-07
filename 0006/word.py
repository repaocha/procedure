#!/usr/bin/python
# -*- coding:utf-8 -*-

import os, re

def find_word(file_path):
    file_list = os.listdir(file_path)    #os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
    word_dic = {}
    word_re = re.compile(r'[\w]+')         #匹配字母数字
    for x in file_list:
        if os.path.isfile(x) and os.path.splitext(x)[1] =='.txt' :    #判断路径是否为文件 and 分割路径，返回路径名和文件扩展名的元组
            try:
                f = open(x, 'r')
                data = f.read()
                f.close()
                words = word_re.findall(data)
                for word in words:
                    if word not in word_dic:
                        word_dic[word] = 1
                    else:
                        word_dic[word] += 1
            except:
                print('Open %s Error' % x)
    Ans_List = sorted(word_dic.items(), key = lambda t : t[1], reverse = True)  #items() 函数以列表返回可遍历的(键, 值) 元组数组.
    for key, value in Ans_List:
        print( 'Word ', key, 'appears %d times' % value )

find_word('.')