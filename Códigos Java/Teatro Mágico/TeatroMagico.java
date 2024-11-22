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
        if (andar < 1 || andar > 3 || coluna < 1 || linha < 1) {
            return false;
        }
        int andarIndex = andar - 1;
        int linhaIndex = linha - 1;
        int colunaIndex = coluna - 1;

        if (teatro[andarIndex][linhaIndex][colunaIndex].equals("Livre")) {
            teatro[andarIndex][linhaIndex][colunaIndex] = "Vendido";

            registrarLog("Vendido", andar, coluna, linha);
            return true;
        }
        return false;
    }

    public static boolean liberarIngresso(String[][][] teatro, int andar, int coluna, int linha) {
        if (andar < 1 || andar > 3 || coluna < 1 || linha < 1) {
            return false;
        }
        int andarIndex = andar - 1;
        int linhaIndex = linha - 1;
        int colunaIndex = coluna - 1;

        if (teatro[andarIndex][linhaIndex][colunaIndex].equals("Vendido")) {
            teatro[andarIndex][linhaIndex][colunaIndex] = "Livre";

            registrarLog("Livre", andar, coluna, linha);
            return true;
        }
        return false;
    }

    public static void exibirAssentos(String[][][] teatro) {
        for (int andar = 0; andar < teatro.length; andar++) {
            for (int linha = 0; linha < teatro[andar].length; linha++) {
                for (int coluna = 0; coluna < teatro[andar][linha].length; coluna++) {
                    String status = teatro[andar][linha][coluna];
                    System.out.println("Andar " + (andar + 1) + " - Coluna " + (coluna + 1) + " - Linha " + (linha + 1) + " - Status: " + status);
                }
            }
        }
    }

    public static void registrarLog(String status, int andar, int coluna, int linha) {
        if (logIndex < logs.length) {
            String log = "Assento: Andar " + andar + " - Coluna " + coluna + " - Linha " + linha
                    + " - Status: " + status;
            logs[logIndex++] = log;
        } else {
            System.out.println("Limite de logs atingido.");
        }
    }

    public static void mostrarLogs() {
        if (logIndex == 0) {
            System.out.println("Nenhum assento vendido foi registrado.");
        } else {
            for (int i = 0; i < logIndex; i++) {
                System.out.println(logs[i]);
            }
        }
    }
}
