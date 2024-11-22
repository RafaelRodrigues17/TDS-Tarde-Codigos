programa
{
	inclua biblioteca Matematica --> M
	
	funcao inicio()
	{
	    inteiro cont,contador = 0
	    real nota,soma = 0.0,media

	    para(cont = 1; cont <= 3; cont ++){

         escreva(" Informe a ",cont, "° nota: ")
         leia(nota)
         soma = soma + nota
         contador ++
	    }
	    
	    media = soma / contador
	    escreva(" Sua média foi: ")
	    escreva(media)

	    se (media < 3.0){
	    	    escreva("reprovado")
	    }
	    senao se (media < 7.0){
	         escreva("recuperação")
	    }
	    senao{
	    	    escreva(" ,aprovado. ")
	    }

	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 556; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */