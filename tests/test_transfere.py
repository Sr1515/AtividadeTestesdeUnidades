from main import conta1, conta2


def test_transfere_certo():
    conta1.transfere(conta1, 200)
    
def test_transfere_errado():
    conta2.transfere('conta3', 100)