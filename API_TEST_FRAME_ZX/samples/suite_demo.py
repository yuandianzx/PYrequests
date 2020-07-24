import unittest
from test01_suite import test01
from test01_suite.test02_suite import test02

class TestCase(unittest.TestCase):
    def test01_demo(self):
        print('test01')

    def test02_demo(self):
        print('test02')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    print(suite)
    suite1 = unittest.TestLoader().loadTestsFromModule(test01)  # 将模块下的用例加载进suite1
    suite2 = unittest.TestLoader().loadTestsFromTestCase(test02.TestCase02)  # 将类下面的用例加载进suite2
    suite3 = unittest.TestLoader().loadTestsFromName('test01_suite.test01.TestCase01.test03')  # 将用例加载进suite3
    suite.addTest(suite1)       # 将suite1加载进suite
    suite.addTest(suite2)
    suite.addTest(suite3)
    unittest.main(defaultTest = 'suite')        #
