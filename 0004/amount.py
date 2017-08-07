# -*- coding:utf-8 -*-

#任一个纯英文的文本文档，统计其中的单词出现的个数.

import re
def num(path):
    with open(path, 'r') as file:
        data=file.read()
        print(data)
        words=re.compile('[a-zA-Z0-9]+')#范围包括a-z,A-Z,0-9的所有字母数字,+表示与之相邻的元素必须出现一次或者多次.
        #使用re的一般步骤是先使用re.compile()函数，将正则表达式的字符串形式编译为Pattern(匹配的正则表达式)实例，
        #然后使用Pattern实例处理文本并获得匹配结果（一个Match实例），最后使用Match实例获得信息，进行其他的操作。
        dict={}

        for x in words.findall(data):     #以列表形式返回全部能匹配的子串.
            if x not in dict:
                dict[x]=1
            else:
                dict[x]+=1

        print(dict)

num('yang.txt')