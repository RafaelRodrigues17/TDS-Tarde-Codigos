import java.text.SimpleDateFormat;
import java.util.Date;

public class Erro {

    public static void registrarErro(String codigoErro, String descricaoErro) {
        String timestamp = new SimpleDateFormat("dd-MM-yyyy HH:mm:ss").format(new Date());
        String log = "ERRO: " + descricaoErro + " - Código: " + codigoErro + " - Data: " + timestamp;

        if (TeatroMagico.logIndex < TeatroMagico.logs.length) {
            TeatroMagico.logs[TeatroMagico.logIndex++] = log;
        } else {
            System.out.println(" ");
        }
    }

    public static void andarInvalido() {
        System.out.println("Erro: Andar inválido.");
        registrarErro("ERR0035", "Andar inválido");
    }

    public static void colunaInvalida() {
        System.out.println("Erro: Coluna inválida.");
        registrarErro("ERR0045", "Coluna inválida");
    }

    public static void linhaInvalida() {
        System.out.println("Erro: Linha inválida.");
        registrarErro("ERR0055", "Linha inválida");
    }

    public static void cadeiraJaComprada() {
        System.out.println("Erro: Cadeira já comprada.");
        registrarErro("ERR0015", "Compra de cadeira já comprada");
    }

    public static void desistenciaCadeiraLivre() {
        System.out.println("Erro: Tentativa de desistência de cadeira livre.");
        registrarErro("ERR0025", "Desistência de cadeira livre");
    }
}
