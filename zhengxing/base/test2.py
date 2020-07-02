import requests
# url = "http://webapi.test.sxmaps.com/authentication/api/notcheck/signin"
# headers = {"Content-Type": "application/json;charset=UTF-8"}
# data = {"password":"suGdkm/JtEPchfKm3VvmfQ==","code":"","phone":"zhengxin"}
# re = requests.post(url, headers = headers, json = data)
# print(re.json())
# print(re.cookies)

# url = "http://www.baidu.com"
# re = requests.get(url)
# print(re.cookies)
#
# print(re.cookies['BDORZ'])

url = "https://www.baidu.com/"
session = requests.Session()
print(session.get(url).cookies)