import asyncio
import time

urls = ['a',
        'b',
        'c']
start = time.time()


# 该函数中必须使用支持异步模块的代码 ‘asyncio.sleep’ 而不是'sleep'
# 有阻塞得操作前必须用await 修饰
async def get_request(url):
    print('processing...')
    await asyncio.sleep(2)
    print(url, 'success!')
    return 'finish'


tasks = []
for url in urls:
    c = get_request(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
# 事件循环注册时需要wait处理
loop.run_until_complete(asyncio.wait(tasks))

print(time.time() - start)
