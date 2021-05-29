# -*- coding: utf-8 -*-
# @Author : feier
# @File : base_api.py
import logging

import requests


class BaseApi:
    # 设置 loging
    fileHandler = logging.FileHandler(filename="../logs/apitest.log", encoding="utf-8")
    logging.getLogger().setLevel(0)
    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s')
    fileHandler.setFormatter(formatter)
    logging.getLogger().addHandler(fileHandler)

    def log_info(self, msg):
        '''
        添加日志信息方法
        :return: info 级别的日志
        '''
        return logging.info(msg)

    def send_api(self, req):
        '''
        对 requests 进行二次封装
        :return: 接口响应结果
        '''
        # req = {
        #     "method": "get",
        #     "url": "xxxxx",
        #     "params": {},
        #     "json":{}
        # }
        # ** req 等同于 requests.request(method="get", url="xxxx", params={}, json={})
        self.log_info("-----request data-----")
        self.log_info(req)
        r = requests.request(**req)
        self.log_info("-----response data-----")
        self.log_info(r.json())
        return r