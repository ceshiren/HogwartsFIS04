# -*- coding: utf-8 -*-
# @Author : feier
# @File : utils.py
import yaml
from jsonpath import jsonpath


class Utils:

    @classmethod
    def get_yaml_data(cls, file_path):
        '''
        封装 yaml 文件读取的方法
        :param file_path: yaml 文件的路径
        :return: 字典格式的 yaml 文件内容
        '''
        with open(file_path) as f:
            datas = yaml.safe_load(f)
        return datas

    @classmethod
    def base_jsonpath(cls, obj, json_expr):
        '''
        封装 jsonpath 断言
        :param obj: 要断言的响应内容
        :param json_expr: jsonpath 表达式
        :return: 提取内容的列表
        '''
        return jsonpath(obj, json_expr)