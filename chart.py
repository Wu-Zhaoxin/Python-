# -*- coding = utf-8 -*-
# @Time : 2022/3/24 16:55
# @Author : WZX
# @File : .py
# @Software : PyCharm

import numpy as np
from matplotlib import pyplot as plt


fx = open(r'C:\Users\Wu Zhaoxin\Desktop\x.txt', 'r')  # 以读方式打开文件
fy = open(r'C:\Users\Wu Zhaoxin\Desktop\y.txt', 'r')


resultx = list()
for line in fx.readlines():  # 依次读取每行
    line = line.strip()  # 去掉每行头尾空白
    if not len(line) or line.startswith('#'):  # 判断是否是空行或注释行
        continue  # 是的话，跳过不处理
    resultx.append(line)  # 保存

new_resultx = [];
for n in resultx:
  new_resultx.append(float(n));
resultx = new_resultx;
print(resultx)
print(type(resultx))


resulty = list()
for line in fy.readlines():  # 依次读取每行
    line = line.strip()  # 去掉每行头尾空白
    if not len(line) or line.startswith('#'):  # 判断是否是空行或注释行
        continue  # 是的话，跳过不处理
    resulty.append(line)  # 保存

new_resulty = [];
for n in resulty:
  new_resulty.append(float(n));
resulty = new_resulty;
print(resulty)
print(type(resulty))

plt.plot(resulty, resultx)
plt.ylabel('Filter response')
plt.xlabel('Wavelength(μm)')
plt.savefig(r'C:\Users\Wu Zhaoxin\Desktop\123.jpg', dpi=500)
plt.show()

fx.close()
fy.close()
