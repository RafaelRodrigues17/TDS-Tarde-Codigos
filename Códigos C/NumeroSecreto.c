#include <stdio.h>

int main() {
    int num1, num2, total;

    printf("Olá, vamos tentar encontrar o número secreto com uma soma? Duvido acertar!\n");
    printf("Digite o primeiro número: ");
    scanf("%d", &num1);

    printf("Digite o segundo número: ");
    scanf("%d", &num2);

    total = num1 + num2;

    printf("O resultado da soma é %d\n", total);

    if (total == 34) {
        printf("Parabéns você encontrou o número secreto (34) !!!!!, Você é o cara.\n");
    } else {
        printf("Não é o número secreto seu bobão!!!\n");
    }

    return 0;
}
