# 1.导包
from selenium import webdriver
from  selenium.webdriver.support.ui import WebDriverWait
import time 

# 2.实例化浏览器并且获得浏览器句柄（打开浏览器并且获得浏览器的操作对象）
driver = webdriver.Chrome(executable_path='chromedriver.exe')

# 3.打开网站
driver.get("http://132.232.44.158:9999/shopxo/")

driver.maximize_window() #浏览器全屏

wd = ("name","wd")
ai_topsearch = ("id","ai-topsearch")
jiage = ("xpath",'/html/body/div[4]/div/ul/li/div/p[2]/strong')

WebDriverWait(driver,10).until(lambda s: s.find_element(*wd)).send_keys("华为")
WebDriverWait(driver,10).until(lambda s: s.find_element(*ai_topsearch)).click()
e = WebDriverWait(driver,10).until(lambda s: s.find_element(*jiage))
try:
    assert e.text == "￥1999.00"
    print("测试用例执行成功")
except:
    print("失败")




