public class ContaPoupanca extends ContaBancaria{
    public Double jurosMensais;
    public ContaPoupanca(Double saldo, Double valor, Double jurosMensais){
        super(saldo, valor);
        this.jurosMensais = jurosMensais;
    }
    public Double sacar(){
        Double resultado = (getSaldo() - getValor()) + (getSaldo() * jurosMensais);
        mostrar(resultado);
        return 0.0;
    }

    public Double depositar(){
        Double resultado = getSaldo() + (getValor() + (getValor() * jurosMensais));
        mostrar(resultado);
        return 0.0;
    }

    public void mostrar(Double resultado){
        System.out.println("O valor restante no banco é de: "+ resultado);
    }
}