import java.text.SimpleDateFormat;
import java.util.Date;

public class TeatroMagico {

    public static String[] logs = new String[100];
    public static int logIndex = 0;

    public static void preencherAssentos(String[][] andar) {
        for (int i = 0; i < andar.length; i++) {
            for (int j = 0; j < andar[i].length; j++) {
                andar[i][j] = "Livre";
            }
        }
    }

    public static boolean venderIngresso(String[][][] teatro, int andar, int coluna, int linha) {
        if (andar < 1 || andar > 3) {
            Erro.andarInvalido();
            return false;
        }
        if (linha < 1 || linha > teatro[andar - 1].length) {
            Erro.linhaInvalida();
            return false;
        }
        if (coluna < 1 || coluna > teatro[andar - 1][0].length) {
            Erro.colunaInvalida();
            return false;
        }

        if (teatro[andar - 1][linha - 1][coluna - 1] =="Vendido") {
            Erro.cadeiraJaComprada();
            return false;
        }

        teatro[andar - 1][linha - 1][coluna - 1] = "Vendido";
        registrarLog("Vendido", andar, coluna, linha);
        return true;
    }

    public static boolean liberarIngresso(String[][][] teatro, int andar, int coluna, int linha) {
        if (andar < 1 || andar > 3) {
            Erro.andarInvalido();
            return false;
        }
        if (linha < 1 || linha > teatro[andar - 1].length) {
            Erro.linhaInvalida();
            return false;
        }
        if (coluna < 1 || coluna > teatro[andar - 1][0].length) {
            Erro.colunaInvalida();
            return false;
        }

        if (teatro[andar - 1][linha - 1][coluna - 1] == "Livre") {
            Erro.desistenciaCadeiraLivre();
            return false;
        }

        teatro[andar - 1][linha - 1][coluna - 1] = "Livre";
        registrarLog("Livre", andar, coluna, linha);
        return true;
    }

    public static void mostrarLogs() {
        if (logIndex == 0) {
            System.out.println("Nenhum assento vendido foi registrado.");
        }else {
            for (int i = 0; i < logIndex; i++) {
                System.out.println(logs[i]);

            }
        }
    }
    public static void registrarLog(String status, int andar, int coluna, int linha) {
        if (logIndex < logs.length) {
            //data e hora atual
            String timestamp = new SimpleDateFormat("dd-MM-yyyy HH:mm:ss").format(new Date());
            String log = timestamp + " - Assento: A" + andar + " L" + linha + " I" + coluna + " - Status: " + status;
            logs[logIndex++] = log;
        } else {
            System.out.println("Limite de logs atingido.");
        }
    }
    public static void exibirAssentos(String[][][] teatro) {
        for (int andar = 0; andar < teatro.length; andar++) {
            for (int linha = 0; linha < teatro[andar].length; linha++) {
                for (int coluna = 0; coluna < teatro[andar][linha].length; coluna++) {
                    String status = teatro[andar][linha][coluna];

                    if (status.equals("Vendido")) {
                        System.out.print(" ---  ");
                    } else {
                        System.out.print("A" + (andar + 1) + " L" + (linha + 1) + " I" + (coluna + 1) + "  ");
                    }
                }
                System.out.println();
            }
        }
    }
}
