"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/3/23 9:23 下午'
"""
import pytest


def add(a, b):
    return a + b


# 整数，浮点数，负数，为0，大数。。。。。。
@pytest.mark.parametrize("a,b,expect", [[1, 2, 3], [0.1, 0.2, 0.3], [-1, -2, -3], [1, 0, 1]],
                         ids=["int", "float", 'minus', 'zero'])
def test_add(a, b, expect):
    assert add(a, b) == expect


def test_add1(login):
    assert add(0.1, 0.2) == 0.3


def test_add2():
    assert add(-1, -2) == -3


@pytest.mark.parametrize("a", [[1, 2], [3, 4]])
def test_a(a):
    print(a)
