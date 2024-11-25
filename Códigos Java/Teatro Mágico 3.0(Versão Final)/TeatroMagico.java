import java.util.Scanner;
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

        if (teatro[andar - 1][linha - 1][coluna - 1].equals("Vendido")) {
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

    
}
