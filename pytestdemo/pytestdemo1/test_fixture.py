"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/3/27 2:52 下午'
"""
def test_search():
    print("搜索")


def test_cart():
    print("添加购物车")


def test_order(login, connect_db):
    url = f"http://xxxx.xxtoken={login}"
    print(url)
    print("下单")


def test_case1(connect_db):
    print("case1")
    print(connect_db)


def test_case2():
    print("case2")
