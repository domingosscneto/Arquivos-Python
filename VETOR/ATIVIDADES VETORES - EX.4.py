#Calcula quantos valores diferentes existem no vetor
vetor = [0]*10
n = len(vetor)

def preencheVetor(vetor):
    for i in range(n):
        vetor[i] = int(input("Digite os números inteiros para incluir no vetor:"))
    return vetor
def retorno(vetor):
    lst=[]
    for i in vetor:
        if i in vetor:
            if i not in lst:
                lst.append(i)
    m = len(lst)
    print(f'Existem {m} valores diferentes no vetor')


print(preencheVetor(vetor))
retorno(vetor)
