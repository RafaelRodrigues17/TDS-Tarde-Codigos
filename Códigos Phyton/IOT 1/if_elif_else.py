numero = 10
numero2: int = "10.10"

numero=int(input("Digite um numero:"))

if numero > 10:
    print("numero", numero, "é maior que 10")
elif numero < 10:
    print(f"numero {numero} é menor que 10")
else:
    print(f"numero {numero} é 10")
    
print(f"numero2 ={numero2}")
    