"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/5/15 4:48 下午'
"""
# 基类 用来存放最基本的方法
import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator):
        logging.info('find')
        logging.info(by)
        logging.info(locator)
        return self.driver.find_element(by, locator)

    def find_and_click(self, by, locator):
        logging.info('find_and_click')
        return self.find(by, locator).click()

    def swipe_find(self, text, num=3):
        # num = 3
        self.driver.implicitly_wait(1)
        for i in range(num):
            try:

                ele = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                self.driver.implicitly_wait(5)
                return ele
            except:
                print("未找到")
                size = self.driver.get_window_size()
                # 'width', 'height'
                width = size.get('width')
                height = size.get("height")

                startx = width / 2
                starty = height * 0.8
                endx = startx
                endy = height * 0.3
                duration = 2000  # 单位是ms

                self.driver.swipe(startx, starty, endx, endy, duration)

            if i == 2:
                self.driver.implicitly_wait(5)
                raise NoSuchElementException()

    def back(self, num=3):
        for i in range(num):
            self.driver.back()
