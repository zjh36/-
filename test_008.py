import mock
import requests



class JinRong:
    def quxian(self,data):
        r = requests.post("http://jy001:8081/futureloan/mvc/api/member/recharge", data=data).json()
        return r

class TestJinRong:
    def test_quxian(self):
        jinrong = JinRong()

        c = {"mobilephone":"15127345432","amount":"3000"}
        r = jinrong.quxian(c)
        assert r ['msg'] == "充值成功"
        assert r ['status'] == 1
        assert r ['code'] == '10001'

        # {'status':0,'code':'20102','data':None,'msg':'服务器异常'}
        jinrong.quxian = mock.Mock(return_value={'status':1,'code':'10001','data':None,'msg':'取现成功'})
        data = {"mobilephone":15127345432,"amount":50}
        r = jinrong.quxian(data)

        assert r['msg'] == "取现成功"
        assert r['code'] == "10001"
        assert r['status'] == 1