programa
{
	
	funcao inicio()
	{
	    inteiro vet [10],n,i

	    escreva("Informe quantos números deseja digitar: ")
	    leia(n)

	    para (i = 0; i < n; i ++){
	    	    escreva("Informe um número: ")
	    	    leia(vet [i])
	    
	   }
        escreva("\nNúmeros negativos:\n ")
        para (i = 0; i < n; i ++){
	    	    se (vet[i] < 0){
	    	        escreva(vet[i],"\n ")
	    	       
	    	   
	    }
         }
     }
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 435; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */