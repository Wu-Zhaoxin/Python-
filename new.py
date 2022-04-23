# -*- coding = utf-8 -*-
# @Time : 2022/3/25 16:08
# @Author : WZX
# @File : .py
# @Software : PyCharm

import numpy as np
import matplotlib.pyplot as plt
import pylab


## 绘制该文件中的数据
## 需要引入pylab库，里面用到的函数和MATLAB里的非常类似
def plotData(x, y):
    length = len(y)

    pylab.figure(1)

    pylab.plot(x, y, 'rx')
    pylab.xlabel('x')
    pylab.ylabel('y')

    pylab.show()  # 让绘制的图像在屏幕上显示出来


x = []
y = []

x = [float(l.split()[3]) for l in open(r'C:\Users\Wu Zhaoxin\Desktop\modis\rtcoef_eos_2_modis_srf_ch01.txt')]
y = [float(l.split()[1]) for l in open(r'C:\Users\Wu Zhaoxin\Desktop\modis\rtcoef_eos_2_modis_srf_ch01.txt')]

plotData(x, y)