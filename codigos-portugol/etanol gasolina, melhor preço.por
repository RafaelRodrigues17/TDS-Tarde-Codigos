programa
{
     real gasolina, etanol, resultado
     
     funcao dividir (){
     	escreva("Informe o preço do etanol: ")
     	leia(etanol)
     	escreva("Informe o preço da gasolina: ")
     	leia(gasolina)
     	resultado = etanol / gasolina
     	escreva("O resultado é: ", resultado, "\n")
     	

      se(resultado <= 0.7){
   		escreva("Etanol é a melhor opção")
      } senao{
      	escreva("Gasolina é a melhor opção")

      }
      
      }
      
      funcao inicio()
{
      dividir()
}
      

}


      



/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 280; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */