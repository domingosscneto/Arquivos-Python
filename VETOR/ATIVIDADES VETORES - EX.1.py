#ordena em ordem crescente
import random


def preencheVetor(vetor):
    n = len(vetor)
    for i in range(n):
        vetor[i] = random.randint(1,50)
    return vetor

def verificaOrdem(vetor):
    n = len(vetor)
    for i in range(n-1):
        if vetor[i]>vetor[i+1]:
            return False
    return True


vetor = [0]*10
print(vetor)


print(preencheVetor(vetor))
print(verificaOrdem(vetor))

vetor.sort()
print (vetor)
print(verificaOrdem(vetor))
