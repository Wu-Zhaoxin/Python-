# -*- coding = utf-8 -*-
# @Time : 2022/3/25 21:58
# @Author : WZX
# @File : .py
# @Software : PyCharm

import numpy as np
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker


def main():

    #  N 维数组对象ndarray
    a = np.loadtxt('C:/Users/Wu Zhaoxin/Desktop/HJ1B/HJ1B-CCD2.txt')
    # print(a[:, 0])
    read_txt(a)


def read_txt(a):

    for i in range(1, 5):

        listx = a[:, i]
        listx = listx.tolist()  # 转为列表
        print(listx)
        print(type(listx))

        listy = a[:, 0]
        listy = listy.tolist()
        listy = [j/1000 for j in listy]  # 列表元素除1000
        print(listy)
        print(type(listy))

        draw_chart(listx, listy, i)


def draw_chart(listx, listy, i):

    line = plt.plot(listy, listx)  #创建对象
    plt.ylabel('Relative Spectral Response', fontsize=14, labelpad=9)  # 标签距离轴线距离为11
    plt.xlabel('Wavelength(μm)', fontsize=14, labelpad=9)

    # 图例
    i = str(i)
    lable = 'Band' + i
    plt.legend(handles=line, labels=(lable,), loc='upper right', fontsize=12)

    path = r'C:/Users/Wu Zhaoxin/Desktop/' + i + '.jpg'
    print(path)
    # plt.savefig(r'C:\Users\Wu Zhaoxin\Desktop\cs.jpg', dpi=500)
    plt.tick_params(axis='both', which='major', labelsize=12)  # 设置刻度的字号
    plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
    plt.savefig(path, dpi=500, bbox_inches='tight')  # 图的形式为紧凑型，没有白边
    plt.show()


if __name__ == "__main__":
    main()
