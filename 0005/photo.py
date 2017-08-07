#!/usr/bin/python
# -*- coding:utf-8 -*-

from PIL import Image
import glob,os

def resize():
       for files in glob.glob('*.jpg'):              #glob.glob（pathname), 返回所有匹配的文件路径列表.
            filepath,filename=os.path.split(files)  #分割路径名和文件名
            #fname=os.path.splitext(filename)   #分割路径，返回路径名和文件扩展名的元组
            im=Image.open(files)

            w,h=im.size
            if w>640:
                x=w/640.0
                w=640
                h=int(h/x)
            if h>1136:
                x=h/1136.0
                h=1136
                w=int(w/x)
            print(w,h)
            im0=im.resize((w,h),Image.ANTIALIAS)  #改变尺寸后的图片
            im0.save('0005'+filename) 
resize()