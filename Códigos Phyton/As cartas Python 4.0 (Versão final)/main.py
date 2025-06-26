from partida import Partida
import random
from personagem import Personagem
from cartas import *

personagem1 = Personagem("Arqueiro")
personagem2 = Personagem("Mago")

carta_aumento_vida_maxima = CartaAumento("Carta de vida extra", 1 , "aumenta o máximo de vida do personagem", 1 , 15)
carta_aumento_defesa = CartaAumento("Carta de defesa reforçada", 1 , "aumenta o máximo de defasa do personagem", 2 , 15)
carta_aumento_ataque = CartaAumento("Carta de pontos extras de ataque", 1 , "aumenta o máximo de ataque do personagem", 3 , 15 )
carta_energia = CartaAumento("Carta de energia extra", 1 , "aumenta a energia", 4 , 25)
carta_dano = CartaDano("Carta de dano", 1 , "causa 25 de dano", 25)
carta_cura = CartaCura("Carta de cura", 1 , "cura 40 pontos de vida", 40)
carta_atordoamento = CartaAtordoamento("Carta de atordoamento", 1 , "causa atordoamento ")
carta_roubo = CartaRoubo("Carta de roubo", 1 , "rouba a carta do oponente")

cartas = [carta_aumento_vida_maxima,
          carta_aumento_defesa, 
          carta_aumento_ataque,
          carta_aumento_vida_maxima,
          carta_energia,
          carta_dano,
          carta_cura,
          carta_atordoamento,
          carta_roubo]

cartas_aleatorias1 = random.sample(cartas, 3)
personagem1.mao_de_cartas.extend(cartas_aleatorias1)

cartas_aleatorias2 = random.sample(cartas, 3)
personagem2.mao_de_cartas.extend(cartas_aleatorias2)

if __name__ == '__main__':
    dado = random.randint(1,2)
    if dado == 1:
       print("\nA partida foi iniciada, o jogador 1 começará!\n ")
       jogador_inicial = personagem1
    else:
       print("\nA partida foi iniciada, o jogador 1 começará!\n ")
       jogador_inicial = personagem2
       
        
    partida = Partida(0, personagem1, personagem2, jogador_inicial)
    partida.iniciar_partida()
    
