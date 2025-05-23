class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.energia = 100
        self.fome = 80
        self.dinheiro = 80
        self.higiene = 100
        self.mental = 100
        self.trabalho = None
        self.saude = 80

    def comer(self):
        if self.dinheiro < 10:
            return f"{self.nome} não tem dinheiro para comer"
        else:
            self.fome = min(100, self.fome + 30)
            self.dinheiro -= 10
            return f"{self.nome} se alimentou!"


    def jogar_futebol(self):
        if self.saude < 30:
            return f"{self.nome} está com a saúde muito baixa para jogar futebol"
        if self.energia < 40:
            return f"{self.nome} está muito cansado para jogar futebol"
        
        self.saude = min(100, self.saude + 15)
        self.energia -= 40
        return f"{self.nome} jogou futebol, gastou energia mas está mais saudável!"

    def dormir(self):
        if(self.energia == 100):
            return f"{self.nome} não está cansado para dormir."
        
        else:
            self.energia = 100
            self.fome -= 40
            self.higiene -= 10
            
    def trabalhar(self):
        if (self.energia < 35):
            return f"{self.nome} está muito cansado para trabalhar!"
        
        self.energia -= 30
        self.mental -= 20
        self.dinheiro += 40
        self.higiene -= 30
        
        return f"{self.nome} trabalhou"

    def mostrar_status(self):
        return f'''
        😀{self.nome}  
        💥 Energia: {self.energia}
        🍕 Fome: {self.fome}
        💰 Dinheiro: {self.dinheiro}
        🙂 Mental: {self.mental}
        😱 Higiêne: {self.higiene}'''
            
if __name__ == '__main__':
    obj1 = Personagem("Lionel Messi")
    obj2 = Personagem("Cristiano Ronaldo")

    print(obj2.mostrar_status())
    print(f"Saúde de {obj2.nome}: {obj2.saude}")
    print(f"Energia de {obj2.nome}: {obj2.energia}")
