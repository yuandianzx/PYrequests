# coding:utf-8
import unittest
import requests
import time
# 禁用安全请求警告
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
class Blog_login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("所有测试方法之前执行")
    @classmethod
    def tearDownClass(cls):
        print("所有测试方法之后执行")
    def setUp(self):
        print('开始')
    def tearDown(self):
        time.sleep(1)
        print('结束')
    def login(self,phone,password):
        '''三个参数：   账号：phone，密码：password,记住登录：extNumber=True'''
        url = "http://webapi.test.sxmaps.com/authentication/api/notcheck/login"
        header = {"Content-Type": "application/json;charset=UTF-8"}
        on_datajs = {"phone": phone,
        "password": password,
        "extNumber":""}
        res = requests.post(url, headers=header, json=json_data, verify=False)
        result1 = res.content # 字节输出
        return res.json() # 返回 json
    def test_login1(self):
        '''测试登录：正确账号，正确密码'''
        phone = "18274852609"
        password = "Admin123"
        result = self.login(phone, password)
        self.assertEqual(result["message"], "success")
        print("测试用例1")
    def test_login2(self):
        '''测试登录：正确账号，错误密码'''
        phone = "18274852609"
        password = "admin123"
        result = self.login(phone, password)
        self.assertEqual(result["message"], "success",msg="ceshi")
        print("测试用例2")
if __name__ == "__main__":
    unittest.main()