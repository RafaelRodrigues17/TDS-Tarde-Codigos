import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite seu peso em kg: ");
        double peso = scanner.nextDouble();

        System.out.print("Digite sua altura em metros: ");
        double altura = scanner.nextDouble();

        double imc = Calculo.calcularIMC(peso, altura);

        System.out.printf("Seu IMC é: %.2f%n", imc);
        System.out.println("Classificação: " + Calculo.classificarIMC(imc));

        scanner.close();
    }
}

