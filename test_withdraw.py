import mock
import requests


class TiQu():
    def quxian(self, data):
        r = requests.post('http://jy001:8081/futureloan/mvc/api/member/withdraw', data=data).json()
        return r



    # 15256666536  15256663536 15256669536 15256665536

class Testquxian:
    def test_quxian(self):
        tiqu = TiQu()
        tiqu.quxian = mock.Mock(return_value={"code": 20119, "msg": "余额不足，请修改提现额度"})
        data = {"mobilephone": "15256667536", "amount": 10000000}
        r = tiqu.quxian(data)
        print(r)

    