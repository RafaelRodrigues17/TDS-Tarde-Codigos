function calcular(){
    var num01 = parseFloat(document.getElementById("num01")).value
    var num02 = parseFloat(document.getElementById("num02")).value
    var resposta = document.getElementById("resultado")
    resposta.textContent = (num01 / (num02 * num02)).toFixed(2)
}