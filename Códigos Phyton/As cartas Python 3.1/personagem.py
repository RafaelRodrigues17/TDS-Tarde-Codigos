from __future__ import annotations
from random import randint
import random

class Personagem:
    def __init__(self, nome): 
        self.nome = nome
        self.vida_maxima = 100
        self.vida_atual = 100
        self.pontos_ataque = 40
        self.pontos_defesa = 25
        self.mao_de_cartas = []
        self.energia_maxima = 10
        self.energia = 100
    
    def exibir_nome(self): # Exibi o nome do jogador vindo da Main
        return self.nome
    
    def atacar(self, inimigo: Personagem):# função para atacar
        if self.energia < 3:
            return f"{self.nome} não tem energia para o ataque"
        
        self.energia -= 3 # Custo do ataque = 3
        
        eficiencia = randint(70, 110) / 100
        dano = (self.pontos_ataque - inimigo.pontos_defesa) * eficiencia
        dano = max(0, round(dano)) # Arredonda o dano
        
        print(inimigo.levar_dano(dano))
        
        return f"{self.nome} atacou {inimigo.nome} com eficiência {eficiencia*100} e causou {dano} de dano"

    def levar_dano(self, dano): # Função para o personagem levar dano
        self.vida_atual -= dano
        return f"{self.nome} levou {dano} de dano, sua a vida atual é {self.vida_atual}"
        
    def comprar_carta(self, baralho): # Função para comprar a carta
        carta_comprada = random.sample(baralho, k = 1)
        self.mao_de_cartas.extend(carta_comprada)
        return f"{self.nome} comprou a carta {carta_comprada.nome}."
    
    def usar_carta(self, carta): # função parar usar a carta
        pass 
    
    def exibir_cartas(self): # Exibe todas as cartas do jogador
        return self.mao_de_cartas
    
    def curar(self, pontos_de_vida): # Função que cura o personagem
        self.vida_atual = min(self.vida_maxima, self.vida_atual + pontos_de_vida)
        return f"self.nome curou {pontos_de_vida} pontos de vida e sua vida atual é {self.vida_atual}"
        
           