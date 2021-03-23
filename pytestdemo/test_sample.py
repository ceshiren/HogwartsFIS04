"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/3/23 8:12 下午'
"""
import pytest


def setup_module():
    print("模块级别 的setup")


def teardown_module():
    print("模块级别 的teardown")


def func(x):
    return x + 1


def test_answer():
    assert func(4) == 5


def test_a():
    assert func(3) == 4


def demo():
    assert False


class TestDemo:
    @pytest.mark.login
    def test_case1(self):
        print("testcase1>>>>>>>")
        assert False

    @pytest.mark.search
    def test_case2(self):
        print("testcase2>>>>>>>")
        assert False

    @pytest.mark.search
    @pytest.mark.login
    def test_case3(self):
        print("testcase3>>>>>>>")
        assert False
