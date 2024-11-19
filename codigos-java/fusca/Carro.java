public class Carro {
    private String modelo;
    private int ano;

    // Construtor
    public Carro(String modelo, int ano) {
        this.modelo = modelo;
        this.ano = ano;
    }
    public void exibirInfo() {
        System.out.println("Modelo: " + modelo + ", Ano: " + ano);
    }
}
