# -*- coding = utf-8 -*-
# @Time : 2022/4/21 21:46
# @Author : WZX
# @File : .py
# @Software : PyCharm

import subprocess


# 拼接视频：
# cmd = 'ffmpeg -f concat -safe 0 -i filelist.txt -c copy output.mp4'
# subprocess.run(cmd, shell=True)

# 拼接音频：
# cmd = 'ffmpeg -f concat -safe 0 -i filelist.txt -c copy output1.mp3'
# subprocess.run(cmd, shell=True)

# 合成音视频：
#     视频无原声时：
# cmd = 'ffmpeg -i "C:/Users/Wu Zhaoxin/PycharmProjects/Work/output.mp4" -i "C:/Users/Wu Zhaoxin/PycharmProjects/Work/output2.mp3" -c:v copy -c:a aac -strict experimental "C:/Users/Wu Zhaoxin/PycharmProjects/Work/combine.mp4"'
# subprocess.run(cmd, shell=True)
# print("完成合并！")

#     视频有原声时：
# cmd = 'ffmpeg -i output.mp4 -i output2.mp3 -c:v copy -c:a aac -strict experimental -map 0:v:0 -map 1:a:0 outputname.mp4'
# subprocess.run(cmd, shell=True)
# print("完成合并！")

# 截取片段：
    # 参数说明：
    #
    # -ss 指定要截取的视频的起始时间。
    #
    # -to 指定要截取的视频的终止时间。
    #
    # -i 输入文件，这里指的就是视频文件。
    #
    # -y 表示无需询问，直接覆盖输出文件（如果有原文件的话）。
    #
    # -f 指定输出视频的格式。
    #
    # -acodec 指定音频编码格式。copy表示编码格式不发生改变，直接复制原来的编码格式，这样会大大提升速度。
    #
    # -vcodec 指定视频编码格式。copy表示编码格式不发生改变，直接复制原来的编码格式，这样会大大提升速度。
    #
    # -q:v 1 q是质量，v是视频，v的取值范围是[1, 35]，取值1的时候，对应着最佳的视频质量。
    #
    # 注意：测试发现把-ss和-to放到-i前面，可以加快处理速度。

# cmd = 'ffmpeg -ss 00:00:00 -to 00:10:37 -i output1.mp3 -y -f mp3 -vcodec copy -acodec copy -q:v 1 output2.mp3'
# subprocess.run(cmd, shell=True)
# print("完成合并！")