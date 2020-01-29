#coding:utf-8

from appium import webdriver
import time

#创建一个字典，包装启动参数
desired_caps = dict()
#需要连接手机的平台
desired_caps['platformName'] = 'android'
#需要连接手机的版本号
desired_caps['platformVersion'] = '5'
#需要连接手机的设备号（Android平台下，看可以随便写，不能不写）
desired_caps['deviceName'] = '192.168.0.1'
#需要启动的程序的包名
desired_caps['appPackage'] = 'com.android.settings'
#需要启动的程序的界面名
desired_caps['appActivity'] = '.Settings'

#当输入中文时，需添加以下2个参数
desired_caps['unicodeKeyboard'] = True
desired_caps['reseKeyboard'] = True

#连接appium服务器,获取driver
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

#获取文本内容
# titles = driver.find_elements_by_id("com.android.settings:id/title")
# for title in titles:
#     print(title.text)


'''
#获取位置及大小
button = driver.find_element_by_id("com.android.settings:id/search")
print(button.location)
print(button.location["x"])
print(button.location["y"])

print(button.size)
print(button.size["width"])
print(button.size["height"])
'''

#获取属性名与属性值
buttons = driver.find_elements_by_id("com.android.settings:id/title")
for i in buttons:
    print(i.get_attribute("enabled"))
    print(i.get_attribute("resourceId"))  #固定格式
    print(i.get_attribute("className"))   #固定格式
