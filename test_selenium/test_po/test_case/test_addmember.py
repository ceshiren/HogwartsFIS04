"""
__author__ = 'jaxon'
__time__ = '2021/4/17 下午3:08'
__desc__ = ''
"""
import pytest

from test_selenium.test_po.package.main_page import MainPage


class TestAddmember:
    def setup(self):
        self.main = MainPage()

    def teardown(self):
        pass

    @pytest.mark.parametrize("name,id,phone",[("王五","0417011","18500000001"),("王五1","0417012","18500000002")])
    def test_addmember(self,name,id,phone):
        # name = "李四6"
        # id = "04175"
        # phone = "18800000006"
        # 链式调用
        # 主页-通讯录页面-点击添加成员-添加成员-获取成员信息
        ele = self.main.goto_contact().click_add_member().add_member(name,id,phone).get_member()
        print(ele)
        # 断言手机是否在成员信息列表
        assert phone in ele