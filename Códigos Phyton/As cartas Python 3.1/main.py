from partida import Partida
import random
from personagem import Personagem
from cartas import *

objeto_personagem1 = Personagem("Messi")
objeto_personagem2 = Personagem("Cristiano Ronaldo")

mensagem = objeto_personagem1.atacar(objeto_personagem2)
print(mensagem)

mensagem = objeto_personagem2.atacar(objeto_personagem1)
print(mensagem)

objeto_carta_aumento_vida_maxima = CartaAumento("carta_vida_maxima", 1 , "aumenta o máximo de vida do personagem", 1 , 15)
objeto_carta_aumento_defesa = CartaAumento("carta_defesa", 1 , "aumenta o máximo de defasa do personagem", 2 , 15)
objeto_carta_aumento_ataque = CartaAumento("carta_ataque", 1 , "aumenta o máximo de ataque do personagem", 3 , 15 )
objeto_carta_energia_maxima = CartaAumento("carta_energia_maxima", 1 , "aumenta a energia máxima", 4 , 15)
objeto_carta_dano = CartaDano("carta_dano", 1 , "causa 25 de dano", 25)
objeto_carta_cura = CartaCura("carta_cura", 1 , "cura 40 pontos de vida", 40)
objeto_carta_atordoamento = CartaAtordoamento("carta_atordoamento", 1 , "causa atordoamento ")
objeto_carta_roubo = CartaRoubo("carta_roubo", 1 , "rouba a carta do oponente")

cartas = [objeto_carta_aumento_vida_maxima,
          objeto_carta_aumento_defesa, 
          objeto_carta_aumento_ataque,
          objeto_carta_aumento_vida_maxima,
          objeto_carta_dano,
          objeto_carta_cura,
          objeto_carta_atordoamento,
          objeto_carta_roubo]

cartas_aleatorias1 = random.sample(cartas, 3)
objeto_personagem1.mao_de_cartas.extend(cartas_aleatorias1)

cartas_aleatorias2 = random.sample(cartas, 3)
objeto_personagem2.mao_de_cartas.extend(cartas_aleatorias2)

if __name__ == '__main__':
    dado = random.randint(1,2)
    print(cartas_aleatorias1)
    if dado == 1:
       print("O personagem 1 começa! ")
    else:
        print("O personagem 2 começa! ")
        
    partida = Partida(0, objeto_personagem1, objeto_personagem2, dado)
    
