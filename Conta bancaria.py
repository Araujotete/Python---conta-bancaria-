class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0.0
        self.historico = []
        self.taxa_saque = 2.0  # Taxa de saque

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.append(f'Depósito: R$ {valor:.2f}')
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso!')
        else:
            print('Valor de depósito deve ser positivo.')

    def sacar(self, valor):
        if valor > 0:
            if valor + self.taxa_saque <= self.saldo:
                self.saldo -= (valor + self.taxa_saque)
                self.historico.append(f'Saque: R$ {valor:.2f} (Taxa: R$ {self.taxa_saque:.2f})')
                print(f'Saque de R$ {valor:.2f} realizado com sucesso! Taxa de R$ {self.taxa_saque:.2f} aplicada.')
            else:
                print('Saldo insuficiente para realizar o saque.')
        else:
            print('Valor de saque deve ser positivo.')

    def extrato(self):
        print(f'\nExtrato da conta de {self.titular}:')
        for operacao in self.historico:
            print(operacao)
        print(f'Saldo atual: R$ {self.saldo:.2f}')

def main():
    print("Bem-vindo!")
    nome = input("Digite o nome do titular da conta: ")
    conta = ContaBancaria(nome)

    while True:
        print("\nEscolha uma operação:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Sair")
        
        opcao = input("Digite o número da operação desejada: ")

        if opcao == '1':
            valor = float(input("Digite o valor a ser depositado: "))
            conta.depositar(valor)
        elif opcao == '2':
            valor = float(input("Digite o valor a ser sacado: "))
            conta.sacar(valor)
        elif opcao == '3':
            conta.extrato()
        elif opcao == '4':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()