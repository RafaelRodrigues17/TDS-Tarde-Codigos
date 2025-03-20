# Criar uma classe que receba o nome o cargo e o salário
# Criar método para mostrar todas as informações

class Funcionario:
    #construtor
    def __init__(self, nome, cargo, salario):
        self.__nome = nome
        self.__cargo = cargo
        self.__salario = salario

    def exibir_informacoes(self):
        print(f"Funcionario: {self.__nome}")
        print(f"Cargo: {self.__cargo}")
        print(f"Salario: R$ {self.__salario: .2f}")
        print("\n")
    
    #método==> aplicar_aumento()
    def aplicar_aumento(self, porcentagem):
        self.__salario *= (1 + porcentagem/100)
    
    #método==> mudar_cargo() 
    @property
    def cargo(self):
        return self.__cargo
    
    @cargo.setter
    def cargo(self, novo_cargo):
        self.__cargo = novo_cargo