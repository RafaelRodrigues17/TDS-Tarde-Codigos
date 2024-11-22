public class ContaCorrente extends ContaBancaria{

    public Double taxaOperacao;
    public ContaCorrente(Double saldo, Double valor, Double taxaOperacao){
        super(saldo, valor);
        this.taxaOperacao = taxaOperacao;
    }
    public Double sacar(){
        Double resultado = getSaldo() - (getValor() + (getValor() * taxaOperacao));
        mostrar(resultado);
        return 0.0;
    }
    public Double depositar(){
        Double resultado = getSaldo() + (getValor() - (getValor() * taxaOperacao));
        mostrar(resultado);
        return 0.0;
    }
    public void mostrar(Double resultado){
        System.out.println("O valor restante no banco é de: "+ resultado);
    }
}
