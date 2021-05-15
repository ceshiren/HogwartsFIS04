"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/5/15 4:26 下午'
"""
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException

from test_appium.page.add_member_page import AddMemeberPage
from test_appium.page.base_page import BasePage


class ContactListPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver

    def click_addmember(self):
        # 点击添加成员
        self.swipe_find("添加成员",num=5).click()
        return AddMemeberPage(self.driver)

