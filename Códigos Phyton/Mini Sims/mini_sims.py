
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
        if not self.trabalho:
            return f"{self.nome} não tem um trabalho no momento."
        if self.trabalho_nivel == 0:
            return f"{self.nome} ainda não foi contratado."

        energia_gasta, higiene_gasta, mental_usado, saude_afetada = self.trabalho.estatisticas_por_cargo(self.trabalho_nivel)
        if self.energia < energia_gasta:
            return f"{self.nome} está muito cansado para trabalhar!"

        self.energia = max(0, self.energia - energia_gasta)
        self.higiene = max(0, self.higiene - higiene_gasta)
        self.mental = max(0, self.mental - mental_usado)
        self.saude = max(0, self.saude - saude_afetada)
        self.dinheiro += self.trabalho.salario_por_cargo(self.trabalho_nivel)

        return f"{self.nome} trabalhou como {self.trabalho.ver_cargo(self.trabalho_nivel)}"

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

    def ser_demitido(self):
        self.trabalho = None
        self.trabalho_nivel = 0  

    def pedir_demissao(self):
        if self.trabalho:
            mensagem = f"{self.nome} pediu demissão da carreira de {self.trabalho.carreira}"
        else:
            mensagem = f"{self.nome} não tem trabalho para pedir demissão"
        self.trabalho = None
        self.trabalho_nivel = 0
        return mensagem

    def definir_trabalho(self, trabalho):
        self.trabalho = trabalho
        self.trabalho_nivel = 1


class Trabalho:
    def __init__(self, carreira, cargos, salarios, higiene_por_cargo, energia_por_cargo, mental_por_cargo, saude_por_cargo):
        self.__carreira = carreira
        self.__cargos = cargos
        self.__salarios = salarios
        self.__higiene_por_cargo = higiene_por_cargo
        self.__energia_por_cargo = energia_por_cargo
        self.__mental_por_cargo = mental_por_cargo
        self.__saude_por_cargo = saude_por_cargo

    @property
    def informacoes(self):
        return f'''Carreira: {self.__carreira}
Cargos: {self.__cargos}
Salários: {self.__salarios}'''

    @property
    def carreira(self):
        return self.__carreira

    def ver_cargo(self, nivel):
        if 1 <= nivel <= len(self.__cargos):
            return self.__cargos[nivel - 1]
        else:
            return "Cargo inválido"

    def salario_por_cargo(self, nivel):
        return self.__salarios[nivel - 1]

    def estatisticas_por_cargo(self, nivel):
        return (
            self.__energia_por_cargo[nivel - 1],
            self.__higiene_por_cargo[nivel - 1],
            self.__mental_por_cargo[nivel - 1],
            self.__saude_por_cargo[nivel - 1]
        )
