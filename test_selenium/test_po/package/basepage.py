"""
__author__ = 'jaxon'
__time__ = '2021/4/17 下午4:04'
__desc__ = ''
"""
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    _base_url = ""

    def __init__(self, _driver_base: WebDriver = None):
        if _driver_base is None:
            # 避免driver重复初始化，第一次初始化的时候driver是空的，就进行初始化
            opt = webdriver.ChromeOptions()
            # 设置debug地址
            opt.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=opt)
            self.driver.implicitly_wait(10)
            print(self._base_url)
        else:
            self.driver = _driver_base

        if self._base_url != "":
            self.driver.get(self._base_url)

    def find(self, by, locator):
        return self.driver.find_element(by,locator)

    def find_and_click(self,by, locator):
        ele: WebElement = self.find(by, locator)
        ele.click()
        return ele


    def finds(self, by, locator):
        return self.driver.find_elements(by,locator)


