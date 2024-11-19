programa
{
	inclua biblioteca Matematica --> M
	
	funcao inicio()
	{
		real nota, soma = 0.0, media = 0.0, senha
		cadeia login
		inteiro n

		escreva("digite seu login, somente letras: \n")
	     leia(login)
	     escreva("digite sua senha, somente números \n")
	     leia (senha)

	     se (login == "Rafael" e senha == 123456){
	     escreva ("Acesso foi feito com sucesso!\n")

		escreva("Informe quantas notas você deseja informar: ")
		leia(n)

		para(inteiro i = 0; i <n; i++){

		    escreva("Informe a ",i + 1, "° nota: ")// usuário irá informar a nota
		    leia(nota)
		    enquanto(nota < 0.0 ou nota > 10.0){ // vai verificar se a nota atende a condição
		    	     escreva("nota invalida!\nInforme uma nota entre 0 e 10\n")
		    	     leia(nota)
		    }
              soma = soma + nota
              media = M.arredondar(soma / n, 2)// utiliza a quantidade de notas que o usuário determinou
		}
	     escreva("A média das notas é; ", media)

	     }senao{
		    escreva("acesso negado")	

   }
}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 910; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */