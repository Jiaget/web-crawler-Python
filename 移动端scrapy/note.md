# 爬取移动端

### 需要抓包工具

- fiddler
- miteproxy （暂不了解）

### Fiddle 相关配置
- tools - connection - allow remote
- 进入fiddle页面下载证书（pc, 手机均需要安装。PC手机需要在同一网段，可以令pc开启热点供手机连接） 信任VPN
- 代理配置

## SCRAPY （框架）
还有pyspider, 之后再研究

- 数据解析，持久化存储，数据爬取（异步）等等功能

- 环境安装
    - `pip install wheel`
    - 下载twisted `pip install Twisted` 帮助scrapy实现异步操作
    - `pip install pywin32` windows 提供给python的api
    - `pip install scrapy`
  
- <h2>使用方法</h2>
  
  - 创建工程`scrapy startproject scrapyProject`
  - spiders目录下创建爬虫文件
    - `cd '$projectName'`
    - `scrapy genspider $spiderName $url`
  - `allowed_domains`  表示限定域名，一般不使用
  - `start_urls` 中的url会自动对其发送请求
  - 执行工程:`scrapy crawl $spiderName`
  - settings.py
    - 不遵从robots协议 ： settings.py -> ROBOTSTXT_OBEY
    - settings.py 还能设置UA等操作
    - 不输出日志 `--nolog` 或者 settings.py -> 增加 `LOG_LEVEL = 'ERROR'`
  - 持久化（两种）
    - 终端：
      - 只可以将parse返回值存在本地文件(不能存数据库，只能存储进限定文件) 
      - `scrapy crawl $spiderName -o $filePath`
      
    - 管道：（较繁琐）
      - 数据解析
      - 定义一个item类型对象。 items.py -> item类型对象。 `name = items.Field() # 这是一个万能类型`
      - 数据封装到该对象中
      ```
      from $projectName.items import XXXItem
    
      item = xxxItem()
      item['name'] = xxx
      # item提交给管道，提交给了优先级最高的管道类
      yield item
      ```
      - pipelines.py： 接收爬虫文件的item。并进行任意形式的持久化存储
      - 重写父类的方法
        - `def open_spider(self, spider):`在开始爬虫的时候，打开写入的文件
        - `def close_spider(self, spider):`在结束爬虫的时候，关闭文件
      - 在settings.py 中开启管道（默认参数300代表优先级，数值越小，优先级越大）
      - pipeline 中return 的item 会根据优先级传递给下一个pipline
        
  