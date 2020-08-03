import re
import ast


class Check():
    def __init__(self, response):
        self.response = response
        # self.response_dict = ast.literal_eval(self.response)
        # if isinstance(self.response, str):
        #     self.response_dict = ast.literal_eval(self.response)    #
        # else:
        #     print("response响应请传入str类型")
        try:
            self.response_dict = ast.literal_eval(self.response)    # 进行正则匹配的时候，response响应必须为str，而dict转str的时候会有坑。所以我们在传入response的时候对其做是否为str的校验
        except:
            print("response响应请传入str类型")

        self.pass_result = {
            'code': 0,
            'response_reason': self.response_dict.reason,
            'response_code': self.response_dict.status_code,
            'response_headers': self.response_dict.headers,
            'response_body': self.response_dict.text,
            'check_result': True,
            'message': ''  # 扩招作为日志输出等
        }

        self.fail_result = {
            'code': 2,
            'response_reason': self.response_dict.reason,
            'response_code': self.response_dict.status_code,
            'response_headers': self.response_dict.headers,
            'response_body': self.response_dict.text,
            'check_result': False,
            'message': ''  # 扩招作为日志输出等
        }

    def no_check(self):
        pass

    def check_key(self, ckeckkey = None):
        """检查json键是否存在"""
        ckeckkey_list = ckeckkey.split(',')  # 将ckeck_key字符串分割后放入列表
        # print(key_list)
        result_list = []       # 将断言结果附加至列表中
        worrykey_list = []      # 将断言错误结果key附加至列表中
        for k in ckeckkey_list:     # 遍历ckeckkey_list，看检查的key是否存在响应中
            if k in self.response_dict.keys():
                result_list.append(True)
            else:
                result_list.append(False)
                worrykey_list.append(k)
        if True in result_list:
            return self.pass_result
        else:
            return self.fail_result

        print('"json键是否存在"断言结果列表：' , result_list)
        print('"json键是否存在"断言错误结果key列表：', worrykey_list)

    def check_key_value(self, ckeck_keyvalue = None):
        """json键值对匹配"""
        ckeck_keyvalue_dict = ast.literal_eval(ckeck_keyvalue)
        result_list = []  # 将断言结果附加至列表中
        worry_keyvalue_list = []  # 将断言错误结果key附加至列表中
        for kv in ckeck_keyvalue_dict.items():
            if kv in self.response_dict.items():
                result_list.append(True)
            else:
                result_list.append(False)
                worry_keyvalue_list.append(kv)

        print('"json键值对匹配"断言结果列表：', result_list)
        print('"json键值对匹配"断言错误结果keyvalue列表：', worry_keyvalue_list)

    def check_regexp(self, checkregexp = None):
        """正则匹配"""
        pattern = re.compile(checkregexp)   # 将正则表达式编译成pattern对象
        result = re.findall(pattern,self.response)      # 断言结果
        if not result:
            return '正则断言结果错误:',False
        else:
            return True


# Check = Check(response)     # 创建断言类对象


if __name__ == '__main__':
    response = '{"access_token":"35_BKh82IAvv_7Obcdwyre-v60qGrcS5rrWo-XN24oxrKZ4X","expires_in":7200}'
    ckeck_keyvalue = '{"expires_in":7200, "access_token":"(.+?)"}'
    checkregexp = '"access_token":"(.+?)"'
    ckeck_key = 'expires_in,access_token'

    Check = Check(response)
    Check.check_key_value(ckeck_keyvalue)
    print('-' * 60)
    check_regexp_result = Check.check_regexp(checkregexp)
    print(check_regexp_result)
    # print(str(response))
