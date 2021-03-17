from selenium import webdriver
from selenium.webdriver import ActionChains
from PIL import Image
from chaojiying import Chaojiying_Client
from time import sleep

bro = webdriver.Edge(executable_path='J:\jupyter\python-crawler\msedgedriver.exe')
url = 'https://kyfw.12306.cn/otn/login/init'
bro.get(url)

# 验证码捕获， 截图-裁剪
sleep(3)

bro.save_screenshot('login.png')
# 定位验证码标签
image_element = bro.find_element_by_xpath('//*[@id="loginForm"]/div/ul[2]/li[4]/div/div/div[3]/img')
location = image_element.location
size = image_element.size
# 验证码的区域 （x, y , x', y'）
rangle = (
    int(location['x']), int(location['y']), int(location['x'] + size['width']), int(location['y'] + size['height']))

image = Image.open('login.png')
# 进行图片裁剪
frame = image.crop(rangle)
frame.save('Verification.png')

# 使用打码平台
chaojiying = Chaojiying_Client('jiaget', 'Jm6242616', '913983')  # 用户中心>>软件ID 生成一个替换 96001
im = open('Verification.png', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//

# 返回的坐标格式是 "x1,y1|x2,y2"的字符串
verification_pos = chaojiying.PostPic(im, 9004)['pic_str']


# 坐标字符串解析
def parse(str):
    list = str.split('|')
    result = []
    for e in list:
        x = e.split(',')[0]
        y = e.split(',')[1]
        result.append((int(x), int(y)))
    print(result)
    return result


for x, y in parse(verification_pos):
    ActionChains(bro).move_to_element_with_offset(image_element, x, y).click().perform()
    sleep(0.5)

sleep(3)
bro.quit()
