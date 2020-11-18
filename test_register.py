"""
命名规则
1，测试文件一test_开头或结尾
2，测试类以Test开头
2，测试方法以test_开头
"""

import requests


def register(data):
    url = 'http://jy001:8081/futureloan/mvc/api/member/register'
    r = requests.post(url, data=data)
    return r


# 手机号码格式不正确
def test_register_001():
    data = {"mobilephone": "137123456789", "pwd": "123456abc", "regname": "aaa"}
    expect = {"status": 0, "code": "20109", "data": None, "msg": "手机号码格式不正确"}
    real = register(data)

    assert real.json()['msg'] == expect['msg']
    assert real.json()['code'] == expect['code']


def test_register_002():
    data = {"pwd": "123456abc", "regname": "aaa"}
    expect = {"status": 0, "code": "20103", "data": None, "msg": "手机号不能为空"}
    real = register(data)
    assert real.json()['msg'] == expect['msg']
    assert real.json()['code'] == expect['code']


def test_register_003():
    data = {"mobilephone": "13745241112", "pwd": "12345", "regname": "aaa"}
    expect = {"status": 0, "code": "20108", "data": None, "msg": "密码长度必须为6~18"}
    real = register(data)

    assert real.json()['msg'] == expect['msg']
    assert real.json()['code'] == expect['code']
