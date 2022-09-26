#Calcula a INTERCALAÇÃO entre dois vetores
import random
vetorA = [0]*3
vetorB = [0]*3
vetorC = [0]*6
n = len(vetorA)
m = len(vetorB)
c = len(vetorC)

def preencheVetor():
    for x in range(n):
        vetorA[x] = random.randint(0,10)
    print(vetorA)
    for i in range(m):
        vetorB[i] = random.randint(0,10)
    print(vetorB)

def intercalaçãoVetor():
    vetorC = vetorA + vetorB
    vetorC.sort()
    print(vetorC)


preencheVetor()
intercalaçãoVetor()