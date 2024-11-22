import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Erro.inicializacaoSistema();  //inicialização do código e erros

        String[][][] teatro = new String[3][][];

        String[][] andar1 = new String[30][50];
        String[][] andar2 = new String[20][30];
        String[][] andar3 = new String[10][15];

        TeatroMagico.preencherAssentos(andar1);
        TeatroMagico.preencherAssentos(andar2);
        TeatroMagico.preencherAssentos(andar3);

        teatro[0] = andar1;
        teatro[1] = andar2;
        teatro[2] = andar3;

        Scanner scanner = new Scanner(System.in);

        while (true) {
            Menu.mostrarMenu();
            int opcao = scanner.nextInt();
            if (opcao == 5) {
                break;
            }
            Menu.opcoes(opcao, scanner, teatro);
        }

        //logs de erro vão ser mostrados
        TeatroMagico.mostrarLogs();
    }
}
