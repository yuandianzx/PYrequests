import unittest

class TestCase01(unittest.TestCase):
    '''测试TestCase01类，并显示在html报告中'''
    def test01(self):
        '''测试test01，并显示在html报告中'''
        print('test01')

    @unittest.skip('无条件忽略')     # 忽略函数test03
    def test03(self):
        print('test03')

    def test04(self):
        '''测试test04，并显示在html报告中'''
        print('test04')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    # print(suite)
    suite.addTest(TestCase01.test01)        # 将用例加载进suite套件中

    unittest.main(defaultTest = 'suite')