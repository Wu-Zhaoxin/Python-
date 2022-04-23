# -*- coding = utf-8 -*-
# @Time : 2022/4/6 17:18
# @Author : WZX
# @File : .py
# @Software : PyCharm

from pathlib import Path
from filecmp import cmp

src_floder = Path('F:\资料')

dest_folder = Path('F:\资料_rep')

if not dest_folder.exists():
    dest_folder.mkdir(parents=True)

file_list = []
result = list(src_floder.rglob('*'))

for i in result:
    if i.is_file():
            file_list.append(i)

for m in file_list:
    for n in file_list:
        if m != n and m.exists() and n.exists():
            if cmp(n, m):
                n.replace(dest_folder / n.name)