"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/3/23 8:53 下午'
"""

# 测试用例，实际结果与预期结果相比较，如果一致，通过，否则，失败
import pytest
import yaml

from pytestdemo.calculator import Calculator


def get_datas():
    with open("./datas/calc.yaml") as f:
        datas = yaml.safe_load(f)
    return datas


def test_data():
    add_int = get_datas()['add_int']['datas']
    # add_float = get_datas()['add_float']
    # div_error = get_datas()['div_error']
    print(add_int)
    # print(add_float)


# 测试类
class TestCal:
    def setup_class(self):
        print("类级别setup")

    def teardown_class(self):
        print("类级别teardown")

    def setup(self):
        self.calc = Calculator()
        print("准备开始计算")

    # 测试相加功能
    # 测试用例：整数，浮点数，负数，为零，大数。。。
    @pytest.mark.parametrize('a,b,expect', get_datas()['add_int']['datas'], ids=get_datas()['add_int']['ids'])
    def test_add_int(self, a, b, expect):
        assert self.calc.add(a, b) == expect

    @pytest.mark.parametrize('a,b,expect', get_datas()['add_float']['datas'], ids=get_datas()['add_float']['ids'])
    def test_add_float(self, a, b, expect):
        assert round(self.calc.add(a, b), 2) == expect

    @pytest.mark.parametrize('a,b,expect', [
        [1, 0, 1]
    ])
    def test_div_error(self, a, b, expect):
        with pytest.raises(ZeroDivisionError):
            self.calc.div(a, b)

    def teardown(self):
        print("结束计算")
