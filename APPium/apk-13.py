#coding:utf-8

#发送键到设备
from appium import webdriver
import time
from appium.webdriver.connectiontype import ConnectionType
# from appium.webdriver.common.touch_action import TouchAction

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
# desired_caps['unicodeKeyboard'] = True
# desired_caps['reseKeyboard'] = True

#连接appium服务器,获取driver
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

'''
#键位操作
#键位参考  https://www.cnblogs.com/sishuiliuyun/p/4432884.html
driver.press_keycode(24) #音量加
driver.press_keycode(24)
driver.press_keycode(24)
driver.press_keycode(25)#音量减

'''

#操作栏操作
driver.open_notifications() #打开通知栏
#关闭通知栏，向上滑动或返回键操作
driver.press_keycode(4) #返回键

print("结束")
driver.quit()


