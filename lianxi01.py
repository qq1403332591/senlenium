# 1.导包
from selenium import webdriver
import time 

# 2.实例化浏览器并且获得浏览器句柄（打开浏览器并且获得浏览器的操作对象）
driver = webdriver.Chrome(executable_path='chromedriver.exe')

# 3.打开网站
driver.get("http://132.232.44.158:9999/shopxo/")

driver.maximize_window() #浏览器全屏

# 4.定位元素
driver.find_element_by_name("wd").send_keys("华为")
driver.find_element_by_id("ai-topsearch").click()


# time.sleep(3)   #静态等待
driver.implicitly_wait(60)

#断言成功就通过,测试用例执行成功  失败就报错 测试用例执行失败 
try: #异常处理
    a = driver.find_element_by_xpath('/html/body/div[4]/div/ul/li/div/p[2]')
    assert a.text == "￥1999.00"
    print("测试用例执行成功")
except:
    print("测试用例执行失败")

# 退出浏览器
driver.quit()


