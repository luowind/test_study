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
desired_caps['appPackage'] = 'tv.danmaku.bili'

#需要启动的程序的界面名
desired_caps['appActivity'] = 'tv.danmaku.bili.MainActivityV2'

#连接appium服务器,获取driver
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

time.sleep(5)

#跳转app
driver.start_activity("com.tencent.news",".activity.SplashActivity")

time.sleep(15)

#关闭应用，不会关闭驱动对象
#driver.close_app()

#退出
driver.quit()
