"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/3/20 2:05 下午'
"""
# 浅拷贝
import money
def send_money(salary):
    print("发工资啦")
    money.mymoney += salary
    print(money.mymoney)

