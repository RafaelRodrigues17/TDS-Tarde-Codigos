
import tkinter as tk
from tkinter import messagebox
from mini_sims import Personagem, Trabalho

class SimsApp:
    def __init__(self, root):
        self.personagem = Personagem("Rafael")
        root.title("Mini Sims")
        root.geometry("800x600")
        
        self.label_status = tk.Label(root, text=self.personagem.mostrar_status(), font=("Arial", 18), pady=20, justify="left")
        self.label_status.pack()

        botoes = [
            ("🍟 Comer", self.acao_botao_comer),
            ("🥱 Trabalhar", self.acao_botao_trabalhar),
            ("😴 Dormir", self.acao_botao_dormir),
            ("🦆 Tomar Banho", self.acao_botao_banho),
            ("📄 Procurar Emprego", self.acao_botao_procurar_emprego)
        ]

        for texto, comando in botoes:
            tk.Button(root, text=texto, font=("Arial", 14), width=20, command=comando).pack(pady=5)

        self.label_mensagem = tk.Label(root, text="", font=("Arial", 16), pady=20, fg="blue")
        self.label_mensagem.pack()

    def atualizar_status(self):
        self.label_status.config(text=self.personagem.mostrar_status())

    def acao_botao_comer(self):
        self.label_mensagem.config(text=self.personagem.comer())
        self.atualizar_status()

    def acao_botao_trabalhar(self):
        self.label_mensagem.config(text=self.personagem.trabalhar())
        self.atualizar_status()

    def acao_botao_dormir(self):
        self.label_mensagem.config(text=self.personagem.dormir())
        self.atualizar_status()

    def acao_botao_banho(self):
        self.label_mensagem.config(text=self.personagem.tomar_banho())
        self.atualizar_status()

    def acao_botao_procurar_emprego(self):
        self.trabalhos = self.criar_trabalhos()
        for trabalho in self.trabalhos:
            resposta = messagebox.askquestion("Oferta de emprego", message=trabalho.informacoes)
            if resposta == "yes":
                self.personagem.definir_trabalho(trabalho)
                self.label_mensagem.config(text=f"Você agora trabalha como {trabalho.ver_cargo(1)}!")
                self.atualizar_status()
                break

    def criar_trabalhos(self):
        lista_trabalhos = []
        lista_trabalhos.append(Trabalho("Motorista",
            ["Motorista de Ônibus", "Uber", "Taxista"],
            [2500, 3000, 3500],
            [30, 25, 20], [40, 30, 25], [25, 20, 15], [10, 5, 5]
        ))
        lista_trabalhos.append(Trabalho("Piloto",
            ["Piloto de Formula 1", "Piloto da Nascar", "Piloto da Le Mans"],
            [5000000, 6000000, 7500000],
            [60, 55, 50], [90, 85, 80], [40, 35, 30], [20, 15, 15]
        ))
        lista_trabalhos.append(Trabalho("Vendedor",
            ["Vendedor das Casas Bahia", "Vendedor da Apple", "Vendedor da Samsung"],
            [2090, 4890, 6590],
            [25, 20, 15], [30, 25, 20], [20, 15, 10], [5, 5, 5]
        ))
        return lista_trabalhos

if __name__ == "__main__":
    root = tk.Tk()
    app = SimsApp(root)
    root.mainloop()
