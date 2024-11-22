import java.util.Scanner;

public class Fibonacci {
    public static int fibonacci(int n) {
        if (n <= 1) {
            return n;
        }
        int a = 0, b = 1, c;
        for (int i = 2; i <= n; i++) {
            c = a + b;
            a = b;
            b = c;
        }
        return b;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite o valor de n: ");
        int n = scanner.nextInt();

        if (n < 0) {
            System.out.println("O valor de n deve ser não-negativo.");
        } else {
            System.out.printf("Fibonacci(%d) = %d%n", n, fibonacci(n));
        }
        scanner.close();
    }
}
