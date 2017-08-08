#!/usr/bin/python
# -*- coding:utf-8 -*-

#有个目录，里面是自己写过的程序，统计一下写过多少行代码.包括空行和注释，但是要分别列出来.

import os
import re

def count_num(a,b):
     number=[0,0,0]
     path=os.path.join(a,b) #把目录和文件名合成一个路径.
     f=open(path,'r').readlines()  #读取所有行并返回列表.
     for i in f:
     	    if re.match(r'^#',i)==None:
     	    	   pass
     	    else:
     	    	   number[1]+=1
     	#没有注释进行下一步，有注释加进去行数
     if f[-1][-1:]=='\n':                               #最后一行为空行时
     	     number[2]=f.count('\n')+1                  #获得空行行数
     	     number[0]=len(f)+1-number[2]-number[1]   #获得代码行数
     else:
     	     number[2]=f.count('\n')
     	     number[0]=len(f)-number[2]-number[1]
     return number
def file_infor(c,d):
      py=[x for x in os.listdir(c) if os.path.splitext(x)[1]==d]          #获得文件列表
      print(py)
      the_num=[0,0,0]
      for i in py:
           num=count_num(c,i)
           the_num[0]+=num[0]
           the_num[1]+=num[1]
           the_num[2]+=num[2]
      print('代码有%s行\n注释有%s行\n空行有%s行'%(the_num[0],the_num[1],the_num[2]))

if __name__=='__main__':
     file='.'
     ext=".py"
     file_infor(file,ext)