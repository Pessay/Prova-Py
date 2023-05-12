import re

numeros_recebidos = input("hobbit digite os números aqui: ")

numeros = []

for numero in numeros_recebidos:
    numeros.append(numero)


lista_tratamento_input = []
j=0
while (j < len(numeros)):
    for s in re.findall(r'\d+', numeros[j]):
        lista_tratamento_input.append(int(s))
    j = j + 1
numeros=lista_tratamento_input


del numeros[0]
i=0
j=0

index_gravar_sequencias = 0
sequencias = []
tamanho = len(numeros)
for x in range (tamanho):  #cria (len-1) listas vazias dentro da lista sequencias
    sequencias.append([])

#preenche o primeiro item de cada lista dentro de "sequencia" com um dos digitos recebidos pelo hobbit
while(j < tamanho):
    sequencias[j].append(numeros[j])
    j = j + 1


j=0
#cria todas as sequencias(crescentes) possiveis
while(index_gravar_sequencias < (tamanho)):
    while(i<tamanho):
        if(i+1 < tamanho and numeros[i+1] > max(sequencias[j])):
            sequencias[j].append(numeros[i+1])
            i = i+1

        else:
            i = i + 1

    j = j + 1
    i = j

    index_gravar_sequencias = index_gravar_sequencias+1

print("Sequencias crescentes possíveis: ", sequencias)
sequencias.sort(key=len)
sequencias.reverse()
print("Maior sequencia possível: ",sequencias[0])

sair = input("digite algo para sair:" )