# -*- coding = utf-8 -*-
# @Time : 2022/3/26 14:32
# @Author : WZX
# @File : .py
# @Software : PyCharm

import xlrd3


def main():
    xlsfile = xlrd3.open_workbook(r"C:\Users\Wu Zhaoxin\Desktop\Landsat5MSS_BandAverageRSR.xlsx")
    try:
        mysheet = xlsfile.sheet_by_name("Band 1")
    except:
        print("无此表单！")
        return 
    print("%d rows, %d clos" % (mysheet.nrows, mysheet.ncols))
    for col in range(0, mysheet.ncols):
        temp = ""
        for row in range(0, mysheet.nrows):
            if mysheet.cell(row, col).value is not None:
                temp += str(mysheet.cell(row, col).value)
        print("一列：" + temp)


if __name__ == '__main__':
    main()

