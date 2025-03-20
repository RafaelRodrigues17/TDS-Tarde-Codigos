from funcionarios import Funcionario

f1 = Funcionario("Rafael","Estudante", 5000)
f1.exibir_informacoes()
f1.cargo = "Estágiario"
f1.aplicar_aumento(10)
f1.exibir_informacoes()