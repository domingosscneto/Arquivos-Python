import sys
print("Operações:")
print("SOMA.........................1")
print("SUBTRAÇÃO....................2")
print("MULTIPLICAÇÃO................3")
print("DIVISÃO......................4")
print("SAIR.........................5")
escolha=int(input("Escolha a operação desejada: "))
while(escolha>=0) or (escolha<=1):
    if (escolha==1):
        num1=int(input("Escolha um número: "))
        num2=int(input("Escolha um número: "))
        soma=(num1+num2)
        print("A soma é: ", soma)
        escolha=int(input("Escolha a operação desejada: "))
    elif (escolha==2):
        num1=int(input("Escolha um número: "))
        num2=int(input("Escolha um número: "))
        subtração=(num1-num2)
        print("A subtração é: ", subtração)
        escolha=int(input("Escolha a operação desejada: "))
    elif (escolha==3):
        num1=int(input("Escolha um número: "))
        num2=int(input("Escolha um número: "))
        multiplicação=(num1*num2)
        print("A multiplicação é: ", multiplicação)
        escolha=int(input("Escolha a operação desejada: "))
    elif (escolha==4):
        num1=int(input("Escolha um número: "))
        num2=int(input("Escolha um número: "))
        divisão=(num1/num2)
        print("A divisão é: ", divisão)
        escolha=int(input("Escolha a operação desejada: "))
    elif(escolha==5):
        sys.exit("Fim")
    else:
        print("Operação inválida")
        escolha=int(input("Escolha a operação desejada: "))
