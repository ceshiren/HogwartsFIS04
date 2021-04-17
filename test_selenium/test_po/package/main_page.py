"""
__author__ = 'jaxon'
__time__ = '2021/4/17 下午3:03'
__desc__ = ''
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

from test_selenium.test_po.package.basepage import BasePage
from test_selenium.test_po.package.contact_page import Contact

# 主页
class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    def goto_contact(self):
        # opt = webdriver.ChromeOptions()
        # # 设置debug地址
        # opt.debugger_address = "127.0.0.1:9222"
        # driver = webdriver.Chrome(options=opt)
        # driver.implicitly_wait(10)
        # self.driver.find_element_by_id("menu_contacts").click()

        self.find_and_click(By.ID, "menu_contacts")
        return Contact(self.driver)