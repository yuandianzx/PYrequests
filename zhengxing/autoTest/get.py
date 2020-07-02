# coding:utf-8
import requests
import json
# p = {"keywords":"yoyoketang"}
# a = requests.get("http://www.cnblogs.com/yoyoketang/",params=p)
# print(a.status_code)
# print(a.text)
url_signin = "http://webapi.test.sxmaps.com/auth/api/notcheck/signin"
url_myFlow = "http://webapi.test.sxmaps.com/hermes/ftmsFlow/myFlow"
headers = {"Content-Type": "application/json;charset=UTF-8"}                    # 定义请求数据类型
p_signin = {"password":"Admin123","phone":"18274852609","extNumber":""}         # 请求参数赋值
p_myFlow = {"createDateStart":"2019-07-29 00:00:00","createDateEnd":"2019-07-29 23:59:59","pageNum":1,"pageSize":20,"timeType":"appraise","flowFrom":0}
# print(type(p_myFlow))
# data_json = json.dumps(p_signin)  # 将参数转化为json格式

signin = requests.post(url_signin,headers=headers,json=p_signin).json()                           # 将post请求和结果赋值给b
print(json.dumps(signin,indent=2,sort_keys=True))
# token = signin.json()['data']['token']
# print(token)
# print(signin.status_code)
# print(json.dumps(signin.json(),indent=2))                   # 如果返回的响应内容是gzip压缩的，可用content方法。与text方法相比可自动解码gzip 和deflate。
#                                                             # 使用json.dumps(signin.json(),indent=2)将响应的数据格式化
# print(".................................................\n")

# headers["token"] = token
# myFlow = requests.post(url_myFlow,headers=headers,json=p_myFlow)
# print(myFlow.json())

