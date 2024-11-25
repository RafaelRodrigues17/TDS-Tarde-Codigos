#include <stdio.h>
#include <string.h>

float reajusteEtanol(float* valor1, float reajuste) {
    float resultado;
    resultado = *valor1 + reajuste;
    return resultado;
}

float reajusteGasolina(float* valor1, float reajuste) {
    float resultado1;
    resultado1 = *valor1 + reajuste;
    return resultado1;
}

int main() {
    float valor1, valor2, reajuste, valorTotal;
    char tipo[10];
    int confirma;

    printf("Informe o valor atual da gasolina: ");
    scanf("%f", &valor1);

    printf("Informe o valor atual do etanol: ");
    scanf("%f", &valor2);

    printf("Informe qual o valor do reajuste: ");
    scanf("%f", &reajuste);

    printf("Informe qual combustível vai ser reajustado (etanol ou gasolina): ");
    scanf("%s", tipo); 

    if (strcmp(tipo, "etanol") == 0) {
        confirma = 1;
        valorTotal = reajusteEtanol(&valor2, reajuste);
        valor1 = valor1 + (valorTotal * 0.27); 
        printf("Valor do Etanol: %.2f\n", valorTotal);
        printf("Valor da Gasolina: %.2f\n", valor1);
    } else {
        valorTotal = reajusteGasolina(&valor1, reajuste);
        printf("Valor do Etanol: %.2f\n", valor2);
        printf("Valor da Gasolina: %.2f\n", valorTotal);
    }

    return 0;
}
