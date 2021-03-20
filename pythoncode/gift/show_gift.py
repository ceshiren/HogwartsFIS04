"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/3/16 9:33 下午'
"""
# from pythoncode.gift import have_gift
import gift

def show_gift():
    have_gift = gift.have_gift
    if have_gift == True:
        print("收到礼物啦，好开心")
    else:
        print("等待礼物中...")
