# -*- coding = utf-8 -*-
# @Time : 2022/4/20 11:15
# @Author : WZX
# @File : .py
# @Software : PyCharm

import asyncio
import aiohttp


urls = [
    "",
    ""
]


async def aio_download(url):
    pass


async def main():
    tasks = []
    for url in urls:
        tasks.append(aio_download(url))

    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
