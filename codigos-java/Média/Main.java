import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        List<Double> valores = new ArrayList<>();

        System.out.println("Digite os números (ou 'sair' para calcular a média):");

        while (true) {
            String entrada = scanner.nextLine();

            if (entrada.equalsIgnoreCase("sair")) {
                break;
            }

            try {
                double numero = Double.parseDouble(entrada);
                valores.add(numero);
            } catch (NumberFormatException e) {
                System.out.println("Por favor, insira um número válido.");
            }
        }

        if (!valores.isEmpty()) {
            double soma = 0;
            for (double valor : valores) {
                soma += valor;
            }
            double media = soma / valores.size();
            System.out.printf("A média dos valores inseridos é: %.2f%n", media);
        } else {
            System.out.println("Nenhum valor foi inserido.");
        }

        scanner.close();
    }
}
