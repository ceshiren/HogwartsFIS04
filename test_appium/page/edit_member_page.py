"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/5/15 4:28 下午'
"""
# from test_appium.page.add_member_page import AddMemeberPage
from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.base_page import BasePage


class EditMemberPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def edit_member(self,name,phonenum):
        # input name
        # input phonenum
        # click 保存
        self.find(MobileBy.XPATH, "//*[contains(@text, '姓名')]/../*[@text='必填']").send_keys(name)
        self.find(MobileBy.XPATH, "//*[contains(@text, '手机')]/..//*[@text='必填']").send_keys(phonenum)
        # self.driver.find_elements(MobileBy.XPATH, '//*[@text="必填"]')[1]
        self.find(MobileBy.XPATH, "//*[@text='保存']").click()
        from test_appium.page.add_member_page import AddMemeberPage
        return AddMemeberPage(self.driver)

