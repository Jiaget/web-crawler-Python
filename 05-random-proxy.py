import urllib.request
import random


def with_proxy():
    proxy = [
        {"http": "113.195.200.209:9999"},
        {"http": "192.227.233.8:8888"},
        {"http": "54.66.244.34:80"},
        {"http": "88.198.24.108:3128"},
        {"http": "5.252.161.48:3128"},
    ]
    for proxy in proxy:
        print("using ip:", proxy)
        proxy_handler = urllib.request.ProxyHandler(proxy)
        opener = urllib.request.build_opener(proxy_handler)
        try:
            opener.open("https://www.youtube.com", timeout=1)
        except Exception as e:
            print(e)


with_proxy()
