# -*- coding = utf-8 -*-
# @Time : 2022/2/26 16:52
# @Author : WZX
# @File : .py
# @Software : PyCharm

import sqlite3

#查询数据
#1连接数据库
conn = sqlite3.connect("test.db") #打开或创建数据库

print("Open database successfully")

c = conn.cursor() #获取游标

sql = "select id,name,age,address,salary from company"

cursor = c.execute(sql) #命令游标执行sql语句

for row in cursor:
    print("id = ",row[0])
    print("name = ",row[1])
    print("age = ", row[2])
    print("address = ",row[3])
    print("salary = ",row[4],"\n")

conn.close() #关闭数据库连接
print("查询数据完毕!")