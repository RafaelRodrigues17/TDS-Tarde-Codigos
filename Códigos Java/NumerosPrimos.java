public class NumerosPrimos {
    public static void main(String[]args){
        for (int i = 1; i <= 100; i++) {
            if (ePrimo(i)) {
                System.out.println(i + " - Sim (Primo)");
            } else {
                System.out.println(i + " - Não (Não é primo)");

            }
        }
    }
    public static boolean ePrimo(int numero) {
        if (numero <= 1) {
            return false;
        }
        for  (int i = 2; i <= Math.sqrt(numero); i++){
            if (numero % i == 0){
                return false;
            }
        }
        return true;
    }
}

