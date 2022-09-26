#Verifica se o valor inteiro digitado está no vetor. Se sim, retorna seu index. Se não, retorna -1.
import random
vetor = [0]*5
n = len(vetor)

def preencheVetor(vetor):
    for i in range(0,n):
        vetor[i] = random.randint(0,50)
    return vetor

def verificaVetor(vetor):
    verifica = int(input('Digite um valor inteiro a ser verificado no vetor: '))
    if verifica in vetor:
        index = vetor.index(verifica)
        return index
    else:
        return -1

print(preencheVetor(vetor))
print(verificaVetor(vetor))
