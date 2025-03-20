from contas import contaBancaria

def main():
    c1 = contaBancaria("Rafael")
    c1.ver_saldo()
    valor = int(input("Digite o valor para depositar: "))
    c1.depositar(valor)
    c1.ver_saldo()
    saque = int(input("Digite o valor a sacar: "))
    c1.sacar(saque)
    c1.ver_saldo()

if __name__ == "__main__":
    main()
