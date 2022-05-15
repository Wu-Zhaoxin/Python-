# -*- coding = utf-8 -*-
# @Time : 2022/5/15 18:24
# @Author : WZX
# @File : .py
# @Software : PyCharm

# 1. pip install selenium 使用pip包管理工具安装selenium
# 2. 安装浏览器驱动 chromedrive 放在python解释器所在文件夹

from selenium.webdriver import Chrome

# 1. 创建浏览器对象
web = Chrome()
# 2. 打开一个网址
web.get("https://www.bilibili.com/video/BV1ZT4y1d7JM?p=84&spm_id_from=pageDriver")
print(web.title)