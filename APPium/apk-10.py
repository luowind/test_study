#coding:utf-8

#touchaction

from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction

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

#---轻敲
'''
button1 = driver.find_element_by_xpath("//*[@text='WLAN']") #找到元素
touch_action = TouchAction(driver)  #创建TouchAction对象
touch_action = touch_action.tap(button1)  #调用想要执行的动作
touch_action.perform()  #使用perform执行动作
'''
#精简
button1 = driver.find_element_by_xpath("//*[@text='WLAN']") #找到元素
TouchAction(driver).tap(button1).perform()

time.sleep(13)