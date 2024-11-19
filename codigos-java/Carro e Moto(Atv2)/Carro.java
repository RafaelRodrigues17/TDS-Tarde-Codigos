// Subclasse Carro
public class Carro extends Veiculo {
    private int numPortas;

    // Construtor
    public Carro(String marca, int velocidadeMaxima, int numPortas) {
        super(marca, velocidadeMaxima);
        this.numPortas = numPortas;
    }

    // Sobrescrevendo o método exibirDetalhes
    public void exibirDetalhes() {
        super.exibirDetalhes();
        System.out.println("Número de Portas: " + numPortas);
    }
}
