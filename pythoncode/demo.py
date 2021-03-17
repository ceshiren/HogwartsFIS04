"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/3/16 8:54 下午'
"""

a = 1

def demo1():
    # 告诉 解释器，现在要使用外面的全局的a
    global a
    a =2
    print(a)
    print(id(a))
    return a


print(demo1())

# print(id(a))

# 支持嵌套函数, 闭包函数
def outer():
    def inner():
        print("inner")
    return inner

outer()
