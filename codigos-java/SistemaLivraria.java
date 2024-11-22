import java.util.Scanner;

class Livro {
    String codigoBarras;
    String titulo;
    String autor;
    int anoPublicacao;
    int quantidade;
    float valorVenda;

    public Livro(String codigoBarras, String titulo, String autor, int anoPublicacao, int quantidade, float valorVenda) {
        this.codigoBarras = codigoBarras;
        this.titulo = titulo;
        this.autor = autor;
        this.anoPublicacao = anoPublicacao;
        this.quantidade = quantidade;
        this.valorVenda = valorVenda;
    }
}

public class SistemaLivraria {
    private static final int MAX_LIVROS = 100;
    private static Livro[] estoque = new Livro[MAX_LIVROS];
    private static int totalLivros = 0;
    private static Scanner scanner = new Scanner(System.in);

    public static void cadastrarLivro() {
        if (totalLivros >= MAX_LIVROS) {
            System.out.println("Estoque cheio!");
            return;
        }

        System.out.print("Código de barras: ");
        String codigoBarras = scanner.nextLine();

        System.out.print("Título: ");
        String titulo = scanner.nextLine();

        System.out.print("Autor: ");
        String autor = scanner.nextLine();

        System.out.print("Ano de publicação: ");
        int anoPublicacao = scanner.nextInt();

        System.out.print("Quantidade em estoque: ");
        int quantidade = scanner.nextInt();

        while (quantidade < 0) {
            System.out.print("Quantidade inválida! Insira novamente: ");
            quantidade = scanner.nextInt();
        }

        System.out.print("Valor de venda: ");
        float valorVenda = scanner.nextFloat();

        while (valorVenda < 0) {
            System.out.print("Valor inválido! Insira novamente: ");
            valorVenda = scanner.nextFloat();
        }
      
        scanner.nextLine(); 

        Livro livro = new Livro(codigoBarras, titulo, autor, anoPublicacao, quantidade, valorVenda);
        estoque[totalLivros++] = livro;

        System.out.println("Livro cadastrado com sucesso!");
    }

    public static void consultarLivro() {
        System.out.print("Digite o código de barras para consulta: ");
        String codigo = scanner.nextLine();

        for (int i = 0; i < totalLivros; i++) {
            if (estoque[i].codigoBarras.equals(codigo)) {
                System.out.println("Título: " + estoque[i].titulo);
                System.out.println("Autor: " + estoque[i].autor);
                System.out.println("Ano de publicação: " + estoque[i].anoPublicacao);
                System.out.println("Valor por unidade: " + estoque[i].valorVenda);
                System.out.println("Quantidade em estoque: " + estoque[i].quantidade);
                return;
            }
        }

        System.out.println("Livro não encontrado.");
    }

    public static void venderLivro() {
        float totalCompra = 0;

        while (true) {
            System.out.print("Digite o código de barras para vender (ou 'sair' para finalizar): ");
            String codigo = scanner.nextLine();

            if (codigo.equals("sair")) {
                break;
            }

            System.out.print("Quantidade a vender: ");
            int quantidadeVendida = scanner.nextInt();
            scanner.nextLine();  // Limpar o buffer

            for (int i = 0; i < totalLivros; i++) {
                if (estoque[i].codigoBarras.equals(codigo)) {
                    if (estoque[i].quantidade >= quantidadeVendida) {
                        estoque[i].quantidade -= quantidadeVendida;
                        totalCompra += quantidadeVendida * estoque[i].valorVenda;
                        System.out.println("Livro vendido: " + estoque[i].titulo + ", Unidades: " + quantidadeVendida + ", Valor unitário: " + estoque[i].valorVenda);
                    } else {
                        System.out.println("Quantidade insuficiente em estoque.");
                    }
                    break;
                }
            }
        }

        System.out.println("Valor total da compra: " + totalCompra);
    }

    public static void exibirEstoque() {
        System.out.println("Itens em estoque:");
        for (int i = 0; i < totalLivros; i++) {
            System.out.println("Código: " + estoque[i].codigoBarras + " | Título: " + estoque[i].titulo + " | Quantidade: " + estoque[i].quantidade + " | Preço: " + estoque[i].valorVenda);
        }
    }

    public static void main(String[] args) {
        int opcao;

        while (true) {
            System.out.println("\nMenu:");
            System.out.println("1. Cadastrar Livro");
            System.out.println("2. Consultar Livro");
            System.out.println("3. Vender Livro");
            System.out.println("4. Exibir Estoque");
            System.out.println("5. Sair");
            System.out.print("Escolha uma opção: ");
            opcao = scanner.nextInt();
            scanner.nextLine(); // Limpar o buffer

            switch (opcao) {
                case 1:
                    cadastrarLivro();
                    break;
                case 2:
                    consultarLivro();
                    break;
                case 3:
                    venderLivro();
                    break;
                case 4:
                    exibirEstoque();
                    break;
                case 5:
                    System.out.println("Saindo...");
                    return;
                default:
                    System.out.println("Opção inválida! Tente novamente.");
            }
        }
    }
}
