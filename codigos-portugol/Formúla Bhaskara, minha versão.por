programa
{
	inclua biblioteca Matematica
     real num1, num2, a,b,c,x1,x2, delta, b2

     funcao somar (){
     	escreva("Informe o primeiro número: ")
     	leia(num1)
     	escreva("Informe o segundo número: ")
     	leia(num2)
     	escreva("O resultado da soma é: ",num1 + num2, "\n")
     }
     funcao subtrair (){
     	escreva("Informe o primeiro número: ")
     	leia(num1)
     	escreva("Informe o segundo número: ")
     	leia(num2)
     	escreva("O resultado da subtração é: ",num1 - num2, "\n")
     	
     }
     funcao multiplicar (){
     	escreva("Informe o primeiro número: ")
     	leia(num1)
     	escreva("Informe o segundo número: ")
     	leia(num2)
     	escreva("O resultado da multiplicação é: ",num1 * num2, "\n")
     	
     }
     funcao dividir (){
     	escreva("Informe o primeiro número: ")
     	leia(num1)
     	escreva("Informe o segundo número: ")
     	leia(num2)

     	enquanto (num2 == 0){
     		escreva("Divisão Inválida, escolha outro número: ")
     		leia(num2)
     	}
     	escreva("O resultado da divisão é: ",num1 / num2, "\n")
     }	
     funcao Bhaskara(){
        escreva("Digite o valor de [a]", "\n")
        leia (a)
        escreva("Digite o valor de B ", "\n")
        leia (b)
        escreva("Digite o valor de [c]", "\n")
        leia (c)
        b2 = b*b
        delta = b2-(4*a*c)
        se(delta<0 ou (2*a)==0)
        {
            escreva("Calculo Inválido", "\n") 
        }
        senao
        {
        x1 = -b + (Matematica.raiz(delta, 2)) / (2*a)
        x2 = -b - (Matematica.raiz(delta, 2)) / (2*a)
        escreva("X1 = ", x1, "\n")
        escreva("X2 = ", x2, "\n")}

     }
	funcao calculadora (){
		inteiro opcao

		faca{
			escreva("Escolha uma opção\n")
			escreva("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Bhaskara\n6 - Sair\n")
			leia(opcao)
               escolha (opcao){
               	caso 1:
               	somar ()
               	pare
               	caso 2:
               	subtrair ()
               	pare
               	caso 3:
               	multiplicar ()
               	pare
               	caso 4:
               	dividir ()
               	pare
               	caso 5:
               	Bhaskara ()
               	pare
               	caso 6:
               	escreva("Saindo da calculadora\n")
               	pare
               	caso contrario:
               	escreva("Opção inválida!!\nInforme uma opção válida!")
               	
               }
			
		}enquanto(opcao != 0)
	}
	funcao inicio()
	{

	calculadora ()
	
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 2342; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */