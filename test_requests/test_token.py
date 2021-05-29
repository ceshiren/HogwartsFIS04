# -*- coding: utf-8 -*-
# @Author : feier
# @File : test_token.py
import requests


class TestToken:

    def test_get_token(self):
        '''
        获取 access_token
        :return:
        '''
        # 定义凭证
        corp_id = "ww876064acebf0fa3c"
        corp_secret = "A7LgEhs_Ty_dYXO9BcgY04PJBdawQ6JPzxNQJpv9YxY"

        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"

        # 定义请求参数
        params = {
            "corpid": corp_id,
            "corpsecret": corp_secret
        }

        # 发出 get 请求
        r = requests.get(url, params=params)
        print(type(r.text))
        # 查看响应信息
        print(r.json())

    def test_get_token2(self):
        # 定义凭证
        corp_id = "ww876064acebf0fa3c"
        corp_secret = "A7LgEhs_Ty_dYXO9BcgY04PJBdawQ6JPzxNQJpv9YxY"

        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={corp_secret}"

        r = requests.request("GET", url)
        print(r.json())
        assert r.status_code == 200
        assert r.json()['errmsg'] == "ok"
