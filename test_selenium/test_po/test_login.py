"""
__author__ = 'jaxon'
__time__ = '2021/4/17 下午2:04'
__desc__ = ''
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_addmember():
    opt = webdriver.ChromeOptions()
    # 设置debug地址
    opt.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    driver.implicitly_wait(10)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    driver.find_element_by_id("menu_contacts").click()
    ele = (By.CSS_SELECTOR,".ww_operationBar .js_add_member")
    # WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable(ele))
    # driver.find_element_by_css_selector(".ww_operationBar .js_add_member").click()
    while True:
        # *ele 解元组
        driver.find_element(*ele).click()
        ele_num = len(driver.find_elements(By.ID,"username"))
        print(ele_num)
        if ele_num>0:
            break
    driver.find_element(By.ID, "username").send_keys("zhangsan")
    driver.find_element_by_id("memberAdd_acctid").send_keys("0417")
    driver.find_element_by_id("memberAdd_phone").send_keys("18300000000")
    driver.find_element_by_css_selector(".js_btn_save").click()
    eles = driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(5)")
    print(eles)
    for value in eles:
        if value.get_attribute("title") == "18300000000":
            return True
