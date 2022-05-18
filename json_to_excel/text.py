# -*- coding = utf-8 -*-
# @Time : 2022/5/17 16:23
# @Author : WZX
# @File : .py
# @Software : PyCharm

import pandas as pd

# get_data = pd.read_excel(r'C:\Users\Wu Zhaoxin\Desktop\task\id.xlsx', sheet_name='Sheet1',
#                          usecols=[i for i in range(0, 1)])
#
# print(get_data)

get_data = pd.read_excel(r'C:\Users\Wu Zhaoxin\Desktop\task\id.xlsx', sheet_name='Sheet1')

title = get_data.columns.to_list()  # 读取表头
# print(title)

# 获取表头
# col = get_data.iloc[:, 0]
# print(col)
# print(type(col))

id = get_data.iloc[:, 0].values
time = get_data.iloc[:, 1].values
print(time)
# print(type(id))
for i, j in zip(id, time):
    if type(i) == float or type(j) == float:
        continue
    else:
        j = str(j)
        text = "影像" + i + "，拍摄于" + j[0:4] + "年" + j[5:7] + "月" + j[8:10] + "日，各波段相对辐射定标精度见下图。"
        print(text)