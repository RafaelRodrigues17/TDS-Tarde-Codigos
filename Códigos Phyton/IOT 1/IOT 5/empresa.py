import mysql.connector

class Funcionario:
    
    def conectar(self):
        return mysql.connector.connect(
            host = 'paparella.com.br',
            user = 'paparell_aluno_4',
            password = '@Senai2025',
            database = 'paparell_python'
        )
        
    def criar_tabela(self):
        conexao = self.conectar()
        cursor = conexao.cursor()
        query = (""" 
                 create table if not exists funcionarios(
                     id int auto_increment primary key,
                     nome varchar(255) not null,
                     idade int not null,
                     cargo varchar(255) not null,
                     departamento varchar(255) not null,
                     salario decimal(10,2)) 
                 """)
        
        cursor.execute(query)
        conexao.commit()
        cursor.close()
        conexao.close()
    
    def adicionar_funcionario(self):
        salario = 0
        conexao = self.conectar()
        cursor = conexao.cursor()
        nome = input("Digite o nome do funcionário: ")
        idade = int(input("Digite a idade: "))
        cargo = input("Digite o cargo: ")
        departamento = input("Digite o departamento: ")
        while True:
            salario = float(input("Digite o Salario:"))
            if salario > 0:
                break
            else:
                print("Valor Inválido! Tente novamente")
        cursor.execute("insert into funcionarios(nome,idade,cargo,departamento,salario) values(%s,%s,%s,%s,%s)",(nome,idade,cargo,departamento,salario))
        conexao.commit()
        cursor.close()
        conexao.close()
        print("Funcionário cadastrado com sucesso! ")
        
    def listar_funcionarios(self):
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute("select * from funcionarios")
        funcionarios = cursor.fetchall()
        if not funcionarios:
            print("Funcionários não encontrados! ")
        else:
            for f in funcionarios:
                print(f"ID: {f[0]} | Nome: {f[1]} | Idade: {f[2]} | Cargo: {f[3]} | Departamento: {f[4]} | Salario: R${f[5]} ")
        conexao.commit()
        cursor.close()
        conexao.close()
    
    def atualizar_salario(self):
        self.listar_funcionarios()
        conexao = self.conectar()
        cursor = conexao.cursor()
        funcionario_id = int(input("Digite o ID do funcionário para atualizar o Salário: "))
        while True:
            novo_salario = float(input("Digite o Salario:"))
            if novo_salario > 0:
                break
            else:
               print("Valor Inválido! Tente novamente")
        cursor.execute("update funcionarios set salario =%s where id =%s",(novo_salario,funcionario_id))
        conexao.commit()
        cursor.close()
        conexao.close()
        print("Salário do funcionário atualizado com sucesso! ")
        
    def excluir_funcionario(self):
        self.listar_funcionarios()
        conexao = self.conectar()
        cursor = conexao.cursor()
        funcionario_id = int(input("Digite o ID do funcionário para exclui-lo: "))
        cursor.execute("delete from funcionarios where id=%s",[funcionario_id])
        conexao.commit()
        cursor.close()
        conexao.close()
        print("Funcionário deletado com sucesso!")
        
    def alterar_cargo(self):
        self.listar_funcionarios()
        conexao = self.conectar()
        cursor = conexao.cursor()
        funcionario_id = int(input("Digite o ID do funcionário para alterar cargo: "))
        novo_cargo = input("Digite o novo Cargo: ")
        cursor.execute("update funcionarios set cargo =%s where id =%s",(novo_cargo,funcionario_id))
        conexao.commit()
        cursor.close()
        conexao.close()
        print("Cargo atualizado com sucesso!")
        
    def alterar_departamento(self):
        self.listar_funcionarios()
        conexao = self.conectar()
        cursor = conexao.cursor()
        funcionario_id = int(input("Digite o ID do funcionário para alterar o departamento: "))
        novo_departamento = input("Digite o novo departamento: ")
        cursor.execute("update funcionarios set departamento =%s where id =%s",(novo_departamento,funcionario_id))
        conexao.commit()
        cursor.close()
        conexao.close()
        print("Departamento atualizado com sucesso!")
    
    def alterar_nome(self):
        self.listar_funcionarios()
        conexao = self.conectar()
        cursor = conexao.cursor()
        funcionario_id = int(input("Digite o ID do funcionário para alterar o nome: "))
        novo_nome = input("Digite o novo nome: ")
        cursor.execute("update funcionarios set nome =%s where id =%s",(novo_nome,funcionario_id))
        conexao.commit()
        cursor.close()
        conexao.close()
        print("Nome atualizado com sucesso!")
        
        
        
        
        