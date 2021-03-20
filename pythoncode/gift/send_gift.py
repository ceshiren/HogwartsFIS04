"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/3/16 9:10 下午'
"""
# 不要起名为系统模块名或者第三方模块名
# 类似这种：sys os, appium,selenium, random


'''
实现发礼物，之后展示礼物
1、默认值（have_gift=False） 没有礼物
2、定义一个发礼物的方法
3、定义一个显摆礼物的方法
4、实现发完礼物之后，能展示礼物
'''

# from gift import have_gift
import gift
def send_gift():
    # global have_gift
    gift.have_gift = True
    print("发礼物啦")
