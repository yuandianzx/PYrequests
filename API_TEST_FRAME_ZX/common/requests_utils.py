import requests
import re
import json
import ast
from config_utils import ConfigUtils

# ConfigUtils = ConfigUtils()
class RequestsUtils():
    def __init__(self):
        self.hosts = ConfigUtils.read_config('host','wechat_host')
        self.headers = {"Content-Type": "application/json;charset=utf-8"}      # 待扩展参数,如果是application/x-www-form-urlencoded重新写一个headers？
        self.session = requests.session()
    def get(self, get_infos):
        '''封装get方法'''
        self.url = self.hosts + get_infos['请求地址']
        response = self.session.get(url = self.url,
                                    headers = self.headers,
                                    params = ast.literal_eval(get_infos['提交数据']),           # get请求使用params,将字符串转换为字典格式，字符串中的值要是字典格式的值
                                    verify = False)       # 如要通过代理抓取请求，加上verify=False
        response.encoding = response.apparent_encoding      # 如果response是网页，会出现乱码的情况，这种方法可以很好的解决
        response_json = json.dumps(response.json(), indent=2, sort_keys=True)   # 将返回的json串格式化
        result = {
            'code' : 0,      # 用来请求是否成功的标志位
            'response_reason': response.reason,
            'response_code' : response.status_code,
            'response_headers' : response.headers,
            'response_json' : response_json,
            'response.text' : response.text
        }

        return result

    def post(self, post_infos):
        '''封装post方法'''
        self.url = self.hosts + post_infos['请求地址']
        response = self.session.post(url= self.url,
                                    headers = self.headers,
                                    params = post_infos['请求参数'],
                                    json = ast.literal_eval(post_infos['提交数据']),
                                    verify = False)
        response.encoding = response.apparent_encoding
        response_json = json.dumps(response.json(), indent=2, sort_keys=True)
        result = {
            'code': 0,  # 用来请求是否成功的标志位
            'response_reason': response.reason,
            'response_code': response.status_code,
            'response_headers': response.headers,
            'response_json': response_json,
            'response.text': response.text
        }
        return result
    def request(self,step_infos):
        '''将get请求和post请求整合到一个方法中'''
        self.url = self.hosts + step_infos['请求地址']
        if step_infos['请求方式'] == 'get':
            result = self.get(step_infos)
        elif step_infos['请求方式'] == 'post':
            result = self.post(step_infos)
        else:
            result = {'code' : 3, 'result' : '请求方式不支持'}
        return result

RequestsUtils =  RequestsUtils()

if __name__ == '__main__':
    get_infos = {'请求参数': '', '测试用例名称': '获取token成功', '测试用例步骤': 1.0, '期望结果': '', '请求地址': 'cgi-bin/token', '取值代码': '', '取值方式': '','期望结果类型': '',
                 '用例执行': '是', '提交数据': '{"grant_type":"client_credential","appid":"wx7cc16178655bc79e","secret":"ed3e70fe8244e88ff52d3abc2101c31d"}',
                 '测试用例编号': 1.0, '接口名称': '获取token', '请求方式': 'get', '传值变量': ''}
    post_infos = {'测试用例步骤': 1.0, '取值代码': '', '期望结果': '', '测试用例编号': 3.0, '接口名称': '创建标签', '用例执行': '是', '请求方式': 'post', '取值方式': '',
     '请求参数': {'access_token' : '35_l9M2JSHWpvesFnedSoWNzHM_R7fvu8I-TdbRDg3hTXQZB2siUAcqq0AzkSZIbEFThlKMe1oET0zmcW89lWyYI_U9d4glXpSgwiCj2FCAcTHHrjkoxVhqbjiVWfGlrQrQjOisgeeJTlNyhVfSEGXhAFAUWN'},
    '测试用例名称': '创建标签成功', '期望结果类型': '', '提交数据': '{ "tag" : {"name" : "abc"} } ', '传值变量': '', '请求地址': 'cgi-bin/tags/create'}
    result = RequestsUtils.request(post_infos)       # 创建封装的请求对象
    try:
        print(result['response_json'])
    except KeyError:
        print({'code': 3, 'result': '请求方式不支持'})

