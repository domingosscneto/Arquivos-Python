import random

escolha=input('Escolha entre par ou ímpar: ')
jogador=int(input('Digite um número inteiro: '))
maquina=(random.randint(0,10))
print('Valor escolhido pela máquina: ',maquina)
print('Valor total: ',maquina+jogador)
if (maquina+jogador)%2==0:
    print('A soma é par')
elif (maquina+jogador)%2==1:
    print('A soma é ímpar')


if escolha=='ímpar' and (jogador+maquina)%2==1:
    print('você ganhou!')
elif escolha=='par' and (jogador+maquina)%2==1:
    print('Você perdeu!')
elif escolha=='ímpar' and (jogador+maquina)%2==0:
    print('Você perdeu!')
elif escolha=='par' and (jogador+maquina)%2==0:
    print('Você ganhou!')
else:
    print('escolha somente entre "par" ou "ímpar"')
