programa
{
	cadeia pais
	real CPF
	real passaporte
	
	funcao inicio()
	{
	escreva("digite seu país: ")
	leia(pais)
	escreva("Seu país é: ", pais, " \n")
	  
	se (pais == "Brasil" ou pais == "brasil"){
	   escreva ("digite seu CPF:")
	   leia(CPF)
	   escreva("O acesso foi feito com sucesso!")
	}
	senao se(pais != "Brasil" ou pais != "brasil"){
		escreva("digite seu Passaporte: ")
		leia(passaporte)
		escreva("O acesso foi feito com sucesso!")
	
	}

	}
} 
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 448; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */