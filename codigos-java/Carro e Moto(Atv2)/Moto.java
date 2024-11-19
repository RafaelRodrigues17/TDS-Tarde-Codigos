// Subclasse Moto
public class Moto extends Veiculo {
    private int cilindradas;

    // Construtor
    public Moto(String marca, int velocidadeMaxima, int cilindradas) {
        super(marca, velocidadeMaxima);
        this.cilindradas = cilindradas;
    }

    // Sobrescrevendo o método exibirDetalhes
    public void exibirDetalhes() {
        super.exibirDetalhes();
        System.out.println("Cilindradas: " + cilindradas + " cc");
    }
}
