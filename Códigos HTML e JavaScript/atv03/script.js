function calcular(){
    var numero1 = parseFloat(document.getElementById("num1").value)
    var numero2 = parseFloat(document.getElementById("num2").value)
    var operador = document.getElementById("operador").value

    switch (operador) {
        case "+": 
            resultado = numero1 + numero2
            break;
        case "-":
            resultado = numero1 - numero2
            break;
        case "*":
            resultado = numero1 * numero2
            break;
        case "/":
            if(numero2 !== 0){
                resultado = numero1 / numero2
            }else{
                resultado = "Erro: Divisão por 0 não existe"
            }
            break;
 
        default:
            resultado = " Operador inválido"          
    }
    document.getElementById("resultado").textContent = resultado
}
