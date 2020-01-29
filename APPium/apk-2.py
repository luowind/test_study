#app的安装与卸载
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

time.sleep(5)

#判断是否安装
if driver.is_app_installed("tv.danmaku.bili"):
#如果安装，则卸载
    driver.remove_app("tv.danmaku.bili")
#如果没安装，则安装(apk文件路径)
else:
    driver.install_app("D:/bao/iBiliPlayer-bili.apk")

time.sleep(15)

driver.quit()