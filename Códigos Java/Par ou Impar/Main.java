import java.util.Random;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        System.out.println("Bem-vindo ao jogo de Par ou Ímpar!");

        // Escolha do jogador
        System.out.print("Escolha um número : ");
        int jogadorNumero = scanner.nextInt();

        System.out.print("Você escolhe Par ou Ímpar? (p/i): ");
        char escolha = scanner.next().charAt(0);

        // Número aleatório do computador
        int computadorNumero = random.nextInt(11);

        System.out.println("Você escolheu: " + jogadorNumero);
        System.out.println("Número do computador: " + computadorNumero);

        int soma = jogadorNumero + computadorNumero;
        boolean isPar = (soma % 2 == 0);

        System.out.println("Soma: " + soma);
        System.out.println("Resultado: " + (isPar ? "Par" : "Ímpar"));

        // Verifica quem ganhou
        if ((escolha == 'p' && isPar) || (escolha == 'i' && !isPar)) {
            System.out.println("Você venceu!");
        } else {
            System.out.println("Você perdeu!");
        }

        scanner.close();
    }
}
