import os

os.system("cls")

numero = 0

#while True:
#   numero = int(input("Digite um número: "))
#   if numero <0 :
#      print("Programa encerrado!")
#      break

pares = []
impares = []

for i in range(10):
    numero = int(input(f"\nDigite o {i+1}º número: "))

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
        
print("\nNúmeros pares:", pares)
print("Números ímpares:", impares,"\n") 
