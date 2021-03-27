"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/3/27 2:52 下午'
"""
import pytest


@pytest.fixture(autouse=True, scope='session')
def login():
    print("登录操作")
    token = "xkjldafaflajfladkfa"
    return token


@pytest.fixture()
def connect_db():
    print("连接数据库")
    yield "用户信息：用户名，密码"  # 相当于激活了fixture 的teardown 操作，在yield 后面的操作步骤 ，将被认为是teardown操作。
    print("断开数据库")


def test_search():
    print("搜索")


def test_cart():
    print("添加购物车")


# @pytest.mark.usefixtures('login')
def test_order(login, connect_db):
    url = f"http://xxxx.xxtoken={login}"
    print(url)
    print("下单")


def test_case1(connect_db):
    print("case1")
    print(connect_db)


def test_case2():
    print("case2")
