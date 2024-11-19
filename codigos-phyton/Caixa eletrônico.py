class Banco:
    def __init__(self):
        self.nr_agencia = 1020
        self.nr_conta = 123
        self.nr_senha = 1234
        self.saldo = 0.0
        self.limite = 500.00
        self.total = 0.0
        self.operacao_credito = []
        self.operacao_debito = []

    def consulta_extrato(self):
        print("Extrato Bancario Completo:\n")
        print("Operacoes feitas com credito:")
        for valor in self.operacao_credito:
            print(f"Deposito: R$ {valor:.2f}")
        print("\nOperacoes de debito:")
        for valor in self.operacao_debito:
            print(f"Saque: R$ {valor:.2f}")
        print(f"\nSaldo final: R$ {self.saldo:.2f}")

    def consulta_saldo(self):
        print(f"Saldo:            R$ {self.saldo:.2f}")
        print(f"Limite:           R$ {self.limite:.2f}")
        print(f"Disponivel:       R$ {self.saldo + self.limite:.2f}")

    def realizar_deposito(self):
        num = float(input("Entre com o valor que gostaria de depositar: "))
        self.saldo += num
        self.operacao_credito.append(num)

    def realizar_saque(self):
        num = float(input("Digite o valor que gostaria de sacar: "))
        total = self.saldo + self.limite

        if total < num:
            print("Numero acima do valor total")
            return

        if num > self.saldo:
            if (self.saldo - num) < self.limite:
                self.limite += (self.saldo - num)
                self.saldo = 0
            else:
                self.saldo -= num
        else:
            self.saldo -= num

        self.operacao_debito.append(num)

    def chama_menu(self):
        while True:
            print("\nEscolha uma opcao:")
            print("1 - Saldo")
            print("2 - Extrato")
            print("3 - Saque")
            print("4 - Deposito")
            print("5 - Sair")
            opcao = int(input("Opcao: "))

            if opcao == 1:
                self.consulta_saldo()
            elif opcao == 2:
                self.consulta_extrato()
            elif opcao == 3:
                self.realizar_saque()
            elif opcao == 4:
                self.realizar_deposito()
            elif opcao == 5:
                print("\nPrograma encerrado pelo usuario")
                break
            else:
                print("Opcao invalida")

def main():
    banco = Banco()
    while True:
        agencia = int(input("Informe sua agencia: "))
        conta = int(input("Informe sua conta: "))
        senha = int(input("Informe sua senha: "))

        if banco.nr_agencia == agencia and banco.nr_conta == conta and banco.nr_senha == senha:
            print("Acesso liberado!\n")
            break
        else:
            print("Dados incorretos\n")

    banco.chama_menu()

if __name__ == "__main__":
    main()
