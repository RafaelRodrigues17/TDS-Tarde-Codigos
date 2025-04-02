from empresa import Funcionario
import os

def main():
    funcionario = Funcionario()
    funcionario.criar_tabela()
    while True:
        print("\n")
        print("[1] Adicionar Funcionário")
        print("[2] Listar Funcionários")
        print("[3] Atualizar Salário")
        print("[4] Excluir Funcionário")
        print("[5] Alterar Cargo")
        print("[6] Alterar Departamento")
        print("[7] Alterar Nome")
        print("[8] Sair do Programa")
        opcao = int(input("Escolha uma opção: "))
        os.system("cls")
        
        match opcao:
            case 1:
                funcionario.adicionar_funcionario()
            case 2:
                funcionario.listar_funcionarios()
            case 3:
                funcionario.atualizar_salario()
            case 4:
                funcionario.excluir_funcionario()
            case 5: 
                funcionario.alterar_cargo()
            case 6:
                funcionario.alterar_departamento()
            case 7:
                funcionario.alterar_nome()
            case 8:
                print("Encerrando o programa! ")
                break
            case _:
                print("Opção Inválida! Tente novamente")
                
if __name__ == '__main__':
    main()