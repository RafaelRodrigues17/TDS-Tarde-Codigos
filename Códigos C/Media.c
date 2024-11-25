#include <stdio.h>
#include <stdlib.h>

int main() {
    double valores[100]; 
    int count = 0; 
    char entrada[50]; 

    printf("Digite os números (ou 'sair' para calcular a média):\n");

    while (1) {
    
        fgets(entrada, sizeof(entrada), stdin);

        entrada[strcspn(entrada, "\n")] = '\0';

        if (strcmp(entrada, "sair") == 0) {
            break;
        }
  
        char *endptr;
        double numero = strtod(entrada, &endptr);

        if (*endptr == '\0') {
       
            valores[count++] = numero;
        } else {
            printf("Por favor, insira um número válido.\n");
        }
    }

    if (count > 0) {
        double soma = 0;
        for (int i = 0; i < count; i++) {
            soma += valores[i];
        }
        double media = soma / count;
        printf("A média dos valores inseridos é: %.2f\n", media);
    } else {
        printf("Nenhum valor foi inserido.\n");
    }

    return 0;
}
