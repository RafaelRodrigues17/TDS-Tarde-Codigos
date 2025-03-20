from contas import contaBancaria

def mostrar_menu():
    print("1. Criar conta Bancaria")
    print("2. Ver saldo")
    print("3. Fazer deposito")
    print("4. Fazer Saque")
    print("5. Sair")

def criar_conta():
    nome = input("Digite o seu nome: ")
    c1 = contaBancaria(nome)
    print("Conta aberta comn sucesso!")

def escolher_opcao():
    opcao = int(input("Digite uma opção: "))
    match opcao:
        case 1:
            criar_conta()
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case _:
            pass  

def main():
    mostrar_menu()
    escolher_opcao()

    # c1 = contaBancaria("Rafael")
    # c1.ver_saldo()
    # valor = int(input("Digite o valor para depositar: "))
    # c1.depositar(valor)
    # c1.ver_saldo()
    # saque = int(input("Digite o valor a sacar: "))
    # c1.sacar(saque)
    # c1.ver_saldo()

if __name__ == "__main__":
    main()
