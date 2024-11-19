programa {

  funcao real prazo_3_dias(real valor_total){
  
    retorne valor_total + 25.00
  }
  funcao real prazo_5_dias(real valor_total){
  
    retorne valor_total + 20.00
  }
  funcao real prazo_7_dias(real valor_total){
  
    retorne valor_total + 15.00
  }
  funcao real prazo_10_dias(real valor_total){
  
    retorne valor_total + 10.00
  }

    funcao inicio (){
    real valor_total_venda, retorno_valor_a_pagar
    inteiro prazo_entrega

    escreva("Informe o valor do pedido: ")
    leia(valor_total_venda)
    faca{ 
      escreva("Informe o prazo da entrega informado pelo cliente: ")
      leia(prazo_entrega)

       }enquanto (prazo_entrega != 3 e prazo_entrega != 5 e prazo_entrega != 7 e prazo_entrega != 10 )

        se (prazo_entrega == 3){
          retorno_valor_a_pagar = prazo_3_dias (valor_total_venda)
          escreva ("Valor total a pagar com prazo de 3 dias úteis: ",retorno_valor_a_pagar)
        }
        se(prazo_entrega == 5){
          retorno_valor_a_pagar = prazo_5_dias (valor_total_venda)
          escreva ("Valor total a pagar com prazo de 5 dias úteis: ",retorno_valor_a_pagar)
        }
        se(prazo_entrega == 7){
          retorno_valor_a_pagar = prazo_7_dias (valor_total_venda)
          escreva ("Valor total a pagar com prazo de 7 dias úteis: ",retorno_valor_a_pagar)
        }
        se (prazo_entrega == 10){
          retorno_valor_a_pagar = prazo_10_dias (valor_total_venda)
          escreva ("Valor total a pagar com prazo de 3 dias úteis: ",retorno_valor_a_pagar)
    
    }





  
  
  
  }



 }

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 1568; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */