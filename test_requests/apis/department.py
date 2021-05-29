# -*- coding: utf-8 -*-
# @Author : feier
# @File : department.py
'''
接口信息描述，只关注业务，不需要做断言
'''
import requests

from test_requests.apis.wework import WeWork


class Department(WeWork):

    def create_department(self, data):
        '''
        创建部门
        :return: 创建部门接口的响应
        '''
        create_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}"
        r = requests.request("POST", create_url, json=data)
        return r.json()

    def update_department(self, data):
        '''
        更新部门信息
        :return: 更新部门接口的响应
        '''
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}"
        r = requests.request(method="POST", url=url, json=data)
        return r.json()

    def delete_department(self, depart_id):
        '''
        删除部门
        :return: 删除部门接口的响应
        '''
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={depart_id}"
        r = requests.request(method="GET", url=url)
        return r.json()

    def get_department(self):
        '''
        获取部门列表
        :return: 获取部门接口的响应
        '''
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        r = requests.request(method="GET", url=url)
        return r.json()