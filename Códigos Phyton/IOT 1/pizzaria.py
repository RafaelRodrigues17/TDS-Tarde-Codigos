# criar um sistema para pizzaria
# ==>titulo

# Menu:
# cadastrar pizza
# listar pizzas
# remover pizza
# sair

# Pizza: nome, ingredientes, status

# Pizzaria ==> Dom Rafael
import os

pizzas =[]

def titulo():
    print("""
▒█▀▀▄ █▀▀█ █▀▄▀█ 　 ▒█▀▀█ █▀▀█ █▀▀ █▀▀█ █▀▀ █░░ 　 ▒█▀▀█ ░▀░ ▀▀█ ▀▀█ █▀▀█ █▀▀█ ░▀░ █▀▀█ 
▒█░▒█ █░░█ █░▀░█ 　 ▒█▄▄▀ █▄▄█ █▀▀ █▄▄█ █▀▀ █░░ 　 ▒█▄▄█ ▀█▀ ▄▀░ ▄▀░ █▄▄█ █▄▄▀ ▀█▀ █▄▄█ 
▒█▄▄▀ ▀▀▀▀ ▀░░░▀ 　 ▒█░▒█ ▀░░▀ ▀░░ ▀░░▀ ▀▀▀ ▀▀▀ 　 ▒█░░░ ▀▀▀ ▀▀▀ ▀▀▀ ▀░░▀ ▀░▀▀ ▀▀▀ ▀░░▀
""")
    
def exibir_menu():
    # criar menu
    print("Bem-vindo a Pizzaria Dom Rafael !\n")
    print("1. Cadastrar Pizza")  
    print("2. Status das Pizzas")     
    print("3. Remover Pizza")  
    print("4. Sair")
    print("\n")
    
def voltar_menu():
    input("\nAperte ENTER para voltar ao menu principal: ")
    principal()
    
def status_pizzas():
    os.system("cls")
    print("\n")
    print("As Pizzas cadastradas são:\n ")
    for pizza in pizzas:
        print(pizza, "(A Pizza está pronta!)")
    voltar_menu()

def remover_pizzas():
    encontrou_pizza = False
    os.system("cls")
    print("As Pizzas cadastradas são")
    print("\n")
    for pizza in pizzas:
        print(pizza)
    print("\n")
    while True:
        remover = input("Qual Pizza gostaria de remover? ")
        for pizza in pizzas:
            if pizza == remover:
               pizzas.remove(pizza) 
               print("Pizza removida com sucesso! ")
               encontrou_pizza = True
        if encontrou_pizza == False:
            print("Pizza não cadastrada! ")
        resposta = input("Gostaria de remover outra Pizza? (s/n) ")
        if resposta.lower() == "n":
            break
        else:
            print("Pizza não existente! ")
    voltar_menu()
    
def adicionar_pizza():
    os.system("cls")
    while True:
        pizza = input("Digite o Sabor da Pizza: ")
        pizzas.append(pizza)
        print("Pizza salva com sucesso!")
        resposta = input("Gostaria de adicionar outra Pizza? (s/n) ")
        if resposta.lower() == "n":
            break
    voltar_menu()
    
def sair():
    os.system("cls")
    print("Pograma Encerrado! ")
        
def escolher_menu():
    escolha = int(input("Escolha uma das opções: "))    
    match escolha:
        case 1:
            # função cadastrar Pizza
            adicionar_pizza()
        case 2:
            # fução status da Pizza
            status_pizzas()
        case 3:
            # Remover Pizza
            remover_pizzas()
        case 4:
            # Sair
            sair()
        case _:
            print("Opção Inválida! Tente novamente ")
            voltar_menu()
    
def principal():
    os.system("cls")
    titulo()
    exibir_menu()
    escolher_menu()
    
# ponto de entrada    
if __name__ == "__main__":
    principal() 