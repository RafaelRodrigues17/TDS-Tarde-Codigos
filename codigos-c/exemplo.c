#include <stdio.h>
#include <string.h>

void limpar_entrada(){
    char c;
    while ((c = getchar ()) != '\n' && c != EOF){}
}

void ler_texto (char *buffer, int lenght) {
    fgets(buffer, lenght, stdin);
    strtok(buffer, "\n");
}

int main (){

    double salario1, salario2;
    char nome1[50], nome2[50];
   
    printf("Informe o nome da primeira pessoa: ");
    ler_texto(nome1, 50);
    printf("Informe o salario: ");
    scanf("%lf", &salario1);
    printf("Informe o segundo nome: ");
    limpar_entrada();
    ler_texto(nome2, 50);
    printf("Informe o segundo salario: ");
    scanf("%lf", &salario2);

    printf("%s possui um salario de %0.2lf e %s possui um salario de %0.2lf", nome1, salario1, nome2, salario2);



    return 0;
}