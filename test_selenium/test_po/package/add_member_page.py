"""
__author__ = 'jaxon'
__time__ = '2021/4/17 下午3:04'
__desc__ = ''
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

from test_selenium.test_po.package.basepage import BasePage

# 添加成员信息
class AddMember(BasePage):
    def add_member(self,name,id,phone):
        # 避免循环导入；局部导入
        from test_selenium.test_po.package.contact_page import Contact
        # opt = webdriver.ChromeOptions()
        # # 设置debug地址
        # opt.debugger_address = "127.0.0.1:9222"
        # driver = webdriver.Chrome(options=opt)
        # driver.implicitly_wait(10)
        self.find(By.ID, "username").send_keys(name)
        self.find(By.ID,"memberAdd_acctid").send_keys(id)
        self.find(By.ID,"memberAdd_phone").send_keys(phone)
        # self.driver.find_element_by_css_selector(".js_btn_save").click()
        self.find_and_click(By.CSS_SELECTOR,".js_btn_save")
        return Contact(self.driver)