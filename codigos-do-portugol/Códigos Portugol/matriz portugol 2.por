programa
{    
     inteiro matriz1 [10][10], matriz2 [10][10], matriz3[10][10],n,m,i,j, soma = 0
	
	funcao inicio()
	{    escreva("Digete a primeira Matriz:\n")
		escreva("Quantas linhas deseja digitar? ")
		leia(m)
		escreva("Quantas colunas deseja digitar? ")
		leia(n)
		
		para (i = 0; i < m; i++){
			para(j = 0; j < n; j++){
				escreva("Elemento [",i,",",j,"]: ")
				leia(matriz1 [i][j])}
	     }
          para (i = 0; i < m; i++){
			para(j = 0; j < n; j++){
				escreva("Elemento [",i,",",j,"]: ")
				leia(matriz2 [i][j])
			}
		}
		para (i = 0; i < m; i++){
			para(j = 0; j < n; j++){
				
				matriz3[i][j] = matriz1[i][j] + matriz2[i][j]
				escreva(matriz3 [i][j], " ")
				
	     }
	     escreva("\n")
	     
          	
		
	}
}

}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 700; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */