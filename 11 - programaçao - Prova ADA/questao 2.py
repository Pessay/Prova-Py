dados_iniciais = input("Digite os dados O M L:")

dados_oml = []

#leitura dos dados do input

for dado in dados_iniciais:

    dados_oml.append(dado)
dados_oml2 = []
index2 = 0
index = 0
tamanho = len(dados_oml)
while(index <= (tamanho - 1)):
    if(dados_oml[index] != " "):
        if( index <= (tamanho-2) and dados_oml[index + 1] != " "):
            if((index+2)<=(tamanho-1) and dados_oml[index + 2] != " "):
                dados_oml2.append(dados_oml[index] + dados_oml[index + 1] + dados_oml[index + 2])
                #index2 = index2 + 1
                index = index + 4

            else:
                dados_oml2.append(dados_oml[index] + dados_oml[index + 1])
                index = index + 3
        else:
            dados_oml2.append(dados_oml[index])
            index = index + 2
    else:
        index = index + 1


#Testa se os numeros sao validos

dados_oml3 = []
for n in dados_oml2:
    dados_oml3.append(int(n))
dados_oml.clear()
dados_oml = dados_oml3

valid_test = 0
if(len(dados_oml) != 3 or not 1<= dados_oml[0] <= 100 or not 1<= dados_oml[1] <= 5 or not 2<=dados_oml[2]<=5  ):
    print("números inválidos ou fora do limite do enunciado!!")
    quit()
else:
    print("entrada:", dados_oml)

objetos = dados_oml[0]
maximo = dados_oml[1]
lotes = dados_oml[2]
index3 = 0
index4 = 0
index5 = 0
lista_resultado = [objetos]


index5= 0
index4 = 0
index3 = 0
while(max(lista_resultado) > maximo):
    if(index4<len(lista_resultado) and lista_resultado[index4] > maximo):
        resto_divisao = lista_resultado[index4]%lotes
        divisao = lista_resultado[index4]//lotes
        if(resto_divisao !=1):
            del lista_resultado[index4]
            while(index5 != lotes):
                lista_resultado.append(divisao)
                index5 = index5 + 1
            index5 = 0


        else:
            del lista_resultado[index4]
            while (index3 != lotes - 1):
                lista_resultado.append(divisao)
                index3 = index3 + 1
            index3 = 0
            a = divisao + 1
            lista_resultado.append(a)


    else:
        if(max(lista_resultado) > maximo and index4<len(lista_resultado) ):
            index4 = index4 + 1






print("tamanho dos lotes", lista_resultado)
print("total de lotes:", len(lista_resultado))

sair = input("digite algo para sair:" )