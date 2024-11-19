// Classe base Veiculo
public class Veiculo {
    private String marca;
    private int velocidadeMaxima;

    // Construtor
    public Veiculo(String marca, int velocidadeMaxima) {
        this.marca = marca;
        this.velocidadeMaxima = velocidadeMaxima;
    }

    // Método para exibir detalhes
    public void exibirDetalhes() {
        System.out.println("Marca: " + marca);
        System.out.println("Velocidade Máxima: " + velocidadeMaxima + " km/h");
    }
}
