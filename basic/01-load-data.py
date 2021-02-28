import urllib.request


def load_data():
    url = "http://www.baidu.com"
    response = urllib.request.urlopen(url)
    data = response.read()
    data_str = data.decode("utf-8")
    with open("baidu.html", "w", encoding="utf-8") as f:
        f.write(data_str)
    print(type(data) is bytes)
load_data()
