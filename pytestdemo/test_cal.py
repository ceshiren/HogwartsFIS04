"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/3/23 8:53 下午'
"""
import allure


@allure.feature("计算器测试")
class TestCal:

    # 测试相加功能
    # 测试用例：整数，浮点数，负数，为零，大数。。。
    # @pytest.mark.parametrize('a,b,expect', get_datas()['add_int']['datas'], ids=get_datas()['add_int']['ids'])
    @allure.story("相加功能")
    def test_add_int(self, get_calc, get_add_datas1):
        assert get_calc.add(get_add_datas1[0], get_add_datas1[1]) == get_add_datas1[2]

    # @pytest.mark.parametrize('a,b,expect', get_datas()['add_float']['datas'], ids=get_datas()['add_float']['ids'])
    # def test_add_float(self,get_calc, a, b, expect):
    #     assert round(get_calc.add(a, b), 2) == expect
    #
    # @pytest.mark.parametrize('a,b,expect', [
    #     [1, 0, 1]
    # ])
    # def test_div_error(self,get_calc, a, b, expect):
    #     with pytest.raises(ZeroDivisionError):
    #         get_calc.div(a, b)
