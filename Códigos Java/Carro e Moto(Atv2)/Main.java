// Classe principal
public class Main {
    public static void main(String[] args) {
        // Criando um objeto da classe Carro
        Carro carro = new Carro("Volkswagen", 183, 2);
        System.out.println("Detalhes do Carro:");
        carro.exibirDetalhes();

        System.out.println(); // Linha em branco para separar as saídas

        // Criando um objeto da classe Moto
        Moto moto = new Moto("Honda", 147, 160);
        System.out.println("Detalhes da Moto:");
        moto.exibirDetalhes();
    }
}
