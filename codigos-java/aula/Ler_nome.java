package aula;

import java.util.Scanner;

public class Ler_nome {
    public static void main (String args[]){
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite seu nome: ");
        String nome = scanner.nextLine();

        System.out.println("Seu nome é: "+nome);

    }

}

