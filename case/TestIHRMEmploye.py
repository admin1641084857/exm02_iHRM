"""
    测试员工模块的增删改查接口
"""
# 导包
import logging
import unittest
import requests

# 创建测试类
import app
from api.EmpAPI import EmpCRUD


class TestEmployee(unittest.TestCase):
    # 初始化函数
    def setUp(self):
        self.session = requests.Session()
        self.emp_obj = EmpCRUD()

    # 资源销毁函数
    def tearDown(self):
        self.session.close()

    # 测试函数1: 增
    def test_emp_add(self):
        # 1.请求业务
        response = self.emp_obj.add(self.session, "凹凸曼31620", "15555454531", "89325243")
        # 2.断言业务
        print("新增成功响应结果:", response.json())

    # 测试函数2: 改
    def test_emp_update(self):
        # 请求业务
        response = self.emp_obj.update(self.session,
                                       "1184445596517617664",
                                       "奥特曼0804AAA")
        # 断言业务
        print("修改后的响应体:", response.json())
        self.assertEqual(True, response.json().get("success"))

    # 测试函数3: 查
    def test_emp_get(self):
        # 1.请求业务
        response = self.emp_obj.get(self.session, "1184445596517617664")
        # 2.断言
        print("查询到的用户信息:", response.json())
        self.assertEqual(10000, response.json().get("code"))

    # 测试函数4: 删
    def test_emp_delete(self):
        app.my_log_config()
        try:
            response = self.emp_obj.delete(self.session, "1184445596517617664")
            print("删除的响应结果:", response.json())
            self.assertIn("操作成功", response.json().get("message"))
        except Exception as e:
            logging.info(e)
