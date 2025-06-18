from partida import Partida
import random
from personagem import Personagem

objeto_personagem1 = Personagem("Messi")
objeto_personagem2 = Personagem("Cristiano Ronaldo")

mensagem = objeto_personagem1.atacar(objeto_personagem2)
print(mensagem)

mensagem = objeto_personagem2.atacar(objeto_personagem1)
print(mensagem)

# if __name__ == '__main__':
#     dado = random.randint(1,2)
#     if dado == 1:
#         print("O personagem 1 começa! ")
#     else:
#         print("O personagem 2 começa! ")
        
# partida = Partida(turno = 0)
