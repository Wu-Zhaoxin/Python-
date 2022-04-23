# -*- coding = utf-8 -*-
# @Time : 2022/4/15 15:36
# @Author : WZX
# @File : .py
# @Software : PyCharm

import os

path = input('请输入文件夹路径：')
# prefix = input('请输入文件名前缀：')
suffix = input('请输入文件名后缀：')

# 获取该目录下所有文件，存入列表中
fileList = os.listdir(path)

m = int(input('请输入开始数：'))  # python中input函数默认返回一个字符串，需强制转化为整数
n = m
for inner_file in fileList:
    # 获取旧文件名（就是路径+文件名）
    old_name = path + os.sep + inner_file  # os.sep添加系统分隔符
    if os.path.isdir(old_name):  # 如果是目录则跳过
        continue

    # 设置新文件名
    prefix = inner_file[7:]
    new_name = path + os.sep + prefix + suffix
    os.rename(old_name, new_name)  # 用os模块中的rename方法对文件改名
    n += 1

print("共修改了", n-m, "个文件。")