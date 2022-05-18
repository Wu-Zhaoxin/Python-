# -*- coding = utf-8 -*-
# @Time : 2022/5/16 10:10
# @Author : WZX
# @File : .py
# @Software : PyCharm

import json
import tablib
import csv

# 获取json数据
with open('f.json', 'r',encoding='utf-8',errors='ignore') as f:
  rows = json.load(f)
# 将json中的key作为header, 也可以自定义header（列名）

#print(type(rows))#2500组数据，以列表形式存储,
#列表中的每一个元素构成是大小为2的列表
#一号位为字符串 title 'SH603919_2017-08-03_1203757451'
#而号位为字典，包含了具体存储元素 {}
#如果我需要生成excel，重点在于第二个元素

print(rows[0][1])

header=tuple([ i for i in rows[0][1].keys()])
# for i in rows[0][1]:
#   print(type(i))


# 创建文件对象
f = open('data.csv', 'w',encoding='utf-8')
csv_write = csv.writer(f)
csv_write.writerow(rows[0][1].keys())
for i in range(len(rows)):
  csv_write.writerow(rows[i][1].values())
f.close()
