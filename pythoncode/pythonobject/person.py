"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/3/20 2:23 下午'
"""
"""
创建一个Person 类
属性：姓名，性别，年龄，存款金额
方法: 吃，睡，跑，赚钱
"""


class Person:
    # 静态属性
    name = None
    gender = "男"
    age = 0
    # 私有属性
    __money = 1000

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    # 动态方法
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print("sleeping")

    def running(self):
        print(f"{self.name} is running")

    def have_money(self):
        return self.__money

    def __get_money(self):
        return self.__money + 1000

    def get_get_money(self):
        self.__get_money()


class Funny(Person):
    skill: str

    # 继承 Person类的属性和方法
    # 新增方法 fun() 搞笑 方法

    def __init__(self, name, gender, age, skill):
        super().__init__(name, gender, age)
        self.skill = skill

    def fun(self):
        print(f"{self.name} is funny")


class Singer(Person):

    def get_money(self):
        return "10000"

# print(Funny.name)
# Funny.running()

# fun1 = Funny("沈腾", "男", "30","搞笑")
# print(fun1.name)
# fun1.running()

# fun1.fun()
# print(fun1.skill)
#
# singer1 = Singer("周杰伦", "男", "30")
# print(singer1.get_money())

# 实例化一个人  ，类的实例化
# p1 = Person(name="张三", gender="女", age="20")
# print(p1.name)
# p1.eat()

# p2 = Person(age="30",name="李四",gender="男")
# print(p2.name)
# print(p2.age)
# print(p2.running())
# print(p2.have_money())
#
# print(dir(p2))
# print(p2._Person__money)
