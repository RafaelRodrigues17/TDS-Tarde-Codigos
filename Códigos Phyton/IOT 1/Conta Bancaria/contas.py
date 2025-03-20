class contaBancaria:

    def __init__(self, nome):
        self.__nome = nome
        self.__saldo = 0
    
    def ver_saldo(self):
        print(f"{self.__nome}, seu saldo é: R$ {self.__saldo:.2f}")
        print("\n")

    def depositar(self, valor):
        if valor >= 0:
           self.__saldo += valor
           print("Deposito efetuado com sucesso!")
        else:
            print("O valor não pode ser negativo!")

    def sacar(self, valor):
        if valor <= self.__saldo:
            if valor >= 0:
              self.__saldo -= valor
              print("Saque efetuado com sucesso!")
            else:
                print("O valor não pode ser negativo!")
        else:
            print("Saldo insuficiente para saque")
 

       