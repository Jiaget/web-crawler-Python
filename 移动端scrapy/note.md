# 爬取移动端

### 需要抓包工具

- fiddler
- miteproxy

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
      
    - 管道：
        - 较为繁琐
        
  