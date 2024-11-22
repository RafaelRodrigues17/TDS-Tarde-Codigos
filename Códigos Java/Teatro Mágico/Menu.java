import java.util.Scanner;

public class Menu {

    public static void mostrarMenu() {
        System.out.println("\nBem vindo ao Teatro Mágico! Por Favor escolha uma das opções a seguir:\n ");
        System.out.println("1. Mostrar todos os assentos");
        System.out.println("2. Comprar assento");
        System.out.println("3. Liberar assento");
        System.out.println("4. Mostrar assentos vendidos");
        System.out.println("5. Sair");
    }

    public static void opcoes(int opcao, Scanner scanner, String[][][] teatro) {
        if (opcao == 1) {
            TeatroMagico.exibirAssentos(teatro);
        } else if (opcao == 2) {
            System.out.print("Digite o andar: ");
            int andar = scanner.nextInt();
            System.out.print("Digite a coluna: ");
            int coluna = scanner.nextInt();
            System.out.print("Digite a linha: ");
            int linha = scanner.nextInt();
            if (TeatroMagico.venderIngresso(teatro, andar, coluna, linha)) {
                System.out.println("Ingresso vendido!");
            } else {
                System.out.println("Erro: Assento já vendido ou inválido.");
            }
        } else if (opcao == 3) {
            System.out.print("Digite o andar: ");
            int andar = scanner.nextInt();
            System.out.print("Digite a coluna: ");
            int coluna = scanner.nextInt();
            System.out.print("Digite a linha: ");
            int linha = scanner.nextInt();
            if (TeatroMagico.liberarIngresso(teatro, andar, coluna, linha)) {
                System.out.println("Ingresso liberado!");
            } else {
                System.out.println("Erro: Não foi possível liberar o assento, pois o mesmo ainda não foi vendido.");
            }
        } else if (opcao == 4) {
            TeatroMagico.mostrarLogs();
        } else if (opcao == 5) {
            System.out.println("Saindo...");
        } else {
            System.out.println("Opção inválida!");
        }
    }
}
