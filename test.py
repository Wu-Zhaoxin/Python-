# -*- coding = utf-8 -*-
# @Time : 2022/3/22 20:33
# @Author : WZX
# @File : .py
# @Software : PyCharm

import os
import shutil
from datetime import datetime

path = input('输入路径')
os.chdir()  # 切换当前路径

file_list = []

# for dirpath, dirname, files in os.walk('./'):
    # for file in os.scandir(dirpath)