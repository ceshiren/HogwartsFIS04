"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/5/15 5:11 下午'
"""
from faker import Faker


class Contact:
    def __init__(self):
        self.fake = Faker('zh_CN')

    def get_name(self):
        return self.fake.name()

    def get_phonenum(self):
        return self.fake.phone_number()