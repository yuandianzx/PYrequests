import requests

session = requests.session()
headers = {"Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
              "Accept-Encoding": "gzip,deflate",
              "User-Agent": "Mozilla/5.0(Windows NT 6.1;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 83.0.4103.116Safari / 537.36",
              "Accept": "text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8, application / signed - exchange;v = b3;q = 0.9"

              }
url1 = 'http://47.107.178.45/phpwind/'
a = session.get(url1, headers = headers)


def forum_register():
    url = 'http://47.107.178.45/phpwind/index.php'
    params = {
            'm' : 'u' ,
            'c' : 'register',
            'a' : 'dorun'
    }
    data = {
        'username' : 'test20200712',
        'password' : '123456',
        'repassword' : '123456',
        'email' : '123141432qq.com',
        'csrf_token':'2ab91b36e1b33513'

            }
    se = session.post(url, headers = headers, params = params,data = data)
    return se

if __name__ == '__main__':
    print(forum_register().text)
