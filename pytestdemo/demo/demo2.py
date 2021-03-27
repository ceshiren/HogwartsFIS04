"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/3/27 3:27 下午'
"""


# yield 用法
# 生成器

def provider():
    for i in range(0, 10):
        print("start")
        yield i  # 相当于 return，返回数据， 还记录了上一次的执行位置，下一次继续执行
        print("end")


p = provider()
print(next(p))  # 0
print(next(p))  # 1
print(next(p))  # 2
print(next(p))
