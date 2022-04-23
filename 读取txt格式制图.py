# -*- coding = utf-8 -*-
# @Time : 2022/3/25 14:17
# @Author : WZX
# @File : .py
# @Software : PyCharm

# MODIS/Landsat/sentinel_AB：以列的形式读取txt文本
import codecs
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker


def main():

    readTxt()


def readTxt():

    for i in range(1, 37):
        base = r'C:\Users\Wu Zhaoxin\Desktop\modis\rtcoef_eos_2_modis_srf_ch'
        path = base + str(i) + str(".txt")

        f = codecs.open(path, mode='r', encoding='utf-8')  # 打开txt文件，以‘utf-8'编码读取

        listx, listy = saveData(f)
        drawChart(listx, listy, i)
        f.close()

def saveData(f):

    line = f.readline()  # 以行的形式进行读取文件 单行
    listx = []
    listy = []
    while line:
        a = line.split()
        x = a[0:1]  # 这是选取需要读取的位数
        x = ''.join(x)
        x = round(10000/float(x), 6)
        listx.append(x)  # 将其添加在列表之中

        y = a[1:2]  # 这是选取需要读取的位数
        y = ''.join(y)
        y = float(y)
        listy.append(y)  # 将其添加在列表之中

        line = f.readline()

        print(listx, listy)
    return (listx, listy)


def drawChart(listx, listy, i):
    # listx = listx.reverse()
    line = plt.plot(listx, listy)
    plt.ylabel('Relative Spectral Response', fontsize=14, labelpad=9)
    plt.xlabel('Wavelength(μm)', fontsize=14, labelpad=9)

    # 图例
    i = str(i)
    lable = 'Band' + i
    plt.legend(handles=line, labels=(lable,), loc='upper right', fontsize=12)

    path = r'C:/Users/Wu Zhaoxin/Desktop/' + i + '.jpg'
    plt.tick_params(axis='both', which='major', labelsize=12)  # 设置刻度的字号
    plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
    # plt.savefig(r'C:\Users\Wu Zhaoxin\Desktop\cs.jpg', dpi=500)
    plt.savefig(path, dpi=500, bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    main()
