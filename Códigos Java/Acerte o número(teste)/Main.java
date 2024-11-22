import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int num1, num2, total;

        System.out.println("Olá, vamos tentar encontrar o número secreto com uma soma? Duvido acertar! ");
        System.out.println("Digite o primeiro número: ");
        num1 = scanner.nextInt();

        System.out.println("Digite o segundo número: ");
        num2 = scanner.nextInt();

        total = num1 + num2;

        System.out.println("O resultado da soma é "+total);

        if (total == 34){
            System.out.println("Parabéns você encontrou o número secreto (34) !!!!!, Você é o cara. ");
        }
        else
            System.out.println("Não é o número secreto seu bobão!!! ");

    }
}