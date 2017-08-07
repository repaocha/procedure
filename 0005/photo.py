#!/usr/bin/python
# -*- coding:utf-8 -*-

#你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone7P 分辨率(1920*1080)的大小。

from PIL import Image
import glob,os

def resize():
       for files in glob.glob('*.jpg'):              #glob.glob（pathname), 返回所有匹配的文件路径列表.
            filepath,filename=os.path.split(files)  #分割路径名和文件名
            #fname=os.path.splitext(filename)   #分割路径，返回路径名和文件扩展名的元组
            im=Image.open(files)

            w,h=im.size
            if w>1080:
                x=w/1080.0
                w=1080
                h=int(h/x)
            if h>1920:
                x=h/1920.0
                h=1920
                w=int(w/x)
            print(w,h)
            im0=im.resize((w,h),Image.ANTIALIAS)  #改变尺寸后的图片
            im0.save('0005'+filename) 
resize()