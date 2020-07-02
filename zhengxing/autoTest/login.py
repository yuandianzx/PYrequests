# coding:utf-8
import requests
import unittest
import time
import json
class Login(unittest.TestCase):
    def setUp(self):
        print("开始")
    def tearDown(self):
        time.sleep(2)
        print("结束")
    def testLogin(self):
        self.url = "http://webapi.test.sxmaps.com/authentication/api/notcheck/login"
        self.headers = {"Content-Type": "application/json;charset=UTF-8"}
        self.data = {"password":"Admin123","phone":"18274852609","extNumber":""}
        self.reb = requests.post(self.url,headers = self.headers,json=self.data).json()
        self.assertEqual(self.reb['message'],"success")
        print("执行测试用例1")
        # # return json.dumps(self.reb,indent=2)
        # rebKey1 = self.reb["message"]
        # print(rebKey1)
        # return self.assertEqual(rebKey1,"success",msg="%s != success，测试失败" % rebKey1)
    def testLogin1(self):
        print("执行测试用例2")
if __name__=="__main__":
    unittest.main()
    # a = Login().testLogin()
    # print(a)