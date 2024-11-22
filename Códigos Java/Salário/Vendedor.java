public class Vendedor extends Funcionario {
    public Vendedor(String nome, double salarioBase) {
        super(nome, salarioBase);
    }

    public double calcularSalario() {
        return super.calcularSalario() * 1.1;
    }
}
