programa
{
    inclua biblioteca Matematica
	
    real a,b,c,x1,x2, delta, b2
    funcao inicio()
    {
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
            escreva("Impossível Calcular", "\n") 
        }
        senao
        {
        x1 = -b + (Matematica.raiz(delta, 2)) / (2*a)
        x2 = -b - (Matematica.raiz(delta, 2)) / (2*a)
        escreva("X1 = ", x1, "\n")
        escreva("X2 = ", x2, "\n")
        }
    }
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 15; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */