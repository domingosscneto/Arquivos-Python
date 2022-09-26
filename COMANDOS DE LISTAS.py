listaCompras = ["cereal", "maça", "banana", "maça", "leite", "yogurt", "café"]

#conta quantos itens tem na lista
n = len(listaCompras)
print('1-', listaCompras)
print('2-', n)

#printa o item na posição 4 da lista
print('3-', listaCompras[4])

#soma os itens das posições indicadas da lista
soma = listaCompras[0]+listaCompras[4]
print('4-', soma)

#substitui um item da lista por um novo
listaCompras[5] = "nescal"
print('5-', listaCompras)

#insere um novo item na lista na posição indicada
listaCompras.insert(2, "mamão")
print('6-', listaCompras)

#deleta um item da lista
del listaCompras[6]
print('7-', listaCompras)

#acrescenta um novo item no final da lista
listaCompras.append("mel")
print('8-', listaCompras)

#coloca em ordem crescente os elementos da lista
listaCompras.sort()
print('9-', listaCompras)

#inverte a posição de todos os elementos
listaCompras.reverse()
print('10-', listaCompras)

#conta quantas vezes um elemento aparece na lista
c = listaCompras.count("maça")
print('11-', c)

#mostra o índice da primeira ocorrência de um determinado item
i = listaCompras.index("maça")
print('12-', i)

#cria uma nova lista ao somar os elementos de duas listas
lista1 = [1, 2, 3, 4, 5]
print("13- lista1", lista1)
novaLista = listaCompras+lista1
print('14-', novaLista)

#mostra o maior, menor ou soma todos os elementos da lista
maior = max(lista1)
menor = min(lista1)
somatoria = sum(lista1)
print('15-', menor)
print('16-', maior)
print('17-', somatoria)

#compara se as duas listas são iguais(retorna True ou False)
lista2 = [1, 2, 3, 4, 5]
print("18- lista2", lista2)
lista3 = [6, 7, 8, 9, 10]
print("19- lista3", lista3)
print("20- A lista1 e lista2 são iguais?", lista1==lista2)
print("21- A lista1 e lista3 são iguais?", lista1==lista3)

#percorre todos os elementos da lista com "while"
indice = 0
tamanho = len(lista3)
while indice < tamanho:
    print('22-', lista3[indice])
    indice=indice+1
print("23- fim")

#percorre todos os elementos da lista com "for"
for x in lista3:
    print('24-', x)
print("25- fim")

#percorre todos os elementos da lista com "for in range"
indicee = 0
for indicee in range(len(lista3)):
    print('26-', lista3[indicee])
print("27- fim")

#como printar uma matriz "bonitinha"
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(A)):
    for j in range(len(A[0])):
        print(A[i][j], '', end='')
    print()