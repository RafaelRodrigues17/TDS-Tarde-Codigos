class Carta: #Super Classe Carta
    def __init__(self, nome, energia_gasta, descricao):
        self.nome = nome
        self.energia_gasta = energia_gasta
        self.descricao = descricao
    
    def usar_carta():
        pass
    
# Subclasses que pertencem a Classe Carta
class CartaAumento (Carta):
    def __init__(self, nome, energia_gasta, descricao, tipo, pontos_aumentados):
        super().__init__(nome, energia_gasta, descricao)
        self.tipo = tipo
        self.pontos_aumentados = pontos_aumentados
        
    def usar_carta():
        pass

class CartaRoubo (Carta):
    def __init__(self, nome, energia_gasta, descricao):
        super().__init__(nome, energia_gasta, descricao)
    
    def usar_carta():
        pass

class CartaAtordoamento (Carta):
    def __init__(self, nome, energia_gasta, descricao):
        super().__init__(nome, energia_gasta, descricao)
        
    def usar_carta():
        pass

class CartaDano (Carta):
    def __init__(self, nome, energia_gasta, descricao, pontos_dano):
        super().__init__(nome, energia_gasta, descricao)
        self.pontos_dano = pontos_dano
    
    def usar_carta():
        pass

class CartaCura (Carta):
    def __init__(self, nome, energia_gasta, descricao, pontos_vida_curado):
        super().__init__(nome, energia_gasta, descricao)
        self.pontos_vida_curado = pontos_vida_curado
        
    def usar_carta():
        pass