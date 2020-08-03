import unittest
from common import requests_utils

class TestCase01(unittest.TestCase):
    '''测试TestCase01类，并显示在html报告中'''
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test01(self):
        '''测试test01，并显示在html报告中'''
        RequestsUtils = requests_utils.RequestsUtils()
        get_infos = {'请求参数': '', '测试用例名称': '获取token成功', '测试用例步骤': 1.0, '期望结果类型': '正则匹配', '期望结果': 72001,
                     '请求地址': 'cgi-bin/token', '取值代码': '"access_token":"(.+?)"', '取值方式': '正则取值',
                     '用例执行': '是',
                     '提交数据': '{"grant_type":"client_credential","appid":"wx7cc16178655bc79e","secret":"ed3e70fe8244e88ff52d3abc2101c31d"}',
                     '测试用例编号': 1.0, '接口名称': '获取token', '请求方式': 'get', '传值变量': ''}
        result = RequestsUtils.request(get_infos)
        # print('期望结果为：', get_infos['期望结果'])
        # print(type(get_infos['期望结果']))
        # print('实际结果为：', result['response_json'])
        # print(type(result['response_json']['expires_in']))
        self.assertEqual(get_infos['期望结果'], result['response_json']['expires_in'])


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