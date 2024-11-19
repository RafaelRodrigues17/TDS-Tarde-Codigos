import java.util.Random;

public class NumeroAleatorio {
    private int numero;

    public NumeroAleatorio() {
        Random random = new Random();
        this.numero = random.nextInt(100) + 1; // Gera número entre 1 e 100
    }

    public int getNumero() {
        return numero;
    }
}

