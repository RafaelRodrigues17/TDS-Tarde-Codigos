import java.util.Scanner;

public class Menu {

    public static void mostrarMenu() {
        System.out.println("\nBem-vindo ao Teatro Mágico! Por favor, escolha uma das opções a seguir:\n");
        System.out.println("1. Mostrar todos os assentos");
        System.out.println("2. Comprar assento");
        System.out.println("3. Liberar assento");
        System.out.println("4. Mostrar os logs");
        System.out.println("5. Sair");
    }

    public static void opcoes(int opcao, Scanner scanner, String[][][] teatro) {
        switch (opcao) {
            case 1:
                TeatroMagico.exibirAssentos(teatro);
                break;
            case 2:
                System.out.print("Digite o andar: ");
                int andar = scanner.nextInt();
                System.out.print("Digite a coluna: ");
                int coluna = scanner.nextInt();
                System.out.print("Digite a linha: ");
                int linha = scanner.nextInt();
                if (TeatroMagico.venderIngresso(teatro, andar, coluna, linha)) {
                    System.out.println("Ingresso vendido com sucesso!");
                }
                break;
            case 3:
                System.out.print("Digite o andar: ");
                andar = scanner.nextInt();
                System.out.print("Digite a coluna: ");
                coluna = scanner.nextInt();
                System.out.print("Digite a linha: ");
                linha = scanner.nextInt();
                if (TeatroMagico.liberarIngresso(teatro, andar, coluna, linha)) {
                    System.out.println("Ingresso liberado com sucesso!");
                }
                break;
            case 4:
                TeatroMagico.mostrarLogs();
                break;
            case 5:
                System.out.println("Encerrando o sistema...");
                break;
            default:
                System.out.println("Opção inválida! Tente novamente.");
        }
    }
}
