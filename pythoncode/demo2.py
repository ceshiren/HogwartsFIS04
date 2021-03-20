"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/3/20 4:15 下午'
"""

import yaml

# yaml.safe_load() 是将yaml 格式 转化成python的对象
with open("./datas/demo.yaml") as f:
    print(yaml.safe_load(f))

# 将 python 对象 转成 yaml 格式
# print(yaml.safe_dump({'name': "hogwarts", 'age': '20', 'gender': 'male'}))
