import aiohttp
import asyncio
import time
from lxml import etree

start = time.time()
urls = [
    'http://www.baidu.com',
    'http://www.baidu.com',
    'http://www.baidu.com',
]


async def req(url):
    # 涉及到资源问题，使用with
    # 注意阻塞操作使用await。
    async with aiohttp.ClientSession() as s:
        async with await s.get(url) as response:
            # response.read() 返回byte类型
            page_text = await response.text()
            return page_text


def parse(tasks):
    page_text = tasks.result()
    tree = etree.HTML(page_text)
    text = tree.xpath('//div[@class="title-text c-font-medium c-color-t"]/text()')[0]
    print(text)


tasks = []

for url in urls:
    c = req(url)
    task = asyncio.ensure_future(c)
    task.add_done_callback(parse)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
print(time.time() - start)
