#Calcula a INTERSECÇÃO entre dois vetores
import random
vetorA = [0]*5
vetorB = [0]*3
n = len(vetorA)
m = len(vetorB)

def preencheVetor():
    for x in range(n):
        vetorA[x] = random.randint(0,10)
    print(vetorA)
    for x in range(m):
        vetorB[x] = random.randint(0,10)
    print(vetorB)

def intersecção():
    lista = []
    for x in range(n):
        for i in range(m):
            if vetorA[x] == vetorB[i]:
                lista.append(vetorB[i])
    print(f'Intersecção entre os dois vetores: {lista}')


preencheVetor()
intersecção()