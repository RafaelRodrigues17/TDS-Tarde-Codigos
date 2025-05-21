import sqlite3

def titulo():
    print("""
  _     _                      _             _         ____        __       
 | |   (_)_   ___ __ __ _ _ __(_) __ _    __| | ___   |  _ \ __ _ / _| __ _ 
 | |   | \ \ / / '__/ _` | '__| |/ _` |  / _` |/ _ \  | |_) / _` | |_ / _` |
 | |___| |\ V /| | | (_| | |  | | (_| | | (_| | (_) | |  _ < (_| |  _| (_| |
 |_____|_| \_/ |_|  \__,_|_|  |_|\__,_|  \__,_|\___/  |_| \_\__,_|_|  \__,_|

""")
    

def exibir_menu():
    print("Bem-Vindo a Livraria! Escolha uma das opções:")
    print("1 - Emprestrar um livro")
    print("2 - Devolver um livro")
    print("3 - Mostrar livros emprestados")

def criar_tabelas():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS livros
                   (id INTEGER PRIMARY KEY, titulo TEXT, autor TEXT, ano INTEGER)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS alunos
                   (id INTEGER PRIMARY KEY, nome TEXT)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS emprestimos
                   (id INTEGER PRIMARY KEY, data_emprestimo TEXT, data_devolucao)''')
    
    conexao.commit()

def adicionar_livro():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    id = input("Digite um id para o livro:")
    titulo = input("Digite o nome do livro:")
    autor = input("Digite o autor do livro:")
    ano = input("Digite o ano do livro:")

    cursor.execute('''INSERT INTO livros(id, titulo, autor, ano)
                   VALUES (?, ?, ?, ?)''',(id, titulo, autor, ano))

    conexao.commit()
    voltar_menu()

def voltar_menu():
    input("\nAperte ENTER para voltar ao menu principal: ")
    principal()

def ver_livros():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute('''SELECT * FROM livros''')
    lista_de_livros = cursor.fetchall()
    print(lista_de_livros)
    voltar_menu()

def devolver_livro():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    id = input("Digite o id do livro para excluir:")
    cursor.execute('''SELECT id FROM livros''')
    cursor.execute('''DELETE FROM livros WHERE id=? ''',(id))

    conexao.commit()
    voltar_menu()

def escolher_menu():
    escolha = int(input("Escolha uma das opções: "))
    match escolha:
        case 1:
            adicionar_livro()
        case 2:
            devolver_livro()
        case 3: 
            ver_livros()
        case _:
            print("Opção Inválida! Tente novamente ")
            voltar_menu()

def principal():
    exibir_menu()
    escolher_menu()

def conectar_banco():
    conexao = sqlite3.connect("livros.db")
    return conexao

if __name__ == '__main__':
    criar_tabelas()
    exibir_menu()
    escolher_menu()