import requests
from API_TEST_FRAME_ZX.common.config_utils import configUtils

session = requests.session()    # 创建session() 对象
headers = {'Content-Type': 'application/json;charset=UTF-8'}

def get_access_token_api(grant_type, appid, secret):
    url = configUtils.read_config('host','wechat_host') + 'cgi-bin/token'
    params = {'grant_type' : grant_type,    # client_credential
            'appid' : appid,     # wx7cc16178655bc79e
            'secret': secret}     # ed3e70fe8244e88ff52d3abc2101c31d
    response = session.get(url, headers = headers, params = params)
    return response
'''
def get_access_token(grant_type, appid, secret):
    access_token = get_access_token_api(grant_type, appid, secret).json()['access_token']       # 需要转换成json串才能截取token
    return access_token
'''

def add_tag_api(access_token, tag):         # 创建标签
    url = configUtils.read_config('host','wechat_host') + 'cgi-bin/tags/create'
    params = {'access_token': access_token}
    data ={'tag' : tag}      # {'id':134, 'name':'广东'}
    response = session.post(url, headers = headers, params = params, json = data)
    return response

def edit_tag_api(access_token, tag):        # 编辑标签
    url = configUtils.read_config('host', 'wechat_host') + 'cgi-bin/tags/update'
    params = {'access_token': access_token}
    data = {'tag': tag}
    response = session.post(url, headers = headers, params = params, json = data)
    return response

def delete_tag_api(access_token, tag):      # 删除标签
    url = configUtils.read_config('host', 'wechat_host') + 'cgi-bin/tags/delete'
    params = {'access_token': access_token}
    data = {'tag': tag}
    response = session.post(url, headers = headers, params = params, json = data)
    return response

def set_use_remark_api(access_token, appid, remark):      # 设置用户备注名
    url = configUtils.read_config('host', 'wechat_host') + 'cgi-bin/user/info/updateremark'
    params = {'access_token': access_token}
    data = {'openid':appid,
	        'remark':remark}
    response = session.post(url, headers=headers, params=params, json=data)
    return response

if __name__ == '__main__':
    access_token_response = get_access_token_api('client_credential', 'wx7cc16178655bc79e', 'ed3e70fe8244e88ff52d3abc2101c31d')
    access_token = access_token_response.json()['access_token']
    print(access_token)
    create_tag_response = add_tag_api(access_token, {'id':138, 'name':'广东4'})
    print(create_tag_response.json())
    # print(add_tag_response.text)
    # access_token = get_access_token('client_credential', 'wx7cc16178655bc79e', 'ed3e70fe8244e88ff52d3abc2101c31d')
    # print(access_token)
