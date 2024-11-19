public class Corsa extends Carro{

    public boolean rebaixado;
    public Corsa(String cor, String marca, String modelo, boolean rebaixado ){
        super(cor, marca, modelo);
        this.rebaixado = rebaixado;
    }

    public void imprimir(){
        System.out.println("A marca é " + getMarca() + " e ele é " + getCor());
        setCor("Roxo");
        System.out.println("A marca é " + getMarca() + " e ele é " + getCor());
    }


}

