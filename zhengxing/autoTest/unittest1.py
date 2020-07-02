# coding:utf-8
import unittest
import time
class Test(unittest.TestCase):
    '''判断两个值是否相等'''     #类的说明，可print(Test.__doc__)输出说明
    def setUp(self):
        print("开始")
    def tearDown(self):
        time.sleep(1)
        print("结束")
    def test2(self):
        a = 6-5
        b = 1
        self.assertEqual(a,b)     #self表示创建的实例本身
        print("执行用例2")
    def test1(self):
        a = "测试啊"
        b = "测试啊"
        self.assertEqual(a,b,msg="如果a!=b，输出自定义异常")    #如果a != b，输出自定义异常
        print("执行用例1")

if __name__ == '__main__':
    unittest.main()
# import sys
# sys.path.append("D:\PYrequests\zhengxing")
# print(Test.__doc__)