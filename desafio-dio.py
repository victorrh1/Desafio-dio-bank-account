class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def cliente_deposito(self, valor):
        self.saldo += valor

    def cliente_saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print('Saldo insuficiente')

    def ObterSaldo(self):
        return self.saldo


titular = input('Digite o nome do titular da conta: ')
saldo_inicial = float(input('Digite o saldo inicial da conta: '))

contabancaria = ContaBancaria(titular, saldo_inicial)

valor_deposito = float(input('Digite o valor a depositar: '))
contabancaria.cliente_deposito(valor_deposito)

valor_saque = float(input('Digite o valor a sacar: '))
contabancaria.cliente_saque(valor_saque)

saldo_disponivel = contabancaria.ObterSaldo()
print('Saldo disponível:', saldo_disponivel)
