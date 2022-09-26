#Calcula a força resultante X, Y e Z entre dois vetores
import random
vetor = [0]*3
vetor2 = [0]*3
n = len(vetor)

def preencheVetores():
    for i in range(n):
        vetor[i] = random.randint(0,50)
    for i in range(n):
        vetor2[i] = random.randint(0,50)
    print(f'Vetor 1:{vetor}')
    print(f'Vetor 2:{vetor2}')

def retornoVetores():
    forçaX = vetor[0]+vetor2[0]
    print(f'A força resultante X é: {forçaX}')
    forçaY = vetor[1]+vetor2[1]
    print(f'A força resultante Y é: {forçaY}')
    forçaZ = vetor[2] + vetor2[2]
    print(f'A força resultante Z é: {forçaZ}')

preencheVetores()
retornoVetores()
