import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class CadastroSistema {
    private Set<String> cpfs;
    private Set<String> rgs;
    private Set<String> nomesUsuarios;

    public CadastroSistema() {
        cpfs = new HashSet<>();
        rgs = new HashSet<>();
        nomesUsuarios = new HashSet<>();
    }

    public void cadastrarPessoa() {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Nome Completo: ");
        String nomeCompleto = scanner.nextLine();

        String cpf;
        while (true) {
            System.out.print("CPF: ");
            cpf = scanner.nextLine();
            if (cpfs.contains(cpf)) {
                System.out.println("CPF já cadastrado! Tente novamente.");
            } else {
                cpfs.add(cpf);
                break;
            }
        }

        System.out.print("Telefone: ");
        String telefone = scanner.nextLine();

        String rg;
        while (true) {
            System.out.print("RG: ");
            rg = scanner.nextLine();
            if (rgs.contains(rg)) {
                System.out.println("RG já cadastrado! Tente novamente.");
            } else {
                rgs.add(rg);
                break;
            }
        }

        System.out.print("Email: ");
        String email = scanner.nextLine();

        System.out.print("Gênero: ");
        String genero = scanner.nextLine();

        System.out.print("Estado Civil: ");
        String estadoCivil = scanner.nextLine();

        System.out.print("Endereço: ");
        String endereco = scanner.nextLine();

        System.out.print("Nome da Mãe: ");
        String nomeMae = scanner.nextLine();

        String nomeUsuario;
        while (true) {
            System.out.print("Nome de Usuário: ");
            nomeUsuario = scanner.nextLine();
            if (nomesUsuarios.contains(nomeUsuario)) {
                System.out.println("Nome de usuário já cadastrado! Tente novamente.");
            } else {
                nomesUsuarios.add(nomeUsuario);
                break;
            }
        }

        System.out.print("Senha: ");
        String senha = scanner.nextLine();

        Pessoa pessoa = new Pessoa(nomeCompleto, cpf, telefone, rg, email, genero, estadoCivil, endereco, nomeMae, nomeUsuario, senha);
        System.out.println("\nCadastro realizado com sucesso!");
        System.out.println(pessoa);
    }

    public static void main(String[] args) {
        CadastroSistema sistema = new CadastroSistema();
        Scanner scanner = new Scanner(System.in);

        while (true) {

            System.out.println("\nSistema de Cadastro");
            System.out.println("1. Cadastrar Nova Pessoa");
            System.out.println("2. Sair");
            System.out.print("Escolha uma opção: ");
            int opcao = scanner.nextInt();
            scanner.nextLine(); // Consumir a linha em branco

            if (opcao == 1) {
                sistema.cadastrarPessoa();
            } else if (opcao == 2) {
                System.out.println("Saindo do sistema...");
                break;
            } else {
                System.out.println("Opção inválida. Tente novamente.");
            }
        }
    }
}
