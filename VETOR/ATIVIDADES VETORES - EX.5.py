#Calcula o percentual de ocorrência do número 6 em 50 lançamentos de um dado
import random
vetor = [0]*50
n=len(vetor)

def preencheVetor(vetor):
    for i in range(n):
        vetor[i] = random.randint(0,6)
    return vetor

def percentualVetor(vetor):
    contador = vetor.count(6)
    porcentagem = (contador*100)/50
    print(f'O percentual de ocorrência da face 6 do dado dentre os 50 lançamentos é {porcentagem} %')


print(preencheVetor(vetor))
percentualVetor(vetor)
