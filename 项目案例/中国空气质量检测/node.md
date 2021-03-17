# 爬虫练手项目： 爬取中国空气质量检测网站
- 网址：https://www.aqistudy.cn/

该网站使用了大量的反爬策略，是爬虫学习的最佳导师


## 准备工具
- PyExecJs: python运行JS代码的库  `pip install PyExecJS`
- node.js环境安装（运行execjs时如果出现语法错误的问题，可能是node.js的版本或者安装过程出现问题。更换版本或者重新安装。具体原因没有进行深入调查）
- chrome、火狐浏览器（火狐浏览器可以跟踪事件调用代码）
- 在线反混淆网站 `https://www.bm8.com.cn/jsConfusion/` `https://prepack.io/repl.html`

## 开始

- 该网站屏蔽了右键和 F12快捷键。可以打开浏览器的工具-开发者工具进入浏览器的开发者工具界面（元素检查）
- 打开工具后，网站后台设置了大量的DEBUG节点，这让元素检查功能无法使用，使用过debug功能的玩家可以轻松取消节点并跳过debug。
- 该网站的数据Post请求发送绑定在搜索键的点击事件中，用火狐浏览器可以跳转到对应函数中。阅读函数可以定位到一个加密函数（函数名经过乱码处理）。此外在该函数中还可以找到请求参数字典params的定义方法
- 在chrome浏览器中对该函数名全局搜索，可以定位到一个js文件。js代码进行混淆处理，使用上面的网站进行反混淆获取js代码
- js代码中使用了大量的别名函数，增加了阅读难度，但是通过阅读还是能定位到乱码的加密函数。并使用该函数自行写加密函数
```
function getPostParamCode(method, city, type, startTime, endTime){
    var param = {};
    param.city = city;
    param.type = type;
    param.startTime = startTime;
    param.endTime = endTime;
    return pNg63WJXHfm8r(method, param);
}
```
- 在python代码中调用该js函数
```
import execjs
import requests

node = execjs.get()

method = 'GETDETAIL'
city = '杭州'
type = 'HOUR'
start_time = '2021-01-25 00:00:00'
end_time = '2021-03-17 23:00:00'

# 编译
file = 'decode.js'
ctx = node.compile(open(file, encoding='utf-8').read())

# 执行js函数
js = 'getPostParamCode("{0}", "{1}", "{2}", "{3}", "{4}")'.format(method, city, type, start_time, end_time)

# 参数加密
params = ctx.call("getPostParamCode", method, city, type, start_time, end_time)
print(params)
```
- 运行python代码后发现，js代码中的hex_md5未定义。md5是js的加密工具，hex_md5明显是该网站自定义的加密方法。该方法可能封装在其他js文件中。
- 回到浏览器全局搜索hex_md5，并找到对应的js文件，反混淆获得的代码粘贴到之前的js文件中。运行python代码，成功获取加密后的字符串。
- 最后，从Js函数中找到解密代码，并在python中调用，获取最终的数据

##### 完整python 代码
```
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
```

## 小结
该项目获取的数据并不重要，重要的是该网站的混淆机制，及一系列的反爬虫手段。包括其时间格式也发生过变化。网站的反爬手段不断增加，网络爬虫需要应对各种反爬手段并随即应变