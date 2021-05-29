# -*- coding: utf-8 -*-
# @Author : feier
# @File : test_department.py
from test_requests.apis.department import Department
'''
1. 通过 ApiObject 设计模式，把框架分为了3层
2. wework 中获取 token， department 中描述接口
3. 测试用例中通过 setup_class 完成接口类的实例化
4. 测试用例中准备测试数据，完成业务拼装，完成断言
'''

class TestDepartment:

    def setup_class(self):
        # 实例化部门类
        self.department = Department()
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

    def test_department_scene(self):
        '''
        部门增删改查场景测试
        '''
        # 创建部门
        self.department.create_department(self.create_data)
        # 查询是否创建成功
        depart_info = self.department.get_department()
        assert depart_info["department"][1]["name"] == "广州研发中心2"

        # 更新部门
        self.department.update_department(self.update_data)
        # 查询是否更新成功
        depart_info = self.department.get_department()
        print(depart_info)
        assert depart_info["department"][1]["name"] == "广州研发中心-update"

        # 删除部门
        self.department.delete_department(self.depart_id)
        # 查询是否删除成功
        depart_info = self.department.get_department()
        assert len(depart_info["department"]) == 1
