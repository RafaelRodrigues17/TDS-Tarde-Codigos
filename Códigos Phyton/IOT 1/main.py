# Bolo de Maça ==> TORTA DI MELE
import os

ingredientes =[]

def titulo():
    print("""
╱╭╮╱╱╱╱╱╭╮╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╭╮
╭╯╰╮╱╱╱╭╯╰╮╱╱╱╱╱┃┃╱╱╱╱╱╱╱┃┃
╰╮╭╋━━┳┻╮╭╋━━╮╭━╯┣╮╭╮╭┳━━┫┃╭━━╮
╱┃┃┃╭╮┃╭┫┃┃╭╮┃┃╭╮┣┫┃╰╯┃┃━┫┃┃┃━┫
╱┃╰┫╰╯┃┃┃╰┫╭╮┃┃╰╯┃┃┃┃┃┃┃━┫╰┫┃━┫
╱╰━┻━━┻╯╰━┻╯╰╯╰━━┻╯╰┻┻┻━━┻━┻━━╯""")
    
def exibir_menu():
    # criar menu
    print("\n")
    print("1. Adicionar ingredintes")  
    print("2. Exibir ingredientes")     
    print("3. Remover ingrediente")  
    print("4. Sair")
    print("\n")
    
def voltar_menu():
    input("\nAperte ENTER para volatar ao menu principal: ")
    principal()
    
def exibir_ingredientes():
    os.system("cls")
    print("\n")
    print("Os Ingredientes são: ")
    print("\n")
    for ingrediente in ingredientes:
        print(ingrediente)
    voltar_menu()

def remover_ingredientes():
    encontrou_ingrediente = False
    os.system("cls")
    print("Os ingredientes cadastrados são")
    print("\n")
    for ingrediente in ingredientes:
        print(ingrediente)
    print("\n")
    while True:
        remover = input("Qual ingrediente gostaria de remover? ")
        for ingrediente in ingredientes:
            if ingrediente == remover:
               ingredientes.remove(ingrediente) 
               print("Ingrediente removido com sucesso! ")
               encontrou_ingrediente = True
        if encontrou_ingrediente == False:
            print("ingredinte não presente na receita")
        resposta = input("Gostaria de remover outro ingrediente? (s/n) ")
        if resposta.lower() == "n":
            break
        else:
            print("Ingrediente não presente na receita! ")
    voltar_menu()
    
def adicionar_ingrediente():
    os.system("cls")
    while True:
        ingrediente = input("Digite o ingrediente: ")
        ingredientes.append(ingrediente)
        print("Ingrediente salvo com sucesso!")
        resposta = input("Gostaria de adicionar outro ingrediente? (s/n) ")
        if resposta.lower() == "n":
            break
    voltar_menu()
    
def sair():
    os.system("cls")
    print("Pograma Encerrado! ")
        
def escolher_menu():
    escolha = int(input("Escolha uma opção: "))    
    match escolha:
        case 1:
            # função adicionar ingredientes
            adicionar_ingrediente()
        case 2:
            # fução exibir ingredientes
            exibir_ingredientes()
        case 3:
            # Remover ingrediente
            remover_ingredientes()
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