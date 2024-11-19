import java.util.Random;
import java.util.Scanner;

    public class Jogo{
    private static final String[] opcoes = {"Pedra", "Papel", "Tesoura"};

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        System.out.println("Escolha: Pedra, Papel ou Tesoura:");
        String escolhaUsuario = scanner.nextLine().trim();

        int escolhaComputadorIndex = random.nextInt(3);
        String escolhaComputador = opcoes[escolhaComputadorIndex];

        System.out.println("Computador escolheu: " + escolhaComputador);
        String resultado = escolhaVencedor(escolhaUsuario, escolhaComputador);
        System.out.println(resultado);

        scanner.close();
    }

    public static String escolhaVencedor(String escolhaUsuario, String escolhaComputador) {
        if(escolhaUsuario.equalsIgnoreCase(escolhaComputador)) {
            return "Empate!";

        }else if((escolhaUsuario.equalsIgnoreCase("Pedra") && escolhaComputador.equals("Tesoura")) ||
                (escolhaUsuario.equalsIgnoreCase("Papel") && escolhaComputador.equals("Pedra")) ||
                (escolhaUsuario.equalsIgnoreCase("Tesoura") && escolhaComputador.equals("Papel"))) {

            return "Você Ganhou!";
        }else{
            return "Você Perdeu!";
        }
    }
}



