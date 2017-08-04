#-*- coding:utf-8 -*-
import uuid
import sqlite3

def generate(num, length):
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

def save(result):
    try:
        connect = sqlite3.connect('codelist.db')
    except:
        print("failed!")
    cur = connect.cursor()
    cur.execute('create table if not exists codes(code char(200) primary key)')
    for item in result:
        cur.execute('insert into codes values (?)', [item])
    print("success!")
    connect.commit()
    cur.close()
    connect.close()

save(generate(200, 10))