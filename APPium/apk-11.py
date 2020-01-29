#coding:utf-8

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

# #按下抬起
# TouchAction(driver).press(x=650,y=650).release().perform()
# #time.sleep(2)
# #TouchAction(driver).press(x=650,y=650).release().perform()
# button = driver.find_element_by_xpath("//*[@text='WLAN']")
# print(button.location) #获取坐标

#TouchAction(driver).press(x=650,y=650).release().press(x=32,y=194).release().perform()

# TouchAction(driver).tap(x=144,y=304).perform() #点击进入
# time.sleep(2)
# TouchAction(driver).press(x=144,y=304).wait(2000).release().perform()  #wait等待2s，

#---------长按操作
TouchAction(driver).tap(x=144,y=304).perform() #点击进入
time.sleep(2)
TouchAction(driver).long_press(x=144,y=304,duration=2000).perform()  #duration持续时间


time.sleep(8)
driver.quit()
