"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/5/15 4:27 下午'
"""
# 添加成员页
# from test_appium.page.edit_member_page import EditMemberPage
from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.base_page import BasePage


class AddMemeberPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def click_addmember_menual(self):
        # click 手动输入添加
        self.find_and_click(MobileBy.XPATH, "//*[@text='手动输入添加']")
        from test_appium.page.edit_member_page import EditMemberPage
        return EditMemberPage(self.driver)

    def verify_toast(self):
        self.find(MobileBy.XPATH, "//*[@text='添加成功']")
        return True
