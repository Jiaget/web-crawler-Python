import urllib.request
import urllib.parse
import string


def get_params():
    url = "http://www.baidu.com/s?wd="
    to_search = "乌孙"
    new_url = url + to_search
    # 如果url中带中文，需要转译
    encoded_url = urllib.parse.quote(new_url, safe=string.printable)
    response = urllib.request.urlopen(encoded_url)
    data = response.read()
    with open("search.html", "w", encoding="utf-8") as file:
        file.write(data.decode("utf-8"))
    print(encoded_url)


get_params()
