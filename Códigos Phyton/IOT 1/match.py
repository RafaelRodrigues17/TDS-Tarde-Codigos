# match/ ease
import os

os.system("cls")

while True:
    opcao = input("\nDigite um número de 1 a 4: ")
    
    match opcao:
        case "1":
            num = int(input("Digite um número: "))
            print(f"O número {num} é {'par' if num % 2 == 0 else 'ímpar'}.")
        case "2":
            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o segundo número: "))
            if num1 > num2:
                print(f"O maior número é {num1}.")
            elif num2 > num1:
                print(f"O maior número é {num2}.")
            else:
                print("Os números são iguais.")
        case "3":
            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o segundo número: "))
            num3 = int(input("Digite o terceiro número: "))
            print(f"A soma dos números é {num1 + num2 + num3}.")
        case "4":
            print("Saindo do programa...")
            break
        case _:
            print("Opção inválida! ")
