public class Main {
    public static void main(String[] args){

        int vetor[] = {2,3,2,5,7,5,4,8,9,1};
        boolean vetorB[] = new boolean[10];

        for (int i = 0; i < vetor.length; i++) {
            for(int j = 0; j < vetor.length; j++) {

                if (vetor[i] == vetor[j] && i != j) {
                    vetorB[j] = true;

                }
            }
        }
        for (int i = 0; i < vetor.length; i++) {
            System.out.println(i+" | "+ vetor[i]+" | " +vetorB[i]);
        }

    }

}