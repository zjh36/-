"""
1，接口测试场景比较难模拟，需要大量的工作才能完成
2，依赖第三方接口，但第三方的接口没有开发完成
测试环境卜崇芬情况下，怎么去做接口测试？使用Mock来模拟
"""
import mock
import requests


class Alipay:
    def zhifu(self, data):
        # 接口功能尚未开发完成
        # 接口地址、get/post，入参，返回值已经定义好，有对应的接口文档
        # 接口参数  {"OrderId":"231214214211","Amount":128.5,"type":"支付宝"}
        # 接口返回值 {"code": 200, "msg": "支付成功"}) {"code": 201, "msg": "支付失败"} {"code": 202, "msg": "支付超时"})
        r = requests.post("http://zhifubao.com/pay", data=data).json()
        return r


class TestMOck:
    def test_alipay(self):
        # 对要模拟的类创建一个对象
        alipay = Alipay()
        # 模拟zhifu的返回值为{"code": 200, "msg": "支付成功"}
        alipay.zhifu = mock.Mock(return_value={"code": 200, "msg": "支付成功"})
        # 调用支付接口
        data = {"OrderId": "231214214211", "Amount": 128.5, "type": "支付宝"}
        r = alipay.zhifu(data)
        print(r)




