public class Main {
    public static void main(String[] args) {

        ContaCorrente minhaconta = new ContaCorrente(600.0, 50.0, 0.05);
        ContaCorrente minhaconta2 = new ContaCorrente(600.0, 250.0, 0.05);
        ContaPoupanca conta1 = new ContaPoupanca(600.0, 250.0, 0.08);
        ContaPoupanca conta2 = new ContaPoupanca(600.0, 250.0, 0.08);

        minhaconta.sacar();
        minhaconta2.depositar();
        conta1.sacar();
        conta2.depositar();
    }
}