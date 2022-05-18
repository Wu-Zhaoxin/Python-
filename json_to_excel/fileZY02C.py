# -*- coding = utf-8 -*-
# @Time : 2022/5/17 11:26
# @Author : WZX
# @File : .py
# @Software : PyCharm

import os as os
import xlwt

# 1.文件夹路径
# 2.提取文件名 存为列表+切片日期 存为列表

# 获取需要进行合并的excel文件夹下的所有excel文件名称
# 通过os.listdir()函数将 文件名称 以列表的形式存储到files中
files = os.listdir(r'C:\Users\Wu Zhaoxin\Desktop\task\title4')
# print(files)

titles = []
times = []
for n in files:
    title = n[3:51]
    time = n[25:33]
    time = time[:4] + '-' + time[4:6] + '-' + time[6:]
    titles.append(title)
    times.append(time)

print(titles, times)

# 3.两列存入excel

book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = book.add_sheet('信息1', cell_overwrite_ok=True)
col = ('title', 'time')

for x in range(0, 2):
    sheet.write(0, x, col[x])

datalist = [titles, times]
for x in range(0, 2):
    data = datalist[x]
    for y in range(0, len(data)):
        sheet.write(y+1, x, data[y])

save_path = '表格ZY02C.xls'
book.save(save_path)