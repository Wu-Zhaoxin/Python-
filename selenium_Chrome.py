# -*- coding = utf-8 -*-
# @Time : 2022/4/7 17:53
# @Author : WZX
# @File : .py
# @Software : PyCharm

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 1.创建浏览器对象


web = Chrome()

# 2.打开一个网址
web.get("http://www.baidu.com")

print(web.title)

el = web.find_element(By.ID, 'kw')
el.click()

# 3.输入
# el.send_keys("马云")
# search = web.find_element_by_xpath('//*[@id="su"]').click()
el.send_keys("马云", Keys.ENTER)

# web.close()