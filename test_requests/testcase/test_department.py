# -*- coding: utf-8 -*-
# @Author : feier
# @File : test_department.py
# from jsonpath import jsonpath
import allure

from test_requests.apis.department import Department
from test_requests.testcase.utils import Utils

'''
1. 通过 ApiObject 设计模式，把框架分为了3层
2. wework 中获取 token， department 中描述接口
3. 测试用例中通过 setup_class 完成接口类的实例化
4. 测试用例中准备测试数据，完成业务拼装，完成断言
'''

@allure.feature("部门管理测试")
class TestDepartment:

    def setup_class(self):
        # 获取通讯录管理的 token 参数
        conf_data = Utils.get_yaml_data("../data/conf.yaml")
        corpid = conf_data["corpid"]["hogwarts"]
        corpsecret = conf_data["secret"]["contact_secret"]
        # 实例化部门类
        self.department = Department(corpid, corpsecret)
        # 清除部门数据
        self.department.clear_departments()
        # 准备测试数据
        self.depart_id = 4
        self.create_data = {
            "name": "广州研发中心2",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1,
            "id": self.depart_id
        }
        self.update_data = {
            "id": self.depart_id,
            "name": "广州研发中心-update",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1
        }

    @allure.story("部门操作场景用例")
    def test_department_scene(self):
        '''
        部门增删改查场景测试
        '''
        # 创建部门
        with allure.step("创建部门"):
            self.department.create_department(self.create_data)
        # 查询是否创建成功
        with allure.step("查询部门创建结果"):
            depart_info = self.department.get_department()
            print(depart_info)
            # assert depart_info["department"][1]["name"] == "广州研发中心2"
            # 通过 jsonpath 进行断言
            name_list = Utils.base_jsonpath(depart_info, "$..name")
            self.department.log_info(name_list)
            assert "广州研发中心2" in name_list

        # 更新部门
        with allure.step("更新部门信息"):
            self.department.update_department(self.update_data)
        # 查询是否更新成功
        with allure.step("查询部门更新结果"):
            depart_info = self.department.get_department()
            print(depart_info)
            # assert depart_info["department"][1]["name"] == "广州研发中心-update"
            # 通过 jsonpath 进行断言
            name_list = Utils.base_jsonpath(depart_info, "$..name")
            self.department.log_info(name_list)
            assert "广州研发中心-update" in name_list

        # 删除部门
        with allure.step("删除部门"):
            self.department.delete_department(self.depart_id)
        # 查询是否删除成功
        with allure.step("查询删除结果"):
            depart_info = self.department.get_department()
            print(depart_info)
            # assert len(depart_info["department"]) == 1
            # 使用 jsonpath 把所有部门 id 提取出来
            id_list = Utils.base_jsonpath(depart_info, "$..id")
            self.department.log_info(id_list)
            assert self.depart_id not in id_list

