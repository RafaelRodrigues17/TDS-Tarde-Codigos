from enum import Enum 
from personagem import Personagem

class Carta:
    def __init__(self, nome, energia_gasta: int, descricao):
        self.nome = nome
        self.energia_gasta = energia_gasta
        self.descricao = descricao
    
    def usar_carta(self, usuario: Personagem, alvo: Personagem = None):
        return "Carta inválida."

class TipoCarta(Enum):
    VIDA_MAXIMA = 1
    DEFESA = 2
    ATAQUE = 3
    ENERGIA_MAXIMA = 4

class CartaAumento(Carta):
    def __init__(self, nome, energia_gasta: int, descricao, tipo: TipoCarta, pontos_aumentados: int):
        super().__init__(nome, energia_gasta, descricao)
        self.tipo = tipo
        self.pontos_aumentados = pontos_aumentados
        
    def usar_carta(self, usuario: Personagem, alvo: Personagem = None):
        if usuario.energia < self.energia_gasta:
            return f"{usuario.nome} não tem energia suficiente para usar a carta {self.nome}"
        usuario.energia -= self.energia_gasta
        match self.tipo:
            case TipoCarta.VIDA_MAXIMA:
                usuario.vida_maxima += self.pontos_aumentados
            case TipoCarta.DEFESA:
                usuario.pontos_defesa += self.pontos_aumentados
            case TipoCarta.ATAQUE:
                usuario.pontos_ataque += self.pontos_aumentados
            case TipoCarta.ENERGIA_MAXIMA:
                usuario.energia_maxima += self.pontos_aumentados
        return f"{usuario.nome} usou {self.nome}!"

class CartaRoubo(Carta):
    def usar_carta(self, usuario: Personagem, alvo: Personagem):
        if usuario.energia < self.energia_gasta or not alvo.mao_de_cartas:
            return f"{usuario.nome} não pode usar {self.nome} agora."
        usuario.energia -= self.energia_gasta
        carta_roubada = alvo.mao_de_cartas.pop(0)
        usuario.mao_de_cartas.append(carta_roubada)
        return f"{usuario.nome} roubou a carta {carta_roubada.nome} de {alvo.nome}"

class CartaAtordoamento(Carta):
    def usar_carta(self, usuario: Personagem, alvo: Personagem):
        if usuario.energia < self.energia_gasta:
            return f"{usuario.nome} não tem energia suficiente para usar a carta {self.nome}"
        usuario.energia -= self.energia_gasta
        alvo.energia = max(0, alvo.energia - 5)
        return f"{usuario.nome} usou {self.nome}, reduzindo a energia de {alvo.nome}"

class CartaDano(Carta):
    def __init__(self, nome, energia_gasta: int, descricao, pontos_dano):
        super().__init__(nome, energia_gasta, descricao)
        self.pontos_dano = pontos_dano
    
    def usar_carta(self, usuario: Personagem, alvo: Personagem):
        if usuario.energia < self.energia_gasta:
            return f"{usuario.nome} não tem energia suficiente para usar {self.nome}"
        usuario.energia -= self.energia_gasta
        return alvo.levar_dano(self.pontos_dano)

class CartaCura(Carta):
    def __init__(self, nome, energia_gasta: int, descricao, pontos_vida_curado):
        super().__init__(nome, energia_gasta, descricao)
        self.pontos_vida_curado = pontos_vida_curado
        
    def usar_carta(self, usuario: Personagem, alvo: Personagem = None):
        if usuario.energia < self.energia_gasta:
            return f"{usuario.nome} não tem energia suficiente para usar {self.nome}"
        usuario.energia -= self.energia_gasta
        return usuario.curar(self.pontos_vida_curado)
