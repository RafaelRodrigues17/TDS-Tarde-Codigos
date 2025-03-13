#for i in range(1,11):
#   print(i)
    
lista = [1,2,3.10,"text", True]
lista.append(100)

#for i in lista:
#print(i)

dicionario ={
    "nome": "Rafael",
    "idade": "18",
    "cidade" : "Curitiba"
}
dicionario_2 = dict(nome="Rafael",idade="18",cidade="Curitiba")

for i in dicionario:
    print(i, "= " ,dicionario[i])
    
for i in dicionario.values():
    print(i)
    
lista1 = []
lista2 = []

for chave, valor in dicionario.items():
    lista1.append(chave)
    lista2.append(valor)

print(lista1)
print(lista2)    
    