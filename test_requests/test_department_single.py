# -*- coding: utf-8 -*-
# @Author : feier
# @File : test_department_single.py
import pytest
import requests


class TestDepartmentSingle:

    def setup_class(self):
        # 定义凭证
        corp_id = "ww876064acebf0fa3c"
        corp_secret = "A7LgEhs_Ty_dYXO9BcgY04PJBdawQ6JPzxNQJpv9YxY"

        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={corp_secret}"

        r = requests.request("GET", url)
        self.token = r.json()["access_token"]

    @pytest.mark.parametrize(
        "name, name_en, parentid, order, depart_id, expect",
        [
            ("技术部", "JISHU1", 1, 2, 4, 0),
            ("技术部", "JISHU2", 1, 3, 1, 60123),
            ("技术部1t6yujk9osjhynnj890lkmbg54321w", "JISHU2", 1, 3, 5, 60001)
        ]
    )
    def test_create_department(self, name, name_en, parentid, order, depart_id, expect):
        '''
        创建部门
        '''
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
        data = {
            "name": name,
            "name_en": name_en,
            "parentid": parentid,
            "order": order,
            "id": depart_id
        }
        params = {
            "access_token": self.token
        }
        r = requests.request("POST", url, params=params, json=data)
        print(r.json())
        assert r.json()["errcode"] == expect