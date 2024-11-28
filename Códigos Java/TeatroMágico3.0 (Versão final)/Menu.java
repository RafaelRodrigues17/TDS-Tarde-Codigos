import java.util.Scanner;

public class Menu {

    public static void mostrarMenu() {
        System.out.println("\nBem-vindo ao Teatro Mágico! Por favor, escolha uma das opções a seguir:\n");
        System.out.println("1. Mostrar todos os assentos");
        System.out.println("2. Comprar assento");
        System.out.println("3. Liberar assento");
        System.out.println("4. Mostrar os logs");
        System.out.println("5. Sair");
        System.out.println("6. Exibir lucros do teatro");
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
            if (Pagamentos.realizarPagamento()) {
            System.out.println("Ingresso vendido com sucesso!");
            } else {
               System.out.println("Venda cancelada devido a falha no pagamento.");
               TeatroMagico.liberarIngresso(teatro, andar, coluna, linha); // Libera o assento caso falhe.
               }
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
                case 6:
                Pagamentos.exibirLucros();
                break;
        }
    }
}
