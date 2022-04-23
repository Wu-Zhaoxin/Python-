# -*- coding = utf-8 -*-
# @Time : 2022/3/25 13:33
# @Author : WZX
# @File : .py
# @Software : PyCharm

# import pandas as pd
#
# excel_file = ''
#
# data = pd.read_excel(excel_file,index_col='')
#
# print(data.loc[''])

# age = int(input('输入年龄：'))
# if age >= 18:
#     print('畅玩')
# else:
#     if age > 12:
#         print('限时2小时')
#     else:
#         print('权限不够！')

f = open('test.py', mode='br')  # br: b二进制（图片、音频等）r读取；tr:文本格式、读取模式；
context = f.read(100)  # 读取字节数
print(context)
f.close()

with open('a.text') as f:
    context = f.read()
    print(context)
print('over!')  # 出了with自动关闭文件 无需用close关闭文件