programa{

    funcao real calcularPorcentagem(){
    real numero = 30.0, porcentagem = 20.0, resultado
    resultado = (numero * (porcentagem/100))
    retorne resultado
    }
    funcao inicio() {
    real porcentagemCalculada
    porcentagemCalculada = calcularPorcentagem()
    escreva("A porcentagem calculada foi: ", porcentagemCalculada)
    }
}
   