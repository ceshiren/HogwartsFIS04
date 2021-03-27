"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/3/27 4:24 下午'
"""
import pytest


@pytest.fixture(params=[[1, 1, 2], [10, 20, 30]], ids=['整数1', 'int2'])
def login(request):
    print("login")
    return request.param


def test_case(login):
    print(login)
