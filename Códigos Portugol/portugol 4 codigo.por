programa
{
	inteiro idade
	cadeia nome
	
	funcao inicio()
	{
	escreva("digite seu nome: ")
	leia(nome)
	escreva("Olá ", nome , ", seja bem vindo.\n")
	  
	escreva("Informe a sua idade atual: ")
	leia(idade)
	se (idade >= 18){
	   escreva ("Bem vindo ao site do Detran")
	}
	senao se(idade < 18){
		escreva("idade não corresponde, não sera possível acessar o site do detran")
		
	}

	}
} 
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 152; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */