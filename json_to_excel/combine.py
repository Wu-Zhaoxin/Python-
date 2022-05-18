# -*- coding = utf-8 -*-
# @Time : 2022/5/16 21:12
# @Author : WZX
# @File : .py
# @Software : PyCharm

import os as os
import pandas as pd

# 获取需要进行合并的excel文件夹下的所有excel文件名称
# 通过os.listdir()函数将文件名称以列表的形式存储到files中
files = os.listdir(r'C:\Users\Wu Zhaoxin\Desktop\task\deal')
print(files)
# 依次遍历每个文件名，并循环读取
df = []
for i in files:
    # 读取文件，并以二维数组形式存储到f
    f = pd.read_excel(r'C:\Users\Wu Zhaoxin\Desktop\task\deal/'+i, sheet_name='信息1')
    print(f)
    df.append(f)

# 然后将列表合并起来，并且变为二维数据结构
result = pd.concat(df, axis=0)  # axis = 1 横向拼接 = 0 纵向拼接

result.to_excel(r'C:\Users\Wu Zhaoxin\Desktop\task\deal\combine.xlsx', index=0)  # index = 0或False 表示不显示索引编号