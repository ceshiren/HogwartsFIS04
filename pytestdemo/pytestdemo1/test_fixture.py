"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/3/27 2:52 下午'
"""
import pytest


@pytest.mark.first
def test_search():
    print("搜索")


@pytest.mark.run(order=3)
def test_cart():
    print("添加购物车")


@pytest.mark.run(order=2)
def test_order(login, connect_db):
    url = f"http://xxxx.xxtoken={login}"
    print(url)
    print("下单")


@pytest.mark.run(order=5)
def test_case1(connect_db):
    print("case1")
    print(connect_db)


@pytest.mark.run(order=4)
def test_case2():
    print("case2")
