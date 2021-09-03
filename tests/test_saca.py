from main import conta1, conta2


def test_saca_certo():
    conta1.saca(200)
    
def test_saca_errado():
    conta2.saca(801)