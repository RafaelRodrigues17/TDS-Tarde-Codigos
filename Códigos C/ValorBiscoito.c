#include <stdio.h>

float calcularPrecoBiscoito(int qtdBiscoito, float valorBiscoito) {
    float resultado;

    if (qtdBiscoito > 10) {
        valorBiscoito = valorBiscoito * 0.9;  
        printf("Desconto de 10%% devido à quantidade de compra. Valor R$ %.2f\n", valorBiscoito);
    }

    resultado = valorBiscoito * qtdBiscoito;
    return resultado;
}

int main() {
    int quantidadeBiscoito;
    float valorBiscoito, valorPagar;

    printf("Digite a quantidade de biscoitos desejada: ");
    scanf("%d", &quantidadeBiscoito);

    printf("Digite o valor do biscoito desejado: ");
    scanf("%f", &valorBiscoito);

    valorPagar = calcularPrecoBiscoito(quantidadeBiscoito, valorBiscoito);

    printf("\nO biscoito sem desconto R$ %.2f\n", valorBiscoito);
    printf("Valor total a ser pago é de R$ %.2f\n", valorPagar);

    return 0;
}
