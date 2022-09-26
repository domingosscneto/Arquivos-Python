#inverte o vetor sem utilizar 'reverse()'
import random

def preencheVetor(vetor):
    n = len(vetor)
    for i in range(n):
        vetor[i] = random.randint(1,50)
    return vetor

def inverteVetor(vetor):
    n = len(vetor)
    vet2 = [0]*n

    for i in range(n):
        vet2[i] = vetor[n-i-1]
    return vet2

vetor = [0]*10
print(preencheVetor(vetor))

print(inverteVetor(vetor))
