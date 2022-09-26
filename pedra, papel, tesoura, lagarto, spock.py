for i in range (int(input())):
    saida = ["Bazinga!", "Raj trapaceou!", "De novo!"]
    entrada = ["pedra", "papel", "tesoura", "lagarto", "Spock"]

    sheldon, raj = input().split()
    if sheldon == raj:
        print("Caso #%i:" % (i + 1), saida[2])

    elif sheldon == "pedra" and raj == "tesoura" or sheldon == "pedra" and raj == "lagarto":
            print("Caso #%i:" %(i+1), saida[0])
    elif sheldon == "tesoura" and raj == "pedra" or sheldon == "lagarto" and raj == "pedra":
        print("Caso #%i:" % (i + 1), saida[1])

    elif sheldon == "papel" and raj == "pedra" or sheldon == "papel" and raj == "Spock":
            print("Caso #%i:" % (i + 1), saida[0])
    elif sheldon == "pedra" and raj == "papel" or sheldon == "Spock" and raj == "papel":
        print("Caso #%i:" % (i + 1), saida[1])

    elif sheldon == "tesoura" and raj == "papel" or sheldon == "tesoura" and raj == "lagarto":
            print("Caso #%i:" % (i + 1), saida[0])
    elif sheldon == "papel" and raj == "tesoura" or sheldon == "lagarto" and raj == "tesoura":
        print("Caso #%i:" % (i + 1), saida[1])

    elif sheldon == "lagarto" and raj == "Spock" or sheldon == "lagarto" and raj == "papel":
            print("Caso #%i:" % (i + 1), saida[0])
    elif sheldon == "Spock" and raj == "lagarto" or sheldon == "papel" and raj == "lagarto":
        print("Caso #%i:" % (i + 1), saida[1])

    elif sheldon == "Spock" and raj == "tesoura" or sheldon == "Spock" and raj == "pedra":
            print("Caso #%i:" % (i + 1), saida[0])
    elif sheldon == "tesoura" and raj == "Spock" or sheldon == "pedra" and raj == "Spock":
        print("Caso #%i:" % (i + 1), saida[1])