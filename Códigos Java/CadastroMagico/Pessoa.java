public class Pessoa {
    private String nomeCompleto;
    private String cpf;
    private String telefone;
    private String rg;
    private String email;
    private String genero;
    private String estadoCivil;
    private String endereco;
    private String nomeMae;
    private String nomeUsuario;
    private String senha;


    public Pessoa(String nomeCompleto, String cpf, String telefone, String rg, String email, String genero,
                  String estadoCivil, String endereco, String nomeMae, String nomeUsuario, String senha) {
        this.nomeCompleto = nomeCompleto;
        this.cpf = cpf;
        this.telefone = telefone;
        this.rg = rg;
        this.email = email;
        this.genero = genero;
        this.estadoCivil = estadoCivil;
        this.endereco = endereco;
        this.nomeMae = nomeMae;
        this.nomeUsuario = nomeUsuario;
        this.senha = senha;
    }
    
    public String getCpf() {
        return cpf;
    }

    public String getRg() {
        return rg;
    }

    public String getNomeUsuario() {
        return nomeUsuario;
    }

    public String toString() {
        return "Nome Completo: " + nomeCompleto + "\n" +
                "CPF: " + cpf + "\n" +
                "Telefone: " + telefone + "\n" +
                "RG: " + rg + "\n" +
                "Email: " + email + "\n" +
                "Gênero: " + genero + "\n" +
                "Estado Civil: " + estadoCivil + "\n" +
                "Endereço: " + endereco + "\n" +
                "Nome da Mãe: " + nomeMae + "\n" +
                "Nome de Usuário: " + nomeUsuario + "\n" +
                "Senha: " + senha;
    }
}
