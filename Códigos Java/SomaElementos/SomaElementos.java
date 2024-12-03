import java.util.ArrayList;

public class SomaElementos {
    public static void main(String[] args) {
        ArrayList<Double> numeros = new ArrayList<>();
        numeros.add(3.5);
        numeros.add(7.2);
        numeros.add(1.8);
        numeros.add(4.6);
        numeros.add(9.3);

        double soma = 0;
        for (double numero : numeros) {
            soma += numero;
        }

        System.out.println("A soma de todos os números é: " + soma);
    }
}
