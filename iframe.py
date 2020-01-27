# 1.导包
from selenium import webdriver
from  selenium.webdriver.support.ui import WebDriverWait
from senleniumtools import find_elment

# 2.实例化浏览器并且获得浏览器句柄（打开浏览器并且获得浏览器的操作对象）
driver = webdriver.Chrome(executable_path='chromedriver.exe')

# 3.打开网站
driver.get("http://132.232.44.158:9999/shopxo/admin.php")

driver.maximize_window() #浏览器全屏

# 用元祖存放定位方式
username = ("name","username")
password = ("name","login_pwd")
loginpwd = ("xpath",'/html/body/div[1]/div/div[2]/div/form/div/div[3]/button')



find_elment(driver,username).send_keys("admin")
find_elment(driver,password).send_keys("shopxo")
find_elment(driver,loginpwd).click()

#ifram切换作用域到子网页中
zuoyongyu = ("id","ifcontent") 
driver.switch_to_frame(driver,zuoyongyu)

zongliang = ("xpath",'/html/body/div[1]/div/div[1]/ul/li[1]/div/p[2]')
a = find_elment(driver,zongliang).text
print(a)

