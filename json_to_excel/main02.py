# -*- coding = utf-8 -*-
# @Time : 2022/5/16 9:30
# @Author : WZX
# @File : .py
# @Software : PyCharm

import os
import json
import xlwt


def getFile(path):
    print(path)

    files = os.listdir(path)  # 得到文件夹下的所有文件，包含文件夹名称

    FileList = []

    for name in files:
        name = r"C:\Users\Wu Zhaoxin\Desktop\task\All_json01/" + name
        FileList.append(name)

    print(FileList)
    return FileList


def get_json(FileList):
    all_list = []
    for file_name, num in zip(FileList, range(1, 76)):
        a = json.load(open(file_name, encoding='utf8'))

        # 获取外部波段字典
        keys = a.keys()
        title = list(keys)
        title.reverse()
        band = []
        for x in title:
            x = x.replace("b", "B")
            band.append(x)

        # 获取内部信息字典
        max = []
        min = []
        me = []
        mae = []
        std = []
        for value in a.values():
            info = value.values()
            info = list(info)
            # print(info)
            # print(type(info))
            for i, j in zip(info, range(0, len(info))):

                if j == 4:
                    max.append(str(i)[0:4])
                elif j == 3:
                    min.append(str(i)[0:5])
                elif j == 1:
                    me.append(str(i)[0:5] + "E" + str(i)[-3:])
                elif j == 0:
                    mae.append(str(i)[0:4])
                elif j == 2:
                    std.append(str(i)[0:4])
                else:
                    continue

        max.reverse()
        min.reverse()
        me.reverse()
        mae.reverse()
        std.reverse()
        # print(band, max, min, me, mae, std)

        datalist = [band, min, max, me, mae, std]
        # print(datalist)
        all_list.append(datalist)
        print(all_list)
    return all_list


def write(all_list):
    for a_list, num in zip(all_list, range(1, 76)):
        # 创建excel
        book = xlwt.Workbook(encoding='utf-8', style_compression=0)
        sheet = book.add_sheet('信息1', cell_overwrite_ok=True)
        col = ('影像波段B', '最小值min', '最大值max', '均值me', '绝对均值mae', '标准差std')
        for i in range(0, 6):
            sheet.write(0, i, col[i])

        # 按列填入数据：
        # 行数（title波段数）
        for x in range(0, 6):
            # 每列数据
            data = a_list[x]
            # print(data)
            # 列数（col）
            for y in range(0, len(data)):
                sheet.write(y + 1, x, data[y])

        save_path = '%d.xls' % num
        book.save(save_path)


if __name__ == '__main__':
    path = "C:/Users/Wu Zhaoxin/Desktop/task/All_json01"
    FileList = getFile(path)
    all_list = get_json(FileList)
    write(all_list)
