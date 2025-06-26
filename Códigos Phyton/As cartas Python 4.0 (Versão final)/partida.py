from personagem import Personagem
from cartas import Carta, CartaAumento, CartaCura, CartaDano, CartaAtordoamento, CartaRoubo, TipoCarta
import random

class Partida:
    def __init__(self, turno, jogador1, jogador2, jogador_atual):
        # Inicializa os atributos da partida
        self.turno = turno
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.jogador_atual = jogador_atual
        self.jogo_ativo = True

    def trocar_turno(self):
        # Alterna entre jogador1 e jogador2
        if self.jogador_atual == self.jogador1:
            self.jogador_atual = self.jogador2
        else:
            self.jogador_atual = self.jogador1

    def remover_carta_usada(self, indice):
        # Remove a carta usada da mão do jogador atual com base no índice
        nova_mao = []
        for i in range(len(self.jogador_atual.mao_de_cartas)):
            if i != indice:
                nova_mao.append(self.jogador_atual.mao_de_cartas[i])
        self.jogador_atual.mao_de_cartas = nova_mao

    def iniciar_partida(self):
        while self.jogo_ativo:
            # Mostra status e cartas do jogador da vez
            print(f"\nVez de {self.jogador_atual.nome}")
            print("Cartas na mão:")
            for i, carta in enumerate(self.jogador_atual.mao_de_cartas):
                print(f"[{i}] {carta.nome} - {carta.descricao}")

            print(f"Vida: {self.jogador_atual.vida_atual}/{self.jogador_atual.vida_maxima}")
            print(f"Energia: {self.jogador_atual.energia}/{self.jogador_atual.energia_maxima}")

            # Menu de opções
            print("\nEscolha: [1] Atacar [2] Usar carta [3] Comprar carta")
            escolha = input("Digite o número da sua escolha: ")

            # Define quem é o inimigo nesta rodada
            if self.jogador_atual == self.jogador1:
                inimigo = self.jogador2
            else:
                inimigo = self.jogador1

            if escolha == "1":
                # Ataca o inimigo
                print(self.jogador_atual.atacar(inimigo))

            elif escolha == "2":
                # Verifica se o jogador tem cartas
                if len(self.jogador_atual.mao_de_cartas) == 0:
                    print("Você não tem cartas para usar!")
                else:
                    # Escolhe e usa a carta
                    escolha_carta = int(input("Digite o número da carta a ser usada: "))
                    carta = self.jogador_atual.mao_de_cartas[escolha_carta]

                    # Verifica se tem energia suficiente
                    if self.jogador_atual.energia < carta.energia_gasta:
                        print("Energia insuficiente para usar essa carta!")
                    else:
                        # Gasta energia
                        self.jogador_atual.energia -= carta.energia_gasta

                        # Aplica efeito da carta conforme o tipo
                        if isinstance(carta, CartaAumento):
                            carta.usar_carta(self.jogador_atual)
                            print("Carta de aumento usada com sucesso!")

                        elif isinstance(carta, CartaCura):
                            self.jogador_atual.vida_atual += carta.pontos_vida_curado
                            # Limita a vida ao máximo
                            if self.jogador_atual.vida_atual > self.jogador_atual.vida_maxima:
                                self.jogador_atual.vida_atual = self.jogador_atual.vida_maxima
                            print("Carta de cura usada!")

                        elif isinstance(carta, CartaDano):
                            inimigo.vida_atual -= carta.pontos_dano
                            if inimigo.vida_atual < 0:
                                inimigo.vida_atual = 0
                            print(f"{inimigo.nome} recebeu {carta.pontos_dano} de dano!")

                        elif isinstance(carta, CartaRoubo):
                            if len(inimigo.mao_de_cartas) > 0:
                                carta_roubada = inimigo.mao_de_cartas[0]
                                nova_mao_inimigo = []
                                for i in range(1, len(inimigo.mao_de_cartas)):
                                    nova_mao_inimigo.append(inimigo.mao_de_cartas[i])
                                inimigo.mao_de_cartas = nova_mao_inimigo
                                self.jogador_atual.mao_de_cartas.append(carta_roubada)
                                print(f"Você roubou a carta {carta_roubada.nome} do {inimigo.nome}!")
                            else:
                                print("O inimigo não tem cartas para roubar!")

                        elif isinstance(carta, CartaAtordoamento):
                            print(f"{inimigo.nome} foi atordoado e perderá a próxima vez!")
                            self.trocar_turno()  # O inimigo perde o turno já na próxima rodada

                        # Remove a carta usada da mão
                        self.remover_carta_usada(escolha_carta)

            elif escolha == "3":
                # Compra uma carta aleatória
                nova_carta = random.choice([
                    CartaCura("Carta de cura", 1, "cura 40 pontos de vida", 40),
                    CartaDano("Carta de dano", 1, "causa 25 de dano", 25),
                    CartaRoubo("Carta de roubo", 1, "rouba a carta do oponente"),
                    CartaAtordoamento("Carta de atordoamento", 1, "causa atordoamento"),
                    CartaAumento("Carta de vida extra", 1, "aumenta a vida", TipoCarta.VIDA_MAXIMA, 10)
                ])
                self.jogador_atual.mao_de_cartas.append(nova_carta)
                print(f"Você comprou a carta: {nova_carta.nome}")

            else:
                print("Escolha inválida!")

            # Verifica se algum jogador perdeu (vida chegou a 0)
            if self.jogador1.vida_atual <= 0 or self.jogador2.vida_atual <= 0:
                vencedor = self.jogador1 if self.jogador1.vida_atual > 0 else self.jogador2
                print(f"\nO jogo acabou! O vencedor foi {vencedor.nome}")
                self.jogo_ativo = False
            else:
                # Passa a vez
                self.trocar_turno()
