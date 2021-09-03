import os
from time import sleep
from subprocess import call
from platform import system


class LimitExceededError(Exception):
    pass


class NotEnoughMoneyError(Exception):
    pass


class NotAnAccountError(Exception):
    pass


class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def deposita(self, valor):

        if not isinstance(valor, (int, float)):
            raise ValueError

        if valor > self.limite:
            raise LimitExceededError

        try:
            self.saldo += valor
        except LimitExceededError:
            print(
                f'Limite excedido, sua conta só permite movimentações até R${self.limite:.2f}.')
        except ValueError:
            print('Valor inválido.')
        else:
            print('Depósito de R${valor:.2f} realizado.')
            self.extrato()

    def saca(self, valor):

        if not isinstance(valor, (int, float)):
            raise ValueError

        if valor > self.limite:
            raise LimitExceededError

        if self.saldo <= 0 or valor > self.saldo:
            raise NotEnoughMoneyError

        try:
            self.saldo -= valor
        except LimitExceededError:
            print(
                f'Limite excedido, sua conta só permite movimentações até R${self.limite:.2f}.')
        except NotEnoughMoneyError:
            print('Saldo insuficiente.')
        except ValueError:
            print('Valor inválido.')
        else:
            print('Saque de R${valor:.2f} realizado.')
            self.extrato()

    def transfere(self, conta_destino, valor):

        if not isinstance(conta_destino, Conta):
            raise NotAnAccountError

        if not isinstance(valor, (int, float)):
            raise ValueError

        if valor > self.limite:
            raise LimitExceededError

        if self.saldo <= 0 or valor > self.saldo:
            raise NotEnoughMoneyError

        try:
            conta_destino.saldo += valor
            self.saldo -= valor
        except NotAnAccountError:
            print(
                'Ops, parece que você tentou realizar uma movimentação com uma conta inválida.')
        except LimitExceededError:
            print(
                f'Limite excedido, sua conta só permite movimentações até R${self.limite:.2f}.')
        except NotEnoughMoneyError:
            print('Saldo insuficiente.')
        except ValueError:
            print('Valor inválido.')
        else:
            print('Saque de R${valor:.2f} realizado.')
            self.extrato()

    def extrato(self):
        print(f'R${self.saldo:.2f}')


# instanciando contas para os testes:

conta1 = Conta('0000', 'João Victor', 800, 200)
conta2 = Conta('1111', 'Joseraldo', 200, 800)

if __name__ == '__main__':

    sistema = system()
    pip_command = ['pip', 'install', '-r', 'requirements.txt']
    venv_env = []
    env_command = []

    if sistema == 'Windows':
        env_path = ['env\\Scripts\\python', '-m']
        env_command = ['python', '-m', 'venv', 'env']

    elif sistema == 'Linux':
        env_path = ['env/bin/python', '-m']
        env_command = ['python3', '-m', 'venv', 'env']

    if not os.path.exists('env'):
        print(
            "\n\n-=-=-=- POR FAVOR AGUARDE CRIAÇÃO E CONFIGURAÇÃO DO AMBIENTE VIRTUAL -=-=-=-\n")
        print('OBS: Isso pode demorar um pouco dependendo das configurações do seu computador.\n\n')
        call(env_command)
        call(env_path + pip_command)
        sleep(1)

    print('\n\n-=-=-=- INICIALIZANDO OS TESTES, FAVOR AGUARDE -=-=-=-\n\n')
    sleep(2)
    call(env_path + ['pytest'])
