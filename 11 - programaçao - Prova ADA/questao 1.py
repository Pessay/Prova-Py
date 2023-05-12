import re

numeros_fornecidos = input("Digite os números: ")

lista_numeros = []
lista_numeros_agrupados = []

for numeros in numeros_fornecidos:
    lista_numeros.append(numeros.strip())

lista2 = []

j = 0
while (j < len(lista_numeros)):
    for s in re.findall(r'\d+', lista_numeros[j]):
        lista2.append(str(s))
    j = j + 1
lista_numeros = lista2
print("números fornecidos ", lista_numeros)
index_ln = 0
index_lna = 0
i = len(lista_numeros) - 1
i2 = len(lista_numeros) - 1

while(index_lna < len(lista_numeros)):
    while(i >= 0):
        if(i > index_ln):
            lista_numeros_agrupados.append(int(lista_numeros[index_ln] + lista_numeros[i]))
            lista_numeros_agrupados.append(int(lista_numeros[i] + lista_numeros[index_ln]))
            i = (i - 1)
        else:
            i = (i - 1)

    i = len(lista_numeros) - 1
    index_ln = index_ln + 1
    index_lna = index_lna + 1

sem_repetidos = {lista_numeros_agrupados[0]}

for numero in lista_numeros_agrupados:
    sem_repetidos.add(numero)

lista_final = []

for num in sem_repetidos:
    lista_final.append(num)

print("combinações: ", lista_final)

j=0
resultado = 0

while(j != len(lista_final)):
    resultado = resultado + lista_final[j]
    j = j + 1

print("resultado da soma: ", resultado)

sair = input("digite algo para sair:" )