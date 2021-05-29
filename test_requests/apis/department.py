# -*- coding: utf-8 -*-
# @Author : feier
# @File : department.py
'''
接口信息描述，只关注业务，不需要做断言
'''
# import requests

from test_requests.apis.wework import WeWork
from test_requests.testcase.utils import Utils


class Department(WeWork):

    def create_department(self, data):
        '''
        创建部门
        :return: 创建部门接口的响应
        '''
        create_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}"
        '''
        1. 把接口信息请求信息封装到字典中
        2. 接口中不需要再引入 requests
        '''
        req = {
            "method": "post",
            "url": create_url,
            "json": data
        }
        # r = requests.request("POST", create_url, json=data)
        r = self.send_api(req)
        return r.json()

    def update_department(self, data):
        '''
        更新部门信息
        :return: 更新部门接口的响应
        '''
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}"
        req = {
            "method": "post",
            "url": url,
            "json": data
        }
        # r = requests.request(method="POST", url=url, json=data)
        r = self.send_api(req)
        return r.json()

    def delete_department(self, depart_id):
        '''
        删除部门
        :return: 删除部门接口的响应
        '''
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={depart_id}"
        req = {
            "method": "get",
            "url": url
        }
        # r = requests.request(method="GET", url=url)
        r = self.send_api(req)
        return r.json()

    def get_department(self):
        '''
        获取部门列表
        :return: 获取部门接口的响应
        '''
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        req = {
            "method": "get",
            "url": url
        }
        # r = requests.request(method="GET", url=url)
        r = self.send_api(req)
        return r.json()

    def clear_departments(self):
        '''
        清理已经存在的部门信息
        '''
        # 查询目前存在的部门
        department_info = self.get_department()
        # 提取部门 id 列表
        id_list = Utils.base_jsonpath(department_info, "$..id")
        # id 为 1 的部门是最基础的父部门，不可以删除
        for i in id_list:
            if i != 1:
                # 删掉删除部门接口
                self.delete_department(i)
