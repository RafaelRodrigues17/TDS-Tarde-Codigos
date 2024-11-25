#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int numeroAleatorio, tentativa, intervaloInferior = 1, intervaloSuperior = 100;

    srand(time(0));

    numeroAleatorio = (rand() % (intervaloSuperior - intervaloInferior + 1)) + intervaloInferior;

    printf("Bem-vindo ao jogo de adivinhação!\n");
    printf("Tente adivinhar o número gerado entre %d e %d.\n", intervaloInferior, intervaloSuperior);

    printf("Digite sua tentativa: ");
    scanf("%d", &tentativa);

    if (tentativa == numeroAleatorio) {
        printf("Parabéns! Você adivinhou o número correto: %d!\n", numeroAleatorio);
    } else {
        printf("Que pena! O número correto era %d. Tente novamente!\n", numeroAleatorio);
    }

    return 0;
}
