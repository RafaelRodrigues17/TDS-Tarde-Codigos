#include <stdio.h>

#define MAX_FRUTAS 5  // Número máximo de frutas

typedef struct {
    char nome[30];
    float preco;
    int quantidade;
} Fruta;

void exibirEstoque(Fruta frutas[], int n);
void realizarCompra(Fruta frutas[], int n);

int main() {
    Fruta frutas[MAX_FRUTAS] = {
        {"Maçã", 3.50, 100},  
        {"Banana", 2.30, 150},
        {"Laranja", 1.80, 120},
        {"Morango", 5.00, 80},
        {"Abacaxi", 4.20, 50}
    };
    
    int opcao;

    do {
        printf("\n*** Mercado de Frutas ***\n");
        printf("1. Exibir estoque de frutas\n");
        printf("2. Realizar compra\n");
        printf("3. Sair\n");
        printf("Escolha uma opção: ");
        scanf("%d", &opcao);

        switch(opcao) {
            case 1:
                exibirEstoque(frutas, MAX_FRUTAS);
                break;
            case 2:
                realizarCompra(frutas, MAX_FRUTAS);
                break;
            case 3:
                printf("Obrigado por usar o sistema. Até logo!\n");
                break;
            default:
                printf("Opção inválida! Tente novamente.\n");
        }

    } while(opcao != 3);

    return 0;
}

void exibirEstoque(Fruta frutas[], int n) {
    printf("\nEstoque de Frutas:\n");
    printf("Nome\t\tPreço\tQuantidade\n");
    for (int i = 0; i < n; i++) {
        printf("%-10s\t%.2f\t%d\n", frutas[i].nome, frutas[i].preco, frutas[i].quantidade);
    }
}

void realizarCompra(Fruta frutas[], int n) {
    int opcao, quantidade;
    float total = 0.0;

    printf("\n*** Realizar Compra ***\n");
    printf("Escolha uma fruta para comprar (1 a %d): ", n);
    scanf("%d", &opcao);

    if (opcao < 1 || opcao > n) {
        printf("Opção inválida! Tente novamente.\n");
        return;
    }

    printf("Quantidade a ser comprada: ");
    scanf("%d", &quantidade);

    if (quantidade > frutas[opcao - 1].quantidade) {
        printf("Quantidade solicitada não disponível. Estoque atual: %d\n", frutas[opcao - 1].quantidade);
    } else {
        frutas[opcao - 1].quantidade -= quantidade;
        total = frutas[opcao - 1].preco * quantidade;
        printf("Compra realizada com sucesso!\n");
        printf("Total a pagar: R$ %.2f\n", total);
    }
}
