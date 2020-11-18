"""
fixture 可以代参数和返回值

"""

# 测试前置：准备测试数据，在v测试用例中使用测试数据，测试数据使用fixture的返回值来表示
import pytest


@pytest.fixture()
def username_pwd():
    return {"username": "root", "pwd": 123456}  # 可以返回任意类型的数值


def test_login(username_pwd):
    print(f"测试数据为：{username_pwd['username']}")


# 相同的测试用例。知识每次输入值不同
@pytest.fixture(params=['root', 'admin', 'administrator', '12345'])  # 多组用户名
def data(request):
    return request.param  # request.param是固定写法，取到每一组数据


@pytest.fixture(params=[
    {"casedata": "root", "except": "成功"},
    {"casedata": 'admin', "except": "成功"}])
def data1(request):
    return request.param


def test_login2(data):
    print(f"使用用户名{data}测试登录功能")


def test_login3(data1):
    print(f"使用用户名{data1['casedata']}测试登录功能,预期结果为{data1['except']}")
