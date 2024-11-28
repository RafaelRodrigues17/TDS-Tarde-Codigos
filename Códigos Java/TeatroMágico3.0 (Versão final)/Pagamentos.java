import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;

public class Pagamentos {

    private static double lucros = 0;

    public static boolean realizarPagamento() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("\nEscolha o método de pagamento:");
        System.out.println("1. PIX");
        System.out.println("2. Cartão de Débito");
        System.out.println("3. Cartão de Crédito");
        System.out.println("4. Dinheiro");

        int opcao = scanner.nextInt();
        String metodoPagamento = "";

        switch (opcao) {
            case 1:
                metodoPagamento = "PIX";
                break;
            case 2:
                metodoPagamento = "Cartão de Débito";
                break;
            case 3:
                metodoPagamento = "Cartão de Crédito";
                break;
            case 4:
                metodoPagamento = "Dinheiro";
                break;
            default:
                System.out.println("Opção inválida! Tente novamente.");
                return false;
        }

        registrarPagamento(metodoPagamento);
        lucros += 20; // Cada ingresso custa 20 reais.
        return true;
    }

    private static void registrarPagamento(String metodo) {
        String timestamp = new SimpleDateFormat("dd-MM-yyyy HH:mm:ss").format(new Date());
        String log = "Pagamento realizado: Método: " + metodo + " - Valor: R$ 20,00 - Data: " + timestamp;

        if (TeatroMagico.logIndex < TeatroMagico.logs.length) {
            TeatroMagico.logs[TeatroMagico.logIndex++] = log;
        }

        System.out.println("Pagamento realizado com sucesso via " + metodo + "!");
    }

    public static void exibirLucros() {
        System.out.println("\nLucros totais do Teatro: R$ " + lucros);
    }
}
