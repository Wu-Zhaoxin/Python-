# -*- coding = utf-8 -*-
# @Time : 2022/5/16 9:30
# @Author : WZX
# @File : .py
# @Software : PyCharm

import json
import xlwt


def get_json(file_name):
    a = json.load(open(file_name, encoding='utf8'))

    print(a)
    print(type(a))

    # 获取外部波段字典
    keys = a.keys()
    title = list(keys)
    title.reverse()
    band = []
    for x in title:
        x = x.replace("b", "B")
        band.append(x)
    print(band)

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
    print(band, max, min, me, mae, std)

    # 创建excel
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('信息1', cell_overwrite_ok=True)
    col = ('影像波段B', '最小值min', '最大值max', '均值me', '绝对均值mae', '标准差std')

    for i in range(0, 6):
        sheet.write(0, i, col[i])

    datalist = [band, min, max, me, mae, std]

    # 按列填入数据：
    # 行数（title波段数）
    for i in range(0, len(title) + 1):
        # 每列数据
        data = datalist[i]
        # 列数（col）
        for j in range(0, 5):
            sheet.write(j+1, i, data[j])

    save_path = '表格.xls'
    book.save(save_path)


if __name__ == '__main__':
    get_json("f.json")
