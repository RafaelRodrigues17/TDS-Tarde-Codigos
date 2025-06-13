from partida import Partida
import random
from personagem import Personagem

personagem1 = Personagem("Mago")
mensagem = personagem1.exibir_nome()
print(mensagem)

personagem2 = Personagem("Bruxa")
mensagem = personagem2.exibir_nome()
print(mensagem)

if __name__ == '__main__':
    dado = random.randint(1,2)
    if dado == 1:
        print("O personagem 1 começa! ")
    else:
        print("O personagem 2 começa! ")
        
partida = Partida(turno = 0)

