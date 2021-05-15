"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/5/15 4:25 下午'
"""

# 主页
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from test_appium.page.base_page import BasePage
from test_appium.page.contactlist_page import ContactListPage


class MainPage(BasePage):
    # def __init__(self, driver:WebDriver):
    #     self.driver = driver
    _address_list_element = (MobileBy.XPATH, "//*[@text='通讯录']")
    def goto_contact(self):
        # click 通讯录
        self.find_and_click(*self._address_list_element)
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return ContactListPage(self.driver)
