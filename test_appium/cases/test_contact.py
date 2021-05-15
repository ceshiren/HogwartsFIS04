"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/5/15 4:31 下午'
"""
from test_appium.page.app import App

from faker import Faker


class TestContact:
    def setup_class(self):
        self.fake = Faker('zh_CN')
        # 启动app
        self.app = App()

    def setup(self):
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.back()

    def teardown_class(self):
        self.app.stop()

    def test_addcontact(self):
        name = self.fake.name()
        phonenum = self.fake.phone_number()
        result = self.main.goto_contact(). \
            click_addmember().click_addmember_menual(). \
            edit_member(name, phonenum).verify_toast()
        assert result

    def test_addcontact1(self):
        name = self.fake.name()
        phonenum = self.fake.phone_number()
        result = self.main.goto_contact(). \
            click_addmember().click_addmember_menual(). \
            edit_member(name, phonenum).verify_toast()
        assert result
