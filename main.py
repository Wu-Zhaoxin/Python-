import datetime
import os
import zipfile
from tempfile import TemporaryDirectory
from tempfile import  TemporaryFile

print(os.getcwd())

os.chdir(r'\Users\Wu Zhaoxin\Documents')  # 指定路径

# print(os.getcwd())

dir_list = os.listdir()
# print(dir_list)
#
# for d in dir_list:
#     print(d, os.path.isdir(d), os.path.isfile(d))

# dir_list = os.scandir()  # os.scandir()可以传指定路径 否则为当前路径
# print(dir_list)  # 输出类型为迭代器 需要遍历
# for file in dir_list:
#     print(file, file.name, file.is_dir())
#     print(file.stat())
#     print(file.stat().st_ctime)
#     print(datetime.datetime.fromtimestamp(file.stat().st_ctime))  # 时间戳转为时间格式

# f = open('test.txt', mode='tr')
# context = f.read(10)
# print(context)
# f.close()

# with open('test.txt') as f:
#     context = f.read()
#     print(context)
# print("出了with as 语句自动释放内存 省去close")
#
# with open('w.txt', mode='w') as f:
#     f.write('123熟悉python123')
#
# # append
# with open('w.txt', mode='a') as f:
#     f.write('123熟悉python123')
#
# with TemporaryDirectory() as temp_dir:
#     print('临时文件夹创建', temp_dir)


# with TemporaryFile(mode='w+') as tem_file:
#     tem_file.write('我是文件搬运工')
#     tem_file.seek(0)
#     data = tem_file.read()
#     print(data)

print(os.getcwd())

# 写入
# with zipfile.ZipFile('myfile.zip', 'w') as zipobj:
#     for file in dir_list:
#         if file.endswith('.png'):
#             zipobj.write(file)

# 读取
# with zipfile.ZipFile('myfile.zip', 'r') as zipobj:
#     print(zipobj.namelist())

# 添加
# with zipfile.ZipFile('myfile.zip', 'a') as zipobj:
#     for file in dir_list:
#         if file.endswith('.jpg'):
#             zipobj.write(file)
# print(zipobj.namelist())

# with zipfile.ZipFile('myfile.zip', 'r') as zipobj:
#     zipobj.extract('微信图片_20220107122238.jpg', r'C:\Users\Wu Zhaoxin\Desktop')

# with zipfile.ZipFile('myfile.zip', 'r') as zipobj:
    # zipobj.extractall(r'C:\Users\Wu Zhaoxin\Desktop')