"""
__author__ = 'jaxon'
__time__ = '2021/4/17 下午3:03'
__desc__ = ''
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from test_selenium.test_po.package.add_member_page import AddMember
from test_selenium.test_po.package.basepage import BasePage

# 通讯录页面
class Contact(BasePage):
    def click_add_member(self):
        # opt = webdriver.ChromeOptions()
        # # 设置debug地址
        # opt.debugger_address = "127.0.0.1:9222"
        # driver = webdriver.Chrome(options=opt)
        # driver.implicitly_wait(10)
        # ele = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
        while True:
            # *ele 解元组
            self.find_and_click(By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
            ele_num = len(self.finds(By.ID, "username"))
            print(ele_num)
            if ele_num > 0:
                break
        return AddMember(self.driver)

    def get_member(self):
        sleep(1)
        member_list = []
        # opt = webdriver.ChromeOptions()
        # # 设置debug地址
        # opt.debugger_address = "127.0.0.1:9222"
        # driver = webdriver.Chrome(options=opt)
        # driver.implicitly_wait(10)
        # eles = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(5)")
        eles = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(5)")
        for value in eles:
            member_list.append(value.get_attribute("title"))
        return member_list