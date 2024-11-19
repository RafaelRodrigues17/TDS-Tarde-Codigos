import java.util.Scanner;

public class EntradaUsuario {
    private Scanner scanner;

    public EntradaUsuario() {
        this.scanner = new Scanner(System.in);
    }

    public int obterPalpite() {
        System.out.print("Digite seu palpite: ");
        return scanner.nextInt();
    }

    public void fechar() {
        scanner.close();
    }
}
