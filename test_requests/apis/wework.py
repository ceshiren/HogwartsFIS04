# -*- coding: utf-8 -*-
# @Author : feier
# @File : wework.py
'''
企业微信特有逻辑，完成 access_token 获取
'''
import requests


class WeWork:

    def __init__(self):
        self.token = self.get_access_token()

    def get_access_token(self):
        '''
        获取 access_token
        :return: access_token 值
        '''
        # 定义凭证
        corp_id = "ww876064acebf0fa3c"
        corp_secret = "A7LgEhs_Ty_dYXO9BcgY04PJBdawQ6JPzxNQJpv9YxY"

        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={corp_secret}"

        r = requests.request("GET", url)
        token = r.json()["access_token"]
        return token
