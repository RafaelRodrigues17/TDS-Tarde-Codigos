#include <stdio.h>

int main() {
    for (int numero = 1; numero < 10000; numero++) {
        int soma = 0;
        for (int i = 1; i < numero; i++) {
            if (numero % i == 0) {
                soma += i;
            }
        }
        if (soma == numero) {
            printf("%d\n", numero);
        }
    }
    return 0;
}
