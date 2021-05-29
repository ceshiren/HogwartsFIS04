# -*- coding: utf-8 -*-
# @Author : feier
# @File : test_wework.py
import requests


class TestWework:

    def setup_class(self):
        # 定义凭证
        corp_id = "ww876064acebf0fa3c"
        corp_secret = "A7LgEhs_Ty_dYXO9BcgY04PJBdawQ6JPzxNQJpv9YxY"

        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={corp_secret}"

        r = requests.request("GET", url)
        self.token = r.json()["access_token"]
        self.depart_id = 5

    def test_create_department(self):
        '''
        创建部门
        '''
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
        data = {
            "name": "广州研发中心2",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1,
            "id": self.depart_id
        }
        params = {
            "access_token": self.token
        }
        r = requests.request("POST", url, params=params, json=data)
        print(r.json())
        assert r.json()["errcode"] == 0
        # 通过查询部门列表接口拿到部门信息
        depart_info = self.test_get_departments()
        print(depart_info)
        assert depart_info["department"][1]["name"] == "广州研发中心2"

    def test_update_department(self):
        '''
        更新部门信息
        '''
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}"
        data = {
            "id": self.depart_id,
            "name": "广州研发中心-update",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1
        }
        r = requests.request(method="POST", url=url, json=data)
        assert r.json()["errcode"] == 0
        # 通过查询部门列表接口拿到部门信息
        depart_info = self.test_get_departments()
        print(depart_info)
        assert depart_info["department"][1]["name"] == "广州研发中心-update"


    def test_delete_department(self):
        '''
        删除部门
        '''
        # depart_id = 3
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={self.depart_id}"
        r = requests.request(method="GET", url=url)
        assert r.json()["errcode"] == 0
        # 通过查询部门列表接口拿到部门信息
        depart_info = self.test_get_departments()
        print(depart_info)
        assert len(depart_info["department"]) == 1


    def test_get_departments(self):
        '''
        查询部门信息
        :return:
        '''
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        r = requests.request(method="GET", url=url)
        assert r.json()["errcode"] == 0
        return r.json()


