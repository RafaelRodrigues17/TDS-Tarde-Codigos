public class AdivinhaNumero {
    public static void main(String[] args) {
        NumeroAleatorio numeroAleatorio = new NumeroAleatorio();
        EntradaUsuario entradaUsuario = new EntradaUsuario();
        int palpite = 0;

        System.out.println("Bem-vindo ao jogo de adivinhação!");
        System.out.println("Eu escolhi um número entre 1 e 100. Tente adivinhá-lo!");

        while (palpite != numeroAleatorio.getNumero()) {
            palpite = entradaUsuario.obterPalpite();

            if (palpite < numeroAleatorio.getNumero()) {
                System.out.println("Muito baixo! Tente novamente.");
            } else if (palpite > numeroAleatorio.getNumero()) {
                System.out.println("Muito alto! Tente novamente.");
            } else {
                System.out.println("Parabéns! Você adivinhou o número!");
            }
        }

        entradaUsuario.fechar();
    }
}
