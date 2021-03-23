"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/3/23 8:53 下午'
"""

# 测试用例，实际结果与预期结果相比较，如果一致，通过，否则，失败
from pytestdemo.calculator import Calculator


# 测试类
class TestCal:
    def setup_class(self):
        print("类级别setup")

    def teardown_class(self):
        print("类级别teardown")

    def setup(self):
        print("准备开始计算")

    # 测试相加功能
    def test_add(self):
        calc = Calculator()
        assert calc.add(1, 1) == 2

    def test_add1(self):
        calc = Calculator()
        assert calc.add(1, 3) == 4

    def teardown(self):
        print("结束计算")
