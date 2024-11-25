#include <stdio.h>
#include <string.h>

int main() {
    char login[50];
    int senha, n, i;
    double nota, soma = 0.0, media = 0.0;

    printf("Digite seu login, somente letras: ");
    scanf("%s", login);

    printf("Digite sua senha, somente números: ");
    scanf("%d", &senha);

    if (strcmp(login, "Rafael") == 0 && senha == 123456) {
        printf("Acesso foi feito com sucesso!\n");

        printf("Informe quantas notas você deseja informar: ");
        scanf("%d", &n);

        for (i = 0; i < n; i++) {
            printf("Informe a %d° nota: ", i + 1);
            scanf("%lf", &nota);

            while (nota < 0.0 || nota > 10.0) {
                printf("Nota inválida! Informe uma nota entre 0 e 10.\n");
                scanf("%lf", &nota);
            }

            soma += nota;
        }

        media = soma / n;
        printf("A média das notas é: %.2f\n", media);
    } else {
        printf("Acesso negado\n");
    }

    return 0;
}
