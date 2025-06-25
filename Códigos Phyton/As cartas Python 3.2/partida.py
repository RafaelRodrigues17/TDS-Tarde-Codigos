from personagem import *

class Partida:
    def __init__(self, turno, jogador1, jogador2, jogador_atual):
        self.turno = None
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.jogador_atual = jogador_atual
        self.jogo_ativo = True
    
    def iniciar_partida(self): # Função para iniciar a partida
            
        print(f"A vez é do jogador: {self.jogador_atual.nome}")
        
        while self.jogo_ativo:
            print(f"Estas são as cartas de {self.jogador_atual.nome}: \n") 
            for carta in self.jogador_atual.mao_de_cartas:
               print(carta.nome)
            print(f"\nA vida atual de {self.jogador_atual.nome} é {self.jogador_atual.vida_atual} pontos")
            print(f"E a sua energia é de {self.jogador_atual.energia} pontos\n")
            print(f"{self.jogador_atual.nome} deseja: |[1] Atacar| - |[2] Usar uma carta| - |[3] Comprar uma carta (passa a vez!)|")
            
            escolha = int(input("Escolha uma das opções acima:\n "))    
            match escolha:
                case 1:
                    self.jogador_atual.atacar(self.inimigo)
                case 2:
                    self.jogador_atual.usar_carta()
                case 3:
                    self.jogador_atual.comprar_carta()
                case _:
                    print("Opção Inválida! Tente novamente ")
            break          
                   
    def trocar_turno(self):
        pass
    
    def trocar_jogador(): # Troca o jagador
        pass
    
    def encerrar_partida(): # encerra a partida (finaliza quando um dos personagens morre)
        pass
    