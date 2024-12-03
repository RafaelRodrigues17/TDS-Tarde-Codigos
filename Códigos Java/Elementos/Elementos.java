import java.util.ArrayList;

public class Elementos {
    public static void main(String[] args) {
        ArrayList<Integer> numeros = new ArrayList<>();
        for (int i = 1; i <= 10; i++) {
            numeros.add(i);
        }

        boolean presenca5 = numeros.contains(5);
        System.out.println("5 está presente na lista? " + presenca5);

        int indice7 = numeros.indexOf(7);
        System.out.println("O índice do número 7 na lista é: " + indice7);

        boolean listaVazia = numeros.isEmpty();
        System.out.println("A lista está vazia? " + listaVazia);
    }
}
