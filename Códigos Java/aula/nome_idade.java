package aula;

import java.util.Scanner;

public class nome_idade {
    public static void main (String args[]){
        Scanner scanner = new Scanner(System.in);

        String nome;
        int idade;
        boolean casado;

        System.out.print("Digite seu nome: ");
        nome = scanner.nextLine();

        System.out.print("Digite sua idade: ");
        idade = scanner.nextInt();

        System.out.print("É casado: ");
        casado = scanner.nextBoolean();

        System.out.println("O "+nome+" mora sozinho em uma casa no meio da floresta e tem "+idade+" e se encontra "+casado);


    }

}

