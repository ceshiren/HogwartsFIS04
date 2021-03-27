"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/3/27 4:03 下午'
"""
import pytest
import yaml

from pytestdemo.calculator import Calculator


@pytest.fixture(scope="session", autouse=True)
def login():
    print("登录操作")
    token = "xkjldafaflajfladkfa"
    yield token
    print("登出操作")


@pytest.fixture()
def connect_db():
    print("连接数据库")
    yield "用户信息：用户名，密码"  # 相当于激活了fixture 的teardown 操作，在yield 后面的操作步骤 ，将被认为是teardown操作。
    print("断开数据库")


@pytest.fixture()
def get_calc():
    print("开始计算")
    calc = Calculator()
    yield calc
    print("结束计算")


def get_datas():
    with open("./datas/calc.yaml") as f:
        datas = yaml.safe_load(f)
    return datas


def get_adddata():
    adddatas = get_datas()['add_int']['datas']
    add_ids = get_datas()['add_int']['ids']
    return adddatas, add_ids


@pytest.fixture(params=get_adddata()[0], ids=get_adddata()[1])
def get_add_datas1(request):
    print(request.param)
    return request.param
