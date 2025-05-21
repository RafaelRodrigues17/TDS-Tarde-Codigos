import sqlite3

def titulo():
    print("""
▒█▀▀▄ █▀▀█ █▀▄▀█ 　 ▒█▀▀█ █▀▀█ █▀▀ █▀▀█ █▀▀ █░░ 　 ▒█▀▀█ ░▀░ ▀▀█ ▀▀█ █▀▀█ █▀▀█ ░▀░ █▀▀█ 
▒█░▒█ █░░█ █░▀░█ 　 ▒█▄▄▀ █▄▄█ █▀▀ █▄▄█ █▀▀ █░░ 　 ▒█▄▄█ ▀█▀ ▄▀░ ▄▀░ █▄▄█ █▄▄▀ ▀█▀ █▄▄█ 
▒█▄▄▀ ▀▀▀▀ ▀░░░▀ 　 ▒█░▒█ ▀░░▀ ▀░░ ▀░░▀ ▀▀▀ ▀▀▀ 　 ▒█░░░ ▀▀▀ ▀▀▀ ▀▀▀ ▀░░▀ ▀░▀▀ ▀▀▀ ▀░░▀
""")
    
    
def exibir_menu():
    print("Bem-Vindo ao cinema escolha uma das opções:")
    print("1 - Adicionar filme")
    print("2 - Editar o nome do filme")
    print("3 - Excluir filme")
    print("4 - Mostrar filmes")

def criar_tabelas():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS filmes
                   (id INTEGER PRIMARY KEY, titulo TEXT, diretor TEXT, ano INTEGER)''')

    conexao.commit()

def adicionar_filme():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    id = input("Digite um id para o filme:")
    titulo = input("Digite o nome do filme:")
    diretor = input("Digite o diretor do filme:")
    ano = input("Digite o ano do filme:")

    cursor.execute('''INSERT INTO filmes(id, titulo, diretor, ano)
                   VALUES (?, ?, ?, ?)''',(id, titulo, diretor, ano))

    conexao.commit()
    voltar_menu()

def editar_filme():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    id = input("Digite o id do filme para editar:")
    cursor.execute('''SELECT id FROM filmes''')
    titulo = input("Digite o novo nome:")
    cursor.execute('''UPDATE filmes SET titulo=? WHERE id=? ''',(titulo,id))

    conexao.commit()
    voltar_menu()

def voltar_menu():
    input("\nAperte ENTER para voltar ao menu principal: ")
    principal()

def ver_filmes():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute('''SELECT * FROM filmes''')
    lista_de_filmes = cursor.fetchall()
    print(lista_de_filmes)
    voltar_menu()

def excluir_filme():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    id = input("Digite o id do filme para excluir:")
    cursor.execute('''SELECT id FROM filmes''')
    cursor.execute('''DELETE FROM filmes WHERE id=? ''',(id))

    conexao.commit()
    voltar_menu()

def escolher_menu():
    escolha = int(input("Escolha uma das opções: "))
    match escolha:
        case 1:
            adicionar_filme()
        case 2:
            editar_filme()
        case 3:
            excluir_filme()
        case 4: 
            ver_filmes()
        case _:
            print("Opção Inválida! Tente novamente ")
            voltar_menu()

def principal():
    exibir_menu()
    escolher_menu()

def conectar_banco():
    conexao = sqlite3.connect("filmes.db")
    return conexao

if __name__ == '__main__':
    criar_tabelas()
    exibir_menu()
    escolher_menu()