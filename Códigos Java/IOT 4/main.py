from database import Pizza

def main():
    pizza = Pizza()
    pizza.adicionar_pizza("Diavola","medias", 35.00)
    pizza.listar_pizzas()
    pizza.excluir_pizza()

if __name__ == "__main__":
    main()