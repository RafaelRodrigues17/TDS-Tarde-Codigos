# Criar  Classe
# Conjunto de Metodos(Funções) e atributos (variáveis)

class Pessoa:
    #construtor
    def __init__(self, nome, idade, cidade):
        self.__nome = nome
        self.__idade = idade
        self.__cidade = cidade

    # #getter
    # def get_nome(self):
    #     return self.__nome
    @property
    def nome(self):
        return self.__nome
        
    # #setter
    # def set_nome(self, novo_nome):
    #     self.__nome = novo_nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    # #getter
    # def get_idade(self):
    #     return self.__idade
        
    @property
    def idade(self):
        return self.__idade

    # #setter
    # def set_idade(self, valor):
    #     self.__idade += valor

    @idade.setter
    def idade(self, valor):
        self.__idade += valor

    def apresentar(self):
        print(f"O Meu nome é {self.nome}")
        print(f"Moro em {self.__cidade}")
        print(f"Tenho {self.idade} anos!")

