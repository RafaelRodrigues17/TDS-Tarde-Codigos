import java.util.Scanner;

public class ReajusteCombustivel {

    public static float reajusteEtanol(float valor, float reajuste) {
        return valor + reajuste;
    }
    public static float reajusteGasolina(float valor, float reajuste) {
        return valor + reajuste;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        float valor1, valor2, reajuste, valorTotal;
        String tipo;

        System.out.print("Informe o valor atual da gasolina: ");
        valor1 = scanner.nextFloat();

        System.out.print("Informe o valor atual do etanol: ");
        valor2 = scanner.nextFloat();

        System.out.print("Informe qual o valor do reajuste: ");
        reajuste = scanner.nextFloat();

        System.out.print("Informe qual combustível vai ser reajustado (etanol ou gasolina): ");
        tipo = scanner.next();

        // Lógica de reajuste
        if (tipo.equalsIgnoreCase("etanol")) {
            valorTotal = reajusteEtanol(valor2, reajuste);
            valor1 = valor1 + (valorTotal * 0.27); 
            System.out.printf("Valor do Etanol: %.2f\n", valorTotal);
            System.out.printf("Valor da Gasolina: %.2f\n", valor1);
        } else {
            valorTotal = reajusteGasolina(valor1, reajuste);
            System.out.printf("Valor do Etanol: %.2f\n", valor2);
            System.out.printf("Valor da Gasolina: %.2f\n", valorTotal);
        }

        scanner.close();
    }
}

