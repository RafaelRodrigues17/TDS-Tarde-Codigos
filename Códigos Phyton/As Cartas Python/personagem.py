class Personagem:
    def __init__(self, nome): 
        self.nome = nome
        self.vida_maxima = 100
        self.vida = 100
        self.ponto_ataque = 20
        self.ponto_defesa = 25
        self.energia = 100
    
    def exibir_nome(self): # Exibi o nome do jogador vindo da Main
        return self.nome
    
    def atacar(self): # função para atacar
        pass
    
    def usar_carta(): # usa a carta
        pass
    
    def levar_dano(): # Função para o personagem levar dano
        pass
    
    def exibir_cartas(self): # Exibe todas as cartas do jogador
        return self.cartas
    
    def curar(self): # Função que cura o personagem
        if self.vida == 100:
           return print("Você já está com a vida cheia!")
        else:
            print("Você foi curado!") 
           
        