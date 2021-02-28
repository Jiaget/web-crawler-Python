# 自定义代理
import urllib.request
import random

URL = "http://www.baidu.com/"
USER_AGENT_LIST = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E) QQBrowser/6.9.11079.201",
]


def handler_openner(url):
    # ssl: 第三方的CA数字证书
    # http 使用端口 80.  https 使用端口 443
    # urllib.request.urlopen()
    # 处理器handler
    handler = urllib.request.HTTPHandler()
    random_user_agent = random.choice(USER_AGENT_LIST)
    request = urllib.request.Request(URL)
    request.add_header("User-agent", random_user_agent)
    handler.http_request(request)
    openner = urllib.request.build_opener(handler)
    response = openner.open(url)
    data = response.read()
    print(response)
    print(data)


handler_openner(URL)
