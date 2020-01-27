# 1.导包
from selenium import webdriver
from  selenium.webdriver.support.ui import WebDriverWait
from senleniumtools import find_elment

# 2.实例化浏览器并且获得浏览器句柄（打开浏览器并且获得浏览器的操作对象）
driver = webdriver.Chrome(executable_path='chromedriver.exe')

# 3.打开网站
driver.get("https://www.bilibili.com/")

driver.maximize_window() #浏览器全屏

#定位元素
dianji = ("xpath",'//*[@id="reportFirst2"]/div[1]/div[2]/div[3]/div/a/img')
find_elment(driver,dianji).click()

# 切换到新窗口 
driver.switch_to_window(driver.window_handles[-1])
print(driver.title)

#点击购买
buy = ("xpath",'//*[@id="arc_toolbar_report"]/div[1]/span[1]')
find_elment(driver,buy).click()



