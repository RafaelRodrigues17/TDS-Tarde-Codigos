import java.util.Scanner;

public class SistemaDeNotas {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        double nota, soma = 0.0, media = 0.0;
        String login;
        int senha, n;

      
        System.out.println("Digite seu login, somente letras: ");
        login = scanner.nextLine();

       
        System.out.println("Digite sua senha, somente números: ");
        senha = scanner.nextInt();
        scanner.nextLine(); 

      
        if (login.equals("Rafael") && senha == 123456) {
            System.out.println("Acesso foi feito com sucesso!");

          
            System.out.println("Informe quantas notas você deseja informar: ");
            n = scanner.nextInt();

            
            for (int i = 0; i < n; i++) {
                System.out.println("Informe a " + (i + 1) + "° nota: ");
                nota = scanner.nextDouble();

                while (nota < 0.0 || nota > 10.0) {
                    System.out.println("Nota inválida! Informe uma nota entre 0 e 10.");
                    nota = scanner.nextDouble();
                }

                soma += nota;
            }

           
            media = Math.round((soma / n) * 100.0) / 100.0;
            System.out.println("A média das notas é: " + media);
        } else {
            System.out.println("Acesso negado");
        }

        scanner.close();
    }
}
