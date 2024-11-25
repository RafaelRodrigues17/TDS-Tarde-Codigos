import java.text.SimpleDateFormat;
import java.util.Date;

public class Sistema {

    public static void registrarEvento(String evento) {
        String timestamp = new SimpleDateFormat("dd-MM-yyyy HH:mm:ss").format(new Date());
        String log = "EVENTO: " + evento + " - Data: " + timestamp;

        if (TeatroMagico.logIndex < TeatroMagico.logs.length) {
            TeatroMagico.logs[TeatroMagico.logIndex++] = log;
        } else {
            System.out.println(" ");
        }
    }

    public static void inicializacaoSistema() {
        registrarEvento("Inicialização do sistema");
    }

    public static void encerramentoSistema() {
        registrarEvento("Encerramento do sistema");
    }
}
