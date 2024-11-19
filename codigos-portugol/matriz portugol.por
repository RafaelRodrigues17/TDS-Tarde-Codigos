programa
{    
     inteiro matriz [10][10],n,m,i,j
	
	funcao inicio()
	{
		escreva("Quantas linhas deseja digitar? ")
		leia(m)
		escreva("Quantas colunas deseja digitar? ")
		leia(n)

		para (i = 0; i < m; i++){
			para(j = 0; j < n; j++){
				escreva("Elemento [",i,",",j,"]: ")
				leia(matriz [i][j])
			}
		}
		para (i = 0; i < m; i++){
			para(j = 0; j < n; j++){
				escreva(matriz [i][j], " ")
		
		
	}
}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 36; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = {matriz, 3, 13, 6};
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */