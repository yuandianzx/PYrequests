import ast

response = '{"access_token":"35_BKh82IAvv_7Obcdwyre","expires_in":7200}'
str2 = '{"expires_in":7200, "access_token":"(.+?)"}'
ckeck_key = 'expires_in,access_token'

response_json = ast.literal_eval(response)
ckeck_key_list = ckeck_key.split(',')  # 将ckeck_key字符串分割后放入列表
# print(key_list)
for k in ckeck_key_list:
    if k in response_json.keys():
        result = True
    else:
        result = False
    print('key值%s是否存在：' % k, result)



