#coding:utf-8
#UI automavirwer 一组元素 定位

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
#连接appium服务器,获取driver
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

'''
#使用ID定位
titles = driver.find_elements_by_id("com.android.settings:id/title")
print(titles)
print(len(titles))  #显示有多少个元素
for title in titles:
    print(title.text)  #打印名称

titles[1].click()   #点击第2各元素
'''


'''
#使用class定位
views = driver.find_elements_by_class_name("android.widget.TextView")
print(views)
print(len(views))  #显示有多少个元素
for view in views:
    print(view.text)  #打印名称

views[4].click()   #点击第5各元素
'''

#使用Xpath定位,查找包含“设”的元素组
wws = driver.find_elements_by_xpath("//*[contains(@text,'设')]")  #包含关系
print(wws)
print(len(wws))  #显示有多少个元素
for ww in wws:
    print(ww.text)  #打印名称
