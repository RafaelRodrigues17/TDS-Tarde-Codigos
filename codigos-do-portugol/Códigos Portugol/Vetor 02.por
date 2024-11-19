programa
{
	
	funcao inicio()
	{
	real vet [10], soma = 0.0, media = 0.0
	inteiro i,n

	escreva("Quantos números você vai digitar ?: ")
	leia(n)

	para(i = 0; i < n; i ++){
     escreva("Digete ",i+1," um número: ")
     leia(vet[i])

     soma = soma + vet[i]
     media = soma/ n
		
	}
	escreva("\nValores = ")
	para(i = 0; i < n; i++){
		escreva(vet [i], " ")
	}
	     escreva("\nSoma: ",soma, "\nMedia = ",media)
	   
     	    	   
     }
}



/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 192; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */