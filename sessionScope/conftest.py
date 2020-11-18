"""
conftest.py session级别的fixture放到这个文件中，文件名不能写错

第一次调用这个fixture执行前置。目录下所有文件执行完，在执行后置
conftest.py 文件有作用域，对同级及子目录生效
一个工程中可以用多个conftest.py文件
"""
import pytest


@pytest.fixture(scope='session')
def login():
    print("登录系统")
    yield
    print("退出登录")