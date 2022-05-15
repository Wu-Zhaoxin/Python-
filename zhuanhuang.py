# -*- coding = utf-8 -*-
# @Time : 2022/3/24 21:15
# @Author : WZX
# @File : .py
# @Software : PyCharm

f = open(r'C:\Users\Wu Zhaoxin\Desktop\123.txt', 'r')  # 以读方式打开文件
result = list()
for line in f.readlines():  # 依次读取每行
    line = line.strip()  # 去掉每行头尾空白
    if not len(line) or line.startswith('#'):  # 判断是否是空行或注释行
        continue  # 是的话，跳过不处理
    result.append(line)  # 保存

print(','.join(result))
f.close()