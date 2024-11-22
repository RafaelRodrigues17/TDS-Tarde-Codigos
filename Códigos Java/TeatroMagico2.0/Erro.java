import java.text.SimpleDateFormat;
import java.util.Date;

public class Erro {

    //salva o erro no log
    public static void registrarErro(String codigoErro, String descricaoErro) {
        String timestamp = new SimpleDateFormat("dd-MM-yyyy HH:mm:ss").format(new Date());
        String log = "ERRO: " + descricaoErro + " - Código: " + codigoErro + " - Data: " + timestamp;

        if (TeatroMagico.logIndex < TeatroMagico.logs.length) {
            TeatroMagico.logs[TeatroMagico.logIndex++] = log;
        } else {
            System.out.println("Limite de logs atingido.");
        }
    }

    public static void andarInvalido() {
        registrarErro("ERR0035", "Andar inválido");
    }

    public static void colunaInvalida() {
        registrarErro("ERR0045", "Coluna inválida");
    }

    public static void linhaInvalida() {
        registrarErro("ERR0055", "Linha inválida");
    }

    public static void poltronaInvalida() {
        registrarErro("ERR0005", "Poltrona inválida");
    }

    public static void cadeiraJaComprada() {
        registrarErro("ERR0015", "Compra de cadeira já comprada");
    }

    public static void desistenciaCadeiraLivre() {
        registrarErro("ERR0025", "Desistência de cadeira livre");
    }

    public static void inicializacaoSistema() {
        registrarErro("SYS0001", "Inicialização do sistema");
    }

    public static void encerramentoSistema() {
        registrarErro("SYS0010", "Encerramento do sistema");
    }
}
