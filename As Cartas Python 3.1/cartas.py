from enum import Enum
from personagem import Personagem

class Carta: #Super Classe Carta
    def __init__(self, nome, energia_gasta: int, descricao):
        self.nome = nome
        self.energia_gasta = energia_gasta
        self.descricao = descricao
    
    def usar_carta(self):
        return "Carta inválida."

class TipoCarta (Enum): #Melhora a legibilidade do código
    
    VIDA_MAXIMA = 1
    DEFESA = 2
    ATAQUE = 3
    ENERGIA_MAXIMA = 4
    
# Subclasses que são herdeiras da Classe Carta:
class CartaAumento (Carta):
    def __init__(self, nome, energia_gasta: int, descricao, tipo: TipoCarta, pontos_aumentados: int):
        super().__init__(nome, energia_gasta, descricao)
        self.tipo = tipo
        self.pontos_aumentados = pontos_aumentados
        
    def usar_carta(self, beneficiado:Personagem):
        match self.tipo:
            case TipoCarta.VIDA_MAXIMA:
                beneficiado.vida_maxima += self.pontos_aumentados
            
            case TipoCarta.DEFESA:
                beneficiado.pontos_defesa += self.pontos_aumentados
            
            case TipoCarta.ATAQUE:
                beneficiado.pontos_ataque += self.pontos_aumentados
                
            case TipoCarta.ENERGIA_MAXIMA:
                beneficiado.energia_maxima += self.pontos_aumentados
            
            case _:
                return f"carta inválida ou inexistente! Tente outra carta"

class CartaRoubo (Carta):
    def __init__(self, nome, energia_gasta: int, descricao):
        super().__init__(nome, energia_gasta, descricao)
    
    def usar_carta():
        pass

class CartaAtordoamento (Carta):
    def __init__(self, nome, energia_gasta: int, descricao):
        super().__init__(nome, energia_gasta, descricao)
        
    def usar_carta():
        pass

class CartaDano (Carta):
    def __init__(self, nome, energia_gasta: int, descricao, pontos_dano):
        super().__init__(nome, energia_gasta, descricao)
        self.pontos_dano = pontos_dano
    
    def usar_carta():
        pass

class CartaCura (Carta):
    def __init__(self, nome, energia_gasta: int, descricao, pontos_vida_curado):
        super().__init__(nome, energia_gasta, descricao)
        self.pontos_vida_curado = pontos_vida_curado
        
    def usar_carta():
        pass