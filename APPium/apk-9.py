#coding:utf-8
#滑动

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

#driver.swipe(100,1500,100,100)
#driver.swipe(100,1500,100,100,5000)  #5000为滑动时间

print("---------")

#scroll滑动
start_button = driver.find_element_by_xpath("//*[@text = '应用']")
end_button = driver.find_element_by_xpath("//*[@text = '更多']")

# driver.scroll(start_button,end_button)

#drag_and_drop滑动
driver.drag_and_drop(start_button,end_button)

print("**************")
time.sleep(8)
driver.quit()