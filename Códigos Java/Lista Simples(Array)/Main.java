import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {

        List<String> nomes = new ArrayList<>();
        nomes.add("Ana");
        nomes.add("Carlos");
        nomes.add("Fernanda");
        nomes.add("João");
        nomes.add("Mariana");

        System.out.println("Lista antes das modificações:");
        System.out.println(nomes);

        nomes.remove("João");

        for (int i = 0; i < nomes.size(); i++) {
            if (nomes.get(i).equals("Ana")) {
                nomes.set(i, new StringBuilder(nomes.get(i)).reverse().toString());
            }
        }
        System.out.println("\nLista depois das modificações:");
        System.out.println(nomes);
    }
}
