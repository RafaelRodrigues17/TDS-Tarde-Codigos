programa
{
	funcao real reajusteEtanol(real &valor1, real reajuste){
		real resultado
		resultado = valor1 + reajuste
		retorne resultado
	}
	funcao real reajusteGasolina(real &valor1, real reajuste){
		real resultado1, resultado2
		resultado1 = valor1 + reajuste
		retorne resultado1
	}
	
	funcao inicio()
	{
		real valor1, valor2, reajuste, valorTotal
		cadeia tipo
		inteiro confirma
		escreva("Informe o valor atual da gasolina: ")
		leia(valor1)
		escreva("Informe o valor atual do etanol: ")
		leia(valor2)
		escreva("Informe qual o valor do reajuste: ")
		leia(reajuste)
		escreva("Informe qual combustível vai ser reajustado: ")
		leia(tipo)

		se (tipo == "etanol"){
			confirma = 1
			valorTotal = reajusteEtanol(valor2, reajuste)
			valor1 = valor1 + (valorTotal * 0.27)
			escreva("valor do Etanol: ", valorTotal)
			escreva("\nValor da Gasolina: ", valor1) 
		}
		senao {
			valorTotal = reajusteGasolina(valor1, reajuste)
			escreva("Valor do Etanol: ", valor2)
			escreva("\nValor da Gasolina: ", valorTotal)
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 596; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */