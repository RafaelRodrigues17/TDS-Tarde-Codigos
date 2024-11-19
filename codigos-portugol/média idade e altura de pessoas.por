programa
{
	
	funcao inicio()
	{
	cadeia N [10] 
	inteiro I [10], x
	real A [10], media, soma = 0, porcent = 0, cont = 0

	escreva("Quantas pessoas você irá analisar ? ")
	leia(x)
	
	para (inteiro i = 0; i < x; i++){
	      escreva("Qual o ", i+1, "° nome ? ")
	      leia(N [i])
	      escreva("Qual a ", i+1, "° idade ? ")
	      leia(I [i])
	      escreva("Qual a ", i+1, "° altura ?" )
	      leia(A [i])
	      soma = soma + A[i]
	      
	}
	media = soma / x
	escreva("\nMédia das Alturas: ", media, "\n")

	para(inteiro i = 0; i < x; i++){
		se (I[i] < 16){
			escreva("\n", N[i])
			cont = cont + 1
			porcent = (cont/x) * 100
		}

	}
	escreva("\n A porcentagem de pessoas com menos de 16 anos é: ", porcent, "%")
}
	
}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 725; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */