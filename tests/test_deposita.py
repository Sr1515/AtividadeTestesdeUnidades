from main import conta1, conta2


def test_deposita_certo():
    conta1.deposita(700)

def test_deposita_errado():
    conta2.deposita(400)