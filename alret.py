# 1.导包
from selenium import webdriver
from  selenium.webdriver.support.ui import WebDriverWait
from senleniumtools import find_elment
import time

# 2.实例化浏览器并且获得浏览器句柄（打开浏览器并且获得浏览器的操作对象）
driver = webdriver.Chrome(executable_path='chromedriver.exe')

# 3.打开网站
driver.get("file:///C:/Users/14033/Desktop/tanchuang.html")

driver.maximize_window() #浏览器全屏

# queding = ("xpath",'/html/body/div/input[2]')
# find_elment(driver,queding).click()

quxiao = ("xpath",'/html/body/div/input[1]')
find_elment(driver,quxiao).click()

time.sleep(5)
#处理弹窗按钮
#driver.switch_to_alert().accept() #点确定按钮

driver.switch_to_alert().dismiss()  #点击取消按钮



