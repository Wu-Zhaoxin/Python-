# -*- coding = utf-8 -*-
# @Time : 2022/4/1 16:28
# @Author : WZX
# @File : .py
# @Software : PyCharm

import xlrd3

def main():
    xlsfile = xlrd3.open_workbook(r"C:\Users\Wu Zhaoxin\Desktop\Landsat5MSS_BandAverageRSR.xlsx")
    try:
        mysheet = xlsfile.sheet_by_name("Band 4")
    except:
        print("无此表单！")
        return  # return结束函数 本函数内return之后的代码不执行
    print("%d rows, %d clos" % (mysheet.nrows, mysheet.ncols))
    for col in range(0, 1):
        Wavelength = []
        for row in range(0, mysheet.nrows):
            try:
                float(mysheet.cell(row, col).value)  # 判断是否可以转为浮点型，如果可以则继续
            except Exception as ex:
                # print("出现如下异常%s" % ex)
                continue  # 跳过
            Wavelength.append(float(mysheet.cell(row, col).value))
        # print(Wavelength)

    for col in range(1, 2):
        Response = []
        for row in range(0, mysheet.nrows):
            try:
                float(mysheet.cell(row, col).value)  # 判断是否可以转为浮点型，如果可以则继续
            except Exception as ex:
                # print("出现如下异常%s" % ex)
                continue  # 跳过
            Response.append(float(mysheet.cell(row, col).value))
        # print(Response)

    return(Wavelength, Response)


if __name__ == '__main__':
    main()