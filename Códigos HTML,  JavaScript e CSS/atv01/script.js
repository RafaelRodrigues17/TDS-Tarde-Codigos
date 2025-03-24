function soma() {
    var numero1 = document.getElementById("number1").valueAsNumber
    var numero2 = parseFloat(document.getElementById("number2").value)
    var resposta = document.getElementById("respSoma")
    resposta.textContent = numero1 + numero2
    console.log(numero1, numero2, resposta)
}

function sub() {
    var numero1 = document.getElementById("number3").valueAsNumber
    var numero2 = parseFloat(document.getElementById("number4").value)
    var resposta = document.getElementById("respSub")
    resposta.textContent = numero1 - numero2
    console.log(numero1, numero2, resposta)
}

function multi() {
    var numero1 = document.getElementById("number5").valueAsNumber
    var numero2 = parseFloat(document.getElementById("number6").value)
    var resposta = document.getElementById("respMulti")
    resposta.textContent = numero1 * numero2
    console.log(numero1, numero2, resposta)
}