"""
fixture 作用域
默认是function级别的，有function，某电了，class,session级别
"""
import pytest


@pytest.fixture(scope='class')  # 每个类执行一次，在类中首次调用function是执行前置，雷利方法执行完执行后置
def login():
    print("登录系统")  # 前置
    yield
    print("退出登录")  # 后置


class TestQuery():
    def test_case1(self):
        print("测试查询1")

    def test_case2(self, login):  # 执行前置
        print("测试查询2")

    def test_case3(self):  # 执行完执行后置
        print("测试查询3")


class TestDelete:
    def test_case1(self, login):  # 执行前置
        print("测试删除1")

    def test_case2(self):
        print("测试删除2")

    def test_case3(self):
        print("测试删除3")
