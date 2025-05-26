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
        self.trabalho_nivel = 0

    def comer(self):
        if self.dinheiro < 10:
            return f"{self.nome} não tem dinheiro para comer"
        else:
            self.fome = min(100, self.fome + 30)
            self.mental = max(0, self.mental + 5)
            self.dinheiro -= 10
            return f"{self.nome} se alimentou!"

    def jogar_futebol(self):
        if self.saude < 30:
            return f"{self.nome} está com a saúde muito baixa para jogar futebol"
        if self.energia < 40:
            return f"{self.nome} está muito cansado para jogar futebol"
        
        self.saude = min(100, self.saude + 15)
        self.energia = max(0, self.energia - 40)
        return f"{self.nome} jogou futebol, gastou energia mas está mais saudável!"

    def dormir(self):
        if self.energia == 100:
            return f"{self.nome} não está cansado para dormir."
        else:
            self.energia = 100
            self.fome = max(0, self.fome - 40)
            self.higiene = max(0, self.higiene - 10)
            self.mental = max(0, self.mental + 30)
            return f"{self.nome} dormiu e recuperou mental e energia!"

    def trabalhar(self):
        if self.energia < 35:
            return f"{self.nome} está muito cansado para trabalhar!"
        
        self.energia = max(0, self.energia - 30)
        self.mental = max(0, self.mental - 30) 
        self.dinheiro += 40
        self.higiene = max(0, self.higiene - 30)
        
        return f"{self.nome} trabalhou"

    def tomar_banho(self):
        if self.higiene == 100:
            return f"{self.nome} já está limpo."
        self.higiene = 100
        self.energia = max(0, self.energia - 2)
        self.mental = max(0, self.mental + 10)
        
        return f"{self.nome} tomou banho!"

    def mostrar_status(self):
        return f'''
        😀 {self.nome}  
        ⚡ Energia: {self.energia}
        🍕 Fome: {self.fome}
        💰 Dinheiro: {self.dinheiro}
        😎 Mental: {self.mental}
        🧻 Higiene: {self.higiene}
        ❤️ Saúde: {self.saude}
        '''

    def ser_contratado(self, objeto_trabalho):
        self.trabalho = objeto_trabalho
        self.trabalho_nivel = 1
        return f"{self.nome} foi contratado na carreira de {self.trabalho.carreira} no cargo {self.trabalho.ver_cargo(self.trabalho_nivel)}"

    def ser_demitido(self, objeto_trabalho):
        self.trabalho = None
        self.trabalho_nivel = 0  # Corrigido: estava como self._trabalho_nivel

    def pedir_demissao(self, objeto_trabalho):
        self.trabalho = None
        self.trabalho_nivel = 0
        return f"{self.nome} pediu demissão da carreira de {objeto_trabalho.carreira}"


class Trabalho:
    def __init__(self, carreira, cargos, salarios, higiene, energia, mental):
        self.__carreira = carreira
        self.__cargos = cargos
        self.__salarios = salarios
        self.__higiene_usada = higiene
        self.__energia_gasta = energia
        self.__mental_usado = mental

    @property
    def informacoes(self):
        return f'''Carreira: {self.__carreira}
Cargos: {self.__cargos}
Salários: {self.__salarios}
Energia necessária: {self.__energia_gasta}
Higiene usada: {self.__higiene_usada}
Mental usado: {self.__mental_usado}'''

    @property
    def carreira(self):
        return self.__carreira

    def ver_cargo(self, nivel):
        if 1 <= nivel <= len(self.__cargos):
            return self.__cargos[nivel - 1]
        else:
            return "Cargo inválido"


# Execução de teste
if __name__ == '__main__':
    carreira = "Motorista"
    cargos = ["Motorista de Ônibus", "Uber", "Taxista"]
    salarios = [2500, 3000, 3500]
    higiene = 50
    energia = 70
    mental = 35

    objeto_trabalho = Trabalho(carreira, cargos, salarios, higiene, energia, mental)
    print(objeto_trabalho.informacoes)

    objeto_personagem = Personagem("Rogério")
    print(objeto_personagem.ser_contratado(objeto_trabalho))
