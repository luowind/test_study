#coding:utf-8
#隐式等待

from appium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait   #显示等待必备


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

#time.sleep(10)  #必须等10s，超时则报错

#隐式等待
'''
driver.implicitly_wait(50)   #隐式等待50s，什么时候找到元素，则结束；若超时，则报错；
FF = driver.find_element_by_xpath("//*[@content-desc='收起']").click()
'''

#显示等待

#wait = WebDriverWait(driver,10)  #10s等待时间
wait = WebDriverWait(driver,15,3)  #15s等待时间,每3秒找一次，3为频率
back_button = wait.until(lambda x:x.find_element_by_xpath("//*[@content-desc='收起']"))
back_button.click()

#写法2
#back_button = WebDriverWait(driver,15,3).until(lambda x:x.find_element_by_xpath("//*[@content-desc='收起']")).click()
print("成功")

time.sleep(3)
driver.quit()
