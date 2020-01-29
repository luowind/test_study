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

time.sleep(2)
driver.find_element_by_id("com.android.settings:id/search").click()
time.sleep(2)
button1 = driver.find_element_by_id("android:id/search_src_text")  #定位输入框
print("---开始输入---")
button1.send_keys("搜索")  #输入内容
print("---结束输入---")
time.sleep(2)
button1.clear()  #清空内容



time.sleep(4)
driver.quit()