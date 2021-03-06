from selenium.webdriver.support.ui import WebDriverWait

def find_elment(driver,locator,timeout=60):
    '''
        参数：
            driver:浏览器句柄
            locator:元素定位方法("id","xxx")
            timeout:超时时间，默认10

        返回值：元素本身
    '''
    return WebDriverWait(driver,timeout).until(lambda s: s.find_element(*locator))