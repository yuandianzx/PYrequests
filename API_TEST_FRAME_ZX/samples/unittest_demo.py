import unittest

class test_demo(unittest.TestCase):
    def setUp(self):
        print('setUp')
    def tearDown(self):
        print('tearDown')
    def test_case1(self):
        print('case1')

if __name__ == '__main__':
    unittest.main()