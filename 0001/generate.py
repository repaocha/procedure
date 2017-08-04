# -*- coding:utf-8 -*-
#做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

'''
import random

str="abcdefghijklmnopqrstuvwxyz0123456789"

def generate(count,length):
	#count=200
	#length=5
	for i  in range(count):
		x=""
		for m in range(length):
			x+=random.choice(str)
		print(x)

if __name__=="__main__":
	generate(200,5)
'''
import uuid


def generate(num, length):
#生成”num“个激活码，每个激活码含有”length“位
    result = []
    while True:
        uuid_id = uuid.uuid1()                             #使用主机ID, 序列号, 和当前时间来生成UUID.
        temp = str(uuid_id).replace('-', '')[:length]  #删去字符串中的'-',取出前length 个字符 
        if temp not in result:    #如果没重复
            result.append(temp)
        if len(result)==num:
            break
    return result
print generate(200, 10)