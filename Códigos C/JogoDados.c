#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int lancar_dado() {
    
    srand(time(NULL));

    int valor1 = rand() % 6 + 1;
    return valor1;
}

void jogar_rodada(int* pontos_jogador1, int* pontos_jogador2) {
   
    int dado1 = lancar_dado();
    int dado2 = lancar_dado();

    usleep(1250000); 

    printf("\nJogador 1 fez: %d", dado1);
    printf("\nJogador 2 fez: %d", dado2);

    
    if (dado1 > dado2) {
        printf("\nJogador 1 venceu a rodada");
        (*pontos_jogador1)++;
    } else if (dado1 < dado2) {
        printf("\nJogador 2 venceu a rodada");
        (*pontos_jogador2)++;
    } else {
        printf("\nEmpate");
    }
}

// Função para mostrar o resultado final
void mostrar_resultado(int pontos_jogador1, int pontos_jogador2) {
    if (pontos_jogador1 > pontos_jogador2) {
        printf("\n\nJogador 1 venceu");
    } else if (pontos_jogador1 < pontos_jogador2) {
        printf("\n\nJogador 2 venceu");
    } else {
        printf("\nEmpate");
    }
}

int main() {
    int pontos_jogador1 = 0, pontos_jogador2 = 0, rodada = 1;

    
    while (pontos_jogador1 < 3 && pontos_jogador2 < 3) {
        printf("\nRodada %d:\n", rodada);
        jogar_rodada(&pontos_jogador1, &pontos_jogador2);
        rodada++;
    }

    mostrar_resultado(pontos_jogador1, pontos_jogador2);

    return 0;
}
