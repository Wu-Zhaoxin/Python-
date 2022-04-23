# -*- coding = utf-8 -*-
# @Time : 2022/3/25 9:25
# @Author : WZX
# @File : .py
# @Software : PyCharm

import numpy as np
from matplotlib import pyplot as plt


def main():
    readTxt()
    # ofx, ofy, xfilename, yfilename = readTxt()
    # resulty, resultx = saveData(ofx, ofy)
    # drawChart(resulty, resultx)


def readTxt():

    for i in range(1, 4):
        base = r'C:/Users/Wu Zhaoxin/Desktop/'
        xfilename = str(i) + str("x.txt")
        yfilename = str(i) + str("y.txt")
        xfile = base + xfilename
        yfile = base + yfilename
        print(xfile, yfile)

        ofx = open(xfile, 'r')  # 以读方式打开文件
        ofy = open(yfile, 'r')

        resulty, resultx = saveData(ofx, ofy)
        drawChart(resulty, resultx, xfilename, yfilename, i)
        # return ofx, ofy, xfilename, yfilename

def saveData(ofx, ofy):
    resultx = list()
    for line in ofx.readlines():  # 依次读取每行
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
    for line in ofy.readlines():  # 依次读取每行
        line = line.strip()  # 去掉每行头尾空白
        if not len(line) or line.startswith('#'):  # 判断是否是空行或注释行
            continue  # 是的话，跳过不处理
        resulty.append(line)  # 保存

    new_resulty = [];
    for n in resulty:
      new_resulty.append(float(n)/1000);
    resulty = new_resulty;
    print(resulty)
    print(type(resulty))

    return resulty, resultx

    ofx.close()
    ofy.close()


def drawChart(resulty, resultx, xfilename, yfilename, i):
    line = plt.plot(resulty, resultx)
    plt.ylabel('Relative Spectral Response', fontsize=12, labelpad=11)
    plt.xlabel('Wavelength(μm)', fontsize=12, labelpad=11)

    # 图例
    i = str(i)
    lable = 'Band' + i
    plt.legend(handles=line, labels=(lable,), loc='upper right', fontsize=12)
    plt.tick_params(axis='both', which='major', labelsize=11)  # 设置刻度的字号

    path = r'C:/Users/Wu Zhaoxin/Desktop/' + xfilename + ' ' + yfilename + '.jpg'
    print(path)
    # plt.savefig(r'C:\Users\Wu Zhaoxin\Desktop\cs.jpg', dpi=500)
    plt.savefig(path, dpi=500, bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    main()