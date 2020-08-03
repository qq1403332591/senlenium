import time
from selenium import  webdriver
from selenium.webdriver import ActionChains
import os
from  selenium.webdriver.support.ui import WebDriverWait
from utils.seleniumtools import find_element


driver = webdriver.Chrome(executable_path='chromedriver.exe')


class Test_admin():
    def test_login(self):
        driver.maximize_window()
        driver.get('https://devadmin.zhixiaoxin.net/login/')
        time.sleep(3)
        driver.find_element_by_id('phone').send_keys('13153117137')
        driver.find_element_by_id('password').send_keys('123456')
        driver.find_element_by_xpath('//*[@id="login_form"]/div[3]/div[2]/button').click()

    def test_02_cource(self):
        kc_name = ("name", "name")
        kc_jianjie = ("name","description")
        kc_leimu = ("id", "select2-certified_id-container")
        insert = ("xpath", '//*[@id="certified-select"]/span')
        jiage = ("name", "price")
        yhjg = ("name", "true_price")
        sxtime = ("id", "starttime")
        sxqueding  = ('xpath', '//*[@id="layui-laydate1"]/div[2]/div/span[3]')
        endtime = ("id", "endtime")
        endqueding = ('xpath', '//*[@id="layui-laydate2"]/div[2]/div/span[3]')
        fanye = ('xpath','//*[@id="layui-laydate2"]/div[1]/div[1]/i[4]')

        time.sleep(2)
        driver.find_element_by_link_text('小新考证').click()
        driver.find_element_by_link_text('课程管理').click()
        driver.find_element_by_link_text('添加课程').click()
        find_element(driver, kc_name).send_keys("java测试课程")
        find_element(driver, kc_jianjie).send_keys("测试课程")
        time.sleep(2)
        # find_element(driver, ('xpath', '//*[@id="certified-select"]/div[1]/span/span[1]/span/span[2]')).click()
        time.sleep(2)
        drop_down = driver.find_element_by_xpath('//*[@id="certified-select"]/div[1]/span/span[1]/span/span[2]')
        ActionChains(driver).click(drop_down).perform()
        time.sleep(2)
        ul = driver.find_element_by_css_selector('#select2-certified_id-results')
        ul_res = ul.find_element_by_xpath('li[3]').click()
        time.sleep(2)
        find_element(driver,insert).click()
        find_element(driver,jiage).send_keys("1221")
        find_element(driver,yhjg).send_keys("0.01")
        find_element(driver,sxtime).click()
        find_element(driver,sxqueding).click()
        find_element(driver,endtime).click()
        find_element(driver,fanye).click()

        # find_element(driver, ('xpath','/html/body/script[16]')).click()
        find_element(driver,endqueding).click()
        find_element(driver,("name","room_id")).send_keys('FFB08EE857D91FA8')
        time.sleep(1)
        find_element(driver, ('xpath','//*[@id="test2"]')).click()
        time.sleep(2)
        os.system("11111.exe")
        time.sleep(2)
        target = driver.find_element_by_id('submit')
        driver.execute_script("arguments[0].scrollIntoView();", target)
        time.sleep(3)


        iframe = driver.find_element_by_xpath('//*[@id="cke_1_contents"]/iframe')
        driver.switch_to_frame(iframe)  #切换作用域
        time.sleep(1)
        driver.find_element_by_xpath('/html/body').send_keys("sdasdasd")
        driver.switch_to.default_content()  # 切回原始作用域
        time.sleep(3)
        driver.find_element_by_id('submit').click()
        time.sleep(2)
        driver.quit()

