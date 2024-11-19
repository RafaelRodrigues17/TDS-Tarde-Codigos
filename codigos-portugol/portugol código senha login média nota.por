programa
{
	cadeia login
	real senha
	real nota1
	real nota2
	real nota3
	real media
	
	funcao inicio()
	{
	escreva("digite seu login, somente letras: \n")
	leia(login)
	escreva("digite sua senha, somente números \n")
	leia (senha)
	  
	se (login == "Rafael" e senha == 123456){
	   escreva ("Acesso foi feito com sucesso!:")
	
		escreva(" Agora vamos calcular a media de suas notas:")
	     escreva(" digete nota 1: ")
	     leia(nota1)
	     escreva(" digete nota 2: ")
	     leia(nota2)
		escreva(" digete nota 3: ")
	     leia(nota3)
	
	     media = (nota1 + nota2 + nota3) / 3
	
	     escreva(" a media de notas é:", media )
	     
		se (media < 3.0){ 
		escreva (" reprovado. ")}
		senao se (media < 7.0){
		escreva (" recuperação. ")}
		senao{
		escreva(" aprovado. ")
		   
		}
	}senao{
		escreva("acesso negado")
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
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */