# -*- coding = utf-8 -*-
# @Time : 2022/3/26 12:40
# @Author : WZX
# @File : .py
# @Software : PyCharm


import numpy as np
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker


def main():

    #  N 维数组对象ndarray
    a = np.loadtxt('C:/Users/Wu Zhaoxin/Desktop/HJ1B/irs.txt')
    # print(a[:, 0])
    read_txt(a)


def read_txt(a):

    for i in range(1, 2):

        listx = a[:, i]
        listx = listx.tolist()  # 转为列表
        listx = [j / 100 for j in listx]
        print(listx)
        print(type(listx))

        listy = a[:, 0]
        listy = listy.tolist()
        # listy = [j/1000 for j in listy]  # 列表元素除1000
        print(listy)
        print(type(listy))

        draw_chart(listx, listy)


def draw_chart(listx, listy):

    line = plt.plot(listy, listx)
    plt.ylabel('Relative Spectral Response', fontsize=14, labelpad=9)
    plt.xlabel('Wavelength(μm)', fontsize=14, labelpad=9)

    # 图例
    i = '5,6'
    lable = 'Band' + i
    plt.legend(handles=line, labels=(lable,), loc='upper right', fontsize=12)

    path = r'C:/Users/Wu Zhaoxin/Desktop/' + i + '.jpg'
    print(path)
    # plt.savefig(r'C:\Users\Wu Zhaoxin\Desktop\cs.jpg', dpi=500)
    plt.tick_params(axis='both', which='major', labelsize=12)  # 设置刻度的字号

    plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))  # x轴小数位
    plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))

    plt.savefig(path, dpi=500, bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    main()