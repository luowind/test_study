#coding:utf-8
#移动操作

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
desired_caps['appActivity'] = '.ChooseLockPattern'

#当输入中文时，需添加以下2个参数
# desired_caps['unicodeKeyboard'] = True
# desired_caps['reseKeyboard'] = True

#连接appium服务器,获取driver
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
time.sleep(1)

# TouchAction(driver).press(x=173,y=678).move_to(x=543,y=678).move_to(x=897,y=678).release().perform()

print(driver.get_window_size())  #获取屏幕分辨率

# driver.get_screenshot_as_file("C:/Users/haha/Desktop/screen.png")  #截图并保存

#获取及设置网络应用
print(driver.network_connection)  #获取

#设置网络
driver.set_network_connection(4)

if driver.network_connection == ConnectionType.DATA_ONLY:
    print(1)
else:
    print(0)


