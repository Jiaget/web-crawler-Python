import execjs
import requests

node = execjs.get()

method = 'GETDETAIL'
city = '杭州'
type = 'HOUR'
start_time = '2021-03-16 09:00'
end_time = '2021-03-17 12:00'

# 编译
file = 'decode.js'
ctx = node.compile(open(file, encoding='utf-8').read())

# 执行js函数
js = 'getPostParamCode("{0}", "{1}", "{2}", "{3}", "{4}")'.format(method, city, type, start_time, end_time)

# 参数加密
params = ctx.call("getPostParamCode", method, city, type, start_time, end_time)
print(params)
# 发送请求
url = "https://www.aqistudy.cn/apinew/aqistudyapi.php"
p = {
    "h0lgYxgR3": params,
}

response_data = requests.post(url, data=p).text

# 数据解密
data = ctx.call("dX506x9jVK3vuMMhoz6ZXx", response_data)

print(data)
