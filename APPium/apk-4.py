#coding:utf-8
#UI automavirwer 一个元素 定位

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

#定位
search = driver.find_element_by_id("com.android.settings:id/search").click()
#输入
shuru = driver.find_element_by_class_name("android.widget.LinearLayout").send_keys("hello")
#返回
fanhui = driver.find_element_by_xpath("//*[@content-desc='收起']").click()

time.sleep(5)

driver.quit()