public class Main {
    public static void main(String[] args) {

        Funcionario funcionario1 = new Funcionario("Serginho", 3000.00);
        System.out.println("Funcionário:");
        System.out.println("Nome: " + funcionario1.getNome());
        System.out.println("Salário Base: " + funcionario1.calcularSalario());

        Funcionario gerente = new Gerente("Rafael Rodrigues", 4200.00);
        System.out.println("\nGerente:");
        System.out.println("Nome: " + gerente.getNome());
        System.out.println("Salário com Bônus: " + gerente.calcularSalario());

        Funcionario vendedor = new Vendedor("Manuel Gomes", 3900.00);
        System.out.println("\nVendedor:");
        System.out.println("Nome: " + vendedor.getNome());
        System.out.println("Salário com Comissão: " + vendedor.calcularSalario());
    }
}
