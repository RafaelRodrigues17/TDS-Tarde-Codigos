public class Main {
    public static void main (String[] args){
        Pessoa pessoa1 = new Pessoa();
        Pessoa pessoa2 = new Pessoa();

        //pessoa1.nome = "Rafael";
        //pessoa1.idade = 17;

        //pessoa2.nome = "Ronaldo";
        //pessoa2.idade = 28;

        //pessoa1.informacoes();
        //System.out.println(pessoa1.nome);
        //pessoa2.informacoes();

        pessoa1.setNome("Rafael");
        pessoa1.setIdade(17);

        System.out.println("Nome: " + pessoa1.getNome() +"\nIdade: " + pessoa1.getIdade());
        

    }
}